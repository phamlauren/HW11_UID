from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import random
from random import shuffle
app = Flask(__name__)

recipes = [
    {
        "id": 1,
        "name": "Whiskey Sour",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, # 2 cups
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Bourbon",
                "amount": 2, # 2 oz
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Lemon juice",
                "amount": 3, # 3 x (1/4 oz)
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Simple syrup",
                "amount": 3, # 3 x (/4 oz)
                "unit": "/4 oz",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Orange wheel",
                "amount": 1, # 1 x (1/2 wheel)
                "unit": " half wheel",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Maraschino cherry",
                "amount": 1, # 1 cherry
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 2,
        "name": "Margarita",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Silver tequila",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Cointreau",
                "amount": 1, 
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Lime juice",
                "amount": 1, 
                "unit": " oz",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Salt",
                "amount": None,
                "unit": " around glass rim",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Ice",
                "amount": None,
                "unit": " pour mixed ingredients over",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Lemon",
                "amount": 1,
                "unit": " wheel",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 3,
        "name": "Cosmopolitan",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Citrus vodka",
                "amount": 3, 
                "unit": "/2 oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Cointreau",
                "amount": 1, 
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Lime juice",
                "amount": 1, 
                "unit": "/2 oz",
                "amount_added": 0,
            },
            {
                "id": 5,
                "ingredient": "Cranberry juice",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Lime",
                "amount": 1,
                "unit": " wheel",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 4,
        "name": "Mojito",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Muddled mint",
                "amount": 3, 
                "unit": " leaves",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cups",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "White rum",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Lime juice",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 5,
                "ingredient": "Simple syrup",
                "amount": 1, 
                "unit": "/2 oz",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Mint",
                "amount": None,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 5,
        "name": "Gimlet",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Gin",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Simple syrup",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Lime juice",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Lime",
                "amount": 1,
                "unit": " wheel",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 6,
        "name": "Sidecar",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "VS or VSOP cognac",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Cointreau",
                "amount": 1, 
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Lemon juice",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Sugar",
                "amount": None,
                "unit": " around glass rim",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 7,
        "name": "French 75",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Gin",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Simple syrup",
                "amount": 2,
                "unit": " dash",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Lemon juice",
                "amount": 1,
                "unit": "/2 oz",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Champagne",
                "amount": None,
                "unit": " to glass fill",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Lemon",
                "amount": 1,
                "unit": " wheel",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 8,
        "name": "Daiquiri",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Light rum",
                "amount": 2,
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Lime juice",
                "amount": 1,
                "unit": " oz",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Lime",
                "amount": 1,
                "unit": " wheel",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 9,
        "name": "Espresso Martini",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Vodka",
                "amount": 1,
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Coffe liqueur",
                "amount": 1,
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Freshly brewed espresso",
                "amount": 1,
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 5,
                "ingredient": "Simple syrup",
                "amount": 1,
                "unit": " teaspoon",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Espresso beans",
                "amount": None,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 10,
        "name": "Negroni",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "London dry gin",
                "amount": 1,
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Campari",
                "amount": 1,
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Vermouth rosso",
                "amount": 1,
                "unit": " oz",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Orange twist",
                "amount": 1,
                "unit": " wheel",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 11,
        "name": "Bloody Mary",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Vodka",
                "amount": 2,
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Tomato juice",
                "amount": 1,
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Lemon juice",
                "amount": 1,
                "unit": " tablespoon",
                "amount_added": 0,
            },
            {
                "id": 5,
                "ingredient": "Lime juice",
                "amount": 3,
                "unit": "/2 teaspoon",
                "amount_added": 0,
            },
            {
                "id": 6,
                "ingredient": "Worcestershire sauce",
                "amount": 3,
                "unit": "/4 teaspoon",
                "amount_added": 0,
            },
            {
                "id": 7,
                "ingredient": "Horseradish",
                "amount": 1,
                "unit": "/2 teaspoon",
                "amount_added": 0,
            },
            {
                "id": 8,
                "ingredient": "Pepper",
                "amount": 1,
                "unit": "/8 teaspoon",
                "amount_added": 0,
            },
            {
                "id": 9,
                "ingredient": "Celery salt",
                "amount": 1,
                "unit": "/8 teaspoon",
                "amount_added": 0,
            },
            {
                "id": 10,
                "ingredient": "Hot pepper sauce",
                "amount": 1,
                "unit": "/8 teaspoon",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Celery",
                "amount": 1,
                "unit": " stalk",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Cucumber",
                "amount": 1,
                "unit": " wheel",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 12,
        "name": "Mai Tai",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Light rum",
                "amount": 2,
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Triple sec",
                "amount": 3,
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Lemon juice",
                "amount": 1,
                "unit": "/2 oz",
                "amount_added": 0,
            },
            {
                "id": 5,
                "ingredient": "Lime juice",
                "amount": 1,
                "unit": " teaspoon",
                "amount_added": 0,
            },
            {
                "id": 6,
                "ingredient": "Amaretto",
                "amount": 1,
                "unit": " teaspoon",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Lime",
                "amount": 1,
                "unit": " half wheel",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 13,
        "name": "Gin fizz",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Gin",
                "amount": 3, 
                "unit": "/2 oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Lemon juice",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Caster sugar",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Soda",
                "amount": 4,
                "unit": " oz",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 14,
        "name": "Planters' Punch",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Simple syrup",
                "amount": 1, 
                "unit": "/2 oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Lemon juice",
                "amount": 5, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Jamaican",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 5,
                "ingredient": "Angostura bitters",
                "amount": None, 
                "unit": " a few dashes",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Soda",
                "amount": None,
                "unit": " to glass fill",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Cherries",
                "amount": None, 
                "unit": "",
                "amount_added": 0,
            },
        ],
    },

    {
        "id": 15,
        "name": "Singapore Sling",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Gin",
                "amount": 3, 
                "unit": "/2 oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Cherry brandy",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Simple syrup",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 5,
                "ingredient": "Lime juice",
                "amount": 1, 
                "unit": "oz",
                "amount_added": 0,
            },
            {
                "id": 6,
                "ingredient": "Angostura bitters",
                "amount": None, 
                "unit": " dash",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Soda",
                "amount": None,
                "unit": " to glass fill",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 16,
        "name": "Floridian",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Lemon juice",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Caster sugar",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Orange vodka",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 5,
                "ingredient": "Cointreau or triple sec",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 6,
                "ingredient": "Cranberry juice",
                "amount": 2, 
                "unit": " splashes",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Orange peel",
                "amount": 2,
                "unit": " twist",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 17,
        "name": "Lemon-Tini",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Lemon vodka",
                "amount": 3, 
                "unit": "/2 oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Lemoncello",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Lemon juice",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 5,
                "ingredient": "Simple syrup",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Lemon twist",
                "amount": 1,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 18,
        "name": "Aviation",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Gin",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Maraschino liqueur",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Crème de violette",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 5,
                "ingredient": "Lemon juice",
                "amount": 1, 
                "unit": "/2 oz",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Flamed lemon peel",
                "amount": 1,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 19,
        "name": "White Lady",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Gin",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Orange liqueur",
                "amount": 1, 
                "unit": "/2 oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Lemon juice",
                "amount": 1, 
                "unit": "/2 oz",
                "amount_added": 0,
            },
            {
                "id": 5,
                "ingredient": "Egg white",
                "amount": 1, 
                "unit": "",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Orange peel",
                "amount": 1,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 20,
        "name": "Bee's Knees",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Gin",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Lemon juice",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Honey syrup",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "",
                "amount": 0,
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
    {
        "id": 21,
        "name": "Blue Hawaii",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Vodka",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Light rum",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
            {
                "id": 4,
                "ingredient": "Blue curaçao",
                "amount": 1, 
                "unit": "/2 oz",
                "amount_added": 0,
            },
            {
                "id": 5,
                "ingredient": "Pineapple juice",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
            },
            {
                "id": 6,
                "ingredient": "Cream of coconut",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Pineapple",
                "amount": 1,
                "unit": " wedge",
                "amount_added": 0,
            },
            {
                "id": 2,
                "ingredient": "Maraschino cherry",
                "amount": 1, 
                "unit": "",
                "amount_added": 0,
            },
            {
                "id": 3,
                "ingredient": "Cocktail umbrella",
                "amount": 1, 
                "unit": "",
                "amount_added": 0,
            },
        ],
    },
]

available_ingredients = []
added_ingredients = []

available_garnishes = []
added_garnishes = []

removed_from_shaker = []
added_to_shaker = []

@app.route('/<recipe_id>')
def recipe(recipe_id=None):
    available_ingredients.clear()
    added_ingredients.clear()

    selected_recipe = recipes[int(recipe_id)-1]
    for ingredient in selected_recipe["mix_ingredients"]:
        ingredient["amount_added"] = 0
        available_ingredients.append(ingredient)
   
    return render_template('mix_recipe.html', recipe=selected_recipe, available_ingredients=available_ingredients, added_ingredients=added_ingredients)


@app.route('/move_to_added_ingredients', methods=['GET', 'POST'])
def move_to_added_ingredients():
    json_data = request.get_json()   
    recipe_id = json_data["recipe_id"]
    ingredient_id = json_data["ingredient_id"]

    selected_recipe = recipes[int(recipe_id)-1]
    ingredient_to_move = selected_recipe["mix_ingredients"][int(ingredient_id)-1]
    ingredient_to_move["amount_added"] = ingredient_to_move["amount_added"] + 1

    if(ingredient_to_move["amount_added"] == ingredient_to_move["amount"] or ingredient_to_move["amount"] is None):
        available_ingredients.remove(ingredient_to_move)
    if(ingredient_to_move["amount_added"] < 2):
        added_ingredients.insert(0, ingredient_to_move)

    return jsonify(recipe=selected_recipe, available_ingredients=available_ingredients, added_ingredients=added_ingredients)

@app.route('/move_to_available_ingredients', methods=['GET', 'POST'])
def move_to_available_ingredients():
    json_data = request.get_json()
    recipe_id = json_data["recipe_id"]
    ingredient_id = json_data["ingredient_id"]

    selected_recipe = recipes[int(recipe_id)-1]
    ingredient_to_move = selected_recipe["mix_ingredients"][int(ingredient_id)-1]
    ingredient_to_move["amount_added"] = ingredient_to_move["amount_added"] - 1

    if(available_ingredients.count(ingredient_to_move) < 1 or ingredient_to_move["amount"] is None):
        available_ingredients.insert(0, ingredient_to_move)
    if(ingredient_to_move["amount_added"] < 1):
        added_ingredients.remove(ingredient_to_move)

    return jsonify(recipe=selected_recipe, available_ingredients=available_ingredients, added_ingredients=added_ingredients)

@app.route('/<recipe_id>/garnish')
def garnish(recipe_id=None):
    available_garnishes.clear()
    added_garnishes.clear()

    selected_recipe = recipes[int(recipe_id)-1]
    for ingredient in selected_recipe["garnish_ingredients"]:
        ingredient["amount_added"] = 0
        available_garnishes.append(ingredient)

    return render_template('garnish_recipe.html', recipe=selected_recipe, available_ingredients=available_garnishes, added_ingredients=added_garnishes)


@app.route('/<recipe_id>/move_to_added_garnishes', methods=['GET', 'POST'])
def move_to_added_garnishes(recipe_id=None):
    json_data = request.get_json()   
    recipe_id = json_data["recipe_id"]
    ingredient_id = json_data["ingredient_id"]

    selected_recipe = recipes[int(recipe_id)-1]
    ingredient_to_move = selected_recipe["garnish_ingredients"][int(ingredient_id)-1]
    ingredient_to_move["amount_added"] = ingredient_to_move["amount_added"] + 1

    if(ingredient_to_move["amount_added"] == ingredient_to_move["amount"] or ingredient_to_move["amount"] is None):
        available_garnishes.remove(ingredient_to_move)
    if(ingredient_to_move["amount_added"] < 2):
        added_garnishes.insert(0, ingredient_to_move)

    return jsonify(recipe=selected_recipe, available_ingredients=available_garnishes, added_ingredients=added_garnishes)

@app.route('/<recipe_id>/move_to_available_garnishes', methods=['GET', 'POST'])
def move_to_available_garnishes(recipe_id=None):
    json_data = request.get_json()
    recipe_id = json_data["recipe_id"]
    ingredient_id = json_data["ingredient_id"]

    selected_recipe = recipes[int(recipe_id)-1]
    ingredient_to_move = selected_recipe["garnish_ingredients"][int(ingredient_id)-1]
    ingredient_to_move["amount_added"] = ingredient_to_move["amount_added"] - 1

    if(available_ingredients.count(ingredient_to_move) < 1):
        available_garnishes.insert(0, ingredient_to_move)
    if(ingredient_to_move["amount_added"] < 1 or ingredient_to_move["amount"] is None):
        added_garnishes.remove(ingredient_to_move)

    return jsonify(recipe=selected_recipe, available_ingredients=available_garnishes, added_ingredients=added_garnishes)

@app.route('/<recipe_id>/quiz')
def quiz(recipe_id=None):
    random_recipe_id1 = random.randint(1, 21)
    random_recipe_id2 = random.randint(1, 21)

    removed_from_shaker.clear()
    added_to_shaker.clear()

    selected_recipe = recipes[int(recipe_id)-1]
    mix_in_recipe1 = recipes[int(random_recipe_id1)-1]
    mix_in_recipe2 = recipes[int(random_recipe_id2)-1]

    temp_list = []

    for ingredient in selected_recipe["mix_ingredients"]:
        ingredient["amount_added"] = 0
        ingredient["quiz_correct"] = True
        removed_from_shaker.append(ingredient)
        temp_list.append(ingredient["ingredient"])
    for ingredient in mix_in_recipe1["mix_ingredients"]:
        if ingredient["ingredient"] not in temp_list:
            ingredient["amount_added"] = 0
            ingredient["quiz_correct"] = False
            removed_from_shaker.append(ingredient)
    for ingredient in mix_in_recipe2["mix_ingredients"]:
        if ingredient["ingredient"] not in temp_list:
            ingredient["amount_added"] = 0
            ingredient["quiz_correct"] = False
            removed_from_shaker.append(ingredient)

    # print(temp_list)
    shuffle(removed_from_shaker)
    i=1
    for ingredient in removed_from_shaker:
        ingredient["quiz_id"] = i
        i = i + 1

    print(removed_from_shaker)

    return render_template('mix_quiz.html', recipe=selected_recipe, available_ingredients=removed_from_shaker, added_ingredients=added_to_shaker)

@app.route('/<recipe_id>/add_to_shaker', methods=['GET', 'POST'])
def add_to_shaker(recipe_id=None):
    json_data = request.get_json()   
    recipe_id = json_data["recipe_id"]
    ingredient_id = json_data["ingredient_id"] # receives QUIZ ID, not regular ID

    selected_recipe = recipes[int(recipe_id)-1]
    ingredient_to_move = removed_from_shaker[int(ingredient_id)-1]

    if ingredient_to_move["quiz_correct"] is False:
        error_message = "Oops! The recipe for a " + selected_recipe["name"] + " doesn't call for any " + ingredient_to_move["ingredient"].lower() + ". Try again!"
    else:
        ingredient_to_move["amount_added"] = ingredient_to_move["amount_added"] + 1
        error_message = None
        if(ingredient_to_move["amount_added"] == ingredient_to_move["amount"] or ingredient_to_move["amount"] is None):
            removed_from_shaker.remove(ingredient_to_move)
            i=1
            for ingredient in removed_from_shaker:
                ingredient["quiz_id"] = i
                i = i + 1
        if(ingredient_to_move["amount_added"] < 2):
            added_to_shaker.insert(0, ingredient_to_move)

    print(removed_from_shaker)
    print(added_to_shaker)

    return jsonify(error_message=error_message, recipe=selected_recipe, available_ingredients=removed_from_shaker, added_ingredients=added_to_shaker)

@app.route('/<recipe_id>/remove_from_shaker', methods=['GET', 'POST'])
def remove_from_shaker(recipe_id=None):
    json_data = request.get_json()
    recipe_id = json_data["recipe_id"]
    ingredient_id = json_data["ingredient_id"]

    selected_recipe = recipes[int(recipe_id)-1]
    ingredient_to_move = selected_recipe["mix_ingredients"][int(ingredient_id)-1]
    ingredient_to_move["amount_added"] = ingredient_to_move["amount_added"] - 1

    if(removed_from_shaker.count(ingredient_to_move) < 1 or ingredient_to_move["amount"] is None):
        removed_from_shaker.insert(0, ingredient_to_move)
    if(ingredient_to_move["amount_added"] < 1):
        added_to_shaker.remove(ingredient_to_move)

    print(removed_from_shaker)
    print(added_to_shaker)

    return jsonify(recipe=selected_recipe, available_ingredients=removed_from_shaker, added_ingredients=added_to_shaker)

if __name__ == '__main__':
   app.run(debug = True)




