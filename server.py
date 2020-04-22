from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

recipes = [
    {
        "id": 1,
        "name": "Whiskey Sour",
        "ordered": False,
        "mix_ingredients": [
            {
                "ingredient": "Ice",
                "amount": 2, # 2 cups
            },
            {
                "ingredient": "Bourbon",
                "amount": 2, # 2 oz
            },
            {
                "ingredient": "Fresh lemon juice",
                "amount": 3, # 3 x (1/4 oz)
            },
            {
                "ingredient": "Simple syrup",
                "amount": 3, # 3 x (/4 oz)
            },
        ],
        "garnish_ingredients": [
            {
                "ingredient": "Orange wheel",
                "amount": 1 # 1 x (1/2 wheel)
            },
            {
                "ingredient": "Maraschino cherry",
                "amount": 1 # 1 cherry
            },
        ],
    },
]

available_ingredients = []
added_ingredients = []

@app.route('/')
def ppc():
    available_ingredients.clear()
    added_ingredients.clear()
    for item in recipes[0]["mix_ingredients"]:
        available_ingredients.append(item["ingredient"])

    return render_template('ppc.html', available_ingredients=available_ingredients, added_ingredients=added_ingredients)

@app.route('/move_to_added_ingredients', methods=['GET', 'POST'])
def move_to_ppc():

    json_data = request.get_json()   
    person_to_move = json_data["name"]


    # added_ingredients.append(person_to_move)
    # prepend instead of append
    added_ingredients.insert(0, person_to_move)
    available_ingredients.remove(person_to_move)

    return jsonify(available_ingredients=available_ingredients, added_ingredients=added_ingredients)

@app.route('/move_to_available_ingredients', methods=['GET', 'POST'])
def move_to_non_ppc():

    json_data = request.get_json()
    person_to_move = json_data["name"]

    # available_ingredients.append(person_to_move)
    # prepend instead of append
    available_ingredients.insert(0, person_to_move)
    added_ingredients.remove(person_to_move)

    return jsonify(available_ingredients=available_ingredients, added_ingredients=added_ingredients)

if __name__ == '__main__':
   app.run(debug = True)




