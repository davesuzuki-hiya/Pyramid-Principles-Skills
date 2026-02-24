# Hypothesis-Driven Problem Solving

Hypothesis-driven thinking is the "secret sauce" of top-tier consulting. Instead of analyzing everything (boiling the ocean), you form educated guesses and systematically prove or disprove them.

## The Core Principle

**Traditional approach:** Gather all data → Analyze everything → Form conclusions
**Hypothesis-driven:** Form hypothesis → Identify proof points → Gather targeted data → Validate or pivot

The hypothesis-driven approach is 3-5x faster because you only gather data that proves or disproves your hypothesis.

## The Hypothesis Cycle

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   1. FORM          2. STRUCTURE       3. TEST               │
│   Hypothesis  →    Proof Points  →    With Data             │
│       ↑                                   │                 │
│       │                                   ↓                 │
│       └──────── 4. ITERATE ←─────────────┘                 │
│                 (if disproved)                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Step 1: Form a Hypothesis

A good hypothesis is:
- **Specific**: Not "we should improve marketing" but "we should shift 30% of paid social budget to influencer marketing"
- **Testable**: Can be proven or disproven with available data
- **Actionable**: Points to a specific action if true
- **Non-obvious**: Worth testing (the opposite could also be true)

### Hypothesis Quality Test

Ask yourself:
1. **Would I care if the opposite were true?** If not, it's not a hypothesis, it's a statement.
2. **Would the CEO find this naive or obvious?** If yes, dig deeper.
3. **Does it point to a specific action?** If not, sharpen it.

### Examples

**Weak hypothesis:**
> "Customer satisfaction is important for retention."
- Problem: Obvious, not testable, no specific action

**Strong hypothesis:**
> "Implementing a Day-3 onboarding call will increase 30-day retention by 15% because users who receive proactive support are 2x more likely to activate key features."
- Specific: Day-3 call, 15% improvement
- Testable: Can measure retention before/after
- Actionable: Implement onboarding calls
- Non-obvious: Costs money, might not work

## Step 2: Structure Proof Points

For each hypothesis, identify what needs to be true for it to hold. These become your proof points.

**Hypothesis:** "We should enter the UK market first"

**Proof points (what needs to be true):**
1. UK market size is sufficient (>$100M addressable)
2. Competitive intensity is manageable (<3 entrenched players)
3. Regulatory barriers are lower than EU alternatives
4. Localization costs are lowest among options
5. UK success enables EU expansion

**For each proof point, define:**
- What data do we need?
- Where can we get it?
- What threshold would prove/disprove it?

## Step 3: Test with Data

### The 80/20 Rule
You don't need 100% certainty. You need 80% confidence as fast as possible.

**Prioritize data gathering:**
1. **Quick wins**: Easy to get, high impact on hypothesis
2. **Must-haves**: Essential to the hypothesis, worth the effort
3. **Nice-to-haves**: Additional validation, but not critical
4. **Skip**: Interesting but doesn't affect the hypothesis

### Data Sources Hierarchy

| Priority | Source Type | Use When |
|----------|-------------|----------|
| 1 | Existing internal data | Always check first |
| 2 | Quick external research | Validating market assumptions |
| 3 | Expert interviews | Need qualitative insight |
| 4 | Primary research | High-stakes decisions |
| 5 | Full market study | Only if others fail |

### Documenting Evidence

For each proof point, document:
- **Finding**: What the data shows
- **Source**: Where it came from
- **Confidence**: High/Medium/Low
- **Implication**: Proves/Disproves/Inconclusive

## Step 4: Iterate

If your hypothesis is disproved:
1. **Don't discard the learning** - Document why it failed
2. **Form the next best hypothesis** - Informed by what you learned
3. **Repeat the cycle** - Usually 2-3 iterations to reach a strong conclusion

**Signs you need to pivot:**
- Multiple proof points fail
- New information fundamentally changes the problem
- Stakeholders surface constraints you didn't know about

## Hypothesis Trees: Structuring Multiple Hypotheses

When the problem is complex, you'll have a tree of hypotheses:

```
Main Hypothesis: Hiya should focus on SMB segment for PLG growth

├── H1: SMB has higher conversion potential than Enterprise
│   ├── H1.1: SMB decision cycles are shorter (<30 days)
│   ├── H1.2: SMB has lower switching costs
│   └── H1.3: SMB responds better to self-serve
│
├── H2: SMB can be served profitably at scale
│   ├── H2.1: CAC can be <$50 with digital channels
│   ├── H2.2: LTV/CAC ratio exceeds 3:1
│   └── H2.3: Support costs are manageable with automation
│
└── H3: SMB success leads to Enterprise expansion
    ├── H3.1: SMB users become advocates
    └── H3.2: Enterprise buyers trial personally first
```

## Common Pitfalls

### Pitfall 1: Confirmation Bias
**Problem:** Only looking for data that supports your hypothesis
**Fix:** Actively seek disconfirming evidence. Ask "What would prove me wrong?"

### Pitfall 2: Hypothesis as Fact
**Problem:** Treating your hypothesis as the answer before testing
**Fix:** Always frame as "We believe X because Y, and we'll test by Z"

### Pitfall 3: Analysis Paralysis
**Problem:** Testing indefinitely without committing
**Fix:** Set a deadline. Make the best decision with available information.

### Pitfall 4: Anchoring on First Hypothesis
**Problem:** Over-investing in initial hypothesis even as evidence mounts against it
**Fix:** Define pivot criteria upfront. If >2 proof points fail, reassess.

## Real-World Application: PLG Pricing Hypothesis

**Context:** Hiya's PLG conversion rate is 0.8%, below 3-5% benchmark.

**Initial Hypothesis:**
> "Introducing a $4.99/month 'Lite' tier between Free and Premium ($9.99) will increase overall conversion by capturing price-sensitive users, resulting in 2.5% conversion rate and 40% revenue increase."

**Proof Points:**

| # | What Needs to Be True | Data Needed | Source | Threshold |
|---|----------------------|-------------|--------|-----------|
| 1 | Users cite price as primary barrier | Exit survey data | Product analytics | >40% cite price |
| 2 | $4.99 is acceptable price point | Willingness-to-pay study | Survey + competitor analysis | >60% acceptance |
| 3 | Lite features are differentiated from Free | Feature value analysis | User interviews | Clear value gap identified |
| 4 | Cannibalization risk is manageable | Conversion modeling | Financial model | <20% Premium cannibalization |
| 5 | Implementation is feasible | Engineering assessment | Tech team | <4 weeks development |

**Testing Results:**
- PP1: ✅ 47% cite price (survey n=500)
- PP2: ✅ 68% would consider $4.99 tier
- PP3: ⚠️ Inconclusive - users want "just spam blocking" which overlaps with Premium
- PP4: ❌ Model shows 35% Premium cannibalization
- PP5: ✅ 3 weeks estimated

**Decision:** Pivot hypothesis. High cannibalization risk suggests different approach needed. New hypothesis: "Usage-based pricing (first 50 blocks free, then $0.10/block) will convert value-realized users without cannibalizing Premium."

## Hypothesis-Driven Checklist

- [ ] Hypothesis is specific and actionable
- [ ] Opposite hypothesis would also be reasonable
- [ ] 3-5 proof points identified
- [ ] Each proof point has data source and threshold
- [ ] Quick wins prioritized in data gathering
- [ ] Pivot criteria defined upfront
- [ ] Disconfirming evidence actively sought
- [ ] Decision deadline set
