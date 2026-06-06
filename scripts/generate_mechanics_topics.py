#!/usr/bin/env python3
"""
Phase 2 (v2): 生成 Mechanics 力学模块的 A-Level 物理知识点 Markdown 文件

六项调整：
1. CAIE 9702 + Edexcel IAL 双考纲合并
2. 全文 [[wikilinks]] 互联（不仅是 Section 13）
3. Past Paper 题号占位列
4. 四级文件夹层级（Hub + 叶子节点）
5. 中英双语对照 + 内容精简 + 📷 图片标记
6. 23 Topics × N Sub-topics = ~110-130 个节点
"""
import asyncio
import sys
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
# MECHANICS_TOPICS — 23 Topics with CAIE + Edexcel + Sub-topics
# ============================================================
MECHANICS_TOPICS = [
    # ── 3.1 Motion / 运动学 ──
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
        "related_topics": [
            "Motion Graphs",
            "Equations of Motion (SUVAT)",
        ],
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

    # ── 3.2 Forces / 动力学 ──
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
        "related_topics": [
            "Linear Momentum and Impulse",
            "Conservation of Momentum",
        ],
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

    # ── 3.3 Work, Energy and Power / 功、能与功率 ──
    {
        "section": "03-Work-Energy-Power",
        "title": "Work Done by a Force",
        "syllabus_ref_cie": "3.3 (a-b)",
        "syllabus_ref_edexcel": "WPH11 U1: 4.1-4.4",
        "level": "AS",
        "difficulty": "foundation",
        "prerequisites": ["Scalars and Vectors", "Newton's Laws of Motion"],
        "related_topics": [
            "Kinetic Energy and Potential Energy",
        ],
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

    # ── 14 Motion in a Circle (A2) / 圆周运动 ──
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
        "related_topics": [
            "Gravitational Force and Field",
            "Circular Orbits",
        ],
        "sub_topics": [
            "Centripetal Acceleration Formula",
            "Centripetal Force",
            "Banked Tracks and Conical Pendulum",
        ],
    },

    # ── 15 Gravitational Fields (A2) / 引力场 ──
    {
        "section": "05-Gravitational-Fields",
        "title": "Gravitational Force and Field",
        "syllabus_ref_cie": "15.1 (a-d)",
        "syllabus_ref_edexcel": "WPH14 U4: 6.1-6.5",
        "level": "A2",
        "difficulty": "intermediate",
        "prerequisites": [
            "Newton's Laws of Motion",
            "Centripetal Acceleration and Force",
        ],
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
        "prerequisites": [
            "Gravitational Force and Field",
            "Centripetal Acceleration and Force",
        ],
        "related_topics": ["Gravitational Potential"],
        "sub_topics": [
            "Orbital Velocity",
            "Kepler's Third Law",
            "Geostationary Satellites",
        ],
    },

    # ── 17 Oscillations (A2) / 振动 ──
    {
        "section": "06-Oscillations",
        "title": "Simple Harmonic Motion",
        "syllabus_ref_cie": "17.1 (a-d)",
        "syllabus_ref_edexcel": "WPH14 U4: 7.1-7.5",
        "level": "A2",
        "difficulty": "intermediate",
        "prerequisites": [
            "Equations of Motion (SUVAT)",
            "Angular Measures",
        ],
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
        "prerequisites": [
            "Simple Harmonic Motion",
            "Kinetic Energy and Potential Energy",
        ],
        "related_topics": ["Damped and Forced Oscillations / Resonance"],
        "sub_topics": [
            "KE and PE in SHM",
            "Energy-Time Graphs for SHM",
            "Energy-Displacement Graphs for SHM",
        ],
    },
    {
        "section": "06-Oscillations",
        "title": "Damped and Forced Oscillations / Resonance",
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
]


# ============================================================
# HUB_SYSTEM_PROMPT — 20-part 完整 Topic 总览（中英双语）
# ============================================================
HUB_SYSTEM_PROMPT = """You are a senior A-Level Physics teacher and examiner for BOTH CAIE 9702 and Edexcel IAL, creating bilingual (EN+CN) Markdown notes for an Obsidian knowledge graph used in RAG retrieval.

CORE RULES (follow strictly):
1. Bilingual throughout: English first, then Chinese. Format: **English:** [text]  **中文:** [text]
2. Use Obsidian [[wikilinks]] EVERYWHERE in ALL sections — when any physics concept/term/law is mentioned
3. LaTeX $$ for display, $ for inline. Mermaid for relationship diagrams.
4. Exam-board differences marked with blockquote:
   > 📋 **CIE Only:** ...
   > 📋 **Edexcel Only:** ...
5. Image prompts in blockquote with 📷:
   > 📷 **IMAGE PROMPT — [CODE]: [Title]** (detailed prompt, labels, style, exam importance)
6. Past Paper references use placeholder: 📝 *待填入*
7. Be detailed but concise. Use tables over paragraphs where possible.
8. ALL 14 sections below are MANDATORY. You have ample output space — do NOT skip any section.

---

# OUTPUT STRUCTURE (14 sections)

# 1. Overview / 概述
**English:** What this topic studies, why it matters, real-world significance, importance in CAIE 9702 + Edexcel IAL.
**中文:** (Chinese translation)

# 2. Syllabus Learning Objectives / 考纲学习目标
Two-column table: | CAIE 9702 | Edexcel IAL |
Then examiner expectations. Use 📋 callouts for board-specific differences.

# 3. Core Definitions / 核心定义
Bilingual table: | Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
Use exam-standard wording. Link terms with [[wikilinks]].

# 4. Key Concepts Explained / 关键概念详解
For EACH major concept:
## 4.X Concept Name / 概念名称
### Explanation / 解释: **English:** (with [[wikilinks])  **中文:** (translation)
### Physical Meaning / 物理意义: **English:** ...  **中文:** ...
### Common Misconceptions / 常见误区: bullet list
### Exam Tips / 考试提示: **English:** ...  **中文:** ...
Include 📷 image prompts where a diagram helps.

# 5. Essential Equations / 核心公式
For EACH equation:
## 5.X Equation Name / 公式名称
$$ LaTeX $$
| Symbol (符号) | Meaning (EN/CN) | Unit (单位) |
Derivation (if examinable), Conditions, Limitations, Rearrangements.

# 6. Graphs and Relationships / 图表与关系
For EACH relevant graph:
## 6.X Graph Name / 图表名称
Axes, Shape, Gradient Meaning (EN+CN), Area Meaning (EN+CN), Exam Interpretation, Common Questions.
Include 📷 prompts and Mermaid where possible.

# 7. Required Diagrams / 必备图表
At least 3 diagrams. For EACH:
## 7.X Diagram Name / 图表名称
> 📷 **IMAGE PROMPT — [CODE]: [Title]** (English AI prompt, Chinese description, Labels, Style, Exam Importance)

# 8. Worked Examples / 典型例题
Provide 2 examples. For EACH:
## Example X: [Title] / [标题]
### Question / 题目 (EN+CN)
### Image Prompt / 图片提示 (📷 diagram for the question if needed)
### Solution / 解答 (step-by-step with LaTeX)
### Final Answer / 最终答案
### Examiner Notes / 考官点评

# 9. Past Paper Question Types / 历年真题题型
Table: | Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
Each row has 📝 *待填入* in the last column.
> 📝 **题库整理中 / Question Bank Under Construction:** (explanation in EN+CN)
Common Command Words (EN+CN).

# 10. Practical Skills Connections / 实验技能链接
**English:** Link to CAIE Paper 3/5 and Edexcel Unit 3/6. Measurements, uncertainties, graph plotting, experimental design.
**中文:** (translation)
> 📋 Board-specific callouts.

# 11. Concept Map / 概念图谱
Mermaid graph TD showing topic structure, prerequisites from other modules, and sub-topics.

# 12. Examiner Insights / 考官洞察
**English:** Most tested ideas (CAIE + Edexcel), mark scheme wording, lost marks, high-scoring structures.
**中文:** (translation)

# 13. Quick Revision Sheet / 速查表
Compact bilingual summary table: | Category / 类别 | Key Points / 要点 |

# 14. Metadata / 元数据
```yaml
title: {en:, cn:}
subject: Physics
syllabus: [CAIE 9702, Edexcel IAL]
cie_ref:
edexcel_ref:
level:
node_type: topic_hub
difficulty:
prerequisites:
related_topics:
sub_topics:
formula_count:
diagram_count:
exam_frequency:
language: bilingual_en_cn
last_updated:
```

---
⚠️ CRITICAL: ALL 14 sections are MANDATORY. You have 32000 output tokens — more than enough. Count your sections before finishing. Section 9 (Past Paper) MUST include the table.
"""


# ============================================================
# LEAF_SYSTEM_PROMPT — 8-part 叶子节点（中英双语）
# ============================================================
LEAF_SYSTEM_PROMPT = """You are a senior A-Level Physics teacher and knowledge graph architect, writing bilingual (English + Chinese) focused content for a single sub-topic within a larger Physics knowledge graph.

Your output is a LEAF NODE — a focused, standalone piece of content on one specific sub-topic. It will be:
1. A standalone Obsidian note
2. A knowledge graph leaf node
3. Used for RAG retrieval
4. Displayed as a detail card in a web frontend

CRITICAL WRITING RULES:
- ALL content MUST be bilingual: English first, Chinese second
- Use [[wikilinks]] LIBERALLY to link to:
  - The parent Hub: [[Parent Topic Name]]
  - Related sub-topics within the same topic
  - Prerequisite concepts from other topics
- Use LaTeX $$ for display equations, $ for inline
- Use blockquote for image prompts with 📷 emoji:
  > 📷 **IMAGE PROMPT — [CODE]: [Title]** ...
- Keep content FOCUSED on this specific sub-topic — don't expand into the whole topic
- Write clearly for A-Level students

---

# OUTPUT STRUCTURE (8 sections)

---

# 1. Overview / 概述

**English:**
Brief focused introduction (2-3 paragraphs). What this sub-topic covers, why it matters, and how it fits into the broader [[Parent Topic Name]] topic.

**中文:**
简要介绍 (2-3段)。本子知识点涵盖的内容、重要性、以及和 [[Parent Topic Name]] 的关系。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Term** / 术语 | Exam-standard English definition | 考试标准中文定义 |

Include 3-6 key terms specific to this sub-topic.

---

# 3. Key Concepts / 关键概念

**English:**
Detailed explanation of the core concept. Use [[wikilinks]] when referencing:
- Other sub-topics within [[Parent Topic Name]]
- Prerequisites from other topics like [[Prerequisite Topic]]
- Related advanced concepts

Include:
* Step-by-step reasoning
* Physical interpretation
* Common pitfalls

**中文:**
核心概念的详细解释。使用 [[wikilinks]] 连接相关概念。

---

# 4. Formulas / 公式

For the key formula(s) of this sub-topic:

$$ [LaTeX equation] $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $x$ | ... | ... | ... |

**Derivation / 推导** (if applicable):
Brief step-by-step derivation.

**Conditions / 适用条件:**
When this formula applies.

> 📷 **IMAGE PROMPT — [CODE]: [Formula/Concept Diagram]**
> [Detailed AI image generation prompt if a diagram helps explain this formula/concept]

---

# 5. Image Prompt / 图片提示

At least one detailed AI image generation prompt for this sub-topic:

> 📷 **IMAGE PROMPT — [CODE]: [Diagram Title]**
>
> **English Prompt:**
> Ultra-detailed prompt for AI image generation (Midjourney/DALL·E/Stable Diffusion).
> Include: layout, perspective, colors, labels, lighting, style direction.
>
> **中文描述:**
> [Chinese version of the prompt]
>
> **Labels Required / 需要标注:**
> * Label 1
> * Label 2
>
> **Style / 风格:** [Textbook vector / 3D render / hand-drawn / photorealistic]
>
> **Exam Relevance / 考试关联:**
> Why this diagram matters for exams.

---

# 6. Worked Example / 典型例题

Provide 1-2 focused examples for this sub-topic:

### Question / 题目
**English:** [Question text]
**中文:** [题目翻译]

### Solution / 解答
Step-by-step with LaTeX.

### Final Answer / 最终答案
**Answer:** ... **答案:** ...

### Quick Tip / 提示
One key exam tip for this type of problem.

---

# 7. Flashcards / 闪卡

Generate exactly 5 bilingual flashcards:

Q (EN): ...
Q (CN): ...
A (EN): ...
A (CN): ...

---

# 8. Metadata / 元数据

```yaml
title:
  en:
  cn:
parent_topic:
parent_hub: "[[Parent Topic Name]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level:
node_type: leaf_concept
difficulty:
related_leaf_nodes:
  - "[[Related Leaf 1]]"
  - "[[Related Leaf 2]]"
language: bilingual_en_cn
```

---

Generate the complete bilingual leaf note now. Stay FOCUSED on this specific sub-topic only.
"""


def safe_path(name: str) -> str:
    """Replace filesystem-unsafe characters in topic/folder names."""
    return name.replace("/", "-").replace("\\", "-").replace(":", " -")


# ============================================================
# Generation Functions
# ============================================================

async def generate_hub_content(topic: dict) -> str:
    """Generate the index.md Hub file (20-part structure) for a topic."""
    user_prompt = f"""
Topic: {topic['title']}

Syllabus References:
- CAIE 9702: {topic['syllabus_ref_cie']}
- Edexcel IAL: {topic['syllabus_ref_edexcel']}

Level: {topic['level']}
Difficulty: {topic['difficulty']}

Parent folder: vault/01-Mechanics/{topic['section']}/{topic['title']}/

This is the HUB (overview) file. Generate the complete 20-section bilingual guide.

Prerequisites (use [[wikilinks]]):
{topic['prerequisites']}

Related Topics (use [[wikilinks]]):
{topic['related_topics']}

Sub-topics (use [[wikilinks]] to these leaf nodes):
{topic['sub_topics']}
"""

    import re

    max_retries = 3
    content = ""
    for attempt in range(1, max_retries + 1):
        retry_label = f" (retry {attempt})" if attempt > 1 else ""
        print(f"  [HUB] Generating: {topic['title']} ({topic['level']}){retry_label}...")
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
        if section_count >= 14:
            return content
        else:
            print(f"    ⚠️  Only {section_count}/14 sections, retrying...")
            await asyncio.sleep(1.0)

    # Last attempt: return what we have
    print(f"    ⚠️  Final attempt: {section_count}/14 sections — keeping best effort")
    return content


async def generate_leaf_content(topic: dict, sub_topic: str) -> str:
    """Generate a leaf node .md file (8-part structure) for a sub-topic."""
    user_prompt = f"""
Parent Topic: {topic['title']}
Sub-topic: {sub_topic}

Syllabus References:
- CAIE 9702: {topic['syllabus_ref_cie']}
- Edexcel IAL: {topic['syllabus_ref_edexcel']}

Level: {topic['level']}
Difficulty: {topic['difficulty']}

Parent Hub: [[{topic['title']}]]

This is a LEAF NODE — a focused sub-topic within "{topic['title']}".
Generate the focused 8-section bilingual guide.

Sibling sub-topics (use [[wikilinks]] where relevant):
{[s for s in topic['sub_topics'] if s != sub_topic]}

Prerequisites from other topics:
{topic['prerequisites']}

Related Topics:
{topic['related_topics']}
"""

    print(f"    [LEAF] Generating: {sub_topic} ...")
    response = await client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": LEAF_SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
        max_tokens=6000,
    )

    content = response.choices[0].message.content or ""
    content = content.strip()
    if content.startswith("```markdown"):
        content = content[11:]
    if content.startswith("```"):
        content = content[3:]
    if content.endswith("```"):
        content = content[:-3]
    return content.strip()


# ============================================================
# Main
# ============================================================

async def main(pilot_only: bool = True):
    if not settings.deepseek_api_key or "your-deepseek" in settings.deepseek_api_key:
        print("❌ 请先在 .env 文件中配置 DEEPSEEK_API_KEY")
        print("   复制 .env.example 为 .env，填入你的 DeepSeek API Key")
        sys.exit(1)

    total_hubs = 1 if pilot_only else len(MECHANICS_TOPICS)
    total_leaves = sum(
        len(t["sub_topics"]) for t in
        (MECHANICS_TOPICS[:1] if pilot_only else MECHANICS_TOPICS)
    )

    print("=" * 70)
    print("ALP_Net Phase 2 (v2): Mechanics 力学模块内容生成")
    print("=" * 70)
    print(f"考纲: CAIE 9702 + Edexcel IAL 双考纲")
    print(f"语言: 中英双语 (EN/CN)")
    print(f"结构: 4级文件夹层级 (Hub + 叶子节点)")
    mode_desc = "试点模式 (1个知识点)" if pilot_only else f"全量模式 ({len(MECHANICS_TOPICS)} 个知识点)"
    print(f"模式: {mode_desc}")
    print(f"预计文件数: {total_hubs} Hub + {total_leaves} Leaf = {total_hubs + total_leaves}")
    print("=" * 70)
    print()

    topics_to_generate = MECHANICS_TOPICS[:1] if pilot_only else MECHANICS_TOPICS

    hubs_generated = 0
    leaves_generated = 0
    skipped = 0

    for topic in topics_to_generate:
        # Create topic folder (sanitize / in name)
        topic_dir = VAULT_PATH / "01-Mechanics" / topic["section"] / safe_path(topic["title"])
        topic_dir.mkdir(parents=True, exist_ok=True)

        # ── Generate Hub (index.md renamed to topic title) ──
        hub_filename = f"{safe_path(topic['title'])}.md"
        hub_path = topic_dir / hub_filename

        if hub_path.exists():
            print(f"  ⏭️  Hub 跳过 (已存在): {topic['title']}/{hub_filename}")
            skipped += 1
        else:
            try:
                content = await generate_hub_content(topic)
                hub_path.write_text(content, encoding="utf-8")
                print(f"  ✅ Hub: {topic['title']}/{hub_filename}")
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

            if leaf_path.exists():
                print(f"    ⏭️  Leaf 跳过 (已存在): {leaf_filename}")
                skipped += 1
                continue

            try:
                content = await generate_leaf_content(topic, sub_topic)
                leaf_path.write_text(content, encoding="utf-8")
                print(f"    ✅ Leaf: {leaf_filename}")
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
    print(f"   文件位置: {VAULT_PATH}/01-Mechanics/")
    print()
    if pilot_only:
        print("👉 请在 Obsidian 中打开 vault/ 目录，检阅试点文件。")
        print("   检查：中英双语、[[wikilinks]]、📷 图片标记、📝 占位符。")
        print("   如果满意，告诉我运行 --all 批量生成。")
    else:
        print("👉 请在 Obsidian 中检阅所有内容。")
        print("   检阅满意后，继续 Phase 3（数据摄入管线）。")
    print("=" * 70)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate Mechanics topic content (v2)")
    parser.add_argument("--all", action="store_true", help="Generate all 23 topics (default: pilot only)")
    args = parser.parse_args()
    asyncio.run(main(pilot_only=not args.all))
