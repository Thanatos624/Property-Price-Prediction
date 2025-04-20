# California Housing Price Prediction

![ChatGPT Image Apr 20, 2025, 09_35_39 PM](https://github.com/user-attachments/assets/1857d5e9-34b4-43d3-b0e8-bcdde80115e4)


## 📊 Project Overview

This project focuses on predicting property prices in various districts of California using machine learning. By analyzing several district-level features such as income, number of rooms, geographical location, and proximity to the ocean, we aim to identify key variables that influence housing prices and improve the accuracy of house value predictions.

The implementation utilizes both simple linear regression and multiple linear regression approaches, ensuring proper data handling and robust model evaluation.

## 🎯 Problem Statement

The objective is to predict the median house value in California districts based on a set of features. Given the dataset, we develop regression models, evaluate their performance, and determine which model provides the best balance between predictive accuracy and interpretability.

## 🗂️ Dataset Information

The dataset (`data_file.csv`) contains information about California housing districts including:

- `longitude`: Geographic coordinate
- `latitude`: Geographic coordinate
- `housing_median_age`: Median age of houses in the district
- `total_rooms`: Total number of rooms in the district
- `total_bedrooms`: Total number of bedrooms in the district
- `population`: Population in the district
- `households`: Number of households in the district
- `median_income`: Median income of residents (in tens of thousands)
- `median_house_value`: Median house value (target variable)
- `ocean_proximity`: Categorical variable indicating proximity to the ocean

## 🛠️ Methodology

### Exploratory Data Analysis (EDA)
- Statistical summaries and distribution analysis
- Correlation analysis between features
- Visualization of geographical patterns
- Identification of key relationships with house prices

### Data Preprocessing
- Handling missing values
- Feature scaling and normalization
- Encoding categorical variables (ocean_proximity)
- Feature engineering to create derived variables:
  - rooms_per_household
  - bedrooms_ratio
  - population_per_household

### Model Development
- **Simple Linear Regression:** Using the single most correlated feature
- **Multiple Linear Regression:** Using all available features

### Model Evaluation
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R-squared (R²) metric
- Residual analysis

## 📈 Results

### Model Performance Comparison

| Model | Training RMSE | Test RMSE | Training R² | Test R² |
|-------|---------------|-----------|-------------|---------|
| Simple Linear Regression | *value* | *value* | *value* | *value* |
| Multiple Linear Regression | *value* | *value* | *value* | *value* |

### Key Insights
- The multiple linear regression model explains approximately XX% of the variance in house prices
- The most influential features were found to be:
  1. Median income
  2. Geographic location (especially proximity to coastal areas)
  3. Housing density metrics

## 💻 Implementation

### Requirements
- Python 3.7+
- Libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - joblib
  - streamlit (for the web app)

### Running the Code

1. Clone the repository:
```bash
git clone https://github.com/your-username/california-housing-prediction.git
cd california-housing-prediction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the training script:
```bash
python train_model.py
```

4. Launch the interactive prediction app:
```bash
streamlit run housing_app.py
```

## 🖥️ Interactive Web Application

The project includes an interactive Streamlit web application that allows users to:

- Input district characteristics
- View predicted median house values
- Understand the key factors influencing the predictions

![Housing App Screenshot](https://i.imgur.com/g5jMBT2.jpg)

## 📝 Future Improvements

- Implement more advanced regression techniques (Random Forest, Gradient Boosting)
- Include additional features (school quality, crime rates, etc.)
- Develop a time-series component to predict future price trends
- Create more advanced visualizations for feature importance

## 📋 Directory Structure

```
california-housing-prediction/
│
├── data/
│   └── data_file.csv
│
├── notebooks/
│   └── housing_analysis.ipynb
│
├── src/
│   ├── train_model.py
│   └── preprocessing.py
│
├── models/
│   └── california_housing_price_model.pkl
│
├── app/
│   └── housing_app.py
│
├── requirements.txt
└── README.md
```

## 👥 Contributors

- [Mainak Saha](https://github.com/Thanatos624)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
