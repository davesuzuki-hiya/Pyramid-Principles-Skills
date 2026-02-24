## Pyramid Principles Skills

This skill is for **product managers and leaders who need to think clearly about messy, strategic problems**—launch decisions, pricing changes, growth plateaus, roadmap trade‑offs, org design, and more.

Instead of staring at a blank page or a jumble of notes, you get a guided way to:

- **Clarify the problem** so you and your stakeholders are actually solving the same thing.
- **Break it down** into a small number of MECE branches instead of a wall of bullets.
- **Form and test hypotheses** quickly, without boiling the ocean on analysis.
- **Push to real insight** using So What / Why So and the 7 So Whats.
- **Turn the thinking into a storyline** that’s ready for execs, a doc review, or a strategy deck.

### Brief explanation of the methods

- **SCQA (Situation–Complication–Question–Answer)**: A simple storytelling frame that forces you to say: what’s going on (S), what changed or is painful (C), what big question that creates (Q), and your proposed answer (A). This is how you stop rambling context and get to a sharp “why this matters now” plus a clear recommendation.

- **MECE issue trees**: A way to break a big question (“Why is growth slowing?”) into smaller buckets that don’t overlap (Mutually Exclusive) and don’t miss anything important (Collectively Exhaustive). In practice, you get a tree of 2–4 branches per level so you can see where to focus instead of chasing random bullets.

- **Hypothesis‑driven problem solving**: Instead of analyzing everything, you write down a specific, testable belief (for example “SMB is our best growth segment because X, Y, Z”) and then list what would need to be true. You then look for data to quickly prove or disprove those few points, which is much faster than boiling the ocean.

- **So What / Why So and the 7 So Whats**: A set of questions you ask yourself about every finding. “So what?” pushes you upward from data to impact and action; “Why so?” forces you to back up each claim with evidence. The “7 So Whats” is just asking “so what?” repeatedly until you land on a real decision or priority, not just a metric movement.

- **Storyline / Pyramid Principle**: Once you’ve done the thinking, you turn it into a pyramid: one governing thought at the top (your main recommendation), supported by three key arguments, each with evidence underneath. This gives you a narrative you can use in a doc, a deck, or a live meeting without losing people in the weeds.

### What problems this helps with

- **“I’m not even sure what the real question is.”**  
  The skill walks you through SCQA to get to a crisp, shared problem statement.

- **“I’m drowning in inputs and slides.”**  
  You’ll use MECE issue trees and hypothesis trees to impose structure and decide what not to analyze.

- **“I have findings but no real insight or recommendation.”**  
  So What / Why So forces you to keep asking “so what?” until you land on a concrete action or strategic implication.

- **“I need something I can put in front of execs tomorrow.”**  
  You can choose a quick analysis, a deeper doc, or a full strategy narrative depending on time and audience.

### How it works (from your perspective)

You use this skill in two main ways:

- **You bring a vague, fuzzy problem**  
  - You describe the situation in your own words.  
  - The skill classifies the problem (root cause, strategic decision, recommendation, sense‑making, comms prep).  
  - It proposes an approach (for example: *SCQA → Issue Tree → Hypotheses → 7 So Whats → Storyline*), checks that this matches what you need, then walks you through each step with checkpoints.

- **You already know what you want**  
  Use plain language like:
  - “Frame this with SCQA”  
  - “Build an issue tree for this”  
  - “Do a quick analysis I can use in a meeting”  
  - “Do a deep analysis for a strategy doc”  
  - “Turn this into an exec‑ready storyline”
  
  The skill will jump straight into the relevant method or template (SCQA, MECE issue tree, hypothesis‑driven, So What / Why So, storyline, quick/deep/strategy templates) and co‑create the content with you.

### What’s in this repo (if you want to dig deeper)

- **Skill definition (`SKILL.md`)**: How the `pyramid-principle` skill wires together the methods below.  
- **Core methods (`pyramid-principle-skill/core/`)**: SCQA, MECE issue trees, hypothesis‑driven problem solving, So What / Why So, and storyline building.  
- **Templates (`pyramid-principle-skill/templates/`)**: Ready‑to‑fill frames for quick analysis, deep analysis, and full strategy docs.  
- **HTML report generator (`pyramid-principle-skill/scripts/generate-report.py`)**: Turn structured JSON into a modern interactive report you can share with stakeholders. See `EXAMPLE_DATA` in the script and `assets/example-report.html` for an example.

### Picking the right “mode” as a PM

- **You have 15–30 minutes before a meeting**  
  - Ask for a **quick analysis**: you’ll get SCQA, a simple structure, a few key arguments, and a clear recommendation you can speak to.

- **You’re doing a real strategy / product deep dive**  
  - Use the **deep analysis** flow: SCQA → issue tree → hypotheses → evidence → 7 So Whats → synthesized storyline.

- **You’re preparing for leadership or board**  
  - Use the **strategy doc** flow: a governing thought, three key arguments, risks, and a concrete implementation path—plus an optional HTML report with interactive sections.


