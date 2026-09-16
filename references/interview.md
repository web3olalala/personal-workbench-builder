# Discovery interview

Use this reference only during discovery or when a later change exposes a genuine requirement gap.

## Goal

Learn enough to describe the user's core scenario without making the user design a product. Ask two or three related questions per turn, summarize what was learned, and follow the user's vocabulary.

Cover these topics adaptively:

- Current identity or role, including which role matters for this first version.
- A real workflow from beginning to end and the tools currently used.
- The most painful, repetitive, forgettable, or fragmented parts.
- Information worth recording for months or years.
- Tasks performed daily, weekly, and occasionally.
- Work the user hopes AI or automation can handle.
- Primary device, secondary device, sync expectations, and offline need.
- Whether the data includes private notes, finances, client material, or other people's data.
- Visual mood, density, color, products or culture they like, and reference images if available.

Do not ask every item if it is already known. When the answer is broad, use one concrete recent example: “Think about the last time you did this—where did it start, what did you open, and where did it end?”

## Useful opening

For a blank project, ask about:

1. What the user mainly does and which part of life or work this version should focus on.
2. What a typical instance of that work looks like from start to finish.
3. The one thing that currently causes the most trouble.

For an existing project, start by summarizing what the code and state files show, then ask only about contradictions or the requested change.

## Domain adaptation

Examples are prompts, not templates:

- Creator: inspiration → topic → script → assets → production → publishing → metrics → review.
- Student: courses → assignments → revision → exams → knowledge capture.
- Freelancer: leads → requirements → quote → project → delivery → invoice/payment.
- Employee: tasks → meetings → projects → work log → reporting → goals.

Follow the user's actual sequence and terminology.

## Stop condition

End discovery when you can state: person, focused scenario, actual workflow, top pains, long-term records, frequent tasks, desired automation, devices/sync, privacy needs, and visual direction. Tell the user you will now organize a proposal rather than start development.

Record facts in `requirements.md` and `workflow.md`; label assumptions and unanswered questions instead of presenting them as confirmed.
