#!/usr/bin/env python3
"""
Phase 2 (v3): 生成 ALP_Net 全部 12 个章节的 A-Level 物理知识点 Markdown 文件

更新内容：
- 基于新的 Know.md 12-section 格式
- 覆盖全部 12 个章节（力学 → 实验技能）
- CAIE 9702 + Edexcel IAL 双考纲
- 中英双语 (EN+CN)
- 4级文件夹层级 (Hub + Leaf nodes)
- DeepSeek API 生成内容
"""

import asyncio
import sys
import re
import argparse
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from openai import AsyncOpenAI
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = {
        "env_file": str(PROJECT_ROOT / ".env"),
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }
    deepseek_api_key: str = ""
    deepseek_base_url: str = "https://api.deepseek.com"


settings = Settings()
client = AsyncOpenAI(api_key=settings.deepseek_api_key, base_url=settings.deepseek_base_url)

VAULT_PATH = PROJECT_ROOT / "vault"

# ============================================================
# HUB_SYSTEM_PROMPT — 12-section 完整 Topic 总览（中英双语）
# 基于 Know.md 新格式
# ============================================================
HUB_SYSTEM_PROMPT = """You are a senior Cambridge International A-Level Physics (9702) and Edexcel A-Level physics teacher, examiner, curriculum designer, and knowledge graph architect.

Your task is to create a COMPLETE KNOWLEDGE GRAPH NODE in Markdown format for a specific Physics topic.

The output will be stored inside an Obsidian-based Physics Knowledge Graph and used for RAG retrieval.

The content must simultaneously satisfy:
- Cambridge 9702 syllabus requirements
- Edexcel A-Level physics syllabus requirements
- Textbook-level explanations
- Exam preparation needs
- Knowledge graph linking
- Retrieval-Augmented Generation (RAG) optimisation

Write in clear educational English suitable for A-Level students.

CORE WRITING RULES:
1. Use Markdown only.
2. Use Obsidian wiki-links [[Topic]] for concept related — LIBERALLY, in ALL sections, not just one.
3. Use LaTeX $$ for display equations, $ for inline.
4. Use Mermaid for diagrams and concept maps.
5. Be extremely detailed.
6. Never skip derivations if examinable.
7. Include examiner-style language.
8. Include practical skills.
9. Include image prompts with 📷 emoji in blockquote format.
10. Optimise for knowledge graph linking and RAG retrieval.
11. Ensure the note can function independently without external references.
12. ALL sections MUST be bilingual: English first, then Chinese (中文). Format each section as:
    **English:** [text]
    **中文 / 中文：** [Chinese translation]
13. Exam-board differences marked with blockquote:
    > 📋 **CIE Only:** ...
    > 📋 **Edexcel Only:** ...
14. Past Paper references use placeholder: 📝 *待填入*
15. ALL 12 sections below are MANDATORY. You have ample output space — do NOT skip any section.

---

# OUTPUT STRUCTURE (12 sections — ALL MANDATORY)

---

# 1. Overview / 概述

Provide a concise introduction.

Include:
* What this topic studies
* Why it matters in Physics
* Real-world applications
* Importance in Cambridge 9702 and Edexcel IAL examinations

**English:** (2-3 paragraphs)
**中文:** (Chinese translation)

---

# 2. Syllabus Learning Objectives / 考纲学习目标

List all syllabus requirements relevant to this topic.

Format as a two-column table:
| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| ... | ... |

Include examiner expectations (EN+CN).

Use 📋 callouts for board-specific differences:
> 📋 **CIE Only:** ...
> 📋 **Edexcel Only:** ...

---

# 3. Core Definitions / 核心定义

Create a bilingual table:

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|

Include:
* official definitions with exam-standard wording
* common mistakes students make
* Link terms with [[wikilinks]]

---

# 4. Key Concepts Explained / 关键概念详解

Explain every major concept.

For EACH concept:

## 4.X Concept Name / 概念名称

### Explanation / 解释
**English:** Detailed explanation with [[wikilinks]] to related concepts.
**中文:** Chinese translation.

### Physical Meaning / 物理意义
**English:** What it means in real life.
**中文:** Chinese translation.

### Common Misconceptions / 常见误区
List frequent student errors (EN+CN).

### Exam Tips / 考试提示
**English:** How Cambridge/Edexcel typically assesses it.
**中文:** Chinese translation.

Include 📷 image prompts where a diagram helps.

---

# 5. Essential Equations / 核心公式

For EVERY equation provide:

## 5.X Equation Name / 公式名称

**Equation / 公式:**
$$ LaTeX $$

**Variables / 变量:**
| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|

**Derivation / 推导:**
Show derivation if required by syllabus (EN+CN).

**Conditions / 适用条件:**
When it can be applied (EN+CN).

**Limitations / 局限性:**
When it cannot be applied (EN+CN).

**Rearrangements / 变形:**
Common algebraic forms (EN+CN).

---

# 6. Graphs and Relationships / 图表与关系

Include all relevant graphs.

For EACH graph:

## 6.X Graph Name / 图表名称

### Axes / 坐标轴
(EN+CN)

### Shape / 形状
(EN+CN)

### Gradient Meaning / 斜率含义
(EN+CN)

### Area Meaning / 面积含义
(EN+CN)

### Exam Interpretation / 考试解读
(EN+CN)

### Common Questions / 常见问题
(EN+CN)

Use Mermaid diagrams where possible.
Include 📷 prompts for graphs.

---

# 7. Required Diagrams / 必备图表

Generate a list of at least 3 diagrams needed.

For EACH diagram:

## 7.X Diagram Name / 图表名称

### Description / 描述
**English:** Detailed description.
**中文:** Chinese description.

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — [CODE]: [Title]**
>
> Ultra-detailed prompt suitable for AI image generation (Midjourney/DALL·E/Stable Diffusion).
> Include: layout, perspective, colors, labels, lighting, style direction.

### Labels Required / 需要标注
List all labels (EN+CN).

### Exam Importance / 考试重要性
Why Cambridge/Edexcel uses this diagram (EN+CN).

---

# 8. Worked Examples / 典型例题

Provide at least 2 examples.

For EACH:

## Example X: [Title] / [标题]

### Question / 题目
**English:** Question text.
**中文:** Chinese translation.

### Image Prompt / 图片提示
> 📷 **IMAGE PROMPT — [CODE]: [Diagram for question]**
> (If a diagram is needed for the question)

### Solution / 解答
Step-by-step with LaTeX.

### Final Answer / 最终答案
**Answer:** ... | **答案：** ...

### Examiner Notes / 考官点评
(EN+CN)

### Alternative Method / 替代方法
(If applicable, EN+CN)

---

# 9. Past Paper Question Types / 历年真题题型

Create table:

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculation / 计算 | High/Med/Low | High/Med/Low | 📝 *待填入* |
| Explanation / 解释 | ... | ... | 📝 *待填入* |
| Graph Analysis / 图表分析 | ... | ... | 📝 *待填入* |
| Practical / 实验 | ... | ... | 📝 *待填入* |
| Derivation / 推导 | ... | ... | 📝 *待填入* |

> 📝 **题库整理中 / Question Bank Under Construction:** 具体试卷编号（如 9702/23/M/J/24 Q3）将在后续整理真题后填入上表。

Mention common command words (EN+CN):
* State / 陈述
* Define / 定义
* Explain / 解释
* Describe / 描述
* Calculate / 计算
* Determine / 确定
* Suggest / 建议

---

# 10. Practical Skills Connections / 实验技能链接

Link topic to:
* CAIE Paper 3 (AS) / Paper 5 (A2)
* Edexcel Unit 3 (AS) / Unit 6 (A2)

Include:
* measurements / 测量
* uncertainties / 不确定度
* graph plotting / 图表绘制
* experimental design / 实验设计

**English:** Detailed practical connections.
**中文:** Chinese translation.

> 📋 Board-specific practical callouts.

---

# 11. Concept Map / 概念图谱

Create Mermaid concept map:

```mermaid
graph TD
    %% Show connections between this topic, prerequisites, related topics, and sub-topics
```

The concept map should show:
* This topic's sub-topics
* Prerequisites from other modules
* Related topics
* Upward/downward connections

---

# 12. Quick Revision Sheet / 速查表

Create a one-page bilingual summary table:

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| Definitions / 定义 | ... |
| Equations / 公式 | ... |
| Graphs / 图表 | ... |
| Key Facts / 关键事实 | ... |
| Exam Reminders / 考试提醒 | ... |

---

⚠️ CRITICAL: ALL 12 sections are MANDATORY. Count your sections before finishing. You have 32000 output tokens — more than enough.
Do NOT skip any section. Do NOT merge sections.
"""

# ============================================================
# LEAF_SYSTEM_PROMPT — 12-part 叶子节点（中英双语）
# ============================================================
LEAF_SYSTEM_PROMPT = """You are a senior Cambridge International A-Level Physics (9702) and Edexcel A-Level physics teacher, examiner, curriculum designer, and knowledge graph architect.

Your output is a LEAF NODE — a focused, standalone piece of content on one specific sub-topic within a larger Physics knowledge graph.

It will be:
1. A standalone Obsidian note
2. A knowledge graph leaf node
3. Used for RAG retrieval
4. Displayed as a detail card in a web frontend

CRITICAL WRITING RULES:
- ALL content MUST be bilingual: English first, then Chinese (中文)
- Use [[wikilinks]] LIBERALLY to link to:
  - The parent Hub: [[Parent Topic Name]]
  - Related sub-topics within the same topic
  - Prerequisite concepts from other topics
- Use LaTeX $$ for display equations, $ for inline
- Use Mermaid for diagrams where possible
- Use blockquote for image prompts with 📷 emoji:
  > 📷 **IMAGE PROMPT — [CODE]: [Title]** ...
- Use blockquote for exam-board differences:
  > 📋 **CIE Only:** ...
  > 📋 **Edexcel Only:** ...
- Keep content FOCUSED on this specific sub-topic — don't expand into the whole topic
- Write clearly for A-Level students
- ALL 12 sections are MANDATORY

---

# OUTPUT STRUCTURE (12 sections — ALL MANDATORY)

---

# 1. Overview / 概述

**English:**
Brief focused introduction (2-3 paragraphs). What this sub-topic covers, why it matters, and how it fits into the broader [[Parent Topic Name]] topic.

**中文:**
简要介绍 (2-3段)。本子知识点涵盖的内容、重要性、以及和 [[Parent Topic Name]] 的关系。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| specific objective | specific objective |

Examiner expectations for this sub-topic (EN+CN).

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Term** / 术语 | Exam-standard English definition | 考试标准中文定义 | Common error |

Include 3-6 key terms specific to this sub-topic. Link with [[wikilinks]].

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 [Main Concept] / [主要概念]

### Explanation / 解释
**English:** Detailed explanation with [[wikilinks]].
**中文:** Chinese translation.

### Physical Meaning / 物理意义
**English:** What it means physically.
**中文:** Chinese translation.

### Common Misconceptions / 常见误区
(EN+CN bullet list)

### Exam Tips / 考试提示
(EN+CN)

Include 📷 image prompts where a diagram helps.

---

# 5. Essential Equations / 核心公式

For each key equation:

$$ LaTeX $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|

**Derivation / 推导:** (if applicable)
**Conditions / 适用条件:** (EN+CN)
**Limitations / 局限性:** (EN+CN)

> 📷 **IMAGE PROMPT — [CODE]: [Formula Diagram]**
> (if a diagram helps)

---

# 6. Graphs and Relationships / 图表与关系

Include relevant graphs for this sub-topic.

## 6.X Graph Name / 图表名称

### Axes / 坐标轴 (EN+CN)
### Shape / 形状 (EN+CN)
### Gradient Meaning / 斜率含义 (EN+CN)
### Area Meaning / 面积含义 (EN+CN)
### Exam Interpretation / 考试解读 (EN+CN)

Include Mermaid or 📷 prompts.

---

# 7. Required Diagrams / 必备图表

At least 1-2 diagrams:

## 7.X Diagram Name / 图表名称

### Description / 描述 (EN+CN)

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — [CODE]: [Title]**
> Ultra-detailed AI image generation prompt.

### Labels Required / 需要标注 (EN+CN)

### Exam Importance / 考试重要性 (EN+CN)

---

# 8. Worked Examples / 典型例题

Provide 1-2 focused examples:

## Example X: [Title] / [标题]

### Question / 题目
**English:** ...
**中文:** ...

### Solution / 解答
Step-by-step with LaTeX.

### Final Answer / 最终答案
**Answer:** ... | **答案：** ...

### Quick Tip / 提示
(EN+CN)

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| ... | ... | ... | 📝 *待填入* |

Common command words for this sub-topic (EN+CN).

---

# 10. Practical Skills Connections / 实验技能链接

**English:** How this sub-topic connects to practical papers.
**中文:** 本子知识点与实验考试的联系。

Include: measurements, uncertainties, graph plotting, experimental design.

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Show connections for this leaf node
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| Definition / 定义 | ... |
| Key Formula / 核心公式 | ... |
| Key Graph / 核心图表 | ... |
| Exam Tip / 考试提示 | ... |

---

Generate the complete bilingual leaf note now. Stay FOCUSED on this specific sub-topic only.
"""


def safe_path(name: str) -> str:
    """Replace filesystem-unsafe characters in topic/folder names."""
    return name.replace("/", "-").replace("\\", "-").replace(":", " -").replace("?", "").replace("*", "-")


# ============================================================
# ALL_TOPICS — 完整 12 章节 × N 知识点
# ============================================================
ALL_TOPICS = {
    # ════════════════════════════════════════════════════════
    # 01-Mechanics (已完成，此处保留用于 --chapter mechanics 重新生成)
    # ════════════════════════════════════════════════════════
    "01-Mechanics": [
        # ── 01-Kinematics ──
        {
            "section": "01-Kinematics",
            "title": "Scalars and Vectors",
            "syllabus_ref_cie": "3.1 (a-c)",
            "syllabus_ref_edexcel": "WPH11 U1: 1.1-1.3",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": [],
            "related_topics": [
                "Displacement, Velocity and Acceleration",
                "Projectile Motion",
                "Types of Force",
            ],
            "sub_topics": [
                "Scalar Quantities",
                "Vector Quantities",
                "Vector Addition and Subtraction",
                "Resolution of Vectors",
            ],
        },
        {
            "section": "01-Kinematics",
            "title": "Displacement, Velocity and Acceleration",
            "syllabus_ref_cie": "3.1 (d-f)",
            "syllabus_ref_edexcel": "WPH11 U1: 1.4-1.8",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": ["Scalars and Vectors"],
            "related_topics": ["Motion Graphs", "Equations of Motion (SUVAT)"],
            "sub_topics": [
                "Displacement and Distance",
                "Speed and Velocity",
                "Acceleration",
                "Terminal Velocity",
            ],
        },
        {
            "section": "01-Kinematics",
            "title": "Equations of Motion (SUVAT)",
            "syllabus_ref_cie": "3.1 (g-k)",
            "syllabus_ref_edexcel": "WPH11 U1: 1.9-1.12",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Displacement, Velocity and Acceleration"],
            "related_topics": ["Motion Graphs", "Projectile Motion"],
            "sub_topics": [
                "The Five SUVAT Equations",
                "Choosing the Right Equation",
                "Free Fall Under Gravity",
                "Two-Stage Motion Problems",
            ],
        },
        {
            "section": "01-Kinematics",
            "title": "Motion Graphs",
            "syllabus_ref_cie": "3.1 (j)",
            "syllabus_ref_edexcel": "WPH11 U1: 1.5-1.8",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": ["Displacement, Velocity and Acceleration"],
            "related_topics": ["Equations of Motion (SUVAT)"],
            "sub_topics": [
                "Displacement-Time Graphs",
                "Velocity-Time Graphs",
                "Acceleration-Time Graphs",
                "Interpreting Gradient and Area",
            ],
        },
        {
            "section": "01-Kinematics",
            "title": "Projectile Motion",
            "syllabus_ref_cie": "3.1 (l-m)",
            "syllabus_ref_edexcel": "WPH11 U1: 1.13-1.16",
            "level": "AS",
            "difficulty": "advanced",
            "prerequisites": ["Scalars and Vectors", "Equations of Motion (SUVAT)"],
            "related_topics": ["Newton's Laws of Motion"],
            "sub_topics": [
                "Horizontal and Vertical Components",
                "Time of Flight and Range",
                "Maximum Height",
                "Projectile Motion Graphs",
            ],
        },
        # ── 02-Forces ──
        {
            "section": "02-Forces",
            "title": "Types of Force",
            "syllabus_ref_cie": "3.2 (a)",
            "syllabus_ref_edexcel": "WPH11 U1: 2.1-2.3",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": ["Scalars and Vectors"],
            "related_topics": ["Free-body Diagrams", "Forces in Fluids (Upthrust and Viscous Force)"],
            "sub_topics": [
                "Weight and Gravitational Force",
                "Normal Contact Force",
                "Tension",
                "Friction",
            ],
        },
        {
            "section": "02-Forces",
            "title": "Free-body Diagrams",
            "syllabus_ref_cie": "3.2 (b-c)",
            "syllabus_ref_edexcel": "WPH11 U1: 2.4-2.6",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": ["Types of Force"],
            "related_topics": ["Newton's Laws of Motion"],
            "sub_topics": [
                "Drawing Free-body Diagrams",
                "Resolving Forces on Inclined Planes",
                "Equilibrium Conditions",
            ],
        },
        {
            "section": "02-Forces",
            "title": "Newton's Laws of Motion",
            "syllabus_ref_cie": "3.2 (d-e)",
            "syllabus_ref_edexcel": "WPH11 U1: 2.7-2.10",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Free-body Diagrams"],
            "related_topics": ["Linear Momentum and Impulse", "Conservation of Momentum"],
            "sub_topics": [
                "Newton's First Law (Inertia)",
                "Newton's Second Law (F=ma)",
                "Newton's Third Law (Action-Reaction)",
                "Applications of Newton's Laws",
            ],
        },
        {
            "section": "02-Forces",
            "title": "Linear Momentum and Impulse",
            "syllabus_ref_cie": "3.2 (f-h)",
            "syllabus_ref_edexcel": "WPH11 U1: 2.11-2.14",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Newton's Laws of Motion"],
            "related_topics": ["Conservation of Momentum"],
            "sub_topics": [
                "Definition of Linear Momentum",
                "Impulse and Force-Time Graphs",
                "Impulse-Momentum Theorem",
            ],
        },
        {
            "section": "02-Forces",
            "title": "Conservation of Momentum",
            "syllabus_ref_cie": "3.2 (i-k)",
            "syllabus_ref_edexcel": "WPH11 U1: 2.15-2.18",
            "level": "AS",
            "difficulty": "advanced",
            "prerequisites": ["Linear Momentum and Impulse"],
            "related_topics": ["Newton's Laws of Motion"],
            "sub_topics": [
                "Elastic Collisions",
                "Inelastic Collisions",
                "Explosions and Recoil",
                "Two-Dimensional Collisions",
            ],
        },
        {
            "section": "02-Forces",
            "title": "Forces in Fluids (Upthrust and Viscous Force)",
            "syllabus_ref_cie": "3.2 (l-m)",
            "syllabus_ref_edexcel": "WPH11 U1: 3.1-3.5",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Types of Force"],
            "related_topics": ["Work Done by a Force"],
            "sub_topics": [
                "Upthrust and Archimedes' Principle",
                "Viscous Drag and Stokes' Law",
                "Terminal Velocity in Fluids",
            ],
        },
        # ── 03-Work-Energy-Power ──
        {
            "section": "03-Work-Energy-Power",
            "title": "Work Done by a Force",
            "syllabus_ref_cie": "3.3 (a-b)",
            "syllabus_ref_edexcel": "WPH11 U1: 4.1-4.4",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": ["Scalars and Vectors", "Newton's Laws of Motion"],
            "related_topics": ["Kinetic Energy and Potential Energy"],
            "sub_topics": [
                "Definition of Work",
                "Work Done by a Force at an Angle",
                "Force-Displacement Graphs",
            ],
        },
        {
            "section": "03-Work-Energy-Power",
            "title": "Kinetic Energy and Potential Energy",
            "syllabus_ref_cie": "3.3 (c-f)",
            "syllabus_ref_edexcel": "WPH11 U1: 4.5-4.8",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Work Done by a Force"],
            "related_topics": ["Conservation of Energy"],
            "sub_topics": [
                "Kinetic Energy (KE)",
                "Gravitational Potential Energy (GPE)",
                "Elastic Potential Energy",
                "Work-Energy Theorem",
            ],
        },
        {
            "section": "03-Work-Energy-Power",
            "title": "Conservation of Energy",
            "syllabus_ref_cie": "3.3 (g)",
            "syllabus_ref_edexcel": "WPH11 U1: 4.9-4.11",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Kinetic Energy and Potential Energy"],
            "related_topics": ["Power and Efficiency"],
            "sub_topics": [
                "Principle of Conservation of Energy",
                "Energy Transfers in Mechanical Systems",
                "Dissipative Forces and Energy Loss",
            ],
        },
        {
            "section": "03-Work-Energy-Power",
            "title": "Power and Efficiency",
            "syllabus_ref_cie": "3.3 (h-k)",
            "syllabus_ref_edexcel": "WPH11 U1: 4.12-4.15",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": ["Work Done by a Force", "Conservation of Energy"],
            "related_topics": [],
            "sub_topics": [
                "Definition of Power",
                "Power and Velocity",
                "Efficiency of Energy Transfers",
            ],
        },
        # ── 04-Circular-Motion (A2) ──
        {
            "section": "04-Circular-Motion",
            "title": "Angular Measures",
            "syllabus_ref_cie": "14.1 (a-e)",
            "syllabus_ref_edexcel": "WPH14 U4: 5.1-5.4",
            "level": "A2",
            "difficulty": "foundation",
            "prerequisites": ["Displacement, Velocity and Acceleration"],
            "related_topics": ["Centripetal Acceleration and Force"],
            "sub_topics": [
                "Radians and Angular Displacement",
                "Angular Velocity",
                "Period and Frequency",
                "Relationship Between Linear and Angular Quantities",
            ],
        },
        {
            "section": "04-Circular-Motion",
            "title": "Centripetal Acceleration and Force",
            "syllabus_ref_cie": "14.2 (a-d)",
            "syllabus_ref_edexcel": "WPH14 U4: 5.5-5.9",
            "level": "A2",
            "difficulty": "advanced",
            "prerequisites": ["Angular Measures", "Newton's Laws of Motion"],
            "related_topics": ["Gravitational Force and Field", "Circular Orbits"],
            "sub_topics": [
                "Centripetal Acceleration Formula",
                "Centripetal Force",
                "Banked Tracks and Conical Pendulum",
            ],
        },
        # ── 05-Gravitational-Fields (A2) ──
        {
            "section": "05-Gravitational-Fields",
            "title": "Gravitational Force and Field",
            "syllabus_ref_cie": "15.1 (a-d)",
            "syllabus_ref_edexcel": "WPH14 U4: 6.1-6.5",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Newton's Laws of Motion", "Centripetal Acceleration and Force"],
            "related_topics": ["Gravitational Potential", "Circular Orbits"],
            "sub_topics": [
                "Newton's Law of Universal Gravitation",
                "Gravitational Field Strength",
                "Radial vs Uniform Gravitational Fields",
            ],
        },
        {
            "section": "05-Gravitational-Fields",
            "title": "Gravitational Potential",
            "syllabus_ref_cie": "15.2 (a-f)",
            "syllabus_ref_edexcel": "WPH14 U4: 6.6-6.10",
            "level": "A2",
            "difficulty": "advanced",
            "prerequisites": ["Gravitational Force and Field", "Kinetic Energy and Potential Energy"],
            "related_topics": ["Circular Orbits"],
            "sub_topics": [
                "Gravitational Potential Energy in a Radial Field",
                "Gravitational Potential (V)",
                "Escape Velocity",
                "Potential Gradients",
            ],
        },
        {
            "section": "05-Gravitational-Fields",
            "title": "Circular Orbits",
            "syllabus_ref_cie": "15.3 (a-e)",
            "syllabus_ref_edexcel": "WPH14 U4: 6.11-6.15",
            "level": "A2",
            "difficulty": "advanced",
            "prerequisites": ["Gravitational Force and Field", "Centripetal Acceleration and Force"],
            "related_topics": ["Gravitational Potential"],
            "sub_topics": [
                "Orbital Velocity",
                "Kepler's Third Law",
                "Geostationary Satellites",
            ],
        },
        # ── 06-Oscillations (A2) ──
        {
            "section": "06-Oscillations",
            "title": "Simple Harmonic Motion",
            "syllabus_ref_cie": "17.1 (a-d)",
            "syllabus_ref_edexcel": "WPH14 U4: 7.1-7.5",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Equations of Motion (SUVAT)", "Angular Measures"],
            "related_topics": ["Energy in SHM"],
            "sub_topics": [
                "Conditions for SHM",
                "Displacement, Velocity and Acceleration in SHM",
                "The Simple Pendulum",
                "Mass-Spring System",
            ],
        },
        {
            "section": "06-Oscillations",
            "title": "Energy in SHM",
            "syllabus_ref_cie": "17.2 (a-c)",
            "syllabus_ref_edexcel": "WPH14 U4: 7.6-7.8",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Simple Harmonic Motion", "Kinetic Energy and Potential Energy"],
            "related_topics": ["Damped and Forced Oscillations - Resonance"],
            "sub_topics": [
                "KE and PE in SHM",
                "Energy-Time Graphs for SHM",
                "Energy-Displacement Graphs for SHM",
            ],
        },
        {
            "section": "06-Oscillations",
            "title": "Damped and Forced Oscillations - Resonance",
            "syllabus_ref_cie": "17.3 (a-d)",
            "syllabus_ref_edexcel": "WPH14 U4: 7.9-7.13",
            "level": "A2",
            "difficulty": "advanced",
            "prerequisites": ["Energy in SHM"],
            "related_topics": [],
            "sub_topics": [
                "Light, Critical and Heavy Damping",
                "Forced Oscillations",
                "Resonance and the Barton Pendulum",
            ],
        },
    ],

    # ════════════════════════════════════════════════════════
    # 02-Waves / 波动
    # ════════════════════════════════════════════════════════
    "02-Waves": [
        # ── 01-Wave-Properties ──
        {
            "section": "01-Wave-Properties",
            "title": "Progressive Waves",
            "syllabus_ref_cie": "7.1 (a-e)",
            "syllabus_ref_edexcel": "WPH11 U2: 5.1-5.5",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": ["Displacement, Velocity and Acceleration", "Simple Harmonic Motion"],
            "related_topics": ["Superposition and Interference", "Polarisation", "The Doppler Effect"],
            "sub_topics": [
                "Transverse and Longitudinal Waves",
                "Wave Speed, Frequency and Wavelength",
                "The Wave Equation",
                "Phase and Phase Difference",
                "Intensity and Amplitude",
            ],
        },
        {
            "section": "01-Wave-Properties",
            "title": "Polarisation",
            "syllabus_ref_cie": "7.2 (a-d)",
            "syllabus_ref_edexcel": "WPH11 U2: 5.6-5.8",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Progressive Waves"],
            "related_topics": ["Superposition and Interference"],
            "sub_topics": [
                "What is Polarisation",
                "Polarisation by Filters (Malus's Law)",
                "Polarisation by Reflection (Brewster's Angle)",
                "Applications of Polarisation",
            ],
        },
        {
            "section": "01-Wave-Properties",
            "title": "The Doppler Effect",
            "syllabus_ref_cie": "7.3 (a-d)",
            "syllabus_ref_edexcel": "WPH11 U2: 5.9-5.11",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Progressive Waves"],
            "related_topics": ["Superposition and Interference"],
            "sub_topics": [
                "The Doppler Effect Explained",
                "Doppler Equation for Sound",
                "Doppler Effect for Light (Redshift and Blueshift)",
                "Applications (Radar, Astronomy, Medical Ultrasound)",
            ],
        },
        # ── 02-Superposition ──
        {
            "section": "02-Superposition",
            "title": "Superposition and Interference",
            "syllabus_ref_cie": "8.1 (a-e)",
            "syllabus_ref_edexcel": "WPH11 U2: 5.12-5.16",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Progressive Waves"],
            "related_topics": ["Stationary Waves", "Diffraction and the Diffraction Grating"],
            "sub_topics": [
                "Principle of Superposition",
                "Constructive and Destructive Interference",
                "Path Difference and Phase Difference",
                "Young's Double-Slit Experiment",
            ],
        },
        {
            "section": "02-Superposition",
            "title": "Stationary Waves",
            "syllabus_ref_cie": "8.2 (a-e)",
            "syllabus_ref_edexcel": "WPH11 U2: 5.17-5.20",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Superposition and Interference"],
            "related_topics": ["Diffraction and the Diffraction Grating"],
            "sub_topics": [
                "Formation of Stationary Waves",
                "Nodes and Antinodes",
                "Stationary Waves on Strings",
                "Stationary Waves in Pipes (Open and Closed)",
            ],
        },
        {
            "section": "02-Superposition",
            "title": "Diffraction and the Diffraction Grating",
            "syllabus_ref_cie": "8.3 (a-e)",
            "syllabus_ref_edexcel": "WPH11 U2: 5.21-5.25",
            "level": "AS",
            "difficulty": "advanced",
            "prerequisites": ["Superposition and Interference"],
            "related_topics": ["Stationary Waves"],
            "sub_topics": [
                "Diffraction at a Single Slit",
                "The Diffraction Grating Equation",
                "Grating Spectra and Line Spacing",
                "Applications of Diffraction Gratings",
            ],
        },
        # ── 03-Optics ──
        {
            "section": "03-Optics",
            "title": "Refraction and Total Internal Reflection",
            "syllabus_ref_cie": "8.4 (a-f)",
            "syllabus_ref_edexcel": "WPH11 U2: 5.26-5.30",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Progressive Waves"],
            "related_topics": ["Superposition and Interference"],
            "sub_topics": [
                "Refraction and Snell's Law",
                "Refractive Index",
                "Total Internal Reflection",
                "Critical Angle",
                "Optical Fibres and Their Applications",
            ],
        },
        {
            "section": "03-Optics",
            "title": "Lenses and the Lens Equation",
            "syllabus_ref_cie": "8.5 (a-d)",
            "syllabus_ref_edexcel": "WPH11 U2: 5.31-5.34",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Refraction and Total Internal Reflection"],
            "related_topics": [],
            "sub_topics": [
                "Converging and Diverging Lenses",
                "Ray Diagrams for Lenses",
                "The Thin Lens Equation",
                "Magnification and Power of a Lens",
            ],
        },
    ],

    # ════════════════════════════════════════════════════════
    # 03-Electricity / 电学
    # ════════════════════════════════════════════════════════
    "03-Electricity": [
        # ── 01-DC-Circuits ──
        {
            "section": "01-DC-Circuits",
            "title": "Electric Current and Charge",
            "syllabus_ref_cie": "9.1 (a-d)",
            "syllabus_ref_edexcel": "WPH11 U2: 3.1-3.4",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": [],
            "related_topics": ["Potential Difference and EMF", "Resistance and Resistivity"],
            "sub_topics": [
                "Definition of Electric Current",
                "Charge Carriers (Electrons, Ions)",
                "The Ampere and the Coulomb",
                "Conventional Current vs Electron Flow",
                "Current in Series and Parallel Circuits",
            ],
        },
        {
            "section": "01-DC-Circuits",
            "title": "Potential Difference and EMF",
            "syllabus_ref_cie": "9.2 (a-e)",
            "syllabus_ref_edexcel": "WPH11 U2: 3.5-3.8",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": ["Electric Current and Charge"],
            "related_topics": ["Resistance and Resistivity", "Kirchhoff's Laws"],
            "sub_topics": [
                "Potential Difference (PD)",
                "Electromotive Force (EMF)",
                "PD vs EMF — Key Differences",
                "Energy Transfer in Circuits",
                "Measuring PD and EMF",
            ],
        },
        {
            "section": "01-DC-Circuits",
            "title": "Resistance and Resistivity",
            "syllabus_ref_cie": "9.3 (a-f)",
            "syllabus_ref_edexcel": "WPH11 U2: 3.9-3.12",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Potential Difference and EMF"],
            "related_topics": ["I-V Characteristics", "Kirchhoff's Laws"],
            "sub_topics": [
                "Ohm's Law",
                "Resistance and the Ohm",
                "Resistivity and the Resistivity Equation",
                "Factors Affecting Resistance",
                "Resistors in Series and Parallel",
            ],
        },
        {
            "section": "01-DC-Circuits",
            "title": "I-V Characteristics",
            "syllabus_ref_cie": "9.3 (g-j)",
            "syllabus_ref_edexcel": "WPH11 U2: 3.13-3.16",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Resistance and Resistivity"],
            "related_topics": ["Potential Dividers"],
            "sub_topics": [
                "Ohmic Conductor I-V Graph",
                "Filament Lamp I-V Graph",
                "Semiconductor Diode I-V Graph",
                "Thermistor and LDR Characteristics",
            ],
        },
        {
            "section": "01-DC-Circuits",
            "title": "Kirchhoff's Laws",
            "syllabus_ref_cie": "9.4 (a-d)",
            "syllabus_ref_edexcel": "WPH11 U2: 3.17-3.20",
            "level": "AS",
            "difficulty": "advanced",
            "prerequisites": ["Potential Difference and EMF", "Resistance and Resistivity"],
            "related_topics": ["Potential Dividers"],
            "sub_topics": [
                "Kirchhoff's First Law (Current Law)",
                "Kirchhoff's Second Law (Voltage Law)",
                "Applying Kirchhoff's Laws to Circuits",
                "Solving Multi-loop Circuit Problems",
            ],
        },
        {
            "section": "01-DC-Circuits",
            "title": "Potential Dividers",
            "syllabus_ref_cie": "9.5 (a-e)",
            "syllabus_ref_edexcel": "WPH11 U2: 3.21-3.24",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Resistance and Resistivity", "Kirchhoff's Laws"],
            "related_topics": ["I-V Characteristics"],
            "sub_topics": [
                "The Potential Divider Formula",
                "Potentiometers and Variable Resistors",
                "Sensing Circuits (Thermistor, LDR)",
                "Loading Effect and Practical Considerations",
            ],
        },
        # ── 02-Capacitors ──
        {
            "section": "02-Capacitors",
            "title": "Capacitance and Capacitors",
            "syllabus_ref_cie": "19.1 (a-d)",
            "syllabus_ref_edexcel": "WPH14 U4: 4.1-4.5",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Potential Difference and EMF"],
            "related_topics": ["Energy Stored in a Capacitor", "Charging and Discharging Capacitors"],
            "sub_topics": [
                "Definition of Capacitance",
                "Parallel Plate Capacitor",
                "Dielectrics and Permittivity",
                "Capacitors in Series and Parallel",
            ],
        },
        {
            "section": "02-Capacitors",
            "title": "Energy Stored in a Capacitor",
            "syllabus_ref_cie": "19.2 (a-c)",
            "syllabus_ref_edexcel": "WPH14 U4: 4.6-4.8",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Capacitance and Capacitors"],
            "related_topics": ["Charging and Discharging Capacitors"],
            "sub_topics": [
                "Energy Stored Formula",
                "Area Under Q-V Graph",
                "Energy Density in Electric Fields",
            ],
        },
        {
            "section": "02-Capacitors",
            "title": "Charging and Discharging Capacitors",
            "syllabus_ref_cie": "19.3 (a-g)",
            "syllabus_ref_edexcel": "WPH14 U4: 4.9-4.14",
            "level": "A2",
            "difficulty": "advanced",
            "prerequisites": ["Capacitance and Capacitors", "Energy Stored in a Capacitor"],
            "related_topics": [],
            "sub_topics": [
                "RC Time Constant",
                "Charging Curve (Exponential Growth)",
                "Discharging Curve (Exponential Decay)",
                "Graphical Analysis of Charging/Discharging",
                "Applications (Flash Photography, Smoothing, Timing)",
            ],
        },
    ],

    # ════════════════════════════════════════════════════════
    # 04-Fields / 场
    # ════════════════════════════════════════════════════════
    "04-Fields": [
        # ── 01-Electric-Fields ──
        {
            "section": "01-Electric-Fields",
            "title": "Electric Fields and Coulomb's Law",
            "syllabus_ref_cie": "18.1 (a-e)",
            "syllabus_ref_edexcel": "WPH14 U4: 2.1-2.5",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Scalars and Vectors", "Gravitational Force and Field"],
            "related_topics": ["Electric Potential", "Capacitance and Capacitors"],
            "sub_topics": [
                "Electric Field Concept and Field Lines",
                "Coulomb's Law",
                "Electric Field Strength",
                "Uniform vs Radial Electric Fields",
                "Electric Field Between Parallel Plates",
            ],
        },
        {
            "section": "01-Electric-Fields",
            "title": "Electric Potential",
            "syllabus_ref_cie": "18.2 (a-f)",
            "syllabus_ref_edexcel": "WPH14 U4: 2.6-2.10",
            "level": "A2",
            "difficulty": "advanced",
            "prerequisites": ["Electric Fields and Coulomb's Law"],
            "related_topics": ["Capacitance and Capacitors", "Gravitational Potential"],
            "sub_topics": [
                "Electric Potential Energy",
                "Electric Potential (V)",
                "Potential Gradients and Field Strength",
                "Equipotential Surfaces",
                "Motion of Charged Particles in Electric Fields",
            ],
        },
        # ── 02-Magnetic-Fields ──
        {
            "section": "02-Magnetic-Fields",
            "title": "Magnetic Fields and Forces",
            "syllabus_ref_cie": "20.1 (a-e)",
            "syllabus_ref_edexcel": "WPH14 U4: 3.1-3.5",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Electric Fields and Coulomb's Law"],
            "related_topics": ["Electromagnetic Induction"],
            "sub_topics": [
                "Magnetic Field Concept and Flux Density",
                "Force on a Current-Carrying Conductor (F=BIL)",
                "Force on a Moving Charge (F=Bqv)",
                "Hall Effect and Hall Voltage",
                "Motion of Charged Particles in Magnetic Fields",
            ],
        },
        {
            "section": "02-Magnetic-Fields",
            "title": "Magnetic Fields of Current-Carrying Conductors",
            "syllabus_ref_cie": "20.2 (a-d)",
            "syllabus_ref_edexcel": "WPH14 U4: 3.6-3.9",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Magnetic Fields and Forces"],
            "related_topics": ["Electromagnetic Induction"],
            "sub_topics": [
                "Magnetic Field Around a Straight Wire",
                "Magnetic Field of a Solenoid",
                "Ampere's Law (Qualitative)",
                "Force Between Parallel Current-Carrying Wires",
            ],
        },
        # ── 03-Electromagnetic-Induction ──
        {
            "section": "03-Electromagnetic-Induction",
            "title": "Electromagnetic Induction",
            "syllabus_ref_cie": "20.3 (a-g)",
            "syllabus_ref_edexcel": "WPH14 U4: 3.10-3.15",
            "level": "A2",
            "difficulty": "advanced",
            "prerequisites": ["Magnetic Fields and Forces"],
            "related_topics": ["AC Generators and Transformers"],
            "sub_topics": [
                "Magnetic Flux and Flux Linkage",
                "Faraday's Law of Electromagnetic Induction",
                "Lenz's Law and the Direction of Induced EMF",
                "Induced EMF in a Moving Conductor",
                "Eddy Currents and Their Applications",
            ],
        },
        {
            "section": "03-Electromagnetic-Induction",
            "title": "AC Generators and Transformers",
            "syllabus_ref_cie": "20.4 (a-f)",
            "syllabus_ref_edexcel": "WPH14 U4: 3.16-3.20",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Electromagnetic Induction"],
            "related_topics": [],
            "sub_topics": [
                "AC Generator (Alternator) Principle",
                "RMS and Peak Values",
                "The Ideal Transformer",
                "Transformer Efficiency and Power Losses",
                "Power Transmission and the National Grid",
            ],
        },
    ],

    # ════════════════════════════════════════════════════════
    # 05-Thermal-Physics / 热物理
    # ════════════════════════════════════════════════════════
    "05-Thermal-Physics": [
        {
            "section": "01-Thermal-Concepts",
            "title": "Temperature and Thermal Equilibrium",
            "syllabus_ref_cie": "10.1 (a-e)",
            "syllabus_ref_edexcel": "WPH11 U1: 5.1-5.4",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": [],
            "related_topics": ["Thermal Expansion", "Specific Heat Capacity and Latent Heat"],
            "sub_topics": [
                "Temperature Scales (Celsius, Kelvin)",
                "Thermal Equilibrium and the Zeroth Law",
                "Thermometers and Temperature Measurement",
                "Absolute Zero and the Kelvin Scale",
            ],
        },
        {
            "section": "01-Thermal-Concepts",
            "title": "Thermal Expansion",
            "syllabus_ref_cie": "10.2 (a-d)",
            "syllabus_ref_edexcel": "WPH11 U1: 5.5-5.7",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": ["Temperature and Thermal Equilibrium"],
            "related_topics": ["Specific Heat Capacity and Latent Heat"],
            "sub_topics": [
                "Linear Expansion",
                "Area and Volume Expansion",
                "Applications and Consequences of Thermal Expansion",
                "Bimetallic Strips and Thermostats",
            ],
        },
        {
            "section": "01-Thermal-Concepts",
            "title": "Specific Heat Capacity and Latent Heat",
            "syllabus_ref_cie": "10.3 (a-g)",
            "syllabus_ref_edexcel": "WPH11 U1: 5.8-5.12",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Temperature and Thermal Equilibrium"],
            "related_topics": ["Internal Energy", "Ideal Gases"],
            "sub_topics": [
                "Specific Heat Capacity",
                "Latent Heat of Fusion and Vaporisation",
                "Heating and Cooling Curves",
                "Experimental Determination of c and L",
                "Phase Changes and Energy",
            ],
        },
        {
            "section": "02-Kinetic-Theory",
            "title": "Internal Energy and the First Law",
            "syllabus_ref_cie": "10.4 (a-d)",
            "syllabus_ref_edexcel": "WPH11 U1: 5.13-5.16",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Specific Heat Capacity and Latent Heat"],
            "related_topics": ["Ideal Gases", "Kinetic Theory of Gases"],
            "sub_topics": [
                "Internal Energy (KE + PE of molecules)",
                "The First Law of Thermodynamics",
                "Work Done by/on a Gas",
                "Isothermal, Adiabatic, Isobaric, and Isochoric Processes",
            ],
        },
        {
            "section": "02-Kinetic-Theory",
            "title": "Ideal Gases",
            "syllabus_ref_cie": "11.1 (a-f)",
            "syllabus_ref_edexcel": "WPH11 U1: 5.17-5.22",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Temperature and Thermal Equilibrium"],
            "related_topics": ["Kinetic Theory of Gases"],
            "sub_topics": [
                "The Mole and Avogadro's Number",
                "Ideal Gas Equation (pV = nRT)",
                "Boyle's Law, Charles's Law, and the Pressure Law",
                "Ideal Gas Assumptions",
                "Real Gases vs Ideal Gases",
            ],
        },
        {
            "section": "02-Kinetic-Theory",
            "title": "Kinetic Theory of Gases",
            "syllabus_ref_cie": "11.2 (a-e)",
            "syllabus_ref_edexcel": "WPH11 U1: 5.23-5.27",
            "level": "AS",
            "difficulty": "advanced",
            "prerequisites": ["Ideal Gases"],
            "related_topics": ["Internal Energy and the First Law"],
            "sub_topics": [
                "Kinetic Theory Assumptions",
                "Derivation of pV = (1/3)Nm(c_rms)^2",
                "Root Mean Square Speed",
                "Mean Kinetic Energy and Temperature",
                "The Boltzmann Constant",
            ],
        },
    ],

    # ════════════════════════════════════════════════════════
    # 06-Nuclear-and-Particle-Physics / 核与粒子物理
    # ════════════════════════════════════════════════════════
    "06-Nuclear-and-Particle-Physics": [
        {
            "section": "01-Atomic-Structure",
            "title": "Atomic Structure and the Nucleus",
            "syllabus_ref_cie": "1.1 (a-e)",
            "syllabus_ref_edexcel": "WPH11 U1: 6.1-6.5",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": [],
            "related_topics": ["Isotopes and Nuclear Reactions", "Fundamental Particles"],
            "sub_topics": [
                "The Nuclear Model of the Atom",
                "Protons, Neutrons, and Electrons",
                "Atomic Number and Mass Number",
                "Nuclide Notation",
                "The Strong Nuclear Force",
            ],
        },
        {
            "section": "01-Atomic-Structure",
            "title": "Isotopes and Nuclear Reactions",
            "syllabus_ref_cie": "1.2 (a-d)",
            "syllabus_ref_edexcel": "WPH11 U1: 6.6-6.9",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": ["Atomic Structure and the Nucleus"],
            "related_topics": ["Radioactive Decay", "Nuclear Fission and Fusion"],
            "sub_topics": [
                "Isotopes and Their Properties",
                "Mass Defect and Binding Energy",
                "Binding Energy Per Nucleon Curve",
                "Nuclear Reactions and Conservation Laws",
            ],
        },
        {
            "section": "02-Radioactivity",
            "title": "Radioactive Decay",
            "syllabus_ref_cie": "23.1 (a-g)",
            "syllabus_ref_edexcel": "WPH14 U4: 8.1-8.6",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Atomic Structure and the Nucleus"],
            "related_topics": ["Half-Life and Activity", "Alpha, Beta and Gamma Radiation"],
            "sub_topics": [
                "Types of Radioactive Decay (Alpha, Beta-, Beta+, Gamma)",
                "Decay Equations and Conservation",
                "Neutrinos and Antineutrinos",
                "The Exponential Decay Law",
            ],
        },
        {
            "section": "02-Radioactivity",
            "title": "Half-Life and Activity",
            "syllabus_ref_cie": "23.2 (a-e)",
            "syllabus_ref_edexcel": "WPH14 U4: 8.7-8.10",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Radioactive Decay"],
            "related_topics": ["Alpha, Beta and Gamma Radiation"],
            "sub_topics": [
                "Activity and the Becquerel",
                "Half-Life Definition and Calculation",
                "Decay Constant",
                "Carbon Dating and Other Applications",
            ],
        },
        {
            "section": "02-Radioactivity",
            "title": "Alpha, Beta and Gamma Radiation",
            "syllabus_ref_cie": "23.3 (a-h)",
            "syllabus_ref_edexcel": "WPH14 U4: 8.11-8.16",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Radioactive Decay"],
            "related_topics": ["Half-Life and Activity"],
            "sub_topics": [
                "Properties of Alpha Particles",
                "Properties of Beta Particles",
                "Properties of Gamma Rays",
                "Absorption and Penetration",
                "Uses and Hazards of Radiation",
            ],
        },
        {
            "section": "03-Particle-Physics",
            "title": "Fundamental Particles",
            "syllabus_ref_cie": "24.1 (a-g)",
            "syllabus_ref_edexcel": "WPH14 U4: 9.1-9.6",
            "level": "A2",
            "difficulty": "advanced",
            "prerequisites": ["Atomic Structure and the Nucleus"],
            "related_topics": ["Quarks and Leptons", "Nuclear Fission and Fusion"],
            "sub_topics": [
                "The Standard Model Overview",
                "Hadrons (Baryons and Mesons)",
                "Leptons",
                "Particle Interactions and Conservation",
            ],
        },
        {
            "section": "03-Particle-Physics",
            "title": "Quarks and Leptons",
            "syllabus_ref_cie": "24.2 (a-f)",
            "syllabus_ref_edexcel": "WPH14 U4: 9.7-9.12",
            "level": "A2",
            "difficulty": "advanced",
            "prerequisites": ["Fundamental Particles"],
            "related_topics": ["Nuclear Fission and Fusion"],
            "sub_topics": [
                "The Six Quarks (Up, Down, Strange, Charm, Top, Bottom)",
                "Quark Composition of Hadrons",
                "Beta Decay in Terms of Quarks",
                "Conservation Laws (Baryon Number, Lepton Number, Strangeness)",
            ],
        },
        {
            "section": "03-Particle-Physics",
            "title": "Nuclear Fission and Fusion",
            "syllabus_ref_cie": "24.3 (a-f)",
            "syllabus_ref_edexcel": "WPH14 U4: 9.13-9.18",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Isotopes and Nuclear Reactions", "Fundamental Particles"],
            "related_topics": ["Radioactive Decay"],
            "sub_topics": [
                "Nuclear Fission Process",
                "Chain Reactions and Critical Mass",
                "Nuclear Fusion Process",
                "Fusion in Stars",
                "Mass-Energy Equivalence (E=mc^2)",
                "Fission Reactors and Fusion Research",
            ],
        },
    ],

    # ════════════════════════════════════════════════════════
    # 07-Quantum-Physics / 量子物理
    # ════════════════════════════════════════════════════════
    "07-Quantum-Physics": [
        {
            "section": "01-Photoelectric-Effect",
            "title": "The Photoelectric Effect",
            "syllabus_ref_cie": "22.1 (a-h)",
            "syllabus_ref_edexcel": "WPH14 U4: 7.1-7.6",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Progressive Waves"],
            "related_topics": ["Wave-Particle Duality", "Energy Levels and Spectra"],
            "sub_topics": [
                "Experimental Observations of the Photoelectric Effect",
                "Failure of Classical Wave Theory",
                "Einstein's Photon Model",
                "The Photoelectric Equation",
                "Work Function and Threshold Frequency",
                "Stopping Potential and Maximum KE",
            ],
        },
        {
            "section": "02-Wave-Particle-Duality",
            "title": "Wave-Particle Duality",
            "syllabus_ref_cie": "22.2 (a-f)",
            "syllabus_ref_edexcel": "WPH14 U4: 7.7-7.12",
            "level": "A2",
            "difficulty": "advanced",
            "prerequisites": ["The Photoelectric Effect"],
            "related_topics": ["Energy Levels and Spectra"],
            "sub_topics": [
                "de Broglie Wavelength",
                "Electron Diffraction and the Davisson-Germer Experiment",
                "Wave-Particle Duality for Matter",
                "The Electron Microscope",
                "Heisenberg Uncertainty Principle (Qualitative)",
            ],
        },
        {
            "section": "03-Atomic-Spectra",
            "title": "Energy Levels and Spectra",
            "syllabus_ref_cie": "22.3 (a-g)",
            "syllabus_ref_edexcel": "WPH14 U4: 7.13-7.18",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["The Photoelectric Effect"],
            "related_topics": ["Wave-Particle Duality"],
            "sub_topics": [
                "Bohr Model of the Atom",
                "Quantised Energy Levels",
                "Emission and Absorption Spectra",
                "Hydrogen Spectrum and the Balmer Series",
                "Line Spectra as Evidence for Quantisation",
                "Fluorescence and Phosphorescence",
            ],
        },
    ],

    # ════════════════════════════════════════════════════════
    # 08-Materials / 材料物理
    # ════════════════════════════════════════════════════════
    "08-Materials": [
        {
            "section": "01-Material-Properties",
            "title": "Density, Hooke's Law and Springs",
            "syllabus_ref_cie": "6.1 (a-f)",
            "syllabus_ref_edexcel": "WPH11 U1: 2.1-2.6",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": ["Types of Force"],
            "related_topics": ["Stress, Strain and Young Modulus"],
            "sub_topics": [
                "Density and Pressure in Solids and Fluids",
                "Hooke's Law and the Spring Constant",
                "Force-Extension Graphs",
                "Elastic Limit and Plastic Deformation",
                "Springs in Series and Parallel",
                "Elastic Potential Energy in a Spring",
            ],
        },
        {
            "section": "01-Material-Properties",
            "title": "Stress, Strain and Young Modulus",
            "syllabus_ref_cie": "6.2 (a-g)",
            "syllabus_ref_edexcel": "WPH11 U1: 2.7-2.12",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Density, Hooke's Law and Springs"],
            "related_topics": ["Stress-Strain Graphs and Material Behaviour"],
            "sub_topics": [
                "Tensile Stress and Strain",
                "Young Modulus Definition and Formula",
                "Experimental Determination of Young Modulus",
                "Ultimate Tensile Strength",
                "Breaking Stress",
            ],
        },
        {
            "section": "01-Material-Properties",
            "title": "Stress-Strain Graphs and Material Behaviour",
            "syllabus_ref_cie": "6.3 (a-e)",
            "syllabus_ref_edexcel": "WPH11 U1: 2.13-2.18",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Stress, Strain and Young Modulus"],
            "related_topics": ["Density, Hooke's Law and Springs"],
            "sub_topics": [
                "Stress-Strain Graph for a Ductile Material (Copper)",
                "Stress-Strain Graph for a Brittle Material (Glass)",
                "Stress-Strain Graph for a Polymeric Material (Rubber)",
                "Elastic and Plastic Regions",
                "Necking and Fracture",
                "Material Selection for Engineering Applications",
            ],
        },
    ],

    # ════════════════════════════════════════════════════════
    # 09-Astrophysics / 天体物理
    # ════════════════════════════════════════════════════════
    "09-Astrophysics": [
        {
            "section": "01-Stellar-Properties",
            "title": "Luminosity, Radiant Flux and Black Body Radiation",
            "syllabus_ref_cie": "25.1 (a-f)",
            "syllabus_ref_edexcel": "WPH14 U4: 10.1-10.6",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Progressive Waves", "Temperature and Thermal Equilibrium"],
            "related_topics": ["Stellar Distances", "The Hertzsprung-Russell Diagram"],
            "sub_topics": [
                "Luminosity and Radiant Flux Intensity",
                "Inverse Square Law for Radiation",
                "Black Body Radiation",
                "Wien's Displacement Law",
                "Stefan-Boltzmann Law",
            ],
        },
        {
            "section": "01-Stellar-Properties",
            "title": "Stellar Distances",
            "syllabus_ref_cie": "25.2 (a-e)",
            "syllabus_ref_edexcel": "WPH14 U4: 10.7-10.12",
            "level": "A2",
            "difficulty": "advanced",
            "prerequisites": ["Luminosity, Radiant Flux and Black Body Radiation"],
            "related_topics": ["The Hertzsprung-Russell Diagram", "Cosmology"],
            "sub_topics": [
                "Astronomical Unit, Light-Year, and Parsec",
                "Stellar Parallax and Distance Measurement",
                "Standard Candles and Cepheid Variables",
                "Apparent and Absolute Magnitude",
            ],
        },
        {
            "section": "02-Stellar-Evolution",
            "title": "The Hertzsprung-Russell Diagram",
            "syllabus_ref_cie": "25.3 (a-f)",
            "syllabus_ref_edexcel": "WPH14 U4: 10.13-10.18",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Luminosity, Radiant Flux and Black Body Radiation"],
            "related_topics": ["Stellar Evolution", "Stellar Distances"],
            "sub_topics": [
                "H-R Diagram Axes and Regions",
                "Main Sequence Stars",
                "Giants, Supergiants, and White Dwarfs",
                "Spectral Classes (OBAFGKM)",
                "Using the H-R Diagram to Determine Stellar Properties",
            ],
        },
        {
            "section": "02-Stellar-Evolution",
            "title": "Stellar Evolution",
            "syllabus_ref_cie": "25.4 (a-h)",
            "syllabus_ref_edexcel": "WPH14 U4: 10.19-10.25",
            "level": "A2",
            "difficulty": "advanced",
            "prerequisites": ["The Hertzsprung-Russell Diagram"],
            "related_topics": ["Cosmology"],
            "sub_topics": [
                "Star Formation (Nebulae and Protostars)",
                "Main Sequence Lifetime",
                "Evolution of Low-Mass Stars (Sun-like → Red Giant → White Dwarf)",
                "Evolution of High-Mass Stars → Supernova → Neutron Star / Black Hole",
                "Nucleosynthesis in Stars",
            ],
        },
        {
            "section": "03-Cosmology",
            "title": "Cosmology — Redshift, Hubble's Law and the Big Bang",
            "syllabus_ref_cie": "25.5 (a-g)",
            "syllabus_ref_edexcel": "WPH14 U4: 10.26-10.32",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["The Doppler Effect", "Stellar Distances"],
            "related_topics": ["Stellar Evolution"],
            "sub_topics": [
                "Redshift and the Expanding Universe",
                "Hubble's Law (v = H₀d)",
                "The Big Bang Theory",
                "Cosmic Microwave Background Radiation (CMB)",
                "Dark Matter and Dark Energy (Brief Overview)",
                "The Fate of the Universe",
            ],
        },
    ],

    # ════════════════════════════════════════════════════════
    # 10-Medical-Physics / 医学物理
    # ════════════════════════════════════════════════════════
    "10-Medical-Physics": [
        {
            "section": "01-Medical-Imaging",
            "title": "X-rays and Medical Imaging",
            "syllabus_ref_cie": "26.1 (a-g)",
            "syllabus_ref_edexcel": "WPH14 U4: 11.1-11.6",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["The Photoelectric Effect", "Alpha, Beta and Gamma Radiation"],
            "related_topics": ["Ultrasound Imaging", "PET Scans and Nuclear Medicine"],
            "sub_topics": [
                "Production of X-rays (X-ray Tube)",
                "X-ray Spectrum (Bremsstrahlung and Characteristic)",
                "Attenuation of X-rays",
                "X-ray Imaging and Contrast",
                "CT Scans and Their Principles",
                "Radiation Dose and Safety",
            ],
        },
        {
            "section": "01-Medical-Imaging",
            "title": "Ultrasound Imaging",
            "syllabus_ref_cie": "26.2 (a-f)",
            "syllabus_ref_edexcel": "WPH14 U4: 11.7-11.12",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Progressive Waves", "Refraction and Total Internal Reflection"],
            "related_topics": ["X-rays and Medical Imaging"],
            "sub_topics": [
                "Production and Detection of Ultrasound",
                "Piezoelectric Effect and Transducers",
                "Acoustic Impedance and Reflection",
                "A-Scan and B-Scan Imaging",
                "Doppler Ultrasound for Blood Flow",
                "Advantages and Safety of Ultrasound",
            ],
        },
        {
            "section": "01-Medical-Imaging",
            "title": "PET Scans and Nuclear Medicine",
            "syllabus_ref_cie": "26.3 (a-f)",
            "syllabus_ref_edexcel": "WPH14 U4: 11.13-11.18",
            "level": "A2",
            "difficulty": "advanced",
            "prerequisites": ["Radioactive Decay", "Fundamental Particles"],
            "related_topics": ["X-rays and Medical Imaging"],
            "sub_topics": [
                "Radioactive Tracers and Their Properties",
                "Positron Emission and Annihilation",
                "PET Scanner Principles",
                "Gamma Cameras",
                "Comparing Imaging Modalities (X-ray, CT, Ultrasound, PET, MRI)",
            ],
        },
        {
            "section": "02-Medical-Treatment",
            "title": "Radiotherapy and Nuclear Medicine Treatment",
            "syllabus_ref_cie": "26.4 (a-e)",
            "syllabus_ref_edexcel": "WPH14 U4: 11.19-11.24",
            "level": "A2",
            "difficulty": "intermediate",
            "prerequisites": ["Alpha, Beta and Gamma Radiation", "PET Scans and Nuclear Medicine"],
            "related_topics": ["X-rays and Medical Imaging"],
            "sub_topics": [
                "External Beam Radiotherapy",
                "Brachytherapy (Internal Radiotherapy)",
                "Targeted Alpha Therapy and Nuclear Medicine",
                "Radiation Protection and Dosimetry",
                "Benefits vs Risks of Medical Radiation",
            ],
        },
    ],

    # ════════════════════════════════════════════════════════
    # 11-Mathematical-Foundations / 数学基础
    # ════════════════════════════════════════════════════════
    "11-Mathematical-Foundations": [
        {
            "section": "01-Measurement-and-Units",
            "title": "SI Units, Prefixes and Homogeneity of Equations",
            "syllabus_ref_cie": "1.1-1.3",
            "syllabus_ref_edexcel": "WPH11 U1: 1.1-1.6",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": [],
            "related_topics": ["Uncertainties and Errors", "Graph Plotting Skills"],
            "sub_topics": [
                "SI Base Units and Derived Units",
                "SI Prefixes (pico to tera)",
                "Homogeneity of Physical Equations",
                "Dimensional Analysis",
                "Converting Between Units",
            ],
        },
        {
            "section": "01-Measurement-and-Units",
            "title": "Uncertainties and Errors",
            "syllabus_ref_cie": "1.4 (a-g)",
            "syllabus_ref_edexcel": "WPH11 U1: 1.7-1.12",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["SI Units, Prefixes and Homogeneity of Equations"],
            "related_topics": ["Graph Plotting Skills"],
            "sub_topics": [
                "Systematic vs Random Errors",
                "Accuracy vs Precision",
                "Absolute, Fractional and Percentage Uncertainty",
                "Combining Uncertainties (Addition, Multiplication, Powers)",
                "Uncertainty from Repeated Measurements",
            ],
        },
        {
            "section": "02-Data-Analysis",
            "title": "Graph Plotting Skills",
            "syllabus_ref_cie": "1.5 (a-f)",
            "syllabus_ref_edexcel": "WPH11 U1: 1.13-1.18",
            "level": "AS",
            "difficulty": "foundation",
            "prerequisites": ["SI Units, Prefixes and Homogeneity of Equations"],
            "related_topics": ["Uncertainties and Errors"],
            "sub_topics": [
                "Choosing Appropriate Axes and Scales",
                "Plotting Data Points with Error Bars",
                "Drawing Lines of Best Fit and Worst Fit",
                "Determining Gradient and Intercept",
                "Linearisation of Non-Linear Relationships",
                "Using Graph Gradients to Find Physical Quantities",
            ],
        },
        {
            "section": "03-Advanced-Maths",
            "title": "Trigonometry, Vectors and Calculus for Physics",
            "syllabus_ref_cie": "Mathematical Requirements (Appendix)",
            "syllabus_ref_edexcel": "WPH11 U1: Mathematical Skills",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": [],
            "related_topics": [
                "Scalars and Vectors",
                "Simple Harmonic Motion",
            ],
            "sub_topics": [
                "Trigonometric Functions and Identities for Physics",
                "Vector Operations (Dot Product, Cross Product)",
                "Differentiation for Kinematics and Rates of Change",
                "Integration for Area Under Curves",
                "Exponentials and Logarithms in Physics",
                "Orders of Magnitude Estimation",
            ],
        },
    ],

    # ════════════════════════════════════════════════════════
    # 12-Practical-Skills / 实验技能
    # ════════════════════════════════════════════════════════
    "12-Practical-Skills": [
        {
            "section": "01-Experimental-Design",
            "title": "Planning and Designing Experiments",
            "syllabus_ref_cie": "Paper 3/5 Skills",
            "syllabus_ref_edexcel": "WPH11 U3 / WPH14 U6",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["SI Units, Prefixes and Homogeneity of Equations", "Uncertainties and Errors"],
            "related_topics": ["Data Recording and Analysis", "Evaluation and Improvements"],
            "sub_topics": [
                "Identifying Variables (Independent, Dependent, Control)",
                "Writing a Clear Method",
                "Choosing Appropriate Apparatus",
                "Risk Assessment and Safety Considerations",
                "Preliminary Experiments and Range Finding",
            ],
        },
        {
            "section": "01-Experimental-Design",
            "title": "Data Recording and Analysis",
            "syllabus_ref_cie": "Paper 3/5 Skills",
            "syllabus_ref_edexcel": "WPH11 U3 / WPH14 U6",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Planning and Designing Experiments"],
            "related_topics": ["Evaluation and Improvements"],
            "sub_topics": [
                "Recording Data in Tables",
                "Significant Figures and Decimal Places",
                "Calculating Means and Identifying Anomalies",
                "Graphical Analysis and Linearisation",
                "Determining Relationships from Graphs",
            ],
        },
        {
            "section": "01-Experimental-Design",
            "title": "Uncertainty Analysis in Practical Work",
            "syllabus_ref_cie": "Paper 3/5 Skills",
            "syllabus_ref_edexcel": "WPH11 U3 / WPH14 U6",
            "level": "AS",
            "difficulty": "advanced",
            "prerequisites": ["Uncertainties and Errors", "Data Recording and Analysis"],
            "related_topics": ["Evaluation and Improvements"],
            "sub_topics": [
                "Calculating Uncertainty from Repeated Readings",
                "Error Bars on Graphs",
                "Using Worst-Fit Lines for Uncertainty in Gradient",
                "Percentage Difference and Percentage Uncertainty",
                "Propagating Uncertainties Through Calculations",
            ],
        },
        {
            "section": "02-Exam-Technique",
            "title": "Evaluation and Improvements",
            "syllabus_ref_cie": "Paper 3/5 Skills",
            "syllabus_ref_edexcel": "WPH11 U3 / WPH14 U6",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Planning and Designing Experiments", "Data Recording and Analysis"],
            "related_topics": ["Uncertainty Analysis in Practical Work"],
            "sub_topics": [
                "Identifying Sources of Error and Uncertainty",
                "Suggesting Realistic Improvements",
                "Evaluating Method and Apparatus Limitations",
                "Commenting on Reliability and Validity",
                "Writing a Conclusion",
            ],
        },
        {
            "section": "02-Exam-Technique",
            "title": "Paper 3 and Paper 5 Exam Technique",
            "syllabus_ref_cie": "CAIE Paper 3 (AS) / Paper 5 (A2)",
            "syllabus_ref_edexcel": "Edexcel Unit 3 (AS) / Unit 6 (A2)",
            "level": "AS",
            "difficulty": "intermediate",
            "prerequisites": ["Planning and Designing Experiments", "Evaluation and Improvements"],
            "related_topics": ["Uncertainty Analysis in Practical Work"],
            "sub_topics": [
                "Paper 3 (AS) Question Types and Mark Schemes",
                "Paper 5 (A2) Question Types and Mark Schemes",
                "Common Practical Experiments to Know",
                "Time Management in Practical Exams",
                "Key Command Words in Practical Papers",
            ],
        },
    ],
}


# ============================================================
# Generation Functions
# ============================================================

async def generate_hub_content(topic: dict, chapter: str) -> str:
    """Generate the Hub file (12-section Know.md format) for a topic."""
    user_prompt = f"""
Topic: {topic['title']}
Chapter: {chapter}

Syllabus References:
- CAIE 9702: {topic['syllabus_ref_cie']}
- Edexcel IAL: {topic['syllabus_ref_edexcel']}

Level: {topic['level']}
Difficulty: {topic['difficulty']}

Parent folder: vault/{chapter}/{topic['section']}/{topic['title']}/

This is the HUB (overview) file. Generate the complete 12-section bilingual guide.

Prerequisites (use [[wikilinks]]):
{topic['prerequisites']}

Related Topics (use [[wikilinks]]):
{topic['related_topics']}

Sub-topics (use [[wikilinks]] to these leaf nodes):
{topic['sub_topics']}
"""

    max_retries = 3
    content = ""
    section_count = 0
    for attempt in range(1, max_retries + 1):
        retry_label = f" (retry {attempt})" if attempt > 1 else ""
        print(f"  [HUB] Generating: {topic['title']} ({topic['level']}){retry_label}...")
        try:
            response = await client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": HUB_SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.2 + (attempt - 1) * 0.1,
                max_tokens=32000,
            )

            content = response.choices[0].message.content or ""
            content = content.strip()
            if content.startswith("```markdown"):
                content = content[11:]
            if content.startswith("```"):
                content = content[3:]
            if content.endswith("```"):
                content = content[:-3]
            content = content.strip()

            # Validate section count
            h1_sections = re.findall(r'^# \d+\.', content, re.MULTILINE)
            section_count = len(h1_sections)
            if section_count >= 11:
                return content
            else:
                print(f"    ⚠️  Only {section_count}/12 sections, retrying...")
        except Exception as e:
            print(f"    ⚠️  API error: {e}, retrying...")
        await asyncio.sleep(1.0)

    # Last attempt: return what we have
    print(f"    ⚠️  Final attempt: {section_count}/12 sections — keeping best effort")
    return content


async def generate_leaf_content(topic: dict, sub_topic: str, chapter: str) -> str:
    """Generate a leaf node .md file (12-section Know.md format) for a sub-topic."""
    user_prompt = f"""
Parent Topic: {topic['title']}
Sub-topic: {sub_topic}
Chapter: {chapter}

Syllabus References:
- CAIE 9702: {topic['syllabus_ref_cie']}
- Edexcel IAL: {topic['syllabus_ref_edexcel']}

Level: {topic['level']}
Difficulty: {topic['difficulty']}

Parent Hub: [[{topic['title']}]]

This is a LEAF NODE — a focused sub-topic within "{topic['title']}".
Generate the focused 12-section bilingual guide.

Sibling sub-topics (use [[wikilinks]] where relevant):
{[s for s in topic['sub_topics'] if s != sub_topic]}

Prerequisites from other topics:
{topic['prerequisites']}

Related Topics:
{topic['related_topics']}
"""

    max_retries = 3
    content = ""
    section_count = 0
    for attempt in range(1, max_retries + 1):
        retry_label = f" (retry {attempt})" if attempt > 1 else ""
        print(f"    [LEAF] Generating: {sub_topic}{retry_label}...")
        try:
            response = await client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": LEAF_SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.2 + (attempt - 1) * 0.1,
                max_tokens=16000,
            )

            content = response.choices[0].message.content or ""
            content = content.strip()
            if content.startswith("```markdown"):
                content = content[11:]
            if content.startswith("```"):
                content = content[3:]
            if content.endswith("```"):
                content = content[:-3]
            content = content.strip()

            h1_sections = re.findall(r'^# \d+\.', content, re.MULTILINE)
            section_count = len(h1_sections)
            if section_count >= 10:
                return content
            else:
                print(f"      ⚠️  Only {section_count}/12 sections, retrying...")
        except Exception as e:
            print(f"      ⚠️  API error: {e}, retrying...")
        await asyncio.sleep(1.0)

    print(f"      ⚠️  Final attempt: {section_count}/12 sections — keeping best effort")
    return content


# ============================================================
# Main
# ============================================================

async def main():
    parser = argparse.ArgumentParser(description="Generate A-Level Physics vault content (v3 — Know.md format)")
    parser.add_argument("--chapter", type=str, default=None,
                        help="Generate only a specific chapter (e.g., '02-Waves', 'all' for all chapters)")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite existing files")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be generated without actually calling API")
    args = parser.parse_args()

    if not settings.deepseek_api_key or "your-deepseek" in settings.deepseek_api_key:
        print("❌ 请先在 .env 文件中配置 DEEPSEEK_API_KEY")
        sys.exit(1)

    # Determine chapters to generate
    if args.chapter and args.chapter != "all":
        if args.chapter not in ALL_TOPICS:
            print(f"❌ Unknown chapter: {args.chapter}")
            print(f"   Available: {list(ALL_TOPICS.keys())}")
            sys.exit(1)
        chapters = {args.chapter: ALL_TOPICS[args.chapter]}
    else:
        chapters = ALL_TOPICS

    # Calculate totals
    total_hubs = sum(len(topics) for topics in chapters.values())
    total_leaves = sum(
        len(t["sub_topics"]) for topics in chapters.values() for t in topics
    )
    total_files = total_hubs + total_leaves

    print("=" * 70)
    print("ALP_Net Phase 2 (v3): 全章节 A-Level 物理内容生成")
    print("=" * 70)
    print(f"考纲: CAIE 9702 + Edexcel IAL 双考纲")
    print(f"语言: 中英双语 (EN/CN)")
    print(f"格式: Know.md 12-section")
    print(f"章节数: {len(chapters)}")
    print(f"知识点 (Hub): {total_hubs} 个")
    print(f"子知识点 (Leaf): {total_leaves} 个")
    print(f"预计总文件数: {total_files}")
    if args.force:
        print("⚠️  --force: 将覆盖已存在的文件")
    if args.dry_run:
        print("🔍 DRY RUN — 不实际调用 API")
    print("=" * 70)
    print()

    if args.dry_run:
        for chapter_name, topics in chapters.items():
            print(f"\n📁 {chapter_name}/")
            for topic in topics:
                print(f"  ├── {topic['section']}/{topic['title']}/{topic['title']}.md (Hub)")
                for st in topic['sub_topics']:
                    print(f"  │   └── {st}.md (Leaf)")
        print(f"\n🔍 Dry run complete. {total_files} files would be generated.")
        return

    hubs_generated = 0
    leaves_generated = 0
    skipped = 0

    for chapter_name, topics in chapters.items():
        print(f"\n{'='*60}")
        print(f"📁 Chapter: {chapter_name}")
        print(f"{'='*60}")

        for topic in topics:
            # Create topic folder
            topic_dir = VAULT_PATH / chapter_name / topic["section"] / safe_path(topic["title"])
            topic_dir.mkdir(parents=True, exist_ok=True)

            # ── Generate Hub ──
            hub_filename = f"{safe_path(topic['title'])}.md"
            hub_path = topic_dir / hub_filename

            if hub_path.exists() and not args.force:
                print(f"  ⏭️  Hub 跳过 (已存在): {topic['title']}")
                skipped += 1
            else:
                try:
                    content = await generate_hub_content(topic, chapter_name)
                    hub_path.write_text(content, encoding="utf-8")
                    print(f"  ✅ Hub: {topic['title']} ({len(content)} chars)")
                    hubs_generated += 1
                    await asyncio.sleep(0.5)
                except Exception as e:
                    print(f"  ❌ Hub 失败: {topic['title']} — {e}")
                    import traceback
                    traceback.print_exc()
                    continue

            # ── Generate Leaf files ──
            for sub_topic in topic["sub_topics"]:
                leaf_filename = f"{safe_path(sub_topic)}.md"
                leaf_path = topic_dir / leaf_filename

                if leaf_path.exists() and not args.force:
                    print(f"    ⏭️  Leaf 跳过 (已存在): {leaf_filename}")
                    skipped += 1
                    continue

                try:
                    content = await generate_leaf_content(topic, sub_topic, chapter_name)
                    leaf_path.write_text(content, encoding="utf-8")
                    print(f"    ✅ Leaf: {leaf_filename} ({len(content)} chars)")
                    leaves_generated += 1
                    await asyncio.sleep(0.3)
                except Exception as e:
                    print(f"    ❌ Leaf 失败: {leaf_filename} — {e}")
                    import traceback
                    traceback.print_exc()

    print()
    print("=" * 70)
    print(f"✅ 完成！")
    print(f"   Hub 文件: {hubs_generated} 个")
    print(f"   Leaf 文件: {leaves_generated} 个")
    print(f"   跳过 (已存在): {skipped} 个")
    print(f"   文件位置: {VAULT_PATH}/")
    print()
    if not args.force and skipped > 0:
        print("💡 使用 --force 覆盖已存在的文件")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())
