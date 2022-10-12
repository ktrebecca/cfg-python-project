# IMPORT

import requests
import random

# AUTHENTICATION #

app_id = "43bea109"
app_key = "18846472c12cfd691cef02a90701e51d"

# OTHER VARIABLES #
dietary_requirements = [
   "vegetarian",
   "vegan",
   "pescatarian",
   "dairy-free",
   "gluten-free",
   "kosher",
]

# INGREDIENT SEARCH RESPONSE #

ingredient = input("Welcome to our recipe search app! What ingredient do you need to use?")
print("You can choose from the following dietary requirements:")
for dietary_requirement in dietary_requirements:
    index_no = dietary_requirements.index(dietary_requirement)
    print(index_no, dietary_requirement)
chosen_diet_no = input('Do you want to select a dietary requirement? Enter number or "none":')

# GENERATE RESULTS #

# checks what dietary requirements are needed, and adds them to the query string
if chosen_diet_no == 'none':
    recipe_url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}&random=true'.format(ingredient, app_id, app_key)

else:
    # generates the URL: added a '&random=true' to randomise results each time
    chosen_diet_int = int(chosen_diet_no)
    chosen_diet = dietary_requirements[chosen_diet_int]
    print("You have chosen {}.".format(chosen_diet))
    recipe_url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}&health={}&random=true'.format(ingredient, app_id, app_key, chosen_diet)

response = requests.get(recipe_url)
results = response.json()
print(response)

# HITS COUNTER #

hits1 = results['hits']
print("We found {} recipes for your search that use {}. Here are a random 10:".format(results['count'], ingredient))

# LIST RECIPE SEARCH RESULTS #

for recipe in hits1:
    recipe_no = hits1.index(recipe)
    print(recipe_no, recipe['recipe']['label'])

# CHOOSE AND PRINT RECIPE FUNCTION #
def chooserecipe():
    chosen_recipe = input('Which recipe would you like to print? [enter number]: ')
    chosen_recipe_no = int(chosen_recipe)
    recipe_toprint = hits1[chosen_recipe_no]['recipe']
    recipe_toprint_name = recipe_toprint['label']

    recipeprintconfirmation = input("Print recipe for {}? [y/n]:".format(recipe_toprint_name))

    if recipeprintconfirmation == 'n':
        chooserecipe()

    if recipeprintconfirmation == 'y':
        with open('print_recipe_file.txt', 'w+') as text_file:
            text_file.write(hits1[chosen_recipe_no]['recipe']['label'].upper() + '\n' + '\n')
            ingredients_list = hits1[chosen_recipe_no]['recipe']['ingredientLines']
            text_file.write('Ingredients:' + '\n')
            for ingredient in ingredients_list:
                text_file.write(ingredient + '\n')
            text_file.write(
                '\n' + "Link to instructions: " + hits1[chosen_recipe_no]['recipe']['url'] + '\n' + '\n')

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

        cocktail_confirmation = input("Are you happy with this choice? [y/n]:")

        if cocktail_confirmation == 'n':
            randomcocktail()

        if cocktail_confirmation == 'y':
            cocktail_printoption = input("Would you like to add the recipe to your file? [y/n]:")

            if cocktail_printoption == 'n':
                print("Enjoy!")

            if cocktail_printoption == 'y':
                with open('print_recipe_file.txt', 'a') as text_file:
                    text_file.write('\n' + '\n' + hits2[chosen_cocktail]['recipe']['label'].upper() + '\n' + '\n')
                    cocktail_ingredients_list = hits2[chosen_cocktail]['recipe']['ingredientLines']
                    text_file.write('Ingredients:' + '\n')
                    for ingredient in cocktail_ingredients_list:
                        text_file.write(ingredient + '\n')
                    text_file.write('\n' + "Link to instructions: " + hits2[chosen_cocktail]['recipe']['url'] + '\n' + '\n')
                    print('Enjoy your food and cocktail!')
                print("Printing complete.")

    cocktailconfirm()

# RUNS PROGRAMME #

chooserecipe()

cocktail_answer = input("Would you like to randomise a cocktail to go with your meal? [y/n]:")

if cocktail_answer == 'n':
    print("Enjoy your meal!")

if cocktail_answer == 'y':
    randomcocktail()















