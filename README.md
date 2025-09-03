# 🏠 Boston House Prices Predictor

This project explores the **Boston Housing dataset** and applies multiple machine learning models to predict the **median value of owner-occupied homes (MEDV)** based on neighborhood characteristics. It demonstrates the full ML workflow: data preprocessing, exploratory data analysis (EDA), model training, evaluation, and interpretation.

---

## 📂 Dataset
The dataset contains 506 rows and 14 columns:
- **Features:** crime rate (CRIM), average number of rooms (RM), pupil-teacher ratio (PTRATIO), property tax rate (TAX), % lower status population (LSTAT), and more.  
- **Target:** `MEDV` — median home value in \$1000s.

Source: [Kaggle - Boston House Prices](https://www.kaggle.com/datasets/vikrishnan/boston-house-prices)

---

## 🔎 Project Steps
1. **Data Cleaning & Preprocessing**
   - Checked for missing values and duplicates.
   - Converted categorical features (`CHAS`, `RAD`).
   - Normalized selected numerical columns.

2. **Exploratory Data Analysis**
   - Histograms, scatter plots, and box plots to understand distributions.
   - Correlation heatmap to identify strong predictors (`RM`, `LSTAT`).

3. **Modeling**
   - Linear Regression (baseline).
   - Decision Tree Regressor.
   - Extra Trees Regressor (best performance).

4. **Evaluation**
   - Metrics: Mean Squared Error (MSE), R² score, cross-validation.
   - Extra Trees achieved the lowest error and highest stability.

5. **Feature Importance**
   - `LSTAT` and `RM` emerged as the most influential predictors of home values.

---

## 📊 Results
- **Tree-based ensemble methods outperformed linear models.**
- **`LSTAT` (% lower status) and `RM` (average rooms)** were the strongest predictors.
- Dataset limitations: capped target values (50.0), small sample size, and ethically problematic features (`B`, `LSTAT`).

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/boston-house-prices-predictor.git
   cd boston-house-prices-predictor
