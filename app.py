from flask import Flask, render_template, request
import numpy as np
import joblib

# Load pre-trained model and scaler
model = joblib.load("house_price_model.pkl")
scaler = joblib.load("scaler.pkl")

# Initialize Flask app
app = Flask(__name__)

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    price = None
    if request.method == "POST":
        try:
            # Collect numeric inputs
            area = float(request.form["area"])
            bedrooms = int(request.form["bedrooms"])
            bathrooms = int(request.form["bathrooms"])
            stories = int(request.form["stories"])
            parking = int(request.form["parking"])

            # Collect binary features
            mainroad = int(request.form.get("mainroad", 0))
            guestroom = int(request.form.get("guestroom", 0))
            basement = int(request.form.get("basement", 0))
            hotwaterheating = int(request.form.get("hotwaterheating", 0))
            airconditioning = int(request.form.get("airconditioning", 0))
            prefarea = int(request.form.get("prefarea", 0))

            # Furnishing status mapping to one-hot
            furnishingstatus = request.form.get("furnishingstatus", "unfurnished")
            if furnishingstatus == "semi-furnished":
                furnish_semi = 1
                furnish_full = 0
            elif furnishingstatus == "furnished":
                furnish_semi = 0
                furnish_full = 1
            else:  # unfurnished
                furnish_semi = 0
                furnish_full = 0

            # Correct feature order: numeric + binary + one-hot
            X_input = np.array([[area, bedrooms, bathrooms, stories,
                                 mainroad, guestroom, basement,
                                 hotwaterheating, airconditioning, parking,
                                 prefarea, furnish_semi, furnish_full]])

            # Scale numeric features (area, bedrooms, bathrooms, stories, parking)
            numeric_indices = [0, 1, 2, 3, 9]
            X_input[:, numeric_indices] = scaler.transform(X_input[:, numeric_indices])

            # Predict house price
            price = round(model.predict(X_input)[0], 2)

        except Exception as e:
            price = f"Error: {e}"

    return render_template("index.html", price=price)

if __name__ == "__main__":
    app.run(debug=True)
