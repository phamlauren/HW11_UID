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
    {
        "id": 2,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 3,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 4,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 5,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 6,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 7,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 8,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 9,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 10,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 11,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 12,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 13,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 14,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },

    {
        "id": 15,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 16,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 17,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 18,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 19,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 20,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 21,
        "name": "",
        "ordered": False,
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0, 
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit_size": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
]

available_ingredients = []
added_ingredients = []
selected_recipe = []

@app.route('/<recipe_id>')
def recipe(recipe_id=None):
    selected_recipe.clear()
    available_ingredients.clear()
    added_ingredients.clear()

    for item in recipes:
        if item["id"] == int(recipe_id):
            selected_recipe.append(item)
            for ingredient in item["mix_ingredients"]:
                ingredient["amount_added"] = 0
                available_ingredients.append(ingredient)
   
    return render_template('mix_recipe.html', recipe=selected_recipe[0], available_ingredients=available_ingredients, added_ingredients=added_ingredients)


@app.route('/move_to_added_ingredients', methods=['GET', 'POST'])
def move_to_added_ingredients():

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

    return jsonify(recipe=selected_recipe[0], available_ingredients=available_ingredients, added_ingredients=added_ingredients)

@app.route('/move_to_available_ingredients', methods=['GET', 'POST'])
def move_to_available_ingredients():

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

    return jsonify(recipe=selected_recipe[0], available_ingredients=available_ingredients, added_ingredients=added_ingredients)

@app.route('/<recipe_id>/garnish')
def garnish(recipe_id=None):
    available_ingredients.clear()
    added_ingredients.clear()

    for item in recipes:
        if item["id"] == int(recipe_id):
            selected_recipe.append(item)
            for ingredient in item["garnish_ingredients"]:
                ingredient["amount_added"] = 0
                available_ingredients.append(ingredient)

    return render_template('garnish_recipe.html', recipe=selected_recipe[0], available_ingredients=available_ingredients, added_ingredients=added_ingredients)


@app.route('/<recipe_id>/move_to_added_garnishes', methods=['GET', 'POST'])
def move_to_added_garnishes(recipe_id=None):
    json_data = request.get_json()   
    ingredient_id = json_data["ingredient_id"]

    i = 0;
    for item in recipes[0]["garnish_ingredients"]:
        if item["id"] == ingredient_id:
            ingredient_to_move = recipes[0]["garnish_ingredients"][i]
            ingredient_to_move["amount_added"] = ingredient_to_move["amount_added"] + 1
        i+=1

    if(ingredient_to_move["amount_added"] == ingredient_to_move["amount"]):
        available_ingredients.remove(ingredient_to_move)
    if(ingredient_to_move["amount_added"] < 2):
        added_ingredients.insert(0, ingredient_to_move)

    return jsonify(recipe=selected_recipe[0], available_ingredients=available_ingredients, added_ingredients=added_ingredients)

@app.route('/<recipe_id>/move_to_available_garnishes', methods=['GET', 'POST'])
def move_to_available_garnishes(recipe_id=None):

    json_data = request.get_json()
    ingredient_id = json_data["ingredient_id"]

    i = 0;
    for item in recipes[0]["garnish_ingredients"]:
        if item["id"] == ingredient_id:
            ingredient_to_move = recipes[0]["garnish_ingredients"][i]
            ingredient_to_move["amount_added"] = ingredient_to_move["amount_added"] - 1
        i+=1

    if(available_ingredients.count(ingredient_to_move) < 1):
        available_ingredients.insert(0, ingredient_to_move)
    if(ingredient_to_move["amount_added"] < 1):
        added_ingredients.remove(ingredient_to_move)

    return jsonify(recipe=selected_recipe[0], available_ingredients=available_ingredients, added_ingredients=added_ingredients)


#@app.route('/<recipe_id>/quiz')
#def quiz(recipe_id=None):

if __name__ == '__main__':
   app.run(debug = True)




