## Pyramid Principles Skills

Structured thinking and communication toolkit based on the Pyramid Principle, SCQA, MECE issue trees, hypothesis‑driven problem solving, So What / Why So, and storyline design. This repository packages the `pyramid-principle` skill plus reference material and templates so you can reuse the same patterns across tools or projects.

### What’s in this repo

- **Skill definition (`SKILL.md`)**: Top‑level description of the `pyramid-principle` skill (name, description, and how it routes between automatic and explicit modes).
- **Embedded skill (`pyramid-principle-skill/SKILL.md`)**: Same core skill doc, intended to live alongside the supporting assets under `pyramid-principle-skill/`.
- **Core methods (`pyramid-principle-skill/core/`)**  
  - `scqa-framework.md`: How to frame Situation–Complication–Question–Answer.  
  - `mece-issue-tree.md`: MECE and issue / hypothesis trees for breaking down problems.  
  - `hypothesis-driven.md`: Hypothesis‑driven problem solving and proof points.  
  - `so-what-why-so.md`: So What / Why So and the 7 So Whats for depth and rigor.  
  - `storyline.md`: Turning analysis into compelling, executive‑ready storylines.
- **Templates (`pyramid-principle-skill/templates/`)**  
  - `quick-analysis.md`: 5–10 minute “good enough” structured take.  
  - `deep-analysis.md`: 30–60 minute deep dive.  
  - `strategy-doc.md`: 1+ hour, executive / board‑level strategy document.
- **HTML report generator (`pyramid-principle-skill/scripts/generate-report.py`)**  
  - Python script that turns structured JSON into a modern, interactive HTML report.
- **Example report (`pyramid-principle-skill/assets/example-report.html`)**  
  - Sample output you can open in a browser to see the style of report this skill can generate.

### How the skill works

At a high level, the `pyramid-principle` skill does two things:

- **Automatic mode (Problem Router)**: When a user gives a vague or open‑ended problem, the skill:  
  - Diagnoses the problem type (ill‑defined, root cause, strategic decision, recommendation, sense‑making, or communication prep).  
  - Recommends an appropriate methodology chain (e.g., SCQA → Issue Tree → Hypotheses → So What → Storyline).  
  - Adjusts depth (quick vs deep vs strategy‑level) and output format (markdown vs HTML vs presentation‑ready).
- **Explicit mode (Direct methods/templates)**: When a user asks for something specific (for example “frame this with SCQA”, “build an issue tree”, “do a deep‑analysis”, “create a strategy‑doc”), the skill jumps directly to the relevant core file or template under `core/` or `templates/` and runs that workflow.

### Installing / using the skill

How you “install” this skill depends on your agent/runtime, but the pattern is:

1. **Copy the skill folder**  
   - Place the `pyramid-principle-skill/` directory (and optionally the root `SKILL.md`) into your skills directory (for example a `skills/` or `.claude/skills/` folder, depending on your setup).
2. **Register the skill**  
   - Ensure your agent/tooling is configured to load `SKILL.md` files as skills and that the `name: pyramid-principle` block is discoverable.
3. **Trigger it from conversations**  
   - Implicitly: ask for help with ambiguous analysis/strategy problems, and let the problem router choose the method.  
   - Explicitly: use trigger phrases like “use pyramid-principle”, “frame this with SCQA”, “build an issue tree”, “do a quick-analysis”, “do a deep-analysis”, or “create a strategy-doc”.

If you are using Cursor or another Codex‑style environment that already supports local skills, you can typically point the tool to this repo (or copy the folder in) and it will pick up `SKILL.md` automatically.

### Generating interactive HTML reports

The `generate-report.py` script converts structured JSON into a polished HTML report that follows the Pyramid Principle:

- **Inputs**: A JSON file with keys like `title`, `subtitle`, `author`, `governing_thought`, `scqa`, `arguments`, `hypothesis`, `recommendations`, and `timeline`. See the `EXAMPLE_DATA` dict inside `generate-report.py` for a full schema.
- **Outputs**: A single HTML file with:
  - Executive summary and governing thought.  
  - SCQA cards laid out responsively.  
  - Expandable “Key Arguments” cards with evidence and So What call‑outs.  
  - Optional hypothesis validation, recommendations, and implementation timeline.

Usage:

```bash
# Generate an example report (no arguments)
cd pyramid-principle-skill/scripts
python generate-report.py

# From your own JSON
python generate-report.py input.json output.html
```

You can then open the resulting HTML file directly in a browser or serve it from any static host.

### When to use which template

- **Quick decision / prep (<30 minutes)**: Start from `templates/quick-analysis.md`.  
- **Serious deep dive (30–60 minutes)**: Use `templates/deep-analysis.md` and chain in `core/mece-issue-tree.md` + `core/hypothesis-driven.md` + `core/so-what-why-so.md` as needed.  
- **Executive / strategy work (1+ hour)**: Use `templates/strategy-doc.md`, plus `core/storyline.md` to turn your analysis into a narrative that’s ready for leadership review.

