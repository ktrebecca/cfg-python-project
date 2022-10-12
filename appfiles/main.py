# IMPORT

import requests
import random

# AUTHENTICATION #

app_id = "8ecbd8b2"
app_key = "40ff04984f164671df86c0247637c67b"

# INGREDIENT SEARCH RESPONSE #

ingredient = input("Welcome! What ingredient do you need to use?")
recipe_url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)

response = requests.get(recipe_url)
results = response.json()
print(response)

# HITS COUNTER #

hits = results['hits']
print("We found {} hits for your search that use {}:".format(str(len(hits)), ingredient))

# LIST RECIPE SEARCH RESULTS #

for recipe in hits:
    recipe_no = hits.index(recipe)
    print(recipe_no, recipe['recipe']['label'])

# CHOOSE AND PRINT RECIPE FUNCTION #
def chooserecipe():
    chosen_recipe = input('Which recipe would you like to print? [enter number]: ')
    chosen_recipe_no = int(chosen_recipe)
    recipe_toprint = hits[chosen_recipe_no]['recipe']
    recipe_toprint_name = recipe_toprint['label']

    recipeprintconfirmation = input("Print recipe for {}? [y/n]:".format(recipe_toprint_name))

    if recipeprintconfirmation == 'n':
        chooserecipe()

    if recipeprintconfirmation == 'y':
        with open('print_recipe_file.doc', 'w+') as text_file:
            text_file.write(hits[chosen_recipe_no]['recipe']['label'].upper() + '\n' + '\n')
            ingredients_list = hits[chosen_recipe_no]['recipe']['ingredientLines']
            text_file.write('Ingredients:' + '\n')
            for ingredient in ingredients_list:
                text_file.write(ingredient + '\n')
            text_file.write(
                '\n' + "Link to instructions: " + hits[chosen_recipe_no]['recipe']['url'] + '\n' + '\n')

# RANDOMISE COCKTAIL #

def randomcocktail():
    cocktail_url = 'https://api.edamam.com/api/recipes/v2?type=public&q=cocktail&app_id=8ecbd8b2&app_key=40ff04984f164671df86c0247637c67b&health=alcohol-cocktail&random=true'
    cocktail_response = requests.get(cocktail_url)
    cocktail_results = cocktail_response.json()
    hits2 = cocktail_results['hits']

    cocktail_list = []

    for recipe in hits2:
        cocktail_id = hits2.index(recipe)
        cocktail_list.append(cocktail_id)

    chosen_cocktail = random.choice(cocktail_list)

    print(hits2[chosen_cocktail]['recipe']['label'])
    def cocktailconfirm():

        cocktail_confirmation = input("Are you happy with this choice? [y/n]")

        if cocktail_confirmation == 'n':
            randomcocktail()

        if cocktail_confirmation == 'y':
            cocktail_printoption = input("Would you like to add the recipe to your file?")

            if cocktail_printoption == 'n':
                print("Enjoy!")

            if cocktail_printoption == 'y':
                with open('print_recipe_file.doc', 'a') as text_file:
                    text_file.write('\n' + '\n' + hits2[chosen_cocktail]['recipe']['label'].upper() + '\n' + '\n')
                    cocktail_ingredients_list = hits2[chosen_cocktail]['recipe']['ingredientLines']
                    text_file.write('Ingredients:' + '\n')
                    for ingredient in cocktail_ingredients_list:
                        text_file.write(ingredient + '\n')
                    text_file.write('\n' + "Link to instructions: " + hits2[chosen_cocktail]['recipe']['url'] + '\n' + '\n')
                    print('Enjoy your food and cocktail!')
                print("Printing complete.")

    cocktailconfirm()

chooserecipe() # runs program

cocktail_answer = input("Would you like to randomise a cocktail to go with your meal? [y/n]")

if cocktail_answer == 'n':
    print("Enjoy your meal!")

if cocktail_answer == 'y':
    randomcocktail()















