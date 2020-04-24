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
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, # 2 cups
                "unit_size": 1,
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Bourbon",
                "amount": 2, # 2 oz
                "unit_size": 1,
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Fresh lemon juice",
                "amount": 3, # 3 x (1/4 oz)
                "unit_size": 1,
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Simple syrup",
                "amount": 3, # 3 x (/4 oz)
                "unit_size": 1,
                "unit": "/4 oz",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Orange wheel",
                "amount": 1, # 1 x (1/2 wheel)
                "unit_size": 1,
                "unit": " half wheel",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Maraschino cherry",
                "amount": 1, # 1 cherry
                "unit_size": 1,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
]

available_ingredients = []
added_ingredients = []

@app.route('/<recipe_id>')
def recipe(recipe_id=None):
    available_ingredients.clear()
    added_ingredients.clear()

    global recipe
    for item in recipes:
        if item["id"] == int(recipe_id):
            for ingredient in item["mix_ingredients"]:
                ingredient["amount_added"] = 0
                available_ingredients.append(ingredient)

    return render_template('ppc.html', available_ingredients=available_ingredients, added_ingredients=added_ingredients)

@app.route('/move_to_added_ingredients', methods=['GET', 'POST'])
def move_to_ppc():

    json_data = request.get_json()   
    ingredient_id = json_data["ingredient_id"]

    i = 0;
    for item in recipes[0]["mix_ingredients"]:
        if item["id"] == ingredient_id:
            ingredient_to_move = recipes[0]["mix_ingredients"][i]
            ingredient_to_move["amount_added"] = ingredient_to_move["amount_added"] + 1
        i+=1

    if(ingredient_to_move["amount_added"] == ingredient_to_move["amount"]):
        available_ingredients.remove(ingredient_to_move)
    if(ingredient_to_move["amount_added"] < 2):
        added_ingredients.insert(0, ingredient_to_move)

    return jsonify(available_ingredients=available_ingredients, added_ingredients=added_ingredients)

@app.route('/move_to_available_ingredients', methods=['GET', 'POST'])
def move_to_non_ppc():

    json_data = request.get_json()
    ingredient_id = json_data["ingredient_id"]

    i = 0;
    for item in recipes[0]["mix_ingredients"]:
        if item["id"] == ingredient_id:
            ingredient_to_move = recipes[0]["mix_ingredients"][i]
            ingredient_to_move["amount_added"] = ingredient_to_move["amount_added"] - 1
        i+=1

    if(available_ingredients.count(ingredient_to_move) < 1):
        available_ingredients.insert(0, ingredient_to_move)
    if(ingredient_to_move["amount_added"] < 1):
        added_ingredients.remove(ingredient_to_move)

    return jsonify(available_ingredients=available_ingredients, added_ingredients=added_ingredients)

if __name__ == '__main__':
   app.run(debug = True)




