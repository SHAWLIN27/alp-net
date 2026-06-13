# 1. Overview / 概述

**English:**
This sub-topic focuses on the critical skill of extracting physical quantities from the gradient of a graph. In A-Level Physics, graphs are not just visual representations of data; they are powerful tools for determining relationships between variables and calculating key physical constants. The gradient of a straight-line graph (or the tangent to a curve) directly relates to a physical quantity, often a constant or a derived parameter. Mastering this skill is essential for both the theory papers (where you interpret given graphs) and the practical papers (where you plot your own data and calculate results). This leaf node connects directly to [[Determining Gradient and Intercept]] and is a core application of [[Graph Plotting Skills]].

**中文:**
本子知识点专注于从图表斜率中提取物理量的关键技能。在A-Level物理中，图表不仅仅是数据的视觉呈现；它们是确定变量间关系和计算关键物理常数的强大工具。直线图（或曲线的切线）的斜率直接与一个物理量相关，通常是一个常数或一个导出参数。掌握这项技能对于理论试卷（你需要解释给定的图表）和实验试卷（你需要绘制自己的数据并计算结果）都至关重要。本叶节点直接连接到[[Determining Gradient and Intercept]]，是[[Graph Plotting Skills]]的核心应用。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 1.5 (a) Recognise that the gradient of a graph represents a physical quantity. | WPH11 U1: 1.13 Understand how to determine the gradient of a linear graph. |
| 1.5 (b) Calculate the gradient of a straight-line graph. | WPH11 U1: 1.14 Understand how to determine the gradient of a curve at a point by drawing a tangent. |
| 1.5 (c) Determine the gradient of a curve at a point by drawing a tangent. | WPH11 U1: 1.15 Be able to use the gradient of a graph to determine a physical quantity. |
| 1.5 (d) Use the gradient of a graph to determine a physical quantity. | WPH11 U1: 1.16 Understand the relationship between the gradient and the units of the physical quantity. |
| 1.5 (e) Understand the relationship between the gradient and the units of the physical quantity. | WPH11 U1: 1.17 Be able to use the gradient of a graph to determine the value of a constant. |
| 1.5 (f) Use the gradient of a graph to determine the value of a constant. | WPH11 U1: 1.18 Be able to use the gradient of a graph to determine the value of a derived quantity. |

**Examiner Expectations / 考官期望:**
- **English:** You must be able to calculate the gradient accurately from a straight-line graph, including using the correct units. For a curve, you must be able to draw an accurate tangent and then calculate its gradient. The final step is to equate this gradient to a physical quantity (e.g., gradient = resistance, gradient = acceleration, gradient = spring constant) and state the final answer with correct units.
- **中文:** 你必须能够从直线图中准确计算斜率，包括使用正确的单位。对于曲线，你必须能够绘制准确的切线，然后计算其斜率。最后一步是将此斜率等同于一个物理量（例如，斜率 = 电阻，斜率 = 加速度，斜率 = 劲度系数），并给出带有正确单位的最终答案。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Gradient** / 斜率 | The rate of change of the y-axis variable with respect to the x-axis variable. For a straight line, it is calculated as $\frac{\Delta y}{\Delta x}$. | y轴变量相对于x轴变量的变化率。对于直线，计算为 $\frac{\Delta y}{\Delta x}$。 | Using data points from the table instead of reading from the line of best fit. / 使用表格中的数据点而不是从最佳拟合线上读取。 |
| **Tangent** / 切线 | A straight line that touches a curve at a single point and has the same gradient as the curve at that point. | 在单点处接触曲线，并且在该点处具有与曲线相同斜率的直线。 | Drawing a line that crosses the curve (a secant) instead of just touching it. / 绘制一条穿过曲线（割线）而不是仅仅接触它的线。 |
| **Physical Quantity** / 物理量 | A property of a material or system that can be measured and expressed as a numerical value with a unit. | 材料或系统的属性，可以测量并以带有单位的数值表示。 | Forgetting to include the unit when stating the physical quantity derived from the gradient. / 在陈述从斜率导出的物理量时忘记包含单位。 |
| **Line of Best Fit** / 最佳拟合线 | The single straight line that best represents the trend of the plotted data points, minimizing the distance between the line and all points. | 最能代表绘制数据点趋势的单条直线，使线与所有点之间的距离最小化。 | Drawing a line that connects the first and last data point, ignoring the scatter of intermediate points. / 绘制连接第一个和最后一个数据点的线，忽略中间点的散布。 |
| **Derived Quantity** / 导出量 | A physical quantity that is calculated from two or more base quantities (e.g., velocity from displacement and time). | 由两个或多个基本量计算得出的物理量（例如，由位移和时间计算出的速度）。 | Confusing the gradient with the intercept. / 将斜率与截距混淆。 |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Gradient as a Physical Quantity / 斜率作为物理量

### Explanation / 解释
**English:** The fundamental principle is that the gradient of a graph is not just a number; it represents the ratio of two physical quantities. For example, on a graph of **displacement (y-axis)** against **time (x-axis)**, the gradient $\frac{\Delta s}{\Delta t}$ is the **velocity**. On a graph of **force (y-axis)** against **extension (x-axis)** for a spring, the gradient $\frac{\Delta F}{\Delta x}$ is the **spring constant**, $k$. The key is to identify what the axes represent and then perform a dimensional analysis to see what physical quantity the gradient must be. This is linked to [[SI Units, Prefixes and Homogeneity of Equations]].

**中文:** 基本原则是图表的斜率不仅仅是一个数字；它代表两个物理量的比率。例如，在**位移（y轴）** 对**时间（x轴）** 的图表上，斜率 $\frac{\Delta s}{\Delta t}$ 就是**速度**。在弹簧的**力（y轴）** 对**伸长量（x轴）** 的图表上，斜率 $\frac{\Delta F}{\Delta x}$ 就是**劲度系数** $k$。关键在于识别坐标轴代表什么，然后进行量纲分析，以确定斜率必须是哪个物理量。这与[[SI Units, Prefixes and Homogeneity of Equations]]有关。

### Physical Meaning / 物理意义
**English:** The gradient tells you how much the y-axis quantity changes for every unit change in the x-axis quantity. A steep gradient means a large change in y for a small change in x. A shallow gradient means a small change in y for a large change in x.
**中文:** 斜率告诉你，对于x轴量的每一个单位变化，y轴量变化了多少。陡峭的斜率意味着x的小变化导致y的大变化。平缓的斜率意味着x的大变化导致y的小变化。

### Common Misconceptions / 常见误区
- **English:** Students often think the gradient is just the "steepness" of the line. While true, they forget that the numerical value of the gradient depends entirely on the scales of the axes.
- **中文:** 学生通常认为斜率只是线的“陡峭程度”。虽然没错，但他们忘记了斜率的数值完全取决于坐标轴的刻度。
- **English:** Another mistake is calculating the gradient using the coordinates of the data points from the table, rather than using two points on the line of best fit. The line of best fit averages out experimental errors.
- **中文:** 另一个错误是使用表格中数据点的坐标来计算斜率，而不是使用最佳拟合线上的两个点。最佳拟合线平均了实验误差。

### Exam Tips / 考试提示
- **English:** Always use a large triangle for your gradient calculation. Choose two points on the line of best fit that are far apart (at least half the length of the line) to minimize percentage uncertainty.
- **中文:** 始终使用大三角形进行斜率计算。在最佳拟合线上选择两个相距较远的点（至少是线长的一半），以最小化百分比不确定度。
- **English:** Show your working clearly: $\text{Gradient} = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$. Then state the physical quantity and its unit.
- **中文:** 清晰地展示你的计算过程：$\text{斜率} = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$。然后说明物理量及其单位。

> 📷 **IMAGE PROMPT — GRADIENT-01: Gradient Calculation Triangle**
> A clear diagram of a straight-line graph with a large right-angled triangle drawn under the line. The points (x1, y1) and (x2, y2) are marked on the line, and the lengths Δx and Δy are clearly labeled with arrows. The graph has labeled axes (e.g., "Force / N" and "Extension / m").

---

## 4.2 Gradient of a Curve (Tangents) / 曲线的斜率（切线）

### Explanation / 解释
**English:** For non-linear relationships, the gradient is not constant. To find the gradient at a specific point (e.g., the initial velocity or the maximum rate of reaction), you must draw a tangent to the curve at that point. A tangent is a straight line that just touches the curve at the point of interest. Once the tangent is drawn, you calculate its gradient using the same $\frac{\Delta y}{\Delta x}$ method as for a straight line. This is crucial for topics like [[Motion Graphs]] and [[Thermal Physics]].

**中文:** 对于非线性关系，斜率不是常数。要找到特定点（例如，初始速度或最大反应速率）的斜率，你必须在那个点绘制曲线的切线。切线是一条在感兴趣的点处刚好接触曲线的直线。一旦画好切线，你就可以使用与直线相同的 $\frac{\Delta y}{\Delta x}$ 方法计算其斜率。这对于[[Motion Graphs]]和[[Thermal Physics]]等主题至关重要。

### Physical Meaning / 物理意义
**English:** The gradient of a curve at a point gives the instantaneous rate of change. For example, on a displacement-time graph for an accelerating car, the gradient of the tangent at a specific time gives the instantaneous velocity at that time.
**中文:** 曲线在某一点的斜率给出了瞬时变化率。例如，在加速汽车的位移-时间图上，特定时间点的切线斜率给出了该时刻的瞬时速度。

### Common Misconceptions / 常见误区
- **English:** Drawing a tangent that is too short or not perfectly aligned with the curve. The tangent must be long enough to allow for an accurate gradient calculation.
- **中文:** 绘制的切线太短或与曲线未完美对齐。切线必须足够长，以便进行准确的斜率计算。
- **English:** Using a point on the curve itself as one of the points for the gradient calculation. The two points must be on the tangent line, not on the curve.
- **中文:** 使用曲线上的一个点作为斜率计算的点之一。这两个点必须在切线上，而不是在曲线上。

### Exam Tips / 考试提示
- **English:** Use a clear plastic ruler to draw the tangent. Place the ruler so that it only touches the curve at the desired point and is symmetrical on either side. Draw the tangent line extending well beyond the point of contact.
- **中文:** 使用透明的塑料尺来绘制切线。放置尺子，使其仅在所需点接触曲线，并在两侧对称。绘制切线，使其远远超出接触点。
- **English:** Mark the point of tangency clearly with a cross (×). Then, choose two points on the tangent line, far apart, to calculate the gradient.
- **中文:** 用叉号（×）清晰地标记切点。然后，在切线上选择两个相距较远的点来计算斜率。

> 📷 **IMAGE PROMPT — TANGENT-01: Drawing a Tangent to a Curve**
> A diagram showing a curved line on a graph. At a specific point (marked with a cross), a straight tangent line is drawn. The tangent line is long and extends on both sides of the point. A gradient triangle is drawn under the tangent line, with Δx and Δy labeled. The axes are labeled (e.g., "Displacement / m" and "Time / s").

---

# 5. Essential Equations / 核心公式

## 5.1 Gradient of a Straight Line / 直线斜率

$$ m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $m$ | Gradient of the line | 线的斜率 | Depends on axes (e.g., m/s, N/m) |
| $\Delta y$ | Change in the y-axis variable | y轴变量的变化 | Unit of y-axis |
| $\Delta x$ | Change in the x-axis variable | x轴变量的变化 | Unit of x-axis |
| $(x_1, y_1)$ | First point on the line of best fit | 最佳拟合线上的第一个点 | Units of axes |
| $(x_2, y_2)$ | Second point on the line of best fit | 最佳拟合线上的第二个点 | Units of axes |

**Derivation / 推导:** This is the standard definition of the slope of a line.
**Conditions / 适用条件:** The relationship between x and y must be linear.
**Limitations / 局限性:** This formula gives the average gradient between two points. For a curve, it only gives the gradient if the two points are infinitesimally close (i.e., a tangent).

## 5.2 Relating Gradient to a Physical Quantity / 将斜率与物理量关联

$$ \text{Physical Quantity} = \text{Gradient} \times \text{Unit Factor} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| Physical Quantity | The constant or derived quantity being found | 正在寻找的常数或导出量 | Depends on the quantity |
| Gradient | The numerical value of the gradient | 斜率的数值 | Depends on axes |
| Unit Factor | A factor of 1, but with the correct derived unit | 一个因子为1，但带有正确的导出单位 | The unit of the physical quantity |

**Derivation / 推导:** This is a conceptual equation. For example, if a graph of $V$ (voltage) against $I$ (current) has a gradient of 10, and the axes are in volts and amperes, then the physical quantity is $R = 10 \, \Omega$.
**Conditions / 适用条件:** The graph must be plotted correctly with the appropriate variables on each axis.
**Limitations / 局限性:** This requires you to know the relationship between the variables. For example, $V = IR$ tells you that the gradient of a $V$ vs $I$ graph is $R$.

> 📋 **CIE Only:** In CIE practical papers, you are often asked to "use the gradient of the graph to determine the value of [a constant]". You must show the gradient calculation and then the substitution into the relevant formula.
> 📋 **Edexcel Only:** In Edexcel, the focus is on "derived quantities". You must be able to explain why the gradient represents a specific derived quantity, often using base units.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Linear Graph: Force vs Extension for a Spring / 线性图：弹簧的力与伸长量

### Axes / 坐标轴
- **x-axis:** Extension, $x$ (m)
- **y-axis:** Force, $F$ (N)

### Shape / 形状
- **English:** A straight line passing through the origin (for an ideal spring obeying Hooke's Law).
- **中文:** 一条通过原点的直线（对于遵循胡克定律的理想弹簧）。

### Gradient Meaning / 斜率含义
- **English:** The gradient represents the spring constant, $k$, where $k = \frac{F}{x}$. The unit is N/m.
- **中文:** 斜率代表劲度系数 $k$，其中 $k = \frac{F}{x}$。单位是 N/m。

### Area Meaning / 面积含义
- **English:** The area under the graph represents the elastic potential energy stored in the spring, $E = \frac{1}{2} F x$.
- **中文:** 图表下的面积代表弹簧中储存的弹性势能 $E = \frac{1}{2} F x$。

### Exam Interpretation / 考试解读
- **English:** If the line does not pass through the origin, it may indicate a systematic error (e.g., the spring had an initial tension). The gradient still gives the spring constant.
- **中文:** 如果线不通过原点，可能表明存在系统误差（例如，弹簧有初始张力）。斜率仍然给出劲度系数。

## 6.2 Curved Graph: Displacement vs Time for an Accelerating Object / 曲线图：加速物体的位移与时间

### Axes / 坐标轴
- **x-axis:** Time, $t$ (s)
- **y-axis:** Displacement, $s$ (m)

### Shape / 形状
- **English:** A curve that gets steeper over time (for constant acceleration from rest).
- **中文:** 一条随时间变陡的曲线（对于从静止开始的匀加速运动）。

### Gradient Meaning / 斜率含义
- **English:** The gradient of the tangent at any point gives the instantaneous velocity at that time. The unit is m/s.
- **中文:** 任意点切线的斜率给出该时刻的瞬时速度。单位是 m/s。

### Area Meaning / 面积含义
- **English:** The area under a velocity-time graph gives displacement. This is not directly applicable here.
- **中文:** 速度-时间图下的面积给出位移。这不直接适用于此处。

### Exam Interpretation / 考试解读
- **English:** To find the velocity at a specific time, you must draw a tangent at that time. The gradient of the tangent is the velocity. The steeper the curve, the greater the velocity.
- **中文:** 要找到特定时间的速度，你必须在那个时间绘制切线。切线的斜率就是速度。曲线越陡，速度越大。

---

# 7. Required Diagrams / 必备图表

## 7.1 Gradient Triangle on a Line of Best Fit / 最佳拟合线上的斜率三角形

### Description / 描述
- **English:** A diagram showing a straight-line graph with a line of best fit. A large right-angled triangle is drawn under the line, with the hypotenuse being a segment of the line of best fit. The vertical side is labeled $\Delta y$ and the horizontal side is labeled $\Delta x$.
- **中文:** 一个显示带有最佳拟合线的直线图的图表。在线下方绘制了一个大的直角三角形，斜边是最佳拟合线的一段。垂直边标记为 $\Delta y$，水平边标记为 $\Delta x$。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM-01: Gradient Triangle**
> A clear, high-contrast diagram of a graph with a straight line of best fit. A large, right-angled triangle is drawn below the line. The hypotenuse of the triangle is a segment of the line. The vertical side of the triangle is labeled "Δy" with an arrow pointing up. The horizontal side is labeled "Δx" with an arrow pointing right. The points (x1, y1) and (x2, y2) are marked on the line at the vertices of the triangle. The axes are labeled "Variable Y / Unit" and "Variable X / Unit". The graph has a grid for clarity.

### Labels Required / 需要标注
- **English:** $\Delta y$, $\Delta x$, $(x_1, y_1)$, $(x_2, y_2)$, Line of Best Fit, Axes labels with units.
- **中文:** $\Delta y$, $\Delta x$, $(x_1, y_1)$, $(x_2, y_2)$, 最佳拟合线, 带单位的坐标轴标签。

### Exam Importance / 考试重要性
- **English:** This is the most common diagram in practical exams. You must be able to draw this triangle on your own graph to calculate the gradient. It is a direct requirement of the syllabus.
- **中文:** 这是实验考试中最常见的图表。你必须能够在自己的图表上绘制这个三角形来计算斜率。这是考纲的直接要求。

## 7.2 Tangent to a Curve / 曲线的切线

### Description / 描述
- **English:** A diagram showing a curved line on a graph. At a specific point (marked with a cross), a straight tangent line is drawn. The tangent line is long and extends on both sides of the point. A gradient triangle is drawn under the tangent line.
- **中文:** 一个显示图表上曲线的图。在特定点（用叉号标记），绘制了一条直线切线。切线很长，并在点的两侧延伸。在切线下方绘制了一个斜率三角形。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM-02: Tangent to a Curve**
> A diagram of a graph with a curved line (e.g., a parabola). At a specific point on the curve, marked with a large "×", a straight line is drawn that just touches the curve. The line is long and extends well beyond the point of contact. A gradient triangle is drawn under this tangent line, with "Δy" and "Δx" labeled. The axes are labeled "Displacement / m" and "Time / s". The point of tangency is clearly indicated.

### Labels Required / 需要标注
- **English:** Tangent, Point of Tangency (×), $\Delta y$, $\Delta x$, Axes labels with units.
- **中文:** 切线, 切点 (×), $\Delta y$, $\Delta x$, 带单位的坐标轴标签。

### Exam Importance / 考试重要性
- **English:** This is essential for finding instantaneous rates of change from non-linear graphs. It is a common question in both theory and practical papers.
- **中文:** 这对于从非线性图中找到瞬时变化率至关重要。这是理论和实验试卷中的常见问题。

---

# 8. Worked Examples / 典型例题

## Example 1: Finding the Spring Constant from a Force-Extension Graph / 从力-伸长量图中求劲度系数

### Question / 题目
**English:** A student plots a graph of force (F) against extension (x) for a spring. The line of best fit passes through the points (0.02 m, 1.5 N) and (0.08 m, 6.0 N). Calculate the spring constant, k.
**中文:** 一名学生绘制了弹簧的力 (F) 对伸长量 (x) 的图表。最佳拟合线通过点 (0.02 m, 1.5 N) 和 (0.08 m, 6.0 N)。计算劲度系数 k。

### Solution / 解答
**Step 1: Calculate the gradient.**
$$ m = \frac{\Delta y}{\Delta x} = \frac{6.0 \, \text{N} - 1.5 \, \text{N}}{0.08 \, \text{m} - 0.02 \, \text{m}} = \frac{4.5 \, \text{N}}{0.06 \, \text{m}} = 75 \, \text{N/m} $$

**Step 2: Relate the gradient to the physical quantity.**
From Hooke's Law, $F = kx$. Therefore, the gradient of a $F$ vs $x$ graph is the spring constant, $k$.
$$ k = \text{Gradient} = 75 \, \text{N/m} $$

### Final Answer / 最终答案
**Answer:** $k = 75 \, \text{N/m}$ | **答案：** $k = 75 \, \text{N/m}$

### Quick Tip / 提示
- **English:** Always include the units in your calculation. The units of the gradient (N/m) tell you the units of the spring constant.
- **中文:** 始终在计算中包含单位。斜率的单位 (N/m) 告诉你劲度系数的单位。

## Example 2: Finding Instantaneous Velocity from a Displacement-Time Graph / 从位移-时间图中求瞬时速度

### Question / 题目
**English:** A car's motion is described by the displacement-time graph $s = 2t^2$. A tangent is drawn at $t = 3.0 \, \text{s}$. The tangent passes through the points (1.0 s, 2.0 m) and (5.0 s, 34.0 m). Calculate the instantaneous velocity at $t = 3.0 \, \text{s}$.
**中文:** 一辆汽车的运动由位移-时间图 $s = 2t^2$ 描述。在 $t = 3.0 \, \text{s}$ 处绘制了一条切线。切线通过点 (1.0 s, 2.0 m) 和 (5.0 s, 34.0 m)。计算在 $t = 3.0 \, \text{s}$ 时的瞬时速度。

### Solution / 解答
**Step 1: Calculate the gradient of the tangent.**
$$ m = \frac{\Delta y}{\Delta x} = \frac{34.0 \, \text{m} - 2.0 \, \text{m}}{5.0 \, \text{s} - 1.0 \, \text{s}} = \frac{32.0 \, \text{m}}{4.0 \, \text{s}} = 8.0 \, \text{m/s} $$

**Step 2: Relate the gradient to the physical quantity.**
The gradient of a displacement-time graph is the velocity.
$$ v = \text{Gradient} = 8.0 \, \text{m/s} $$

### Final Answer / 最终答案
**Answer:** $v = 8.0 \, \text{m/s}$ | **答案：** $v = 8.0 \, \text{m/s}$

### Quick Tip / 提示
- **English:** The two points used for the gradient calculation must be on the tangent line, not on the original curve.
- **中文:** 用于斜率计算的两个点必须在切线上，而不是在原始曲线上。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate gradient from a given straight-line graph. | Very High | Easy | 📝 *待填入* |
| Draw a tangent and calculate gradient from a curve. | High | Medium | 📝 *待填入* |
| Use gradient to determine a physical constant (e.g., $g$, $k$, $R$). | Very High | Medium | 📝 *待填入* |
| Explain the physical meaning of the gradient. | Medium | Easy | 📝 *待填入* |
| Determine the units of the gradient and the physical quantity. | Medium | Medium | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** Calculate, Determine, Use, Show, Explain, State.
- **中文:** 计算, 确定, 使用, 展示, 解释, 陈述。

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic is the core of the practical paper (Paper 3 for CAIE, Unit 6 for Edexcel). After plotting your data and drawing a line of best fit, you will almost always be asked to:
1. **Calculate the gradient** of the line of best fit.
2. **Determine a physical quantity** from the gradient (e.g., the Young modulus, the resistivity of a wire, the acceleration due to gravity).
3. **Calculate the uncertainty** in the gradient (using the worst acceptable line) and hence the uncertainty in the physical quantity. This connects to [[Uncertainties and Errors]].
4. **State the units** of the gradient and the physical quantity.

**中文:**
本子知识点是实验试卷（CAIE的Paper 3，Edexcel的Unit 6）的核心。在绘制数据并画出最佳拟合线后，你几乎总是会被要求：
1. **计算**最佳拟合线的**斜率**。
2. 从斜率中**确定一个物理量**（例如，杨氏模量、导线的电阻率、重力加速度）。
3. **计算斜率的不确定度**（使用最差可接受线），从而计算物理量的不确定度。这与[[Uncertainties and Errors]]有关。
4. **陈述**斜率和物理量的**单位**。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Show connections for this leaf node
    A[Graph Plotting Skills] --> B[Using Graph Gradients to Find Physical Quantities]
    B --> C[Calculate Gradient of Straight Line]
    B --> D[Draw Tangent & Calculate Gradient of Curve]
    B --> E[Relate Gradient to Physical Quantity]
    B --> F[Determine Units of Gradient & Quantity]
    
    C --> G[Use Δy/Δx Formula]
    C --> H[Use Large Triangle]
    C --> I[Use Points on Line of Best Fit]
    
    D --> J[Draw Accurate Tangent]
    D --> K[Calculate Gradient of Tangent]
    
    E --> L[Identify Relationship (e.g., F=kx)]
    E --> M[Equate Gradient to Constant]
    
    F --> N[Units of Gradient = Units of Quantity]
    
    B --> O[Practical Skills]
    O --> P[Paper 3 / Unit 6]
    O --> Q[Uncertainty Calculation]
    
    subgraph Prerequisites
        R[SI Units, Prefixes and Homogeneity of Equations]
    end
    
    subgraph Related Topics
        S[Uncertainties and Errors]
        T[Motion Graphs]
        U[Thermal Physics]
    end
    
    R --> B
    B --> S
    B --> T
    B --> U
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Gradient = $\frac{\Delta y}{\Delta x}$. It represents the rate of change of y with respect to x. / 斜率 = $\frac{\Delta y}{\Delta x}$。它表示y相对于x的变化率。 |
| **Key Formula / 核心公式** | $m = \frac{y_2 - y_1}{x_2 - x_1}$ (for a straight line or tangent). / $m = \frac{y_2 - y_1}{x_2 - x_1}$（用于直线或切线）。 |
| **Key Graph / 核心图表** | Force vs Extension: Gradient = Spring Constant ($k$). / 力 vs 伸长量：斜率 = 劲度系数 ($k$)。 |
| **Key Graph / 核心图表** | Displacement vs Time: Gradient of Tangent = Instantaneous Velocity ($v$). / 位移 vs 时间：切线斜率 = 瞬时速度 ($v$)。 |
| **Exam Tip / 考试提示** | Always use a large triangle. Use points on the line of best fit, not data points. Include units in your answer. / 始终使用大三角形。使用最佳拟合线上的点，而不是数据点。在答案中包含单位。 |
| **Common Mistake / 常见错误** | Using data points instead of line of best fit points. Forgetting units. Drawing a secant instead of a tangent. / 使用数据点而不是最佳拟合线上的点。忘记单位。绘制割线而不是切线。 |