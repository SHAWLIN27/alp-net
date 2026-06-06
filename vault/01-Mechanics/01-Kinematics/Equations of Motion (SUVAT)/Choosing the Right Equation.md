# 1. Overview / 概述

**English:**
Choosing the right SUVAT equation is a critical skill in kinematics. With five equations and five variables ($s, u, v, a, t$), students must learn to identify which three variables are known and which one is required, then select the equation that contains exactly those four variables. This sub-topic bridges the gap between memorising [[The Five SUVAT Equations]] and applying them to real problems in [[Free Fall Under Gravity]] and [[Two-Stage Motion Problems]]. Mastering this skill reduces calculation time and prevents common errors in exams.

**中文:**
选择合适的SUVAT方程是运动学中的关键技能。面对五个方程和五个变量（$s, u, v, a, t$），学生必须学会识别已知的三个变量和需要求解的一个变量，然后选择恰好包含这四个变量的方程。本子知识点连接了记忆[[The Five SUVAT Equations]]和在[[Free Fall Under Gravity]]及[[Two-Stage Motion Problems]]中实际应用之间的桥梁。掌握这一技能可以减少计算时间，并防止考试中的常见错误。

---

# 2. Core Definition / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) |
| ------------ | --------------- | --------------- |
| **Variable Identification** / 变量识别 | The process of listing known and unknown SUVAT quantities from a problem statement before selecting an equation. | 在选择题目前，从问题陈述中列出已知和未知的SUVAT量的过程。 |
| **Missing Variable** / 缺失变量 | The SUVAT quantity that is neither given nor required, which must be absent from the chosen equation. | 既未给出也非所求的SUVAT量，必须从所选方程中排除。 |
| **Equation Selection** / 方程选择 | Matching the four known/required variables to the unique SUVAT equation that contains exactly those four. | 将四个已知/所求变量与恰好包含这四个变量的唯一SUVAT方程匹配。 |
| **Zero Initial Velocity** / 初速度为零 | A common special case where $u = 0$, often occurring in problems involving objects starting from rest. | 一种常见的特殊情况，$u = 0$，通常出现在涉及从静止开始运动的物体的问题中。 |
| **Sign Convention** / 符号约定 | A consistent rule for assigning positive/negative signs to displacement, velocity, and acceleration (e.g., upward = positive). | 为位移、速度和加速度分配正/负号的一致规则（例如，向上为正）。 |

---

# 3. Key Concepts / 关键概念

**English:**
The core idea is simple: each SUVAT equation omits exactly one of the five variables. The table below shows which variable is missing from each equation:

| Equation | Missing Variable |
|----------|-----------------|
| $v = u + at$ | $s$ |
| $s = ut + \frac{1}{2}at^2$ | $v$ |
| $s = \frac{1}{2}(u+v)t$ | $a$ |
| $v^2 = u^2 + 2as$ | $t$ |
| $s = vt - \frac{1}{2}at^2$ | $u$ |

**Step-by-step selection process:**

1. **List all five variables**: $s, u, v, a, t$
2. **Identify knowns**: Circle the three variables given in the problem
3. **Identify the unknown**: Underline the variable you need to find
4. **Find the missing variable**: The one variable that is neither known nor required
5. **Select the equation**: Choose the equation that omits that missing variable

**Common pitfalls:**
- Forgetting to check units (e.g., mixing km/h with m/s)
- Ignoring sign convention — especially in [[Free Fall Under Gravity]] where $a = -9.81 \text{ m/s}^2$ when upward is positive
- Assuming $u = 0$ when not stated — only use this if the object "starts from rest" or "is dropped"
- Using the wrong equation when the missing variable is not obvious

**中文:**
核心思想很简单：每个SUVAT方程恰好省略五个变量中的一个。下表显示了每个方程缺失的变量：

| 方程 | 缺失变量 |
|------|----------|
| $v = u + at$ | $s$ |
| $s = ut + \frac{1}{2}at^2$ | $v$ |
| $s = \frac{1}{2}(u+v)t$ | $a$ |
| $v^2 = u^2 + 2as$ | $t$ |
| $s = vt - \frac{1}{2}at^2$ | $u$ |

**逐步选择过程：**

1. **列出所有五个变量**：$s, u, v, a, t$
2. **识别已知量**：圈出问题中给出的三个变量
3. **识别未知量**：在需要求解的变量下划线
4. **找出缺失变量**：既非已知也非所求的那个变量
5. **选择方程**：选择省略该缺失变量的方程

**常见陷阱：**
- 忘记检查单位（例如，将km/h与m/s混用）
- 忽略符号约定——特别是在[[Free Fall Under Gravity]]中，当向上为正时，$a = -9.81 \text{ m/s}^2$
- 未明确说明时假设$u = 0$——仅当物体"从静止开始"或"被释放"时才使用
- 当缺失变量不明显时使用错误的方程

---

# 4. Formulas / 公式

The five SUVAT equations are:

$$ v = u + at $$
$$ s = ut + \frac{1}{2}at^2 $$
$$ s = \frac{1}{2}(u+v)t $$
$$ v^2 = u^2 + 2as $$
$$ s = vt - \frac{1}{2}at^2 $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
| ------------- | ------------ | ------------ | ----------- |
| $s$ | Displacement | 位移 | m |
| $u$ | Initial velocity | 初速度 | m/s |
| $v$ | Final velocity | 末速度 | m/s |
| $a$ | Acceleration | 加速度 | m/s² |
| $t$ | Time | 时间 | s |

**Selection Rule / 选择规则:**
Identify the missing variable (the one not given and not required), then pick the equation that omits that variable.

**Conditions / 适用条件:**
- All equations assume **constant acceleration**
- All variables must be in **consistent SI units** (m, m/s, m/s², s)
- Direction matters — use a consistent **sign convention**

> 📷 **IMAGE PROMPT — SUVAT-SELECTION-01: SUVAT Equation Selection Flowchart**
>
> **English Prompt:**
> A clean, textbook-style flowchart diagram showing the process of selecting the correct SUVAT equation. Start with a diamond "List s, u, v, a, t". Then a rectangle "Identify 3 knowns + 1 unknown". Then a diamond "Which variable is missing?" with five branches leading to five rectangles, each showing one SUVAT equation with the missing variable crossed out in red. Use a blue-to-white gradient background, black text, and red X marks. Labels in English. Vector illustration style, suitable for an A-Level physics textbook.
>
> **中文描述:**
> 一个干净、教科书风格的流程图，展示选择正确SUVAT方程的过程。从一个菱形"列出s, u, v, a, t"开始。然后是一个矩形"识别3个已知量+1个未知量"。然后是一个菱形"哪个变量缺失？"，有五个分支通向五个矩形，每个矩形显示一个SUVAT方程，缺失变量用红色叉号标记。使用蓝到白渐变背景，黑色文字，红色X标记。英文标签。矢量插图风格，适合A-Level物理教科书。
>
> **Labels Required / 需要标注:**
> * "List s, u, v, a, t" (start)
> * "Identify 3 knowns + 1 unknown"
> * "Which variable is missing?"
> * Each equation with missing variable crossed out
>
> **Style / 风格:** Textbook vector
>
> **Exam Relevance / 考试关联:**
> This flowchart is a quick reference for exam problems — students can mentally run through it in seconds.

---

# 5. Image Prompt / 图片提示

> 📷 **IMAGE PROMPT — SUVAT-SELECTION-02: Variable Identification Table**
>
> **English Prompt:**
> A clean, organized table with five rows and four columns. The first column lists the five SUVAT equations: v = u + at, s = ut + ½at², s = ½(u+v)t, v² = u² + 2as, s = vt - ½at². The second column shows the missing variable for each (s, v, a, t, u) in red. The third column shows a simple example problem for each equation (e.g., "Find v given u, a, t"). The fourth column shows a small icon representing the missing variable (e.g., a clock icon for t). White background, black text, red highlights. Minimalist textbook design.
>
> **中文描述:**
> 一个干净、有组织的表格，五行四列。第一列列出五个SUVAT方程：v = u + at, s = ut + ½at², s = ½(u+v)t, v² = u² + 2as, s = vt - ½at²。第二列用红色显示每个方程的缺失变量（s, v, a, t, u）。第三列显示每个方程的简单示例问题（例如，"已知u, a, t，求v"）。第四列显示代表缺失变量的小图标（例如，t用时钟图标）。白色背景，黑色文字，红色高亮。极简教科书设计。
>
> **Labels Required / 需要标注:**
> * Equation column
> * Missing variable column (red)
> * Example problem column
> * Icon column
>
> **Style / 风格:** Textbook vector
>
> **Exam Relevance / 考试关联:**
> This table is a quick cheat sheet for exam revision — students can memorize which variable each equation omits.

---

# 6. Worked Example / 典型例题

### Example 1: Basic Selection

### Question / 题目
**English:** A car accelerates uniformly from rest at $2.0 \text{ m/s}^2$ for $5.0$ seconds. Calculate the distance travelled.

**中文:** 一辆汽车从静止开始以$2.0 \text{ m/s}^2$的加速度匀加速行驶$5.0$秒。计算行驶的距离。

### Solution / 解答

**Step 1: Identify variables**
- Known: $u = 0$ (from rest), $a = 2.0 \text{ m/s}^2$, $t = 5.0 \text{ s}$
- Required: $s$
- Missing: $v$ (not given, not required)

**Step 2: Select equation**
The equation that omits $v$ is:
$$ s = ut + \frac{1}{2}at^2 $$

**Step 3: Substitute**
$$ s = (0)(5.0) + \frac{1}{2}(2.0)(5.0)^2 $$
$$ s = 0 + \frac{1}{2}(2.0)(25) $$
$$ s = 25 \text{ m} $$

### Final Answer / 最终答案
**Answer:** $s = 25 \text{ m}$ **答案:** $s = 25 \text{ 米}$

### Quick Tip / 提示
Always write "from rest" as $u = 0$ explicitly. This is the most common trigger for using $s = ut + \frac{1}{2}at^2$.

---

### Example 2: Missing Time

### Question / 题目
**English:** A ball is thrown vertically upward with an initial velocity of $15 \text{ m/s}$. It reaches a maximum height of $11.5 \text{ m}$. Calculate the acceleration due to gravity. (Assume upward is positive.)

**中文:** 一个球以$15 \text{ m/s}$的初速度竖直向上抛出，达到最大高度$11.5 \text{ m}$。计算重力加速度。（假设向上为正。）

### Solution / 解答

**Step 1: Identify variables**
- Known: $u = 15 \text{ m/s}$, $v = 0$ (at maximum height), $s = 11.5 \text{ m}$
- Required: $a$
- Missing: $t$ (not given, not required)

**Step 2: Select equation**
The equation that omits $t$ is:
$$ v^2 = u^2 + 2as $$

**Step 3: Substitute**
$$ 0^2 = (15)^2 + 2a(11.5) $$
$$ 0 = 225 + 23a $$
$$ 23a = -225 $$
$$ a = -9.78 \text{ m/s}^2 $$

### Final Answer / 最终答案
**Answer:** $a = -9.78 \text{ m/s}^2$ (downward) **答案:** $a = -9.78 \text{ m/s}^2$（向下）

### Quick Tip / 提示
At maximum height, $v = 0$. This is a key fact for [[Free Fall Under Gravity]] problems. The negative sign indicates acceleration is downward, opposite to the positive direction.

---

# 7. Flashcards / 闪卡

**Flashcard 1**
Q (EN): Which SUVAT equation omits displacement ($s$)?
Q (CN): 哪个SUVAT方程省略了位移（$s$）？
A (EN): $v = u + at$
A (CN): $v = u + at$

**Flashcard 2**
Q (EN): What is the first step in choosing the right SUVAT equation?
Q (CN): 选择正确SUVAT方程的第一步是什么？
A (EN): List all five variables ($s, u, v, a, t$) and identify which three are known and which one is required.
A (CN): 列出所有五个变量（$s, u, v, a, t$），并识别哪三个是已知的，哪一个是要求的。

**Flashcard 3**
Q (EN): If you know $u$, $a$, and $t$, and need to find $s$, which equation should you use?
Q (CN): 如果已知$u$、$a$和$t$，需要求$s$，应该使用哪个方程？
A (EN): $s = ut + \frac{1}{2}at^2$ (missing $v$)
A (CN): $s = ut + \frac{1}{2}at^2$（缺失$v$）

**Flashcard 4**
Q (EN): What is the "missing variable" in equation selection?
Q (CN): 方程选择中的"缺失变量"是什么？
A (EN): The variable that is neither given in the problem nor required to find — it must be absent from the chosen equation.
A (CN): 既未在问题中给出也非要求求解的变量——它必须从所选方程中排除。

**Flashcard 5**
Q (EN): When can you assume $u = 0$?
Q (CN): 何时可以假设$u = 0$？
A (EN): Only when the problem states the object "starts from rest" or "is dropped" (not thrown).
A (CN): 仅当问题说明物体"从静止开始"或"被释放"（而非被抛出）时。

---

# 8. Metadata / 元数据

```yaml
title:
  en: Choosing the Right SUVAT Equation
  cn: 选择合适的SUVAT方程
parent_topic: Equations of Motion (SUVAT)
parent_hub: "[[Equations of Motion (SUVAT)]]"
subject: Physics
syllabus:
  - CAIE 9702
  - Edexcel IAL
level: AS
node_type: leaf_concept
difficulty: intermediate
related_leaf_nodes:
  - "[[The Five SUVAT Equations]]"
  - "[[Free Fall Under Gravity]]"
  - "[[Two-Stage Motion Problems]]"
prerequisites:
  - "[[Displacement, Velocity and Acceleration]]"
related_topics:
  - "[[Motion Graphs]]"
  - "[[Projectile Motion]]"
language: bilingual_en_cn