# 🏠 House Price Prediction Web App

## Overview
This project predicts house prices based on property features such as area, bedrooms, bathrooms, number of stories, parking, furnishing status, and other facilities. It uses **machine learning** with **Linear Regression** and **Gradient Boosting** models to provide accurate predictions. The app is built using **Flask** and features a **modern, responsive UI** for easy interaction.

---

## Features
- Predict house prices based on user input.
- Supports numeric features (area, bedrooms, bathrooms, stories, parking).
- Supports binary features (main road, guest room, basement, hot water heating, air conditioning, preferred area).
- Furnishing status selection: Furnished, Semi-Furnished, or Unfurnished.
- Gradient Boosting model with hyperparameter tuning for improved accuracy.
- Modern UI design with sliders, checkboxes, and radio buttons.
- Displays predicted price clearly in a result card.

---

## Dataset
The model was trained on the **House Price Prediction dataset**, which includes the following features:
- `price` (target)
- `area` (square footage)
- `bedrooms`, `bathrooms`, `stories`, `parking`
- `mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea`
- `furnishingstatus` (Furnished, Semi-Furnished, Unfurnished)

---

## Model
- **Linear Regression**: Baseline model for predictions.
- **Gradient Boosting Regressor**: Tuned with `GridSearchCV` for improved accuracy.
- Numeric features are scaled using `StandardScaler`.
- Categorical features like `furnishingstatus` are one-hot encoded.

**Model Performance (Example):**
MAE: $1,048,755
RMSE: $1,404,717
R^2: 0.542

Install dependencies
pip install -r requirements.txt

Run the Flask app
python app.py

Open a browser and go to http://127.0.0.1:5000/ to use the app.

UI Features

Sliders for numeric inputs like area, bedrooms, bathrooms, stories, and parking.

Checkboxes for facilities (main road, guest room, basement, hot water heating, air conditioning, preferred area).

Radio buttons for furnishing status selection.

Responsive design using modern CSS and Bootstrap.

Future Enhancements

Add more relevant features like year built, lot size, and location quality.

Deploy the app to cloud platforms like Heroku or AWS.

Integrate interactive visualizations for price trends.
