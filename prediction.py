import pickle
import pandas as pd
import os

# === Load Model and Encoder ===
model_path = os.path.join("model", "xgb_usn_house_rent_model.pkl")
encoder_path = os.path.join("model", "tiles_encoder.pkl")

try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(encoder_path, "rb") as f:
        encoder = pickle.load(f)
    print("✅ Model and encoder loaded successfully!")
except Exception as e:
    print(f"⚠️ Error loading model or encoder: {e}")


# === Main Prediction Function ===
def predict_rent(total_area, no_of_bed_room, no_of_bath_room, tiles, balcony, city):
    """
    Predicts rent based on apartment details.
    """
    input_data = {
        'total_area': [float(total_area)],
        'no_of_bed_room': [int(no_of_bed_room)],
        'no_of_bath_room': [int(no_of_bath_room)],
        'tiles': [tiles],
        'balcony': [int(balcony)],
        'lakshmipur city': [0],
        'noakhali city': [0],
        'raipur city': [0]
    }

    # One-hot encode city
    city = city.lower().strip()
    if city == 'noakhali':
        input_data['noakhali city'] = [1]
    elif city == 'lakshmipur':
        input_data['lakshmipur city'] = [1]
    elif city == 'raipur':
        input_data['raipur city'] = [1]
    elif city == 'feni':
        pass  # all 0
    else:
        raise ValueError("Unknown city! Choose from: noakhali, lakshmipur, feni, raipur")

    # Convert to DataFrame
    input_df = pd.DataFrame(input_data)

    # Encode tiles
    input_df['tiles'] = encoder.transform(input_df['tiles']) + 1

    # Predict
    predicted_rent = model.predict(input_df)[0]
    return round(predicted_rent, 2)


# === Optional test ===
# if __name__ == "__main__":
#     result = predict_rent(1300, 3, 2, 'yes', 2, 'noakhali')
#     print("Predicted Rent:", result, "Taka")
