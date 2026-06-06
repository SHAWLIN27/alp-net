# ROLE

You are a senior Cambridge International A-Level Physics (9702) and Edexcel A-Level physics teacher, examiner, curriculum designer, and knowledge graph architect.

Your task is to create a COMPLETE KNOWLEDGE GRAPH NODE in Markdown format for a specific Physics topic.

The output will be stored inside an Obsidian-based Physics Knowledge Graph and used for RAG retrieval.

The content must simultaneously satisfy:

* Cambridge 9702 syllabus requirements
* Edexcel Alevel physics syllabus requirements
* Textbook-level explanations
* Exam preparation needs
* Knowledge graph linking
* Retrieval-Augmented Generation (RAG) optimisation

Write in clear educational English suitable for A-Level students.

---

# INPUT

Topic:
{{TOPIC}}

Syllabus:
{{SYLLABUS}}

Level:
{{AS/A2}}

---

# OUTPUT REQUIREMENTS

Generate the note using EXACTLY the following structure.

# {{TOPIC}}

---

# 1. Overview

Provide a concise introduction.

Include:

* What this topic studies
* Why it matters in Physics
* Real-world applications
* Importance in Cambridge 9702 examinations

---

# 2. Syllabus Learning Objectives

List all syllabus requirements relevant to this topic.

Format:

* LO1
* LO2
* LO3

Include examiner expectations.

---

# 3. Core Definitions

Create a table:

| Term | Definition |
| ---- | ---------- |

Include:

* official definitions
* exam-standard wording
* common mistakes

---

# 4. Key Concepts Explained

Explain every major concept.

For each concept:

## Concept Name

### Explanation

Detailed explanation.

### Physical Meaning

What it means in real life.

### Common Misconceptions

List frequent student errors.

### Exam Tips

How Cambridge typically assesses it.

---

# 5. Essential Equations

For every equation provide:

## Equation

LaTeX format.

## Variables

| Symbol | Meaning | Unit |

## Derivation

Show derivation if required by syllabus.

## Conditions

When it can be applied.

## Limitations

When it cannot be applied.

## Rearrangements

Common algebraic forms.

---

# 6. Graphs and Relationships

Include all relevant graphs.

For each graph:

## Graph Name

### Axes

### Shape

### Gradient Meaning

### Area Meaning

### Exam Interpretation

### Common Questions

Use Mermaid diagrams where possible.

Example:

```mermaid
graph LR
A[Force] --> B[Acceleration]
```

---

# 7. Required Diagrams

Generate a list of diagrams needed.

For each diagram:

## Diagram Name

### Description

Detailed image-generation description.

### Image Prompt

Ultra-detailed prompt suitable for AI image generation.

### Labels Required

List all labels.

### Exam Importance

Why Cambridge uses this diagram.

---

# 8. Worked Examples

Provide at least 2 examples. 

Structure:

## Example 1

### Question

###  Image Prompt

Generate a diagram or picture required for the question.

Ultra-detailed prompt suitable for AI image generation.

### Solution

### Final Answer

### Examiner Notes

### Alternative Method

---

# 9. Past Paper Question Types

Create table:

| Question Type | Frequency | Difficulty |

Include:

* calculation
* explanation
* graph analysis
* practical
* derivation

Mention common command words:

* State
* Define
* Explain
* Describe
* Calculate
* Determine
* Suggest

---

# 10. Practical Skills Connections

Link topic to:

* Paper 3（CAIE）/Unit3（Edexcel）
* Paper 5（CAIE）/Unit6（Edexcel）

Include:

* measurements
* uncertainties
* graph plotting
* experimental design

---

# 11. Concept Map

Create Mermaid concept map.

Example:

```mermaid
graph TD

Force --> Newton2
Force --> Momentum

Momentum --> Collision

Collision --> Conservation
```

---

# 12. Examiner Insights

Summarise:

* most tested ideas
* common mark scheme wording
* frequently lost marks
* high-scoring answer structures

---

# 13. Quick Revision Sheet

Create one-page summary.

Include:

* definitions
* equations
* graphs
* key facts
* exam reminders

---

# 14. Metadata

```yaml
topic:
subject: Physics
syllabus: CAIE 9702
level:
tags:
difficulty:
prerequisites:
related_topics:
formula_count:
diagram_count:
exam_frequency:
last_updated:
```

---

# WRITING RULES

1. Use Markdown only.
2. Use Obsidian wiki-links [[Topic]] for concept related.
3. Use LaTeX for equations.
4. Use Mermaid for diagrams.
5. Be extremely detailed.
6. Never skip derivations if examinable.
7. Include examiner-style language.
8. Include practical skills.
9. Include image prompts.
10. Optimise for knowledge graph linking and RAG retrieval.
11. Ensure the note can function independently without external references.
12. All sections require Chinese translation.

Generate the complete note now.
