---
name: pyramid-principle
description: Structured thinking and communication framework used by McKinsey, BCG, and Bain consultants. AUTOMATICALLY activates for any problem-solving, analysis, strategy, or recommendation request - Claude will diagnose the problem type and recommend the appropriate analysis depth. Also responds to explicit requests like "use pyramid-principle", "SCQA", "MECE", "issue tree", "hypothesis-driven", "so what analysis". Handles both vague requests ("help me think through this") and specific requests ("do a deep-analysis on X").
---

# Pyramid Principle Skill

A comprehensive structured thinking toolkit that automatically adapts to user needs.

## How This Skill Works

```
┌─────────────────────────────────────────────────────────────────┐
│  USER REQUEST                                                   │
│  (vague or specific)                                            │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │  Explicit method set?  │
         │  (template/method name)│
         └────────────┬───────────┘
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼ YES                   ▼ NO
   ┌──────────────┐      ┌──────────────────┐
   │ Run specified│      │ PROBLEM ROUTER   │
   │ analysis     │      │ (auto-diagnosis) │
   └──────────────┘      └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Diagnose problem │
                         │ + propose method │
                         │ + confirm with   │
                         │   user           │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ After agreement, │
                         │ run analysis     │
                         └──────────────────┘
```

---

## PART 1: AUTOMATIC MODE (Problem Router)

When user gives a vague or open-ended request, follow this diagnostic flow.

### Step 1: Problem Intake

Ask yourself these questions about the user's request:

| Question | Determines |
|----------|------------|
| Is there a clear decision to make? | Decision vs Exploration |
| Is the problem well-defined? | Framing needed or not |
| How urgent/time-constrained? | Analysis depth |
| Who is the audience? | Output format |
| Is data available? | Hypothesis vs Discovery |

### Step 2: Problem Type Classification

Classify into one of these types:

| Type | Signals | Recommended Approach |
|------|---------|---------------------|
| **Ill-defined Problem** | "I'm not sure what's wrong", "something feels off", vague discomfort | Start with SCQA framing → then diagnose |
| **Root Cause Analysis** | "Why is X happening?", metrics declining, unexpected results | Issue Tree → Hypothesis-driven |
| **Strategic Decision** | "Should we do X?", "Which option?", resource allocation | Options Framework → deep-analysis |
| **Recommendation Request** | "What should we do about X?", needs action plan | Full pyramid → strategy-doc |
| **Sense-making** | "Help me understand X", lots of data/info to synthesize | MECE structuring → storyline |
| **Communication Prep** | "Help me present X", "convince stakeholders" | Storyline → output format |

### Step 3: Propose and Confirm

**Always confirm with the user before proceeding.** Use this template:

```
Based on what you've shared, here's how I'd approach this:

**Problem Type:** [Classification]
**My Understanding:** [1-2 sentence summary of the problem]
**Recommended Approach:** [Method + why]
**Depth:** [Quick/Deep/Strategy-level]
**Output:** [Markdown/HTML Report/Presentation-ready]

Does this match what you need? Or would you prefer:
- [ ] Go deeper / less deep
- [ ] Different output format  
- [ ] Focus on specific aspect
- [ ] Something else entirely
```

### Step 4: Execute with Checkpoints

For deep analyses, pause at key points:

1. **After SCQA framing** → "Does this capture the problem correctly?"
2. **After Issue Tree** → "Are these the right branches to explore?"
3. **After key findings** → "Any surprises here? Should we dig deeper anywhere?"
4. **Before final output** → "Shall I generate the report, or iterate further?"

---

## PART 2: EXPLICIT MODE (Direct Specification)

When user explicitly requests a specific analysis, skip diagnosis and execute directly.

### Trigger Phrases → Action

| User Says | Action |
|-----------|--------|
| "use pyramid-principle" | Full methodology, ask for depth preference |
| "do a quick-analysis" | Use `templates/quick-analysis.md` |
| "do a deep-analysis" | Use `templates/deep-analysis.md` |
| "create a strategy-doc" | Use `templates/strategy-doc.md` |
| "frame this with SCQA" | Use `core/scqa-framework.md` only |
| "build an issue tree" | Use `core/mece-issue-tree.md` only |
| "apply hypothesis-driven" | Use `core/hypothesis-driven.md` |
| "do 7 so-whats" | Use `core/so-what-why-so.md` |
| "build the storyline" | Use `core/storyline.md` |
| "generate HTML report" | Run `scripts/generate-report.py` |

### Depth Override

User can always override recommended depth:

```
User: "Just give me a quick take, don't need the full analysis"
→ Switch to quick-analysis regardless of problem complexity

User: "Go really deep on this, I have time"
→ Use deep-analysis or strategy-doc
```

---

## PART 3: OUTPUT SELECTION

### Automatic Output Recommendation

| Audience | Time Constraint | Recommended Output |
|----------|-----------------|-------------------|
| Self/Thinking | Any | Markdown (simple) |
| Team discussion | <30 min | quick-analysis |
| Stakeholder review | 30-60 min | deep-analysis |
| Executive/Board | Unlimited | strategy-doc + HTML |
| Async communication | Any | HTML Report |

### Output Formats Available

1. **Markdown** - Simple, copy-paste ready
2. **Structured Markdown** - With tables, trees, checklists
3. **Interactive HTML** - Visual, expandable sections, printable
4. **Presentation-ready** - Slide-by-slide structure with speaker notes

---

## PART 4: METHODOLOGY QUICK REFERENCE

### When to Use What

```
Problem unclear? 
    → SCQA Framework (core/scqa-framework.md)
    
Need to break down complexity?
    → MECE + Issue Tree (core/mece-issue-tree.md)
    
Have a hypothesis to test?
    → Hypothesis-Driven (core/hypothesis-driven.md)
    
Analysis feels shallow?
    → 7 So Whats (core/so-what-why-so.md)
    
Need to communicate findings?
    → Storyline (core/storyline.md)
```

### Methodology Chaining

Most real problems need multiple methodologies in sequence:

```
Typical Flow:
SCQA (frame) → Issue Tree (structure) → Hypothesis (focus) 
    → So What (deepen) → Storyline (communicate)

Quick Flow:
SCQA → Key findings → Recommendation

Deep Flow:
SCQA → Issue Tree → Hypothesis per branch → Evidence gathering
    → 7 So Whats per finding → Synthesis → Storyline → HTML Report
```

---

## PART 5: EXAMPLE INTERACTIONS

### Example 1: Vague Request

```
User: "Our growth is slowing down and I'm not sure why or what to do"

Claude: "Let me help you work through this systematically.

**Problem Type:** Root Cause + Recommendation (combined)
**My Understanding:** Growth metrics are declining, cause unknown, need both diagnosis and action plan
**Recommended Approach:** 
  1. First, frame the problem with SCQA to ensure we're solving the right thing
  2. Then build an issue tree to identify possible causes
  3. Form hypotheses and identify which to test
  4. Develop recommendations based on findings

**Depth:** Deep analysis (this warrants thorough investigation)
**Output:** Structured Markdown, can convert to HTML report after

Before I start - can you share:
- Which growth metric specifically? (Revenue, users, engagement?)
- Over what time period?
- Any changes you've made recently?

Does this approach work for you?"
```

### Example 2: Specific Request

```
User: "Do a SCQA analysis on our pricing strategy"

Claude: [Immediately uses core/scqa-framework.md]

"Here's the SCQA framing for your pricing strategy:

**Situation:**
[Drafts based on known context]

**Complication:**
[Identifies tension]

**Question:**
[Formulates the key question]

**Answer (Hypothesis):**
[Proposes initial answer to validate]

Does this framing capture the problem accurately? 
I can then build out the full analysis or adjust the framing."
```

### Example 3: Time-Constrained

```
User: "I have a meeting in 20 minutes, help me think through whether we should launch in UK or Germany first"

Claude: "Got it - let me give you a quick-analysis you can use in that meeting.

**SCQA (30 sec version):**
- S: Ready to expand to Europe, budget for one market
- C: UK and Germany both viable, different tradeoffs
- Q: Which market first?
- A: [Hypothesis based on quick assessment]

**Key Decision Factors:**
1. Market size & growth
2. Entry barriers
3. Strategic optionality

**Quick Recommendation:**
[Direct answer with 2-3 supporting points]

**One-liner for your meeting:**
'We recommend [X] because [single strongest reason].'

Want me to elaborate on any point before your meeting?"
```

### Example 4: Depth Override

```
User: "Analyze our competitor landscape - but keep it high level, don't need a full deep dive"

Claude: "Understood - I'll do a focused quick-analysis on competitors.

[Uses quick-analysis template but applies to competitive analysis]

**SCQA:**
...

**Top 3 Competitors at a Glance:**
| Competitor | Strength | Weakness | Threat Level |
...

**Key Insight:**
[One main takeaway]

**If You Want to Go Deeper:**
I can expand on any competitor or analyze specific dimensions (pricing, features, positioning). Let me know."
```

---

## CORE REFERENCES

For detailed methodology, these files are loaded as needed:

| File | Use When |
|------|----------|
| `core/scqa-framework.md` | Framing problems, setting context |
| `core/mece-issue-tree.md` | Breaking down complexity |
| `core/hypothesis-driven.md` | Efficient problem-solving |
| `core/so-what-why-so.md` | Deepening analysis, finding insights |
| `core/storyline.md` | Building narratives, presenting |

## TEMPLATES

| Template | Time | Use Case |
|----------|------|----------|
| `templates/quick-analysis.md` | 5-10 min | Rapid decisions, status updates |
| `templates/deep-analysis.md` | 30-60 min | Thorough investigation |
| `templates/strategy-doc.md` | 1+ hour | Executive presentations, major decisions |

## SCRIPTS

| Script | Function |
|--------|----------|
| `scripts/generate-report.py` | Creates interactive HTML from JSON data |
