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
        "media": "https://s3.amazonaws.com/commonwealthcocktailsimages/whiskey_sour.png", 
        "glass": "lowball", 
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, # 2 cups
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Bourbon",
                "amount": 2, # 2 oz
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Lemon juice",
                "amount": 3, # 3 x (1/4 oz)
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Simple syrup",
                "amount": 3, # 3 x (/4 oz)
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Orange",
                "amount": 1, # 1 x (1/2 wheel)
                "unit": " half wheel",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Maraschino cherry",
                "amount": 1, # 1 cherry
                "unit": "",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 2,
        "name": "Margarita",
        "media": "https://www.patrontequila.com/binaries/largeretina/content/gallery/patrontequila/recipes/roca-patron-reposado/tommys-margarita/tommy-marg.jpg", 
        "glass": "lowball",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Silver tequila",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Cointreau",
                "amount": 1, 
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Lime juice",
                "amount": 1, 
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Salt",
                "amount": None,
                "unit": " around glass rim",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Ice",
                "amount": None,
                "unit": " pour mixed ingredients over",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Lemon",
                "amount": 1,
                "unit": " wheel",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 3,
        "name": "Cosmopolitan",
        "media": "https://i.pinimg.com/originals/7d/54/74/7d547450ee5fdcd471922b1c5d37203e.jpg", 
        "glass": "martini",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Citrus vodka",
                "amount": 3, 
                "unit": "/2 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Cointreau",
                "amount": 1, 
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Lime juice",
                "amount": 1, 
                "unit": "/2 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 5,
                "ingredient": "Cranberry juice",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Lime",
                "amount": 1,
                "unit": " wheel",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 4,
        "name": "Mojito",
        "media": "https://assets.bonappetit.com/photos/57acc0be1b33404414975167/master/pass/mojito.jpg", 
        "glass": "highball",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Muddled mint",
                "amount": 3, 
                "unit": " leaves",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cups",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "White rum",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Lime juice",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 5,
                "ingredient": "Simple syrup",
                "amount": 1, 
                "unit": "/2 oz",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Mint",
                "amount": None,
                "unit": "",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 5,
        "name": "Gimlet",
        "media": "https://www.titosvodka.com/uploads/Recipes/Cocktails-White-Background/_auto1000/Titos-Vodka-Gimlet-W.jpg", 
        "glass": "martini",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Gin",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Simple syrup",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Lime juice",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Lime",
                "amount": 1,
                "unit": " wheel",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 6,
        "name": "Sidecar",
        "media": "https://i.pinimg.com/600x315/84/cb/c9/84cbc9ceaf87ac9a17d4020cb7cfaca0.jpg", 
        "glass": "martini",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "VS or VSOP cognac",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Cointreau",
                "amount": 1, 
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Lemon juice",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Sugar",
                "amount": None,
                "unit": " around glass rim",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 7,
        "name": "French 75",
        "media": "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2011/11/15/0/FNM_120111-Centerfold-002_s4x3.jpg.rend.hgtvcom.616.462.suffix/1371600652446.jpeg", 
        "glass": "martini",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Gin",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Simple syrup",
                "amount": 2,
                "unit": " dash",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Lemon juice",
                "amount": 1,
                "unit": "/2 oz",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Champagne",
                "amount": None,
                "unit": " to glass fill",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Lemon",
                "amount": 1,
                "unit": " wheel",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 8,
        "name": "Daiquiri",
        "media": "https://www.my-vb.com/sites/default/files/styles/image_recette/public/ebiz/Daiquiri%20Gimlet.jpg?itok=q90SMAsa", 
        "glass": "martini",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Light rum",
                "amount": 2,
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Lime juice",
                "amount": 1,
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Lime",
                "amount": 1,
                "unit": " wheel",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 9,
        "name": "Espresso Martini",
        "media": "https://shake-that.com/wp-content/uploads/2015/07/Espresso-martini.jpg", 
        "glass": "martini",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Vodka",
                "amount": 1,
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Coffe liqueur",
                "amount": 1,
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Freshly brewed espresso",
                "amount": 1,
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 5,
                "ingredient": "Simple syrup",
                "amount": 1,
                "unit": " teaspoon",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Espresso beans",
                "amount": None,
                "unit": "",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 10,
        "name": "Negroni",
        "media": "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2017/1/18/4/FNM030117_Classic-Negroni_s4x3.jpg.rend.hgtvcom.616.462.suffix/1484859730499.jpeg", 
        "glass": "lowball",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "London dry gin",
                "amount": 1,
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Campari",
                "amount": 1,
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Vermouth rosso",
                "amount": 1,
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Orange",
                "amount": 1,
                "unit": " twist",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 11,
        "name": "Bloody Mary",
        "media": "https://www.monin.com/us/media/catalog/product/cache/9a4060007a6b38763b086819271c5c8a/H/o/Hot_Caribbean_Bloody_Mary-1534124666-0.png", 
        "glass": "highball",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Vodka",
                "amount": 2,
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Tomato juice",
                "amount": 1,
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Lemon juice",
                "amount": 1,
                "unit": " tablespoon",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 5,
                "ingredient": "Lime juice",
                "amount": 3,
                "unit": "/2 teaspoon",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 6,
                "ingredient": "Worcestershire sauce",
                "amount": 3,
                "unit": "/4 teaspoon",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 7,
                "ingredient": "Horseradish",
                "amount": 1,
                "unit": "/2 teaspoon",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 8,
                "ingredient": "Pepper",
                "amount": 1,
                "unit": "/8 teaspoon",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 9,
                "ingredient": "Celery salt",
                "amount": 1,
                "unit": "/8 teaspoon",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 10,
                "ingredient": "Hot pepper sauce",
                "amount": 1,
                "unit": "/8 teaspoon",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Celery",
                "amount": 1,
                "unit": " stalk",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Cucumber",
                "amount": 1,
                "unit": " wheel",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 12,
        "name": "Mai Tai",
        "media": "https://us.inshaker.com/uploads/cocktail/promo/552/1542205346-Golden-Mai-Tai-_promo.jpg", 
        "glass": "lowball",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Light rum",
                "amount": 2,
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Triple sec",
                "amount": 3,
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Lemon juice",
                "amount": 1,
                "unit": "/2 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 5,
                "ingredient": "Lime juice",
                "amount": 1,
                "unit": " teaspoon",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 6,
                "ingredient": "Amaretto",
                "amount": 1,
                "unit": " teaspoon",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Lime",
                "amount": 1,
                "unit": " half wheel",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Mint",
                "amount": None,
                "unit": " leaves",
                "amount_added": 0,
                "media": "",
            }
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 13,
        "name": "Gin fizz",
        "media": "https://s3.amazonaws.com/commonwealthcocktailsimages/uGledHgmIVXDY4DB_d-rAA==-Ramos-Gin-Fizz-IBA-commonwealth-cocktails.png", 
        "glass": "highball",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Gin",
                "amount": 3, 
                "unit": "/2 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Lemon juice",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Caster sugar",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Soda",
                "amount": 4,
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Lemon",
                "amount": 1,
                "unit": " half wheel",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Mint",
                "amount": None,
                "unit": " leaves",
                "amount_added": 0,
                "media": "",
            }
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 14,
        "name": "Planters' Punch",
        "media": "http://shake-that.com/wp-content/uploads/2015/07/Planters-Punch-780x780.png", 
        "glass": "highball",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Simple syrup",
                "amount": 1, 
                "unit": "/2 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Lemon juice",
                "amount": 5, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Jamaican",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 5,
                "ingredient": "Angostura bitters",
                "amount": None, 
                "unit": " a few dashes",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Soda",
                "amount": None,
                "unit": " to glass fill",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Cherries",
                "amount": None, 
                "unit": "",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Orange",
                "amount": 1,
                "unit": " wheel",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },

    {
        "id": 15,
        "name": "Singapore Sling",
        "media": "https://www.kitchengeekery.com/images/uploads/cocktails/_watermark/singapore-sling.jpg", 
        "glass": "highball",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Gin",
                "amount": 3, 
                "unit": "/2 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Cherry brandy",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Simple syrup",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 5,
                "ingredient": "Lime juice",
                "amount": 1, 
                "unit": "oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 6,
                "ingredient": "Angostura bitters",
                "amount": None, 
                "unit": " dash",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Soda",
                "amount": None,
                "unit": " to glass fill",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Cherries",
                "amount": None, 
                "unit": "",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Orange",
                "amount": 1,
                "unit": " wheel",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 16,
        "name": "Kamikaze",
        "media": "https://www.cocktail-db.com/stat/img/640/Kamikaze.jpg", 
        "glass": "martini",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Vodka",
                "amount": 1, 
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Triple Sec",
                "amount": 1, 
                "unit": "/2 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Lime juice",
                "amount": 1, 
                "unit": "/2 oz",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Lime",
                "amount": 1,
                "unit": " wedge",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 17,
        "name": "Lemon-Tini",
        "media": "https://fbworld.com/wp-content/uploads/2015/06/Chili-Lemontini.jpg", 
        "glass": "martini",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Lemon vodka",
                "amount": 3, 
                "unit": "/2 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Lemoncello",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Lemon juice",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 5,
                "ingredient": "Simple syrup",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Lemon twist",
                "amount": 1,
                "unit": "",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 18,
        "name": "Aviation",
        "media": "https://www.diageobaracademy.com/uploads/photos/cc7c3e436af3079a48e3703e01cfcae1.jpg", 
        "glass": "martini",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Gin",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Maraschino liqueur",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Crème de violette",
                "amount": 1, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 5,
                "ingredient": "Lemon juice",
                "amount": 1, 
                "unit": "/2 oz",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Flamed lemon peel",
                "amount": 1,
                "unit": "",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 19,
        "name": "White Lady",
        "media": "https://shake-that.com/wp-content/uploads/2015/07/White-Lady.jpg", 
        "glass": "martini",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Gin",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Orange liqueur",
                "amount": 1, 
                "unit": "/2 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Lemon juice",
                "amount": 1, 
                "unit": "/2 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 5,
                "ingredient": "Egg white",
                "amount": 1, 
                "unit": "",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Orange",
                "amount": 1,
                "unit": " peel",
                "amount_added": 0,
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 20,
        "name": "Bee's Knees",
        "media": "https://www.agalima.com/wp-content/uploads/sites/6/2018/02/BeesKnees_430.png", 
        "glass": "martini",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Gin",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Lemon juice",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Honey syrup",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Lemon",
                "amount": 0,
                "unit": " peel",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
    {
        "id": 21,
        "name": "Blue Hawaii",
        "media": "https://kinkybeverages.com/wp-content/uploads/2018/04/Recipe-Aloha-BlueHawaiian.jpg", 
        "glass": "highball",
        "mix_ingredients": [
            {
                "id": 1,
                "ingredient": "Ice",
                "amount": 2, 
                "unit": " cup",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Vodka",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Light rum",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 4,
                "ingredient": "Blue curaçao",
                "amount": 1, 
                "unit": "/2 oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 5,
                "ingredient": "Pineapple juice",
                "amount": 2, 
                "unit": " oz",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 6,
                "ingredient": "Cream of coconut",
                "amount": 3, 
                "unit": "/4 oz",
                "amount_added": 0,
                "media": "",
            },
        ],
        "garnish_ingredients": [
            {
                "id": 1,
                "ingredient": "Pineapple",
                "amount": 1,
                "unit": " wedge",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 2,
                "ingredient": "Maraschino cherry",
                "amount": 1, 
                "unit": "",
                "amount_added": 0,
                "media": "",
            },
            {
                "id": 3,
                "ingredient": "Cocktail umbrella",
                "amount": 1, 
                "unit": "",
                "amount_added": 0,
                "media": "",
            },
        ],
        "progress": 0,
        "until_complete": 0,
    },
]

available_ingredients = []
added_ingredients = []

available_garnishes = []
added_garnishes = []

removed_from_shaker = []
added_to_shaker = []

removed_from_glass = []
added_to_glass = []

@app.route('/recipe_list/<search_string>')
def search_recipes(search_string=None):
    matching_recipes = []
    for recipe in recipes:
        if search_string.lower() in recipe["name"].lower():
            matching_recipes.append(recipe)
        else:
            for ingredient in recipe["mix_ingredients"]:
                if search_string.lower() in ingredient["ingredient"].lower():
                    matching_recipes.append(recipe)
            if recipe not in matching_recipes:
                for ingredient in recipe["garnish_ingredients"]:
                    if search_string.lower() in ingredient["ingredient"].lower():
                        matching_recipes.append(recipe)

    return render_template('recipe_list.html', recipes=matching_recipes, search_string=search_string)

@app.route('/recipe_list')
def display_recipes():

    search_string = None
    return render_template('recipe_list.html', recipes=recipes, search_string=search_string)

@app.route('/<int:recipe_id>')
def recipe(recipe_id=None):
    available_ingredients.clear()
    added_ingredients.clear()

    selected_recipe = recipes[recipe_id-1]
    for ingredient in selected_recipe["mix_ingredients"]:
        ingredient["amount_added"] = 0
        available_ingredients.append(ingredient)

    print(available_ingredients)
    print(added_ingredients)
   
    return render_template('mix_recipe.html', recipe=selected_recipe, available_ingredients=available_ingredients, added_ingredients=added_ingredients)


@app.route('/move_to_added_ingredients', methods=['GET', 'POST'])
def move_to_added_ingredients():
    print(available_ingredients)
    print(added_ingredients)

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

    print(available_ingredients)
    print(added_ingredients)

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

@app.route('/<int:recipe_id>/garnish')
def garnish(recipe_id=None):
    available_garnishes.clear()
    added_garnishes.clear()

    selected_recipe = recipes[recipe_id-1]
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

@app.route('/<int:recipe_id>/quiz_mix')
def quiz_recipe(recipe_id=None):
    random_recipe_id1 = random.randint(1, 21)
    random_recipe_id2 = random.randint(1, 21)

    removed_from_shaker.clear()
    added_to_shaker.clear()

    selected_recipe = recipes[recipe_id-1]
    selected_recipe["progress"] = 0
    counter=0
    for ingredient in selected_recipe["mix_ingredients"]:
        try:
            counter=counter+ingredient["amount"]
        except: 
            counter = counter + 1
    selected_recipe["until_complete"]=counter

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

    shuffle(removed_from_shaker)
    i=1
    for ingredient in removed_from_shaker:
        ingredient["quiz_id"] = i
        i = i + 1

    return render_template('mix_quiz.html', recipe=selected_recipe, available_ingredients=removed_from_shaker, added_ingredients=added_to_shaker)

@app.route('/<recipe_id>/add_to_shaker', methods=['GET', 'POST'])
def add_to_shaker(recipe_id=None):
    json_data = request.get_json()   
    recipe_id = json_data["recipe_id"]
    ingredient_id = json_data["ingredient_id"] # receives QUIZ ID, not regular ID

    selected_recipe = recipes[int(recipe_id)-1]
    for ingredient in removed_from_shaker:
        if ingredient["quiz_id"] == int(ingredient_id):
            ingredient_to_move = ingredient

    ingredient_to_move["amount_added"] = ingredient_to_move["amount_added"] + 1
    if ingredient_to_move["quiz_correct"]:
        selected_recipe["progress"] = str(int(selected_recipe["progress"]) + 1)
        if ingredient_to_move["amount_added"] == ingredient_to_move["amount"] or ingredient_to_move["amount"] is None:
            removed_from_shaker.remove(ingredient_to_move)
        if(ingredient_to_move["amount_added"] == 1):
            added_to_shaker.insert(0, ingredient_to_move)
    
    else:
        removed_from_shaker.remove(ingredient_to_move)
        added_to_shaker.insert(0, ingredient_to_move)

    return jsonify(recipe=selected_recipe, available_ingredients=removed_from_shaker, added_ingredients=added_to_shaker)

@app.route('/<recipe_id>/remove_from_shaker', methods=['GET', 'POST'])
def remove_from_shaker(recipe_id=None):
    json_data = request.get_json()
    recipe_id = json_data["recipe_id"]
    ingredient_id = json_data["ingredient_id"]

    selected_recipe = recipes[int(recipe_id)-1]
    for ingredient in added_to_shaker:
        if ingredient["quiz_id"] == int(ingredient_id):
            ingredient_to_move = ingredient
    
    ingredient_to_move["amount_added"] = ingredient_to_move["amount_added"] - 1
    if ingredient_to_move["quiz_correct"]:
        selected_recipe["progress"] = str(int(selected_recipe["progress"]) - 1)
        if ingredient_to_move["amount_added"] == 0:
            added_to_shaker.remove(ingredient_to_move)
        if (ingredient_to_move["amount_added"]+1) == ingredient_to_move["amount"]:
            removed_from_shaker.insert(0, ingredient_to_move)
    
    else:
        added_to_shaker.remove(ingredient_to_move)
        removed_from_shaker.insert(0, ingredient_to_move)

    return jsonify(recipe=selected_recipe, available_ingredients=removed_from_shaker, added_ingredients=added_to_shaker)

@app.route('/<int:recipe_id>/quiz_garnish')
def quiz_garnish(recipe_id=None):
    random_recipe_id1 = random.randint(1, 21)
    random_recipe_id2 = random.randint(1, 21)

    removed_from_glass.clear()
    added_to_glass.clear()

    selected_recipe = recipes[recipe_id-1]
    selected_recipe["progress"]=0
    counter=0
    for ingredient in selected_recipe["garnish_ingredients"]:
        try:
            counter=counter+ingredient["amount"]
        except: 
            counter = counter + 1
    selected_recipe["until_complete"]=counter
    selected_recipe["progress"]=0

    mix_in_recipe1 = recipes[int(random_recipe_id1)-1]
    mix_in_recipe2 = recipes[int(random_recipe_id2)-1]

    temp_list = []

    for ingredient in selected_recipe["garnish_ingredients"]:
        ingredient["amount_added"] = 0
        ingredient["quiz_correct"] = True
        removed_from_glass.append(ingredient)
        temp_list.append(ingredient["ingredient"])
    for ingredient in mix_in_recipe1["garnish_ingredients"]:
        if ingredient["ingredient"] not in temp_list:
            ingredient["amount_added"] = 0
            ingredient["quiz_correct"] = False
            removed_from_glass.append(ingredient)
    for ingredient in mix_in_recipe2["garnish_ingredients"]:
        if ingredient["ingredient"] not in temp_list:
            ingredient["amount_added"] = 0
            ingredient["quiz_correct"] = False
            removed_from_glass.append(ingredient)

    # print(temp_list)
    shuffle(removed_from_glass)
    i=1
    for ingredient in removed_from_glass:
        ingredient["quiz_id"] = i
        i = i + 1

    return render_template('garnish_quiz.html', recipe=selected_recipe, available_ingredients=removed_from_glass, added_ingredients=added_to_glass)

@app.route('/<recipe_id>/add_to_glass', methods=['GET', 'POST'])
def add_to_glass(recipe_id=None):
    json_data = request.get_json()   
    recipe_id = json_data["recipe_id"]
    ingredient_id = json_data["ingredient_id"] # receives QUIZ ID, not regular ID

    selected_recipe = recipes[int(recipe_id)-1]
    for ingredient in removed_from_glass:
        if ingredient["quiz_id"] == int(ingredient_id):
            ingredient_to_move = ingredient

    ingredient_to_move["amount_added"] = ingredient_to_move["amount_added"] + 1
    if ingredient_to_move["quiz_correct"]:
        selected_recipe["progress"] = str(int(selected_recipe["progress"]) + 1)
        if ingredient_to_move["amount_added"] == ingredient_to_move["amount"] or ingredient_to_move["amount"] is None:
            removed_from_glass.remove(ingredient_to_move)
        if ingredient_to_move["amount_added"] == 1:
            added_to_glass.insert(0, ingredient_to_move)

    else:
        removed_from_glass.remove(ingredient_to_move)
        added_to_glass.insert(0, ingredient_to_move)

    return jsonify(recipe=selected_recipe, available_ingredients=removed_from_glass, added_ingredients=added_to_glass)

@app.route('/<recipe_id>/remove_from_glass', methods=['GET', 'POST'])
def remove_from_glass(recipe_id=None):
    json_data = request.get_json()   
    recipe_id = json_data["recipe_id"]
    ingredient_id = json_data["ingredient_id"] # receives QUIZ ID, not regular ID

    selected_recipe = recipes[int(recipe_id)-1]
    for ingredient in added_to_glass:
        if ingredient["quiz_id"] == int(ingredient_id):
            ingredient_to_move = ingredient

    ingredient_to_move["amount_added"] = ingredient_to_move["amount_added"] - 1
    if ingredient_to_move["quiz_correct"]:
        selected_recipe["progress"] = str(int(selected_recipe["progress"]) - 1)
        if ingredient_to_move["amount_added"] == 0:
            added_to_glass.remove(ingredient_to_move)
        if (ingredient_to_move["amount_added"]+1) == ingredient_to_move["amount"] or ingredient_to_move["amount"] is None:
            removed_from_glass.insert(0, ingredient_to_move)

    else:
        added_to_glass.remove(ingredient_to_move)
        removed_from_glass.insert(0, ingredient_to_move)

    return jsonify(recipe=selected_recipe, available_ingredients=removed_from_glass, added_ingredients=added_to_glass)

if __name__ == '__main__':
   app.run(debug = True)




