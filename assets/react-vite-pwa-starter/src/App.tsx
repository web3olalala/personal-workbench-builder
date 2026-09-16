const phases = ['Discover', 'Plan', 'Prototype', 'Build', 'Verify']

export default function App() {
  return (
    <main className="shell">
      <p className="eyebrow">Personal Workbench</p>
      <h1>Start with the workflow, not the widgets.</h1>
      <p className="lede">
        This starter is intentionally neutral. Replace this shell only after the user confirms
        the functional plan and a clickable design direction.
      </p>
      <ol className="phases" aria-label="Build phases">
        {phases.map((phase, index) => (
          <li key={phase}>
            <span>{String(index + 1).padStart(2, '0')}</span>
            {phase}
          </li>
        ))}
      </ol>
    </main>
  )
}
