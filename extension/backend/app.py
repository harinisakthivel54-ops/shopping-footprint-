from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Demo carbon factors by product category
CARBON_DATA = {
    "laptop": {
        "manufacturing": 150,
        "transport": 15,
        "packaging": 5,
        "usage": 8,
        "end_of_life": 2
    },
    "smartphone": {
        "manufacturing": 55,
        "transport": 8,
        "packaging": 3,
        "usage": 3,
        "end_of_life": 1
    },
    "headphones": {
        "manufacturing": 8,
        "transport": 2,
        "packaging": 1,
        "usage": 1,
        "end_of_life": 0.6
    },
    "shoes": {
        "manufacturing": 6,
        "transport": 1.5,
        "packaging": 0.5,
        "usage": 0.2,
        "end_of_life": 0.2
    },
    "tshirt": {
        "manufacturing": 1.4,
        "transport": 0.4,
        "packaging": 0.2,
        "usage": 0.1,
        "end_of_life": 0.1
    },
    "bottle": {
        "manufacturing": 0.8,
        "transport": 0.3,
        "packaging": 0.1,
        "usage": 0.1,
        "end_of_life": 0.1
    }
}


def find_category(product_name):
    name = product_name.lower()

    if "laptop" in name or "computer" in name:
        return "laptop"

    if "phone" in name or "smartphone" in name:
        return "smartphone"

    if "headphone" in name or "earphone" in name:
        return "headphones"

    if "shoe" in name or "sneaker" in name:
        return "shoes"

    if "t-shirt" in name or "tshirt" in name or "shirt" in name:
        return "tshirt"

    if "bottle" in name:
        return "bottle"

    return None


def calculate_emission(data):
    return round(sum(data.values()), 2)


def calculate_eco_score(carbon):
    if carbon <= 3:
        return 90
    elif carbon <= 10:
        return 70
    elif carbon <= 50:
        return 50
    else:
        return 30


def impact_level(score):
    if score >= 75:
        return "Low"
    elif score >= 50:
        return "Moderate"
    else:
        return "High"


@app.route("/")
def home():
    return jsonify({
        "message": "Shopping Footprint API is running 🌱"
    })


@app.route("/carbon", methods=["POST"])
def carbon():

    data = request.get_json()

    if not data or "product_name" not in data:
        return jsonify({
            "error": "product_name is required"
        }), 400

    product_name = data["product_name"]

    category = find_category(product_name)

    if category is None:
        return jsonify({
            "product": product_name,
            "message": "Product category not found",
            "estimated_carbon_kg": 4.2,
            "eco_score": 60,
            "impact": "Moderate"
        })

    breakdown = CARBON_DATA[category]

    total_carbon = calculate_emission(breakdown)

    score = calculate_eco_score(total_carbon)

    return jsonify({
        "product": product_name,
        "category": category,
        "carbon_kg_co2e": total_carbon,
        "eco_score": score,
        "impact": impact_level(score),
        "breakdown": breakdown
    })


if __name__ == "__main__":
    app.run(debug=True)