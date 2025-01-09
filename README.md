# DataVisualization
# Airplane Crash Analysis Project

This project analyzes airplane crash data from 1908 to 2019, providing insights into fatal accidents, their causes, and potential patterns. The analysis utilizes Python for data cleaning, visualization, and statistical calculations.

---

## Dataset

- **Source:** [Kaggle - Airplane Crash Data Since 1908](https://www.kaggle.com/datasets/cgurkan/airplane-crash-data-since-1908/data)
- **Description:** The dataset includes details about airplane crashes worldwide, with fields such as date, location, operator, number of fatalities, and more.
- **Rows:** 4,968  
- **Fields:**
  - `Date`, `Time`, `Location`, `Operator`, `Flight #`, `Route`, `AC Type`, `Registration`, `cn/ln`, `Aboard`, `Aboard Passengers`, `Aboard Crew`, `Fatalities`, `Fatalities Passengers`, `Fatalities Crew`, `Ground`, `Summary`.

---

## Project Goals

1. Identify key factors contributing to fatal airplane crashes.
2. Analyze trends in crashes over time.
3. Highlight airlines and aircraft types associated with higher crash rates.
4. Explore the relationship between various parameters (e.g., fatalities vs. passengers).

---

## Methods

### Data Cleaning:
- Removed duplicates and filled missing values:
  - Numeric fields: Filled with the column mean.
  - Non-numeric fields: Filled with `Unknown`.

### Normalization:
- All numeric fields were normalized to a range of 0 to 1.

### Statistical Metrics:
- **For numeric columns:**
  - Mean, Median, Standard Deviation, Range, Missing Values.
- **For non-numeric columns:**
  - Missing Values, Unique Value Count, Most Common Value.

---

## Visualizations

1. **Joint Plot:** Relationship between fatalities and aboard passengers.
2. **Bar Plot:** Fatalities per airline.
3. **KDE Plot:** Fatalities distribution.
4. **Bubble Plot:** Relationships among passengers aboard, fatalities, and airline.
5. **Pair Plot:** Correlations among numeric fields.

---

