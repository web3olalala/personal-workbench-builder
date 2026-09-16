from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ScriptTests(unittest.TestCase):
    def run_script(self, name: str, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / name), *args],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_state_initializes_and_validates(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            result = self.run_script("init_workbench_state.py", "--project-root", temporary)
            self.assertEqual(result.returncode, 0, result.stderr)
            state_path = Path(temporary) / ".personal-workbench" / "project-state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual(state["phase"], "discovery")
            validated = self.run_script("validate_workbench_state.py", "--project-root", temporary)
            self.assertEqual(validated.returncode, 0, validated.stdout + validated.stderr)

    def test_state_initializer_refuses_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            first = self.run_script("init_workbench_state.py", "--project-root", temporary)
            second = self.run_script("init_workbench_state.py", "--project-root", temporary)
            self.assertEqual(first.returncode, 0)
            self.assertEqual(second.returncode, 3)

    def test_starter_copy_refuses_nonempty_destination(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "app"
            copied = self.run_script("copy_starter.py", str(destination))
            self.assertEqual(copied.returncode, 0, copied.stderr)
            self.assertTrue((destination / "package.json").is_file())
            refused = self.run_script("copy_starter.py", str(destination))
            self.assertEqual(refused.returncode, 3)

    def test_scenario_contracts(self) -> None:
        result = self.run_script("validate_scenarios.py")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_portable_skill_contract(self) -> None:
        result = self.run_script("validate_skill.py")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
