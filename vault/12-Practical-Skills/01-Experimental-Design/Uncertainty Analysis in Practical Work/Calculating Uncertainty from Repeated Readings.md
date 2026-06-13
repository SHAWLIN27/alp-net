# 1. Overview / 概述

**English:**
This sub-topic focuses on how to calculate the uncertainty in a measurement when you have taken multiple readings of the same quantity. In practical work, repeating measurements is a fundamental technique to reduce the impact of random errors and to estimate the reliability of your data. The key idea is that the spread of your repeated readings gives you a measure of the uncertainty. This sub-topic covers two main methods: using the range (half the range) and using the standard deviation (often simplified to the mean deviation for A-Level). You will learn how to calculate the mean, the uncertainty, and how to express the final result correctly with its absolute uncertainty. This is a core skill for [[Uncertainty Analysis in Practical Work]] and is essential for [[Propagating Uncertainties Through Calculations]] and for drawing [[Error Bars on Graphs]].

**中文:**
本子知识点专注于当您对同一物理量进行了多次读数时，如何计算测量中的不确定度。在实验工作中，重复测量是减少随机误差影响并评估数据可靠性的基本技术。其核心思想是，重复读数的离散程度为您提供了不确定度的度量。本子知识点涵盖两种主要方法：使用极差（半极差）和使用标准偏差（在A-Level中通常简化为平均偏差）。您将学习如何计算平均值、不确定度，以及如何正确地将最终结果连同其绝对不确定度一起表达。这是[[Uncertainty Analysis in Practical Work]]的核心技能，对于[[Propagating Uncertainties Through Calculations]]和绘制[[Error Bars on Graphs]]至关重要。

---

# 2. Syllabus Learning Objectives / 考纲学习目标

| CAIE 9702 | Edexcel IAL |
|-----------|-------------|
| 1. Understand that repeating measurements reduces the effect of random errors and allows an estimate of uncertainty to be made. | 1. Know how to calculate the mean of a set of repeated readings. |
| 2. Calculate the mean of a set of repeated readings. | 2. Know how to calculate the uncertainty in a measurement from the range of repeated readings. |
| 3. Calculate the uncertainty in a measurement from the range of repeated readings (using half the range). | 3. Understand that the uncertainty can be expressed as an absolute uncertainty (e.g., ±0.1 cm) or as a percentage uncertainty. |
| 4. Express the final result as (mean ± uncertainty) with correct units and significant figures. | 4. Be able to use the formula: uncertainty = (max value - min value) / 2. |
| 5. Understand the difference between absolute and percentage uncertainty in this context. | 5. Be able to combine uncertainties from repeated readings with other uncertainties in calculations. |

**Examiner Expectations / 考官期望:**
- **CAIE:** You must be able to calculate the mean and the uncertainty from the range. The uncertainty is always quoted to 1 significant figure, and the mean is quoted to the same number of decimal places as the uncertainty. You must show your working clearly.
- **Edexcel:** You must be able to calculate the mean and the uncertainty from the range. You should also be able to express the uncertainty as a percentage. The formula for uncertainty from repeated readings is explicitly given in the formula booklet.

---

# 3. Core Definitions / 核心定义

| Term (EN/CN) | Definition (EN) | Definition (CN) | Common Mistakes / 常见错误 |
|--------------|-----------------|-----------------|---------------------------|
| **Mean** / 平均值 | The sum of all repeated readings divided by the number of readings. | 所有重复读数的总和除以读数次数。 | Forgetting to divide by the correct number of readings. |
| **Range** / 极差 | The difference between the largest and smallest value in a set of repeated readings. | 一组重复读数中最大值与最小值之差。 | Using the range as the uncertainty directly, instead of half the range. |
| **Uncertainty (from repeated readings)** / 不确定度（来自重复读数） | An estimate of the likely error in a measurement, calculated as half the range of repeated readings. | 对测量中可能误差的估计，计算为重复读数极差的一半。 | Quoting the uncertainty to too many significant figures. |
| **Absolute Uncertainty** / 绝对不确定度 | The uncertainty expressed in the same units as the measurement (e.g., ±0.2 cm). | 以与测量值相同单位表示的不确定度（例如，±0.2 cm）。 | Confusing absolute uncertainty with percentage uncertainty. |
| **Percentage Uncertainty** / 百分比不确定度 | The absolute uncertainty divided by the mean, multiplied by 100%. | 绝对不确定度除以平均值，再乘以100%。 | Forgetting to multiply by 100%. |

---

# 4. Key Concepts Explained / 关键概念详解

## 4.1 Why Repeat Readings? / 为什么要重复读数？

### Explanation / 解释
**English:** When you take a single measurement, you have no way of knowing how reliable it is. Random errors (e.g., reaction time, parallax error, slight variations in the object being measured) can cause the reading to be too high or too low. By taking multiple readings (typically 3-6), you can calculate a mean, which is a better estimate of the true value. The spread of the readings (the range) gives you a measure of the random error, which is the uncertainty. This is a fundamental concept in [[Uncertainties and Errors]].

**中文:** 当您只进行一次测量时，您无法知道其可靠性。随机误差（例如，反应时间、视差误差、被测物体的微小变化）可能导致读数偏高或偏低。通过进行多次读数（通常3-6次），您可以计算出一个平均值，这是对真实值的更好估计。读数的离散程度（极差）为您提供了随机误差的度量，即不确定度。这是[[Uncertainties and Errors]]中的一个基本概念。

### Physical Meaning / 物理意义
**English:** The uncertainty from repeated readings represents the precision of your measurement technique. A small range means your readings are very consistent, indicating high precision. A large range means your readings are scattered, indicating low precision. It does NOT tell you about accuracy (how close you are to the true value), which is affected by systematic errors.

**中文:** 来自重复读数的不确定度代表了您测量技术的精密度。极差小意味着您的读数非常一致，表明精密度高。极差大意味着您的读数分散，表明精密度低。它并不能告诉您准确度（与真实值的接近程度），准确度受系统误差影响。

### Common Misconceptions / 常见误区
- **Misconception:** The uncertainty is the difference between the mean and the true value.
  - **Correction:** The uncertainty is an estimate of the likely error, not the actual error. You don't know the true value.
- **Misconception:** More readings always give a smaller uncertainty.
  - **Correction:** More readings give a more reliable mean, but the uncertainty (half the range) depends on the spread of the readings, which may not decrease with more readings.
- **Misconception:** The uncertainty should be quoted to the same number of decimal places as the raw readings.
  - **Correction:** The uncertainty is always quoted to 1 significant figure. The mean is then quoted to the same number of decimal places as the uncertainty.

### Exam Tips / 考试提示
- **CAIE:** Always show the calculation of the mean and the uncertainty clearly. Use the formula: $\text{uncertainty} = \frac{\text{range}}{2}$.
- **Edexcel:** You may be asked to calculate the percentage uncertainty. Remember: $\text{percentage uncertainty} = \frac{\text{absolute uncertainty}}{\text{mean}} \times 100\%$.
- **General:** If you have an anomalous result (a reading that is clearly different from the others), you should discard it before calculating the mean and range. State this in your answer.

> 📷 **IMAGE PROMPT — DIAGRAM-01: Spread of Repeated Readings**
> A diagram showing a number line with several data points plotted. The mean is marked with a vertical line. The range is shown as a double-headed arrow from the minimum to the maximum value. Half the range is shown as a smaller arrow from the mean to the maximum value, labeled "Uncertainty". The final result is written as "Mean ± Uncertainty".

---

# 5. Essential Equations / 核心公式

## Equation 1: Mean / 平均值

$$ \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\bar{x}$ | Mean value | 平均值 | Same as the measured quantity |
| $x_i$ | Individual reading | 单个读数 | Same as the measured quantity |
| $n$ | Number of readings | 读数次数 | Dimensionless |

**Derivation / 推导:** This is the standard definition of the arithmetic mean.

## Equation 2: Uncertainty from Range / 来自极差的不确定度

$$ \Delta x = \frac{x_{\text{max}} - x_{\text{min}}}{2} $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\Delta x$ | Absolute uncertainty | 绝对不确定度 | Same as the measured quantity |
| $x_{\text{max}}$ | Maximum reading | 最大读数 | Same as the measured quantity |
| $x_{\text{min}}$ | Minimum reading | 最小读数 | Same as the measured quantity |

**Conditions / 适用条件:**
- **English:** This formula is used when you have at least 3 repeated readings. It assumes that the readings are normally distributed around the true value.
- **中文:** 当您至少有3次重复读数时使用此公式。它假设读数围绕真实值呈正态分布。

**Limitations / 局限性:**
- **English:** This method is sensitive to outliers. A single anomalous reading can significantly increase the range and therefore the calculated uncertainty. It is a simple estimate and is less robust than the standard deviation for large datasets.
- **中文:** 此方法对异常值敏感。单个异常读数会显著增加极差，从而增加计算出的不确定度。这是一种简单的估计，对于大数据集，其稳健性不如标准偏差。

## Equation 3: Percentage Uncertainty / 百分比不确定度

$$ \text{Percentage Uncertainty} = \frac{\Delta x}{\bar{x}} \times 100\% $$

| Symbol (符号) | Meaning (EN) | Meaning (CN) | Unit (单位) |
|--------------|-------------|-------------|------------|
| $\Delta x$ | Absolute uncertainty | 绝对不确定度 | Same as the measured quantity |
| $\bar{x}$ | Mean value | 平均值 | Same as the measured quantity |

**Conditions / 适用条件:**
- **English:** This is used to express the uncertainty as a percentage of the measurement. It is useful for comparing the precision of different measurements.
- **中文:** 用于将不确定度表示为测量值的百分比。它对于比较不同测量的精密度很有用。

---

# 6. Graphs and Relationships / 图表与关系

## 6.1 Distribution of Repeated Readings / 重复读数的分布

### Axes / 坐标轴
- **X-axis:** Measured Value / 测量值
- **Y-axis:** Frequency / 频率

### Shape / 形状
**English:** The shape is a histogram. For a set of repeated readings with only random errors, the histogram should be roughly bell-shaped (a normal distribution), with the highest frequency at the mean value.

**中文:** 形状是直方图。对于仅存在随机误差的一组重复读数，直方图应大致呈钟形（正态分布），在平均值处频率最高。

### Gradient Meaning / 斜率含义
**English:** Not applicable for a histogram.

**中文:** 不适用于直方图。

### Area Meaning / 面积含义
**English:** The total area under the histogram is equal to the total number of readings.

**中文:** 直方图下的总面积等于总读数次数。

### Exam Interpretation / 考试解读
**English:** You will not be asked to draw this graph in an exam, but you should understand the concept. A narrow, tall histogram indicates high precision (small uncertainty). A wide, flat histogram indicates low precision (large uncertainty).

**中文:** 考试中不会要求您绘制此图，但您应理解其概念。窄而高的直方图表示精密度高（不确定度小）。宽而平的直方图表示精密度低（不确定度大）。

> 📷 **IMAGE PROMPT — DIAGRAM-02: Histogram of Repeated Readings**
> Two histograms side-by-side. The left one is tall and narrow, centered around a value, labeled "High Precision". The right one is short and wide, centered around the same value, labeled "Low Precision". The mean is marked on both.

---

# 7. Required Diagrams / 必备图表

## 7.1 Diagram: Calculating Uncertainty from Repeated Readings / 图表：从重复读数计算不确定度

### Description / 描述
**English:** A diagram showing a set of repeated readings (e.g., 5 readings of the length of a pendulum: 25.1 cm, 25.3 cm, 25.0 cm, 25.2 cm, 25.4 cm). The mean is calculated and shown. The maximum and minimum values are identified. The range is shown as an arrow, and half the range is calculated as the uncertainty. The final result is written as (mean ± uncertainty) cm.

**中文:** 一个显示一组重复读数的图表（例如，摆长的5次读数：25.1 cm, 25.3 cm, 25.0 cm, 25.2 cm, 25.4 cm）。计算并显示平均值。识别最大值和最小值。用箭头显示极差，并计算极差的一半作为不确定度。最终结果写为 (平均值 ± 不确定度) cm。

### Image Prompt / 图片生成提示
> 📷 **IMAGE PROMPT — DIAGRAM-03: Worked Example of Uncertainty Calculation**
> A step-by-step visual guide. Step 1: List of 5 readings. Step 2: Calculate mean (25.2 cm). Step 3: Identify max (25.4 cm) and min (25.0 cm). Step 4: Calculate range (0.4 cm). Step 5: Calculate uncertainty (0.2 cm). Step 6: Write final result: (25.2 ± 0.2) cm. Use clear boxes and arrows.

### Labels Required / 需要标注
- **English:** Mean, Maximum, Minimum, Range, Uncertainty, Final Result.
- **中文:** 平均值, 最大值, 最小值, 极差, 不确定度, 最终结果。

### Exam Importance / 考试重要性
**English:** This is a core skill. You must be able to perform this calculation and present the result correctly. This diagram helps you visualize the process.

**中文:** 这是一项核心技能。您必须能够执行此计算并正确呈现结果。此图有助于您将过程可视化。

---

# 8. Worked Examples / 典型例题

## Example 1: Basic Calculation / 例题1：基本计算

### Question / 题目
**English:** A student measures the diameter of a metal sphere five times using a micrometer. The readings are: 12.45 mm, 12.52 mm, 12.48 mm, 12.50 mm, 12.46 mm. Calculate the mean diameter, the absolute uncertainty, and express the final result correctly.

**中文:** 一名学生使用千分尺五次测量金属球的直径。读数为：12.45 mm, 12.52 mm, 12.48 mm, 12.50 mm, 12.46 mm。计算平均直径、绝对不确定度，并正确表达最终结果。

### Solution / 解答
**Step 1: Calculate the mean.**
$$ \bar{x} = \frac{12.45 + 12.52 + 12.48 + 12.50 + 12.46}{5} = \frac{62.41}{5} = 12.482 \text{ mm} $$

**Step 2: Identify the maximum and minimum readings.**
$$ x_{\text{max}} = 12.52 \text{ mm} $$
$$ x_{\text{min}} = 12.45 \text{ mm} $$

**Step 3: Calculate the range.**
$$ \text{Range} = 12.52 - 12.45 = 0.07 \text{ mm} $$

**Step 4: Calculate the absolute uncertainty.**
$$ \Delta x = \frac{0.07}{2} = 0.035 \text{ mm} $$

**Step 5: Round the uncertainty to 1 significant figure.**
$$ \Delta x = 0.04 \text{ mm} $$

**Step 6: Round the mean to the same number of decimal places as the uncertainty.**
$$ \bar{x} = 12.48 \text{ mm} $$

**Step 7: Write the final result.**
$$ \text{Diameter} = (12.48 \pm 0.04) \text{ mm} $$

### Final Answer / 最终答案
**Answer:** $(12.48 \pm 0.04) \text{ mm}$ | **答案：** $(12.48 \pm 0.04) \text{ mm}$

### Quick Tip / 提示
**English:** Always round the uncertainty to 1 significant figure first, then round the mean to match. Never round the mean before the uncertainty.
**中文:** 始终先将不确定度四舍五入到1位有效数字，然后将平均值四舍五入到与之匹配的小数位数。切勿在不确定度之前先四舍五入平均值。

---

## Example 2: With an Anomalous Result / 例题2：包含异常结果

### Question / 题目
**English:** A student measures the time for 20 oscillations of a pendulum. The readings are: 15.2 s, 15.4 s, 15.3 s, 16.8 s, 15.1 s. Calculate the mean time and the absolute uncertainty. Explain any steps you take.

**中文:** 一名学生测量了摆锤20次全振动的时间。读数为：15.2 s, 15.4 s, 15.3 s, 16.8 s, 15.1 s。计算平均时间和绝对不确定度。解释您采取的任何步骤。

### Solution / 解答
**Step 1: Identify and discard the anomalous result.**
The reading 16.8 s is clearly different from the others. It is an anomalous result and should be discarded.

**Step 2: Calculate the mean using the remaining readings.**
$$ \bar{x} = \frac{15.2 + 15.4 + 15.3 + 15.1}{4} = \frac{61.0}{4} = 15.25 \text{ s} $$

**Step 3: Identify the maximum and minimum of the remaining readings.**
$$ x_{\text{max}} = 15.4 \text{ s} $$
$$ x_{\text{min}} = 15.1 \text{ s} $$

**Step 4: Calculate the range.**
$$ \text{Range} = 15.4 - 15.1 = 0.3 \text{ s} $$

**Step 5: Calculate the absolute uncertainty.**
$$ \Delta x = \frac{0.3}{2} = 0.15 \text{ s} $$

**Step 6: Round the uncertainty to 1 significant figure.**
$$ \Delta x = 0.2 \text{ s} $$

**Step 7: Round the mean to the same number of decimal places as the uncertainty.**
$$ \bar{x} = 15.3 \text{ s} $$

**Step 8: Write the final result.**
$$ \text{Time} = (15.3 \pm 0.2) \text{ s} $$

### Final Answer / 最终答案
**Answer:** $(15.3 \pm 0.2) \text{ s}$ | **答案：** $(15.3 \pm 0.2) \text{ s}$

### Quick Tip / 提示
**English:** Always state that you have discarded an anomalous result and explain why. This shows the examiner you understand the process.
**中文:** 始终说明您已丢弃了异常结果并解释原因。这向考官表明您理解该过程。

---

# 9. Past Paper Question Types / 历年真题题型

| Question Type / 题型 | Frequency / 频率 | Difficulty / 难度 | Past Paper References / 真题索引 |
|----------------------|------------------|------------------|-------------------------------|
| Calculate mean and uncertainty from a set of readings | Very High | Easy | 📝 *待填入* |
| Calculate percentage uncertainty from absolute uncertainty | High | Easy | 📝 *待填入* |
| Identify and discard anomalous results | Medium | Medium | 📝 *待填入* |
| Combine uncertainty from repeated readings with other uncertainties | Medium | Hard | 📝 *待填入* |
| Explain why repeating measurements reduces uncertainty | Low | Medium | 📝 *待填入* |

**Common Command Words / 常见指令词:**
- **Calculate / 计算:** Perform a numerical calculation.
- **Determine / 确定:** Find a value, often from a graph or calculation.
- **Explain / 解释:** Give reasons for a phenomenon or a step in a method.
- **State / 陈述:** Give a brief answer without explanation.
- **Show that / 证明:** Demonstrate that a given result is correct.

---

# 10. Practical Skills Connections / 实验技能链接

**English:**
This sub-topic is directly linked to the practical papers (CAIE Paper 3/5, Edexcel U3/U6). In any experiment where you take repeated readings, you will be expected to:
1. **Record data:** Present your repeated readings in a table.
2. **Calculate the mean:** Show your working.
3. **Calculate the uncertainty:** Use the range method.
4. **Express the final result:** Write it as (mean ± uncertainty).
5. **Use the uncertainty:** This uncertainty will be used to draw [[Error Bars on Graphs]] and to [[Propagating Uncertainties Through Calculations]].
6. **Evaluate the experiment:** The size of the uncertainty can be used to suggest improvements (e.g., "The uncertainty was large, so I should use a more precise instrument" or "I should take more readings"). See [[Evaluation and Improvements]].

**中文:**
本子知识点与实验试卷（CAIE Paper 3/5, Edexcel U3/U6）直接相关。在任何需要重复读数的实验中，您都需要：
1. **记录数据：** 将重复读数呈现在表格中。
2. **计算平均值：** 展示您的计算过程。
3. **计算不确定度：** 使用极差法。
4. **表达最终结果：** 写为 (平均值 ± 不确定度)。
5. **使用不确定度：** 该不确定度将用于绘制[[Error Bars on Graphs]]和[[Propagating Uncertainties Through Calculations]]。
6. **评估实验：** 不确定度的大小可用于提出改进建议（例如，“不确定度很大，所以我应该使用更精密的仪器”或“我应该进行更多次读数”）。参见[[Evaluation and Improvements]]。

---

# 11. Concept Map / 概念图谱

```mermaid
graph TD
    %% Show connections for this leaf node
    A[Calculating Uncertainty from Repeated Readings] --> B[Take Multiple Readings]
    A --> C[Calculate Mean]
    A --> D[Calculate Range]
    A --> E[Calculate Uncertainty = Range/2]
    A --> F[Express Final Result: Mean ± Uncertainty]

    B --> G[Identify and Discard Anomalous Results]
    C --> H[Mean is Best Estimate of True Value]
    D --> I[Range Measures Spread of Data]
    E --> J[Absolute Uncertainty]
    E --> K[Percentage Uncertainty = (Uncertainty/Mean) x 100%]

    F --> L[Used for Error Bars on Graphs]
    F --> M[Used for Propagating Uncertainties Through Calculations]
    F --> N[Used for Evaluation and Improvements]

    subgraph "Prerequisites"
        O[Uncertainties and Errors]
        P[Data Recording and Analysis]
    end

    O --> A
    P --> A

    subgraph "Sibling Topics"
        Q[Error Bars on Graphs]
        R[Using Worst-Fit Lines for Uncertainty in Gradient]
        S[Percentage Difference and Percentage Uncertainty]
        T[Propagating Uncertainties Through Calculations]
    end

    A --> Q
    A --> R
    A --> S
    A --> T
```

---

# 12. Quick Revision Sheet / 速查表

| Category / 类别 | Key Points / 要点 |
|----------------|------------------|
| **Definition / 定义** | Uncertainty from repeated readings estimates the random error in a measurement. It is calculated from the spread of the data. / 来自重复读数的不确定度估计了测量中的随机误差。它由数据的离散程度计算得出。 |
| **Key Formula / 核心公式** | $\bar{x} = \frac{\sum x_i}{n}$ (Mean / 平均值) <br> $\Delta x = \frac{x_{\text{max}} - x_{\text{min}}}{2}$ (Uncertainty / 不确定度) <br> $\text{Percentage Uncertainty} = \frac{\Delta x}{\bar{x}} \times 100\%$ |
| **Key Graph / 核心图表** | Histogram of repeated readings. Narrow = high precision (small uncertainty). Wide = low precision (large uncertainty). / 重复读数的直方图。窄 = 高精密度（小不确定度）。宽 = 低精密度（大不确定度）。 |
| **Exam Tip / 考试提示** | 1. Always round uncertainty to 1 s.f. first. <br> 2. Then round the mean to match the decimal places of the uncertainty. <br> 3. Discard anomalous results and state why. <br> 4. Show all your working. <br> 5. Always include units. <br> 1. 始终先将不确定度四舍五入到1位有效数字。 <br> 2. 然后将平均值四舍五入到与不确定度相同的小数位数。 <br> 3. 丢弃异常结果并说明原因。 <br> 4. 展示所有计算过程。 <br> 5. 始终包含单位。 |