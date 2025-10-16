from flask import Flask, render_template, request
from prediction import predict_rent

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        city = request.form['city']
        area = request.form['area']
        bed = request.form['no_bedroom']
        bath = request.form['no_bathroom']
        balcony = request.form['balcony']
        tiles = request.form['tiles']

        predicted_rent = predict_rent(
            total_area=area,
            no_of_bed_room=bed,
            no_of_bath_room=bath,
            tiles=tiles,
            balcony=balcony,
            city=city
        )

        return render_template('index.html', prediction=f"Predicted Rent: {predicted_rent} BDT")

    except Exception as e:
        return render_template('index.html', error=f"⚠️ Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
