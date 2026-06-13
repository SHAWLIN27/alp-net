# 1. Overview / 概述

**English:**
This sub-topic focuses on how to determine the uncertainty when a measurement is repeated multiple times. When you measure the same quantity several times, you typically get slightly different readings due to [[Random Errors]]. The best estimate of the true value is the **mean** (average), and the uncertainty is quantified using the **range** (half the range) or the **standard deviation** (at A-Level, primarily the range method). This process is fundamental to all experimental physics, as it provides a quantitative measure of the reliability and precision of your measurements. It directly connects to [[Absolute, Fractional and Percentage Uncertainty]] and is a prerequisite for [[Combining Uncertainties (Addition, Multiplication, Powers)]].

**中文:**
本子知识点专注于如何确定当测量重复多次时的不确定度。当你多次测量同一物理量时，由于[[Random Errors]]，通常会得到略有不同的读数。真实值的最佳估计是**平均值**，不确定度则通过**极差**（半极差）或**标准差**（在A-Level中，主要使用极差法）来量化。这一过程是所有实验物理的基础，因为它为测量的可靠性和精密度提供了定量度量。它直接联系到[[Absolute, Fractional and Percentage Uncertainty]]，并且是学习[[Combining Uncertainties (Addition, Multiplication, Powers)]]的先决条件。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 1.4(a) Explain what is meant by uncertainty in a measurement. | 1.7 Understand the difference between systematic errors and random errors. |
| 1.4(b) Determine uncertainties from repeated measurements. | 1.8 Know that the measurement of a physical quantity can be expressed as a best estimate with a range of uncertainty. |
| 1.4(c) Identify random and systematic errors. | 1.9 Determine the uncertainty of a value from a set of repeated measurements. |
| 1.4(d) Determine the uncertainty in a derived quantity (combining uncertainties). | 1.10 Determine the uncertainty of a derived quantity. |

**Examiner Expectations / 考官期望:**
- **English:** You must be able to calculate the mean of a set of repeated readings, calculate the range, and express the final result as `mean ± half-range`. You must also understand that increasing the number of readings reduces the effect of random errors but does not eliminate systematic errors.
- **中文:** 你必须能够计算一组重复读数的平均值，计算极差，并将最终结果表示为 `平均值 ± 半极差`。你还必须理解，增加读数次数可以减少随机误差的影响，但不能消除系统误差。

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Mean (Average)** / 平均值 | The sum of all measured values divided by the number of measurements. It is the best estimate of the true value. | 所有测量值的总和除以测量次数。它是真实值的最佳估计。 | Forgetting to include all readings, especially outliers. / 忘记包含所有读数，尤其是异常值。 |
| **Range** / 极差 | The difference between the largest and smallest measured values in a set of repeated readings. | 一组重复读数中最大值与最小值之间的差值。 | Confusing range with uncertainty. The range is the spread; the uncertainty is half the range. / 将极差与不确定度混淆。极差是散布范围；不确定度是半极差。 |
| **Half-Range (Uncertainty)** / 半极差（不确定度） | The uncertainty in the mean value, calculated as `(largest value - smallest value) / 2`. It represents the precision of the measurement. | 平均值的标准不确定度，计算公式为 `(最大值 - 最小值) / 2`。它代表测量的精密度。 | Using the full range as the uncertainty instead of half the range. / 使用整个极差作为不确定度，而不是半极差。 |
| **Outlier** / 异常值 | A reading that lies far outside the general pattern of the data, often due to a blunder or a sudden, large random error. | 一个远超出数据总体模式的读数，通常是由于操作失误或突然的、大的随机误差造成的。 | Including outliers in the calculation of the mean and range without justification. / 在没有合理解释的情况下，将异常值包含在平均值和极差的计算中。 |
| **Precision** / 精密度 | The degree of agreement between repeated measurements of the same quantity. High precision means a small range. | 同一物理量重复测量结果之间的一致程度。高精密度意味着小极差。 | Confusing precision with [[Accuracy vs Precision\|accuracy]]. Precision is about consistency, not correctness. / 将精密度与[[Accuracy vs Precision\|准确度]]混淆。精密度关乎一致性，而非正确性。 |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 The Mean as the Best Estimate / 平均值作为最佳估计

### Explanation / 解释
**English:** When you repeat a measurement, random errors cause the readings to scatter around the true value. By calculating the **mean** (average), you are effectively summing all the positive and negative random errors, which tend to cancel each other out. Therefore, the mean is the most reliable single value to represent the measurement. The formula is:
$$ \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} $$
where $\bar{x}$ is the mean, $x_i$ are the individual readings, and $n$ is the number of readings. This concept is a prerequisite for understanding [[Absolute, Fractional and Percentage Uncertainty]].

**中文:** 当你重复测量时，随机误差会导致读数在真实值周围散布。通过计算**平均值**，你实际上是在求和所有正的和负的随机误差，它们往往会相互抵消。因此，平均值是代表该测量结果最可靠的单一数值。公式为：
$$ \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} $$
其中 $\bar{x}$ 是平均值，$x_i$ 是单个读数，$n$ 是读数次数。这个概念是理解[[Absolute, Fractional and Percentage Uncertainty]]的先决条件。

### Physical Meaning / 物理意义
**English:** The mean is the point around which the random errors are balanced. It is the most probable value of the true measurement.
**中文:** 平均值是随机误差围绕其平衡的点。它是真实测量值的最可能值。

### Common Misconceptions / 常见误区
- **English:** Thinking the mean is the exact true value. It is only an estimate. The uncertainty tells us how good that estimate is.
- **中文:** 认为平均值就是精确的真实值。它只是一个估计值。不确定度告诉我们这个估计值有多好。
- **English:** Rounding the mean incorrectly. The mean should be rounded to the same number of decimal places as the raw data, or one more.
- **中文:** 错误地四舍五入平均值。平均值应四舍五入到与原始数据相同的小数位数，或多一位。

### Exam Tips / 考试提示
- **English:** Always show your working for the mean calculation, even if it seems simple.
- **中文:** 即使看起来很简单，也一定要写出平均值计算的过程。
- **English:** Use the `$ \bar{x} $` notation in your working.
- **中文:** 在计算过程中使用 `$ \bar{x} $` 符号。

## 4.2 Uncertainty from the Range / 从极差确定不确定度

### Explanation / 解释
**English:** The **range** ($R$) is the simplest measure of the spread of your data. The uncertainty in the mean is taken as **half the range** ($\Delta x$). This is the standard A-Level method.
$$ \Delta x = \frac{R}{2} = \frac{x_{max} - x_{min}}{2} $$
The final result is then expressed as:
$$ \text{Value} = \bar{x} \pm \Delta x $$
This method is valid when there are no obvious outliers and the number of readings is small (typically 3-10). This is the foundation for [[Combining Uncertainties (Addition, Multiplication, Powers)]].

**中文:** **极差** ($R$) 是衡量数据散布范围的最简单方法。平均值的不确定度取为**半极差** ($\Delta x$)。这是标准的A-Level方法。
$$ \Delta x = \frac{R}{2} = \frac{x_{max} - x_{min}}{2} $$
最终结果表示为：
$$ \text{Value} = \bar{x} \pm \Delta x $$
当没有明显的异常值且读数次数较少（通常为3-10次）时，此方法有效。这是[[Combining Uncertainties (Addition, Multiplication, Powers)]]的基础。

### Physical Meaning / 物理意义
**English:** Half the range represents the average deviation of the individual readings from the mean. It gives a measure of the precision of the measurement set.
**中文:** 半极差代表单个读数与平均值的平均偏差。它给出了测量组精密度的度量。

### Common Misconceptions / 常见误区
- **English:** Using the full range ($R$) as the uncertainty. The uncertainty is always half the range.
- **中文:** 使用整个极差 ($R$) 作为不确定度。不确定度始终是半极差。
- **English:** Forgetting to include the units in the final expression.
- **中文:** 忘记在最终表达式中包含单位。

### Exam Tips / 考试提示
- **English:** If you have only two readings, the uncertainty is simply half the difference between them.
- **中文:** 如果你只有两个读数，不确定度就是它们差值的一半。
- **English:** If all readings are identical, the uncertainty is zero? **No!** The uncertainty is then determined by the resolution of the instrument (e.g., half the smallest division). This is because the instrument's precision limits the measurement.
- **中文:** 如果所有读数都相同，不确定度为零？**不！** 此时不确定度由仪器的分辨率决定（例如，最小刻度的一半）。这是因为仪器的精密度限制了测量。

> 📷 **IMAGE PROMPT — DIAGRAM-01: Visualizing Mean and Range**
> A simple dot plot showing 5 data points (e.g., 22.1, 22.3, 22.0, 22.4, 22.2) on a number line. A vertical line marks the mean (22.2). A double-headed arrow spans from the minimum (22.0) to the maximum (22.4), labeled "Range (R)". Another arrow spans from the mean to the maximum, labeled "Half-Range (Δx)". The final result is written as "22.2 ± 0.2 cm".

---

# 5. Essential Equations / 核心公式

## Equation 1: Mean / 平均值

$$ \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\bar{x}$ | Mean value | 平均值 | Same as $x_i$ |
| $x_i$ | Individual reading | 单个读数 | Same as $\bar{x}$ |
| $n$ | Number of readings | 读数次数 | Dimensionless (无量纲) |

**Derivation / 推导:** N/A (Definition)
**Conditions / 适用条件:** N/A
**Limitations / 局限性:** N/A

## Equation 2: Uncertainty from Range / 从极差确定不确定度

$$ \Delta x = \frac{x_{max} - x_{min}}{2} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\Delta x$ | Absolute uncertainty in the mean | 平均值的绝对不确定度 | Same as $x_i$ |
| $x_{max}$ | Largest reading | 最大读数 | Same as $x_i$ |
| $x_{min}$ | Smallest reading | 最小读数 | Same as $x_i$ |

**Derivation / 推导:** N/A (Definition)
**Conditions / 适用条件:** 
- **English:** Valid for a small number of repeated readings (typically 3-10) with no obvious outliers.
- **中文:** 适用于少量重复读数（通常为3-10次）且没有明显异常值的情况。
**Limitations / 局限性:**
- **English:** Not robust to outliers. A single outlier can significantly inflate the range and thus the uncertainty.
- **中文:** 对异常值不稳健。一个异常值会显著增大极差，从而增大不确定度。

## Equation 3: Final Result Expression / 最终结果表达

$$ \text{Value} = \bar{x} \pm \Delta x $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\bar{x}$ | Mean value | 平均值 | Same as $x_i$ |
| $\Delta x$ | Absolute uncertainty | 绝对不确定度 | Same as $x_i$ |

**Conditions / 适用条件:** 
- **English:** The uncertainty should be quoted to 1 significant figure (or 2 if the first digit is 1). The mean should be rounded to the same number of decimal places as the uncertainty.
- **中文:** 不确定度应保留1位有效数字（如果第一位是1，则保留2位）。平均值应四舍五入到与不确定度相同的小数位数。

> 📋 **CIE Only:** CIE often expects the uncertainty to be quoted to 1 significant figure. For example, `22.2 ± 0.2 cm` is correct, but `22.2 ± 0.20 cm` is not.
> 📋 **Edexcel Only:** Edexcel is slightly more flexible but still prefers 1 significant figure for the uncertainty.

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Dot Plot of Repeated Readings / 重复读数的点图

### Axes / 坐标轴 (EN+CN)
- **X-axis:** Reading Number (or just a label for the measurement) / 读数序号（或测量的标签）
- **Y-axis:** Measured Value (with units) / 测量值（带单位）

### Shape / 形状 (EN+CN)
- **English:** A scatter of points around a central value (the mean). The spread of the points indicates the precision.
- **中文:** 点围绕一个中心值（平均值）散布。点的散布范围表示精密度。

### Gradient Meaning / 斜率含义 (EN+CN)
- **English:** N/A. This is not a line graph.
- **中文:** 不适用。这不是线图。

### Area Meaning / 面积含义 (EN+CN)
- **English:** N/A.
- **中文:** 不适用。

### Exam Interpretation / 考试解读 (EN+CN)
- **English:** You may be asked to draw a dot plot or to interpret one. A wider spread means a larger uncertainty (lower precision). A narrow spread means a smaller uncertainty (higher precision).
- **中文:** 你可能会被要求绘制或解读点图。散布范围越宽，不确定度越大（精密度越低）。散布范围越窄，不确定度越小（精密度越高）。

> 📷 **IMAGE PROMPT — DIAGRAM-02: Dot Plot Comparison**
> Two dot plots side-by-side. Plot A shows points tightly clustered (e.g., 22.1, 22.2, 22.1, 22.3, 22.2) with a small range. Plot B shows points widely scattered (e.g., 21.5, 22.0, 22.8, 21.9, 22.5) with a large range. Label Plot A as "High Precision" and Plot B as "Low Precision".

---

# 7. Required Diagrams / 必备图表

## 7.1 Diagram: Mean and Range on a Number Line / 图表：数轴上的平均值和极差

### Description / 描述 (EN+CN)
- **English:** A number line showing the spread of repeated readings. The mean is marked, and the range and half-range are indicated with arrows.
- **中文:** 显示重复读数散布范围的数轴。标记出平均值，并用箭头指示极差和半极差。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM-03: Mean and Range on a Number Line**
> A clean, educational diagram. A horizontal number line from 22.0 to 22.5. Five data points are plotted as dots above the line at 22.1, 22.2, 22.0, 22.4, and 22.2. A vertical dashed line drops from the mean (22.2) to the number line. A horizontal double-headed arrow spans from 22.0 to 22.4, labeled "Range (R) = 0.4". Another horizontal arrow spans from 22.2 to 22.4, labeled "Half-Range (Δx) = 0.2". The final result is written below: "Value = 22.2 ± 0.2 cm".

### Labels Required / 需要标注 (EN+CN)
- Mean ($\bar{x}$) / 平均值 ($\bar{x}$)
- Maximum ($x_{max}$) / 最大值 ($x_{max}$)
- Minimum ($x_{min}$) / 最小值 ($x_{min}$)
- Range ($R$) / 极差 ($R$)
- Half-Range ($\Delta x$) / 半极差 ($\Delta x$)
- Final Result / 最终结果

### Exam Importance / 考试重要性 (EN+CN)
- **English:** High. You may be asked to sketch this diagram to explain how you determined the uncertainty from repeated readings.
- **中文:** 高。你可能会被要求画出此图来解释你是如何从重复读数中确定不确定度的。

---

# 8. Worked Examples / 典型例题

## Example 1: Basic Calculation / 例题1：基础计算

### Question / 题目
**English:** A student measures the diameter of a metal sphere five times using a micrometer. The readings are: 12.45 mm, 12.52 mm, 12.48 mm, 12.50 mm, 12.46 mm. Determine the mean diameter and the uncertainty. Express the final result correctly.

**中文:** 一名学生用千分尺测量一个金属球的直径五次。读数分别为：12.45 mm, 12.52 mm, 12.48 mm, 12.50 mm, 12.46 mm。确定平均直径和不确定度。正确表达最终结果。

### Solution / 解答
**Step 1: Calculate the Mean**
$$ \bar{x} = \frac{12.45 + 12.52 + 12.48 + 12.50 + 12.46}{5} = \frac{62.41}{5} = 12.482 \text{ mm} $$

**Step 2: Find the Range**
$$ x_{max} = 12.52 \text{ mm} $$
$$ x_{min} = 12.45 \text{ mm} $$
$$ R = 12.52 - 12.45 = 0.07 \text{ mm} $$

**Step 3: Calculate the Uncertainty (Half-Range)**
$$ \Delta x = \frac{R}{2} = \frac{0.07}{2} = 0.035 \text{ mm} $$

**Step 4: Round the Uncertainty**
- **English:** The uncertainty should be quoted to 1 significant figure. 0.035 mm rounds to 0.04 mm.
- **中文:** 不确定度应保留1位有效数字。0.035 mm 四舍五入为 0.04 mm。

**Step 5: Round the Mean**
- **English:** The mean must be rounded to the same number of decimal places as the uncertainty. The uncertainty (0.04 mm) has 2 decimal places. So, the mean (12.482 mm) rounds to 12.48 mm.
- **中文:** 平均值必须四舍五入到与不确定度相同的小数位数。不确定度 (0.04 mm) 有2位小数。因此，平均值 (12.482 mm) 四舍五入为 12.48 mm。

### Final Answer / 最终答案
**Answer:** $12.48 \pm 0.04$ mm | **答案：** $12.48 \pm 0.04$ mm

### Quick Tip / 提示
(EN+CN)
- **English:** Always round the uncertainty first, then round the mean to match.
- **中文:** 总是先四舍五入不确定度，然后将平均值四舍五入到与之匹配。

---

## Example 2: Handling Outliers / 例题2：处理异常值

### Question / 题目
**English:** A student measures the time for 10 oscillations of a pendulum. The readings are: 15.2 s, 15.1 s, 15.3 s, 14.8 s, 15.2 s, 15.0 s, 15.1 s, 15.4 s, 15.2 s, 18.5 s. Determine the mean time and the uncertainty. Explain your reasoning.

**中文:** 一名学生测量单摆10次全振动的时间。读数分别为：15.2 s, 15.1 s, 15.3 s, 14.8 s, 15.2 s, 15.0 s, 15.1 s, 15.4 s, 15.2 s, 18.5 s。确定平均时间和不确定度。解释你的推理。

### Solution / 解答
**Step 1: Identify the Outlier**
- **English:** The reading of 18.5 s is clearly an outlier. It is far from the other readings (which are all between 14.8 s and 15.4 s). This is likely due to a timing error (a blunder). It should be discarded.
- **中文:** 18.5 s 的读数明显是异常值。它远大于其他读数（都在14.8 s 和 15.4 s 之间）。这很可能是计时错误（操作失误）。应将其剔除。

**Step 2: Calculate the Mean (excluding the outlier)**
$$ \bar{x} = \frac{15.2 + 15.1 + 15.3 + 14.8 + 15.2 + 15.0 + 15.1 + 15.4 + 15.2}{9} = \frac{136.3}{9} = 15.144... \text{ s} $$

**Step 3: Find the Range (excluding the outlier)**
$$ x_{max} = 15.4 \text{ s} $$
$$ x_{min} = 14.8 \text{ s} $$
$$ R = 15.4 - 14.8 = 0.6 \text{ s} $$

**Step 4: Calculate the Uncertainty**
$$ \Delta x = \frac{0.6}{2} = 0.3 \text{ s} $$

**Step 5: Round**
- **English:** Uncertainty is 0.3 s (1 s.f.). Mean rounds to 15.1 s.
- **中文:** 不确定度为 0.3 s (1位有效数字)。平均值四舍五入为 15.1 s。

### Final Answer / 最终答案
**Answer:** $15.1 \pm 0.3$ s | **答案：** $15.1 \pm 0.3$ s

**Reasoning / 推理:**
- **English:** The reading of 18.5 s was identified as an outlier and discarded because it was inconsistent with the rest of the data. The mean and range were calculated from the remaining 9 readings.
- **中文:** 18.5 s 的读数被识别为异常值并被剔除，因为它与其余数据不一致。平均值和极差是根据剩余的9个读数计算的。

### Quick Tip / 提示
(EN+CN)
- **English:** You must always justify discarding an outlier in your answer. Never just ignore it without comment.
- **中文:** 你必须在答案中证明剔除异常值的合理性。切勿不加说明就直接忽略它。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate mean and uncertainty from raw data / 从原始数据计算平均值和不确定度 | Very High / 非常高 | Easy / 简单 | 📝 *待填入* |
| Identify and handle an outlier / 识别并处理异常值 | Medium / 中等 | Medium / 中等 | 📝 *待填入* |
| Explain the effect of increasing the number of readings / 解释增加读数次数的影响 | Medium / 中等 | Medium / 中等 | 📝 *待填入* |
| Interpret a dot plot or table of results / 解读点图或结果表格 | Low / 低 | Medium / 中等 | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **English:** "Calculate", "Determine", "State", "Explain", "Suggest", "Justify"
- **中文:** "计算", "确定", "写出", "解释", "提出", "证明...合理"

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic is directly assessed in the practical papers (Paper 3 for CAIE, Unit 6 for Edexcel). You will be expected to:
1. **Take repeated readings** of a physical quantity (e.g., time for oscillations, length, current).
2. **Record data in a table** with appropriate headings and units.
3. **Calculate the mean** of the repeated readings.
4. **Calculate the uncertainty** using the half-range method.
5. **Express the final result** correctly as `mean ± uncertainty`.
6. **Identify and discard outliers** with justification.
7. **Plot a graph** of your results, including error bars (which are derived from this uncertainty). This connects to [[Graph Plotting Skills]].

**中文:**
本子知识点在实验考试（CAIE的Paper 3，Edexcel的Unit 6）中直接考查。你将被期望能够：
1. **进行重复读数**（例如，振动时间、长度、电流）。
2. **在表格中记录数据**，并带有适当的表头和单位。
3. **计算重复读数的平均值**。
4. **使用半极差法计算不确定度**。
5. **正确表达最终结果**为 `平均值 ± 不确定度`。
6. **识别并剔除异常值**，并给出理由。
7. **绘制结果图表**，包括误差棒（由该不确定度得出）。这联系到[[Graph Plotting Skills]]。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Show connections for this leaf node
    A[Uncertainty from Repeated Measurements] --> B[Mean (Best Estimate)]
    A --> C[Range]
    A --> D[Outlier Identification]
    
    B --> E[Formula: Σxᵢ / n]
    C --> F[Formula: x_max - x_min]
    C --> G[Half-Range: Δx = R/2]
    G --> H[Final Result: x̄ ± Δx]
    
    D --> I[Justify Discarding]
    D --> J[Recalculate without Outlier]
    
    A --> K[Connects to: Absolute Uncertainty]
    A --> L[Connects to: Combining Uncertainties]
    A --> M[Connects to: Graph Plotting (Error Bars)]
    
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style H fill:#bbf,stroke:#333,stroke-width:2px
    style I fill:#fbb,stroke:#333,stroke-width:2px
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Uncertainty from repeated measurements quantifies the spread of data due to [[Random Errors]]. / 重复测量的不确定度量化了由[[Random Errors]]引起的数据散布。 |
| **Key Formula / 核心公式** | Mean: $\bar{x} = \frac{\sum x_i}{n}$; Uncertainty: $\Delta x = \frac{x_{max} - x_{min}}{2}$; Result: $\bar{x} \pm \Delta x$ |
| **Key Graph / 核心图表** | Dot plot showing scatter of readings around the mean. / 显示读数围绕平均值散布的点图。 |
| **Exam Tip / 考试提示** | 1. Round uncertainty to 1 s.f. first. 2. Round mean to match. 3. Always justify discarding outliers. 4. Include units in final answer. / 1. 先四舍五入不确定度到1位有效数字。2. 将平均值四舍五入到匹配。3. 始终证明剔除异常值的合理性。4. 在最终答案中包含单位。 |