# Using Worst-Fit Lines for Uncertainty in Gradient
# 使用最差拟合线确定梯度不确定度

---

# 1. Overview / 概述

**English:**
This sub-topic covers the technique of using **worst-fit lines** (also called maximum/minimum slope lines) to estimate the uncertainty in the gradient of a straight-line graph. When experimental data points have [[Error Bars on Graphs|error bars]], the best-fit line represents the most likely relationship, but the true relationship could lie anywhere within the uncertainty range. By drawing the steepest and shallowest reasonable lines that still pass through all error bars, we can calculate the uncertainty in the gradient. This is a critical skill for [[Uncertainty Analysis in Practical Work]] at A-Level, particularly in Paper 3/5 (CAIE) and Unit 3/6 (Edexcel) practical examinations.

**中文:**
本子知识点涵盖使用**最差拟合线**（也称为最大/最小斜率线）来估算直线图梯度不确定度的技术。当实验数据点带有[[Error Bars on Graphs|误差棒]]时，最佳拟合线代表最可能的关系，但真实关系可能位于不确定度范围内的任何位置。通过绘制穿过所有误差棒的最陡和最缓的合理直线，我们可以计算梯度的不确定度。这是A-Level[[Uncertainty Analysis in Practical Work|实验不确定度分析]]中的关键技能，尤其在CAIE Paper 3/5和Edexcel Unit 3/6实验考试中。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| Draw and use worst-fit lines (maximum and minimum gradient lines) to determine the uncertainty in a gradient | Use worst-fit lines to estimate the uncertainty in the gradient of a linear graph |
| Calculate the uncertainty in gradient as $\frac{\text{max gradient} - \text{min gradient}}{2}$ | Determine the range of possible gradients from worst-fit lines |
| Apply this technique to evaluate the reliability of experimental results | Use gradient uncertainty to assess whether a relationship is valid |

**Examiner Expectations / 考官期望:**
- **English:** You must draw both best-fit and worst-fit lines on the same graph, clearly labelled. The worst-fit lines must pass through ALL error bars (or data points if no error bars are given). The gradient uncertainty is then calculated as half the range between maximum and minimum gradients.
- **中文:** 你必须在同一张图上绘制最佳拟合线和最差拟合线，并清晰标注。最差拟合线必须穿过所有误差棒（如果没有误差棒则穿过所有数据点）。梯度不确定度计算为最大和最小梯度之间范围的一半。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Best-fit line** / 最佳拟合线 | The straight line that best represents the trend of the data, passing as close as possible to all data points | 最能代表数据趋势的直线，尽可能靠近所有数据点 | Drawing a line that connects the first and last points instead of balancing the points |
| **Worst-fit line** / 最差拟合线 | A line of extreme slope (maximum or minimum) that still passes through all error bars or data points | 仍能穿过所有误差棒或数据点的极端斜率线（最大或最小） | Drawing lines that miss error bars or are not straight |
| **Maximum gradient line** / 最大梯度线 | The steepest possible straight line that passes through all error bars | 穿过所有误差棒的最陡直线 | Using only the top of the first error bar and bottom of the last |
| **Minimum gradient line** / 最小梯度线 | The shallowest possible straight line that passes through all error bars | 穿过所有误差棒的最缓直线 | Using only the bottom of the first error bar and top of the last |
| **Gradient uncertainty** / 梯度不确定度 | Half the range between maximum and minimum gradients: $\Delta m = \frac{m_{\text{max}} - m_{\text{min}}}{2}$ | 最大和最小梯度之间范围的一半 | Forgetting to divide by 2, or using the wrong sign |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Principle of Worst-Fit Lines / 最差拟合线原理

### Explanation / 解释
**English:**
When you plot experimental data with [[Error Bars on Graphs|error bars]], the [[Best-Fit Line|best-fit line]] represents the most probable relationship between variables. However, due to random uncertainties, the true relationship could be different. The **worst-fit lines** define the boundaries of what is still consistent with the data. The maximum gradient line is the steepest line that still passes through all error bars, while the minimum gradient line is the shallowest. Together, they define a range of possible gradients, and the uncertainty is half this range.

**中文:**
当你绘制带有[[Error Bars on Graphs|误差棒]]的实验数据时，[[Best-Fit Line|最佳拟合线]]代表变量之间最可能的关系。然而，由于随机不确定度，真实关系可能不同。**最差拟合线**定义了仍然与数据一致的边界。最大梯度线是仍然穿过所有误差棒的最陡直线，而最小梯度线是最缓的直线。它们共同定义了一个可能的梯度范围，不确定度是这个范围的一半。

### Physical Meaning / 物理意义
**English:**
The gradient uncertainty represents the confidence interval for the slope of the relationship. If the gradient uncertainty is large relative to the gradient itself, the relationship is poorly defined, and you may not be able to conclude whether a linear relationship exists at all.

**中文:**
梯度不确定度代表了关系斜率的置信区间。如果梯度不确定度相对于梯度本身很大，那么关系定义不清，你可能无法得出是否存在线性关系的结论。

### Common Misconceptions / 常见误区
- ❌ **Drawing worst-fit lines that miss error bars** — Worst-fit lines MUST pass through ALL error bars, not just most of them.
- ❌ **Using only two points** — Worst-fit lines are not simply connecting the top of the first error bar to the bottom of the last; they must consider ALL data points.
- ❌ **Confusing worst-fit with best-fit** — The worst-fit line is NOT a bad drawing; it is a deliberate extreme line.
- ❌ **Forgetting to label** — All three lines (best-fit, max gradient, min gradient) must be clearly labelled on the graph.
- ❌ **Using worst-fit lines when there are no error bars** — If no error bars are given, worst-fit lines should pass through the data points themselves, but this is less reliable.

- ❌ **绘制错过误差棒的最差拟合线** — 最差拟合线必须穿过所有误差棒，而不仅仅是大部分。
- ❌ **只使用两个点** — 最差拟合线不仅仅是连接第一个误差棒的顶部和最后一个的底部；它们必须考虑所有数据点。
- ❌ **混淆最差拟合与最佳拟合** — 最差拟合线不是画得不好；它是故意绘制的极端线。
- ❌ **忘记标注** — 所有三条线（最佳拟合、最大梯度、最小梯度）必须在图上清晰标注。
- ❌ **在没有误差棒时使用最差拟合线** — 如果没有给出误差棒，最差拟合线应穿过数据点本身，但这不太可靠。

### Exam Tips / 考试提示
- **English:** Always use a transparent ruler to draw worst-fit lines. Mark the points where the line touches the error bars. Calculate gradients using large triangles (at least half the line length). Show all working.
- **中文:** 始终使用透明直尺绘制最差拟合线。标记线与误差棒接触的点。使用大三角形（至少线长的一半）计算梯度。展示所有计算过程。

> 📷 **IMAGE PROMPT — WFL-01: Worst-Fit Lines on a Graph**
> A scatter graph with 6 data points, each with vertical error bars. Three straight lines are drawn: a central best-fit line (dashed), a steeper maximum gradient line (solid, labelled "max gradient"), and a shallower minimum gradient line (solid, labelled "min gradient"). All three lines pass through all error bars. The graph has labelled axes "x" and "y". Triangles are shown for gradient calculations on each line.

---

# 5. Essential Equations / 核心公式

## 5.1 Gradient Uncertainty Formula / 梯度不确定度公式

$$ \Delta m = \frac{m_{\text{max}} - m_{\text{min}}}{2} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\Delta m$ | Uncertainty in gradient | 梯度不确定度 | Same as gradient units |
| $m_{\text{max}}$ | Gradient of maximum slope line | 最大斜率线的梯度 | Same as gradient units |
| $m_{\text{min}}$ | Gradient of minimum slope line | 最小斜率线的梯度 | Same as gradient units |

**Derivation / 推导:**
The true gradient lies somewhere between the maximum and minimum possible gradients. The range is $m_{\text{max}} - m_{\text{min}}$. The uncertainty is half this range, assuming the true value is equally likely to be anywhere within the range.

**Conditions / 适用条件:**
- **English:** Only valid when the relationship is expected to be linear. Error bars must be present on at least one axis (usually y-axis). The worst-fit lines must pass through ALL error bars.
- **中文:** 仅当关系预期为线性时有效。至少一个轴（通常是y轴）上必须有误差棒。最差拟合线必须穿过所有误差棒。

**Limitations / 局限性:**
- **English:** This method assumes the uncertainty is symmetric. It does not account for systematic errors. It requires subjective judgment in drawing the worst-fit lines. For non-linear relationships, this method cannot be used directly.
- **中文:** 该方法假设不确定度是对称的。它不考虑系统误差。绘制最差拟合线需要主观判断。对于非线性关系，不能直接使用此方法。

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Graph Showing Best-Fit and Worst-Fit Lines / 显示最佳拟合和最差拟合线的图表

### Axes / 坐标轴
- **x-axis:** Independent variable (e.g., mass, time, length) / 自变量（如质量、时间、长度）
- **y-axis:** Dependent variable (e.g., extension, voltage, temperature) / 因变量（如伸长量、电压、温度）

### Shape / 形状
- **English:** Three straight lines on the same scatter graph. The best-fit line is central. The maximum gradient line is steeper, and the minimum gradient line is shallower. All three lines should pass through the error bars.
- **中文:** 同一散点图上的三条直线。最佳拟合线在中间。最大梯度线更陡，最小梯度线更缓。所有三条线都应穿过误差棒。

### Gradient Meaning / 斜率含义
- **Best-fit gradient ($m_{\text{best}}$):** Most probable value of the physical constant / 物理常数的最可能值
- **Max gradient ($m_{\text{max}}$):** Upper bound of the gradient / 梯度的上限
- **Min gradient ($m_{\text{min}}$):** Lower bound of the gradient / 梯度的下限

### Area Meaning / 面积含义
- **English:** Not applicable for gradient analysis. The area under the graph is not typically used in this context.
- **中文:** 不适用于梯度分析。此上下文中通常不使用图下面积。

### Exam Interpretation / 考试解读
- **English:** If the gradient uncertainty is less than 10% of the gradient itself, the result is considered reliable. If it exceeds 20%, the data may be too scattered to draw meaningful conclusions.
- **中文:** 如果梯度不确定度小于梯度本身的10%，结果被认为是可靠的。如果超过20%，数据可能过于分散，无法得出有意义的结论。

> 📷 **IMAGE PROMPT — WFL-02: Gradient Calculation Triangles**
> Close-up of a graph showing one of the worst-fit lines with a large gradient triangle drawn. The triangle has horizontal base $\Delta x$ and vertical height $\Delta y$ clearly marked. The line extends beyond the triangle. Labels show the coordinates of the two points used.

---

# 7. Required Diagrams / 必备图表

## 7.1 Worst-Fit Lines on a Linear Graph / 线性图上的最差拟合线

### Description / 描述
**English:**
A complete graph showing experimental data points with error bars, a best-fit line (dashed), a maximum gradient line (solid, labelled "max"), and a minimum gradient line (solid, labelled "min"). All lines pass through all error bars. Gradient triangles are shown for each line.

**中文:**
一个完整的图表，显示带有误差棒的实验数据点、最佳拟合线（虚线）、最大梯度线（实线，标注"max"）和最小梯度线（实线，标注"min"）。所有线都穿过所有误差棒。每条线都显示了梯度三角形。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — WFL-03: Complete Worst-Fit Lines Diagram**
> A professional scientific graph with 8 data points plotted. Each point has vertical error bars of varying sizes. Three straight lines are drawn: a central dashed line labelled "best fit", a steep solid line labelled "max gradient", and a shallow solid line labelled "min gradient". All three lines pass through all error bars. Large right-angled triangles are drawn on each line for gradient calculation, with $\Delta x$ and $\Delta y$ labelled. The graph has clear axis labels, a title, and a legend. The background is white grid paper style.

### Labels Required / 需要标注
| Label (EN) | Label (中文) | Description |
|------------|-------------|-------------|
| Best fit | 最佳拟合 | Dashed line through the centre of data |
| Max gradient | 最大梯度 | Steepest line through all error bars |
| Min gradient | 最小梯度 | Shallowest line through all error bars |
| $\Delta x$ | $\Delta x$ | Horizontal distance for gradient triangle |
| $\Delta y$ | $\Delta y$ | Vertical distance for gradient triangle |
| Error bars | 误差棒 | Vertical lines showing uncertainty range |

### Exam Importance / 考试重要性
- **English:** This diagram is essential for Paper 3 (CAIE) and Unit 3 (Edexcel). You may be asked to draw worst-fit lines on a provided graph or to calculate gradient uncertainty from given lines. Marks are awarded for correct line placement, labelling, and calculation.
- **中文:** 此图对于CAIE Paper 3和Edexcel Unit 3至关重要。你可能被要求在提供的图上绘制最差拟合线，或根据给定的线计算梯度不确定度。正确的线位置、标注和计算都会获得分数。

---

# 8. Worked Examples / 典型例题

## Example 1: Calculating Gradient Uncertainty / 例题1：计算梯度不确定度

### Question / 题目
**English:**
A student investigates the extension of a spring under different loads. The graph shows the following data with error bars. The best-fit line has gradient $m_{\text{best}} = 2.5 \, \text{cm/N}$. The maximum gradient line gives $m_{\text{max}} = 2.8 \, \text{cm/N}$ and the minimum gradient line gives $m_{\text{min}} = 2.3 \, \text{cm/N}$. Calculate the uncertainty in the gradient and express the final result.

**中文:**
一名学生研究弹簧在不同负载下的伸长量。图表显示带有误差棒的以下数据。最佳拟合线的梯度为 $m_{\text{best}} = 2.5 \, \text{cm/N}$。最大梯度线给出 $m_{\text{max}} = 2.8 \, \text{cm/N}$，最小梯度线给出 $m_{\text{min}} = 2.3 \, \text{cm/N}$。计算梯度的不确定度并表达最终结果。

### Solution / 解答

**Step 1: Calculate the range / 步骤1：计算范围**
$$ \text{Range} = m_{\text{max}} - m_{\text{min}} = 2.8 - 2.3 = 0.5 \, \text{cm/N} $$

**Step 2: Calculate the uncertainty / 步骤2：计算不确定度**
$$ \Delta m = \frac{m_{\text{max}} - m_{\text{min}}}{2} = \frac{0.5}{2} = 0.25 \, \text{cm/N} $$

**Step 3: Express the final result / 步骤3：表达最终结果**
$$ m = m_{\text{best}} \pm \Delta m = 2.5 \pm 0.3 \, \text{cm/N} $$
(Rounded to 1 significant figure for uncertainty)

### Final Answer / 最终答案
**Answer:** $m = 2.5 \pm 0.3 \, \text{cm/N}$ | **答案：** $m = 2.5 \pm 0.3 \, \text{cm/N}$

### Quick Tip / 提示
- **English:** Always round the uncertainty to 1 significant figure, then round the gradient to match the decimal place of the uncertainty.
- **中文:** 始终将不确定度四舍五入到1位有效数字，然后将梯度四舍五入到与不确定度相同的小数位数。

---

## Example 2: Drawing Worst-Fit Lines from Data / 例题2：根据数据绘制最差拟合线

### Question / 题目
**English:**
A student measures the voltage across a resistor at different currents. The data is:

| Current / A | Voltage / V |
|-------------|-------------|
| 0.0 ± 0.1 | 0.0 ± 0.2 |
| 0.5 ± 0.1 | 1.2 ± 0.2 |
| 1.0 ± 0.1 | 2.1 ± 0.2 |
| 1.5 ± 0.1 | 3.0 ± 0.2 |
| 2.0 ± 0.1 | 4.1 ± 0.2 |

Plot the graph, draw best-fit and worst-fit lines, and determine the resistance and its uncertainty.

**中文:**
一名学生测量不同电流下电阻两端的电压。数据如下：

| 电流 / A | 电压 / V |
|----------|----------|
| 0.0 ± 0.1 | 0.0 ± 0.2 |
| 0.5 ± 0.1 | 1.2 ± 0.2 |
| 1.0 ± 0.1 | 2.1 ± 0.2 |
| 1.5 ± 0.1 | 3.0 ± 0.2 |
| 2.0 ± 0.1 | 4.1 ± 0.2 |

绘制图表，画出最佳拟合线和最差拟合线，并确定电阻及其不确定度。

### Solution / 解答

**Step 1: Plot the data with error bars / 步骤1：绘制带有误差棒的数据**
- x-axis: Current (0 to 2.5 A)
- y-axis: Voltage (0 to 5.0 V)
- Each point has horizontal error bars of ±0.1 A and vertical error bars of ±0.2 V

**Step 2: Draw best-fit line / 步骤2：绘制最佳拟合线**
- Pass through the origin (0,0) and as close as possible to all points
- Gradient: $m_{\text{best}} = \frac{4.1 - 0}{2.0 - 0} = 2.05 \, \text{V/A}$

**Step 3: Draw maximum gradient line / 步骤3：绘制最大梯度线**
- Steepest line through all error bars
- Pass through top of first error bar (0, 0.2) and bottom of last error bar (2.0, 3.9)
- Gradient: $m_{\text{max}} = \frac{3.9 - 0.2}{2.0 - 0} = 1.85 \, \text{V/A}$

**Step 4: Draw minimum gradient line / 步骤4：绘制最小梯度线**
- Shallowest line through all error bars
- Pass through bottom of first error bar (0, -0.2) and top of last error bar (2.0, 4.3)
- Gradient: $m_{\text{min}} = \frac{4.3 - (-0.2)}{2.0 - 0} = 2.25 \, \text{V/A}$

**Step 5: Calculate uncertainty / 步骤5：计算不确定度**
$$ \Delta m = \frac{2.25 - 1.85}{2} = 0.20 \, \text{V/A} $$

**Step 6: Express result / 步骤6：表达结果**
$$ R = 2.05 \pm 0.20 \, \Omega $$

### Final Answer / 最终答案
**Answer:** $R = 2.05 \pm 0.20 \, \Omega$ | **答案：** $R = 2.05 \pm 0.20 \, \Omega$

### Quick Tip / 提示
- **English:** When the line must pass through the origin (as in Ohm's law), ensure all worst-fit lines also pass through the origin. This constrains the lines and reduces uncertainty.
- **中文:** 当线必须通过原点时（如欧姆定律），确保所有最差拟合线也通过原点。这会约束线并减少不确定度。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate gradient uncertainty from given worst-fit lines | Very High | Medium | 📝 *待填入* |
| Draw worst-fit lines on a provided graph | High | Hard | 📝 *待填入* |
| Determine if a relationship is valid using gradient uncertainty | Medium | Medium | 📝 *待填入* |
| Explain why worst-fit lines are used | Low | Easy | 📝 *待填入* |
| Compare gradient uncertainty with percentage uncertainty | Low | Hard | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** "Draw", "Calculate", "Determine", "State", "Explain", "Show that", "Estimate"
- **中文:** "画出"、"计算"、"确定"、"说明"、"解释"、"证明"、"估算"

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic directly connects to practical examination skills:

1. **Graph Plotting (Paper 3/5 CAIE, Unit 3/6 Edexcel):** You must be able to plot data points accurately, draw error bars, and then draw best-fit and worst-fit lines. Marks are awarded for line placement and labelling.

2. **Uncertainty Analysis:** The gradient uncertainty feeds into [[Propagating Uncertainties Through Calculations|propagation of uncertainties]] when the gradient is used in further calculations. For example, if gradient = resistance, then $\Delta R = \Delta m$.

3. **Evaluation of Results:** A large gradient uncertainty ( > 20% of the gradient) suggests the data is unreliable. You may need to suggest improvements such as taking more readings, using more precise equipment, or reducing systematic errors.

4. **Data Recording:** The quality of worst-fit lines depends on the quality of error bars. Error bars come from [[Calculating Uncertainty from Repeated Readings|repeated readings]] or instrument precision.

**中文:**
本子知识点直接与实验考试技能相关：

1. **图表绘制（CAIE Paper 3/5，Edexcel Unit 3/6）：** 你必须能够准确绘制数据点、画出误差棒，然后绘制最佳拟合线和最差拟合线。线的位置和标注都会获得分数。

2. **不确定度分析：** 当梯度用于进一步计算时，梯度不确定度会输入到[[Propagating Uncertainties Through Calculations|不确定度传播]]中。例如，如果梯度=电阻，则 $\Delta R = \Delta m$。

3. **结果评估：** 大的梯度不确定度（> 梯度的20%）表明数据不可靠。你可能需要提出改进建议，如获取更多读数、使用更精密的仪器或减少系统误差。

4. **数据记录：** 最差拟合线的质量取决于误差棒的质量。误差棒来自[[Calculating Uncertainty from Repeated Readings|重复读数]]或仪器精度。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Core concept
    WFL[Using Worst-Fit Lines for Uncertainty in Gradient]
    
    %% Prerequisites
    UE[Uncertainties and Errors] --> WFL
    DRA[Data Recording and Analysis] --> WFL
    EB[Error Bars on Graphs] --> WFL
    
    %% Key components
    WFL --> BF[Best-Fit Line]
    WFL --> MAX[Maximum Gradient Line]
    WFL --> MIN[Minimum Gradient Line]
    
    %% Calculations
    MAX --> GC[Gradient Calculation]
    MIN --> GC
    GC --> GU[Gradient Uncertainty: Δm = (mmax - mmin)/2]
    
    %% Applications
    GU --> FR[Final Result: m ± Δm]
    GU --> EV[Evaluation of Reliability]
    GU --> PC[Propagating Uncertainties Through Calculations]
    
    %% Related topics
    EV --> EI[Evaluation and Improvements]
    PC --> PU[Percentage Difference and Percentage Uncertainty]
    
    %% Practical skills
    WFL --> GP[Graph Plotting Skills]
    WFL --> UA[Uncertainty Analysis in Practical Work]
    
    %% Styling
    classDef core fill:#f9f,stroke:#333,stroke-width:2px
    classDef calc fill:#bbf,stroke:#333,stroke-width:1px
    classDef related fill:#dfd,stroke:#333,stroke-width:1px
    
    class WFL core
    class BF,MAX,MIN,GC,GU,FR calc
    class UE,DRA,EB,EV,PC,PU,EI,GP,UA related
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Worst-fit lines are the steepest (max) and shallowest (min) straight lines that still pass through ALL error bars / 最差拟合线是仍然穿过所有误差棒的最陡（最大）和最缓（最小）直线 |
| **Key Formula / 核心公式** | $\Delta m = \frac{m_{\text{max}} - m_{\text{min}}}{2}$ — Uncertainty is half the range / 不确定度是范围的一半 |
| **Key Graph / 核心图表** | Three lines on one graph: best-fit (dashed), max gradient (solid), min gradient (solid). All pass through error bars / 同一图上的三条线：最佳拟合（虚线）、最大梯度（实线）、最小梯度（实线）。全部穿过误差棒 |
| **Exam Tip / 考试提示** | Use a transparent ruler. Draw large gradient triangles (at least half the line length). Label all lines clearly. Round uncertainty to 1 s.f. / 使用透明直尺。画大梯度三角形（至少线长的一半）。清晰标注所有线。将不确定度四舍五入到1位有效数字 |
| **Common Mistake / 常见错误** | Drawing worst-fit lines that miss error bars; forgetting to divide by 2; not labelling lines / 绘制错过误差棒的最差拟合线；忘记除以2；未标注线 |
| **When to Use / 何时使用** | When data has error bars and relationship is linear / 当数据有误差棒且关系为线性时 |
| **Reliability Check / 可靠性检查** | If $\Delta m / m_{\text{best}} < 10\%$: reliable; $> 20\%$: unreliable / 如果 $\Delta m / m_{\text{best}} < 10\%$：可靠；$> 20\%$：不可靠 |
| **Edexcel Specific / Edexcel 特定** | May ask to use worst-fit lines to test if a relationship is valid (e.g., does gradient = expected value within uncertainty?) / 可能要求使用最差拟合线测试关系是否有效（例如，梯度是否在不确定度范围内等于预期值？） |
| **CAIE Specific / CAIE 特定** | Paper 3 often provides a pre-drawn graph; you draw worst-fit lines and calculate uncertainty. Paper 5 may ask you to evaluate the method / Paper 3通常提供预绘制的图表；你绘制最差拟合线并计算不确定度。Paper 5可能要求你评估方法 |