# 🏠 Bahrain Rent Predictor

An interactive machine learning web application that predicts the estimated monthly rental price of properties in Bahrain based on property characteristics and location information.

🌐 **Live Demo:** [Bahrain Rent Predictor](https://bahrain-rent-predictor1.streamlit.app/?utm_source=chatgpt.com)

---

## 📌 Project Overview

**Bahrain Rent Predictor** is a Machine Learning regression project developed to estimate residential property rental prices in Bahrain.

The project explores different regression algorithms and compares their performance before selecting a tuned **XGBoost Regressor** as the final model.

The trained model is integrated into an interactive **Streamlit** application, allowing users to enter property details and receive an estimated monthly rental price.

---

## 🎯 Project Goal

The main goal of this project is to demonstrate how Machine Learning can be used to estimate property rental prices and support data-driven decision-making in the Bahrain real estate market.

---

## ✨ Features

* 🏠 Predict estimated monthly property rent
* 📍 Select property location and governorate
* 🛏️ Enter number of bedrooms and bathrooms
* 📐 Enter property size
* 🏊 Select property amenities and features
* 🌊 Include features such as sea view, pool, garden, parking, and gym
* 🛋️ Specify furnishing status
* 🤖 Generate predictions using a trained XGBoost model
* 📊 Display model performance metrics
* 💻 Interactive Streamlit interface
* 🌐 Deployed online using Streamlit Community Cloud

---

## 🧠 Machine Learning

Several regression models were explored and compared during the project, including:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* Extra Trees Regressor
* XGBoost Regressor
* LightGBM

After model comparison and tuning, **XGBoost** was selected as the final model.

---

## 📊 Model Performance

The final model was evaluated on a separate test set.

| Metric       |         Result |
| ------------ | -------------: |
| **MAE**      |  **99.06 BHD** |
| **RMSE**     | **183.99 BHD** |
| **R² Score** |      **0.779** |

The R² score indicates that the final model explains approximately **77.9% of the variation** in rental prices in the test data.

> **Note:** Predictions are estimates and actual rental prices may vary depending on market conditions, property condition, location, and other factors.

---

## 🔍 Features Used

The model uses property-related and location-related information, including:

### Property Information

* Number of bedrooms
* Number of bathrooms
* Property size
* Total rooms
* Property type
* Number of amenities

### Location

* Area
* Governorate
* Property location information

### Property Features

* Sea view
* Swimming pool
* Garden
* Parking
* Gym
* Balcony
* Beach access
* Luxury features
* Modern features
* Renovation
* Duplex
* Private features

### Furnishing

* Furnished
* Semi-furnished
* Unfurnished

### Other Information

* Agency
* Availability
* Utilities
* Season

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **XGBoost**
* **LightGBM**
* **Joblib**
* **Streamlit**
* **Git/GitHub**

---

## 📁 Project Structure

```text
bahrain-rent-predictor/
│
├── app.py
├── bahrain_rent_model.pkl
├── requirements.txt
└── README.md
```

### Main Files

**`app.py`**
The Streamlit application responsible for collecting property information and displaying rental price predictions.

**`bahrain_rent_model.pkl`**
The trained machine learning model used to generate rental price predictions.

**`requirements.txt`**
Contains the Python libraries required to run the application.

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/bahrain-rent-predictor.git
cd bahrain-rent-predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

**Live Demo:** [Bahrain Rent Predictor](https://bahrain-rent-predictor1.streamlit.app/?utm_source=chatgpt.com)

---

## 🔮 Future Improvements

Future versions of the project could include:

* 📚 Increasing the size and diversity of the dataset
* 📍 Adding more detailed location information
* 📊 Adding interactive rental price visualizations
* 🗺️ Integrating property maps
* 🏘️ Adding neighborhood-level price analysis
* 🤖 Improving model performance through further tuning
* 📈 Adding prediction intervals
* 💡 Providing explanations for individual predictions
* 📱 Improving the application for mobile users

---

## 🎓 Project Context

This project was developed as part of a **Data Science Bootcamp** and demonstrates practical experience in:

* Data preprocessing
* Exploratory Data Analysis
* Feature Engineering
* Regression Modeling
* Model Comparison
* Hyperparameter Tuning
* Model Evaluation
* Machine Learning Deployment
* Streamlit Application Development

---

## 👩🏻‍💻 Author

**Zainab Mohamed Moosa**

Data Science 
