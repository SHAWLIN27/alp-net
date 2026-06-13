---
# Choosing the Right SUVAT Equation / 选择合适的SUVAT方程

---

# 1. Overview / 概述

**English:**
This sub-topic focuses on the critical skill of selecting the correct SUVAT equation from the five available options when solving kinematics problems. While memorising the five equations is essential, knowing *which* equation to apply in a given scenario is what distinguishes a successful student. This leaf node provides a systematic decision-making framework based on the "suvat" variables: displacement ($s$), initial velocity ($u$), final velocity ($v$), acceleration ($a$), and time ($t$). The core principle is that each equation omits exactly one of these five variables. By identifying which variable is **not given** and **not asked for**, you can instantly select the correct equation. This skill is fundamental to solving problems in [[Equations of Motion (SUVAT)]], including [[Free Fall Under Gravity]] and [[Two-Stage Motion Problems]], and is a prerequisite for [[Projectile Motion]].

**中文:**
本子知识点专注于从五个SUVAT方程中选择正确方程的关键技能。虽然记住五个方程是必要的，但知道在给定场景中*应用哪个*方程才是区分成功学生的关键。本叶节点提供了一个基于“suvat”变量（位移 $s$、初速度 $u$、末速度 $v$、加速度 $a$、时间 $t$）的系统性决策框架。核心原则是每个方程恰好省略这五个变量中的一个。通过识别哪个变量**未给出**且**未要求**，你可以立即选择正确的方程。这项技能是解决[[Equations of Motion (SUVAT)]]问题的基础，包括[[Free Fall Under Gravity]]和[[Two-Stage Motion Problems]]，也是[[Projectile Motion]]的先决条件。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 3.1(g): Select and use the equations of motion for constant acceleration (SUVAT) in appropriate contexts. | 1.9: Use the equations of motion for constant acceleration (SUVAT) to solve problems. |
| 3.1(h): Solve problems involving motion in a straight line with constant acceleration. | 1.10: Select and apply the appropriate equation(s) of motion to solve problems. |
| 3.1(k): Derive and use the equations of motion for constant acceleration. | 1.12: Solve problems involving motion under gravity (free fall). |

**Examiner Expectations / 考官期望:**
- **English:** You must be able to quickly identify which SUVAT equation is appropriate for a given problem. Marks are often lost not because of incorrect algebra, but because the wrong equation was chosen. You should be able to justify your choice by stating which variable is missing.
- **中文:** 你必须能够快速识别哪个SUVAT方程适用于给定的问题。丢分通常不是因为代数错误，而是因为选择了错误的方程。你应该能够通过说明哪个变量缺失来证明你的选择。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **SUVAT Variables** / SUVAT变量 | The five standard variables used in constant acceleration kinematics: displacement ($s$), initial velocity ($u$), final velocity ($v$), acceleration ($a$), time ($t$). | 恒定加速度运动学中使用的五个标准变量：位移 ($s$)、初速度 ($u$)、末速度 ($v$)、加速度 ($a$)、时间 ($t$)。 | Confusing $s$ (displacement) with distance. Confusing $u$ and $v$. |
| **Missing Variable** / 缺失变量 | The one SUVAT variable that is neither given in the question nor asked for in the answer. This determines which equation to use. | 问题中既未给出也未要求答案的那个SUVAT变量。这决定了使用哪个方程。 | Thinking you need to find the missing variable first. You don't; you use it to select the equation. |
| **Constant Acceleration** / 恒定加速度 | Acceleration that does not change with time. All SUVAT equations are only valid under this condition. | 不随时间变化的加速度。所有SUVAT方程仅在此条件下有效。 | Applying SUVAT to problems with changing acceleration (e.g., air resistance). |
| **Deceleration** / 减速 | Negative acceleration. In SUVAT, this is represented by a negative value of $a$ when the object is slowing down. | 负加速度。在SUVAT中，当物体减速时，这由 $a$ 的负值表示。 | Forgetting to assign a negative sign to $a$ when an object is slowing down. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Missing Variable Method / 缺失变量法

### Explanation / 解释
**English:** The five SUVAT equations are:
1.  $v = u + at$ (missing $s$)
2.  $s = \frac{(u+v)}{2}t$ (missing $a$)
3.  $s = ut + \frac{1}{2}at^2$ (missing $v$)
4.  $s = vt - \frac{1}{2}at^2$ (missing $u$)
5.  $v^2 = u^2 + 2as$ (missing $t$)

The "Missing Variable Method" is a systematic approach:
1.  **List** the five SUVAT variables: $s, u, v, a, t$.
2.  **Identify** which three variables are given in the question.
3.  **Identify** which one variable is asked for (the unknown).
4.  **Find** the one variable that is **neither given nor asked for**. This is the "missing variable".
5.  **Select** the equation that also omits this same variable.

**中文:**
五个SUVAT方程是：
1.  $v = u + at$ (缺失 $s$)
2.  $s = \frac{(u+v)}{2}t$ (缺失 $a$)
3.  $s = ut + \frac{1}{2}at^2$ (缺失 $v$)
4.  $s = vt - \frac{1}{2}at^2$ (缺失 $u$)
5.  $v^2 = u^2 + 2as$ (缺失 $t$)

“缺失变量法”是一种系统性的方法：
1.  **列出**五个SUVAT变量：$s, u, v, a, t$。
2.  **识别**问题中给出的三个变量。
3.  **识别**问题要求的一个变量（未知量）。
4.  **找出**既**未给出也未要求**的那个变量。这就是“缺失变量”。
5.  **选择**也省略了相同变量的方程。

### Physical Meaning / 物理意义
**English:** This method works because each equation is a unique relationship between four of the five variables. By knowing which variable is irrelevant to the problem (not needed as input or output), you can directly use the relationship that excludes it. This avoids unnecessary algebraic manipulation.

**中文:** 这种方法之所以有效，是因为每个方程都是五个变量中四个变量之间的独特关系。通过知道哪个变量与问题无关（不需要作为输入或输出），你可以直接使用排除它的关系。这避免了不必要的代数运算。

### Common Misconceptions / 常见误区
- **English:**
  - Thinking you must always find the missing variable first. You don't; you use it to select the equation.
  - Confusing "not given" with "unknown". The unknown is what you are asked to find. The missing variable is the one that is neither given nor asked for.
  - Forgetting to check if acceleration is constant before using this method.
- **中文:**
  - 认为必须首先找到缺失的变量。不需要；你用它来选择方程。
  - 混淆“未给出”和“未知”。未知量是你被要求找到的。缺失变量是既未给出也未要求的变量。
  - 在使用此方法之前忘记检查加速度是否恒定。

### Exam Tips / 考试提示
- **English:**
  - **Always** write down the five variables and tick/cross them as you read the question.
  - If a variable is implied (e.g., "starts from rest" implies $u=0$), treat it as given.
  - If a variable is zero (e.g., "comes to rest" implies $v=0$), treat it as given.
  - For multi-stage problems, apply this method separately to each stage.
- **中文:**
  - **始终**写下五个变量，并在阅读问题时勾选/叉选它们。
  - 如果一个变量是隐含的（例如，“从静止开始”意味着 $u=0$），将其视为已给出。
  - 如果一个变量为零（例如，“停下来”意味着 $v=0$），将其视为已给出。
  - 对于多阶段问题，对每个阶段分别应用此方法。

> 📷 **IMAGE PROMPT — DIAGRAM-01: The Missing Variable Flowchart**
> A flowchart showing the decision process. Start with "Read the problem". Then "List s, u, v, a, t". Then "Identify given variables (tick)". Then "Identify unknown variable (circle)". Then "Find the missing variable (cross)". Then "Select equation that omits the crossed variable". Finally "Solve". Use clear boxes and arrows.

---

# 5. Essential Equations / 核心公式

## Equation 1: $v = u + at$ (Missing $s$)

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $v$ | Final velocity | 末速度 | m/s |
| $u$ | Initial velocity | 初速度 | m/s |
| $a$ | Acceleration | 加速度 | m/s² |
| $t$ | Time | 时间 | s |

**Derivation / 推导:** From the definition of acceleration: $a = \frac{v-u}{t} \implies v = u + at$.
**Conditions / 适用条件:** Constant acceleration. Missing $s$.
**Limitations / 局限性:** Does not involve displacement. Cannot be used if displacement is needed.

## Equation 2: $s = \frac{(u+v)}{2}t$ (Missing $a$)

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $s$ | Displacement | 位移 | m |
| $u$ | Initial velocity | 初速度 | m/s |
| $v$ | Final velocity | 末速度 | m/s |
| $t$ | Time | 时间 | s |

**Derivation / 推导:** Average velocity = $\frac{u+v}{2}$. Displacement = average velocity × time.
**Conditions / 适用条件:** Constant acceleration. Missing $a$.
**Limitations / 局限性:** Does not involve acceleration. Cannot be used if acceleration is needed.

## Equation 3: $s = ut + \frac{1}{2}at^2$ (Missing $v$)

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $s$ | Displacement | 位移 | m |
| $u$ | Initial velocity | 初速度 | m/s |
| $t$ | Time | 时间 | s |
| $a$ | Acceleration | 加速度 | m/s² |

**Derivation / 推导:** From area under a velocity-time graph (trapezium area).
**Conditions / 适用条件:** Constant acceleration. Missing $v$.
**Limitations / 局限性:** Does not involve final velocity. Cannot be used if final velocity is needed.

## Equation 4: $s = vt - \frac{1}{2}at^2$ (Missing $u$)

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $s$ | Displacement | 位移 | m |
| $v$ | Final velocity | 末速度 | m/s |
| $t$ | Time | 时间 | s |
| $a$ | Acceleration | 加速度 | m/s² |

**Derivation / 推导:** Rearrangement of $s = \frac{(u+v)}{2}t$ and $v = u + at$.
**Conditions / 适用条件:** Constant acceleration. Missing $u$.
**Limitations / 局限性:** Does not involve initial velocity. Less commonly used than equation 3.

## Equation 5: $v^2 = u^2 + 2as$ (Missing $t$)

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $v$ | Final velocity | 末速度 | m/s |
| $u$ | Initial velocity | 初速度 | m/s |
| $a$ | Acceleration | 加速度 | m/s² |
| $s$ | Displacement | 位移 | m |

**Derivation / 推导:** Eliminate $t$ from $v = u + at$ and $s = \frac{(u+v)}{2}t$.
**Conditions / 适用条件:** Constant acceleration. Missing $t$.
**Limitations / 局限性:** Does not involve time. Cannot be used if time is needed.

> 📷 **IMAGE PROMPT — DIAGRAM-02: SUVAT Equation Selection Table**
> A table with 5 rows. Column 1: Equation. Column 2: Missing Variable. Column 3: When to Use. Row 1: v = u + at, s, When time is known but displacement is not needed. Row 2: s = (u+v)t/2, a, When acceleration is not needed. Row 3: s = ut + 1/2 at², v, When final velocity is not needed. Row 4: s = vt - 1/2 at², u, When initial velocity is not needed. Row 5: v² = u² + 2as, t, When time is not needed.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Velocity-Time Graph and SUVAT / 速度-时间图与SUVAT

### Axes / 坐标轴 (EN+CN)
- **X-axis:** Time ($t$) / 时间 ($t$)
- **Y-axis:** Velocity ($v$) / 速度 ($v$)

### Shape / 形状 (EN+CN)
- A straight line with constant gradient (for constant acceleration). / 具有恒定斜率的直线（对于恒定加速度）。

### Gradient Meaning / 斜率含义 (EN+CN)
- Gradient = Acceleration ($a$) / 斜率 = 加速度 ($a$)

### Area Meaning / 面积含义 (EN+CN)
- Area under the graph = Displacement ($s$) / 图线下面积 = 位移 ($s$)

### Exam Interpretation / 考试解读 (EN+CN)
- **English:** The velocity-time graph is a visual representation of the SUVAT equations. The gradient gives $a$, the y-intercept gives $u$, and the area gives $s$. This graph can be used to derive the equations and to check your answers.
- **中文:** 速度-时间图是SUVAT方程的直观表示。斜率给出 $a$，y轴截距给出 $u$，面积给出 $s$。此图可用于推导方程和检查答案。

> 📷 **IMAGE PROMPT — DIAGRAM-03: Velocity-Time Graph with SUVAT Labels**
> A velocity-time graph showing a straight line starting at (0, u) and ending at (t, v). The gradient is labeled "a = (v-u)/t". The area under the line is shaded and labeled "s = area of trapezium". The y-intercept is labeled "u". The final point is labeled "v".

---

# 7. Required Diagrams / 必备图表

## 7.1 SUVAT Decision Flowchart / SUVAT决策流程图

### Description / 描述 (EN+CN)
- **English:** A flowchart that guides the student through the process of selecting the correct SUVAT equation.
- **中文:** 一个引导学生完成选择正确SUVAT方程过程的流程图。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM-04: SUVAT Decision Flowchart**
> A detailed flowchart. Start: "Read the problem". Decision 1: "Is acceleration constant?" If No: "Cannot use SUVAT". If Yes: "Proceed". Step 2: "List s, u, v, a, t". Step 3: "Identify given variables (tick)". Step 4: "Identify unknown variable (circle)". Step 5: "Find the missing variable (cross)". Decision 2: "Which variable is missing?" Branches to 5 boxes, each containing one SUVAT equation. Box 1: "Missing s: v = u + at". Box 2: "Missing a: s = (u+v)t/2". Box 3: "Missing v: s = ut + 1/2 at²". Box 4: "Missing u: s = vt - 1/2 at²". Box 5: "Missing t: v² = u² + 2as". End: "Solve the equation".

### Labels Required / 需要标注 (EN+CN)
- **English:** "Start", "Is acceleration constant?", "Cannot use SUVAT", "Proceed", "List variables", "Identify given", "Identify unknown", "Find missing", "Select equation", "Solve".
- **中文:** “开始”、“加速度是否恒定？”、“不能使用SUVAT”、“继续”、“列出变量”、“识别已知”、“识别未知”、“找出缺失”、“选择方程”、“求解”。

### Exam Importance / 考试重要性 (EN+CN)
- **English:** High. This flowchart is a mental model that should be internalised for exams. It prevents the common mistake of using the wrong equation.
- **中文:** 高。这个流程图是一个心理模型，应该在考试中内化。它防止了使用错误方程的常见错误。

---

# 8. Worked Examples / 典型例题

## Example 1: Car Accelerating / 汽车加速

### Question / 题目
**English:** A car accelerates uniformly from rest at $2.5 \text{ m/s}^2$ for $8.0 \text{ s}$. Calculate the distance travelled during this time.
**中文:** 一辆汽车从静止开始以 $2.5 \text{ m/s}^2$ 的加速度匀加速 $8.0 \text{ s}$。计算这段时间内行驶的距离。

### Solution / 解答
1.  **List variables:** $s = ?$, $u = 0 \text{ m/s}$ (from rest), $v = ?$, $a = 2.5 \text{ m/s}^2$, $t = 8.0 \text{ s}$.
2.  **Identify given:** $u$, $a$, $t$.
3.  **Identify unknown:** $s$.
4.  **Find missing:** $v$ is neither given nor asked for.
5.  **Select equation:** Missing $v$ → $s = ut + \frac{1}{2}at^2$.
6.  **Substitute:**
    $$ s = (0)(8.0) + \frac{1}{2}(2.5)(8.0)^2 $$
    $$ s = 0 + \frac{1}{2}(2.5)(64) $$
    $$ s = \frac{1}{2}(160) $$
    $$ s = 80 \text{ m} $$

### Final Answer / 最终答案
**Answer:** $80 \text{ m}$ | **答案：** $80 \text{ 米}$

### Quick Tip / 提示
(EN+CN)
- **English:** "From rest" is a key phrase meaning $u = 0$. Always look for implied variables.
- **中文:** “从静止开始”是一个关键短语，意味着 $u = 0$。始终寻找隐含的变量。

## Example 2: Braking Car / 刹车汽车

### Question / 题目
**English:** A car travelling at $20 \text{ m/s}$ brakes uniformly and comes to a stop in a distance of $50 \text{ m}$. Calculate the deceleration of the car.
**中文:** 一辆以 $20 \text{ m/s}$ 行驶的汽车匀减速，在 $50 \text{ m}$ 的距离内停下来。计算汽车的减速度。

### Solution / 解答
1.  **List variables:** $s = 50 \text{ m}$, $u = 20 \text{ m/s}$, $v = 0 \text{ m/s}$ (comes to a stop), $a = ?$, $t = ?$.
2.  **Identify given:** $s$, $u$, $v$.
3.  **Identify unknown:** $a$.
4.  **Find missing:** $t$ is neither given nor asked for.
5.  **Select equation:** Missing $t$ → $v^2 = u^2 + 2as$.
6.  **Substitute:**
    $$ 0^2 = 20^2 + 2(a)(50) $$
    $$ 0 = 400 + 100a $$
    $$ -400 = 100a $$
    $$ a = -4.0 \text{ m/s}^2 $$
    The negative sign indicates deceleration.

### Final Answer / 最终答案
**Answer:** $4.0 \text{ m/s}^2$ (deceleration) | **答案：** $4.0 \text{ m/s}^2$ (减速度)

### Quick Tip / 提示
(EN+CN)
- **English:** "Comes to a stop" means $v = 0$. The negative answer for $a$ confirms deceleration. You can state the magnitude as the deceleration.
- **中文:** “停下来”意味着 $v = 0$。$a$ 的负答案确认了减速。你可以将大小表述为减速度。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Direct SUVAT selection (single stage) | Very High | Easy | 📝 *待填入* |
| Multi-stage motion (e.g., two different accelerations) | High | Medium | 📝 *待填入* |
| Free fall under gravity (using $g$) | Very High | Medium | 📝 *待填入* |
| SUVAT with algebraic unknowns (e.g., prove that...) | Medium | Hard | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Calculate, Determine, Find, Show that, Derive, State.
- **中文:** 计算、确定、求出、证明、推导、说明。

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
Choosing the right equation is essential when analysing experimental data. For example, in an experiment to measure acceleration using a ticker timer or light gates:
- You might measure $u$, $v$, and $t$ directly, then use $a = \frac{v-u}{t}$ (missing $s$).
- You might measure $u$, $a$, and $t$, then use $s = ut + \frac{1}{2}at^2$ (missing $v$) to predict displacement.
- You must also consider uncertainties: if you have a precise measurement of $t$ but not $s$, you would choose an equation that does not require $s$.

**中文:**
在分析实验数据时，选择正确的方程至关重要。例如，在使用打点计时器或光门测量加速度的实验中：
- 你可能直接测量 $u$、$v$ 和 $t$，然后使用 $a = \frac{v-u}{t}$（缺失 $s$）。
- 你可能测量 $u$、$a$ 和 $t$，然后使用 $s = ut + \frac{1}{2}at^2$（缺失 $v$）来预测位移。
- 你还必须考虑不确定度：如果你对 $t$ 有精确测量但对 $s$ 没有，你会选择一个不需要 $s$ 的方程。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    subgraph "Core Concept"
        A[Choosing the Right SUVAT Equation] --> B[Missing Variable Method]
    end

    subgraph "Prerequisites"
        C[Displacement, Velocity and Acceleration] --> A
        D[The Five SUVAT Equations] --> A
    end

    subgraph "Application"
        A --> E[Free Fall Under Gravity]
        A --> F[Two-Stage Motion Problems]
        A --> G[Projectile Motion]
    end

    subgraph "Related Skills"
        A --> H[Motion Graphs]
        H --> I[Velocity-Time Graph]
        I --> J[Gradient = a]
        I --> K[Area = s]
    end

    subgraph "Key Equations"
        B --> L[v = u + at]
        B --> M[s = (u+v)t/2]
        B --> N[s = ut + 1/2 at²]
        B --> O[s = vt - 1/2 at²]
        B --> P[v² = u² + 2as]
    end

    L --> |Missing| Q[s]
    M --> |Missing| R[a]
    N --> |Missing| S[v]
    O --> |Missing| T[u]
    P --> |Missing| U[t]
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | The skill of selecting the correct SUVAT equation based on which variable is missing. / 根据缺失变量选择正确SUVAT方程的技能。 |
| **Key Formula / 核心公式** | $v = u + at$ (missing $s$), $s = \frac{(u+v)}{2}t$ (missing $a$), $s = ut + \frac{1}{2}at^2$ (missing $v$), $s = vt - \frac{1}{2}at^2$ (missing $u$), $v^2 = u^2 + 2as$ (missing $t$). |
| **Key Graph / 核心图表** | Velocity-Time Graph: Gradient = $a$, Area = $s$. / 速度-时间图：斜率 = $a$，面积 = $s$。 |
| **Exam Tip / 考试提示** | 1. List all 5 variables. 2. Tick given ones. 3. Circle unknown. 4. Cross the missing one. 5. Select the equation with the same missing variable. / 1. 列出所有5个变量。2. 勾选已知的。3. 圈出未知的。4. 叉掉缺失的。5. 选择具有相同缺失变量的方程。 |
| **Common Mistake / 常见错误** | Using an equation that includes a variable you don't know and can't find. / 使用包含你不知道且无法找到的变量的方程。 |
| **Conditions / 适用条件** | Constant acceleration only. / 仅适用于恒定加速度。 |