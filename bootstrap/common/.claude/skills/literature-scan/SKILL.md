---
name: literature-scan
description: Find and summarize relevant papers or references for the project
---

# Literature Scan

## When to Use

Use this skill when:
- Starting work in a new area and need background reading
- Looking for prior art on a specific technique
- The operator asks "what papers should I read about X?"

## Inputs

- Topic or research question
- Scope constraints (e.g., "last 2 years", "specific to transformers")
- Number of references desired (default: 5)

## Steps

1. **Define search scope:**
   - Clarify the topic with the operator if needed
   - Identify key terms and synonyms

2. **Search for references:**
   - Use available search tools (web search, arxiv, semantic scholar)
   - Prioritize recent, well-cited, and relevant papers

3. **Create literature notes:**
   - For each reference, create `docs/literature/NNNN-title.md`
   - Fill in citation, key takeaways, and relevance

4. **Produce summary:**
   - Write a brief overview connecting the references
   - Highlight the most important findings
   - Note any gaps in the literature

## Output Format

```
## Literature Scan — Topic

### References Found
1. Author (Year) — "Title" — Key finding
2. Author (Year) — "Title" — Key finding
...

### Summary
Brief overview connecting the references.

### Recommended Reading Order
1. Start with: Paper X (foundational)
2. Then: Paper Y (builds on X)
3. Deep dive: Paper Z (most relevant to our work)

### Files Created
- docs/literature/0001-title.md
- docs/literature/0002-title.md
```

## Safety Notes

- Clearly distinguish between papers you have read/verified and those you are
  recommending based on metadata alone.
- Always include proper citations with links.
- Do not fabricate paper titles, authors, or findings.
- If search tools are unavailable, tell the operator rather than guessing.
