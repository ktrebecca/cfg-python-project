# IMPORT

import requests

# AUTHENTICATION #

app_id = "8ecbd8b2"
app_key = "40ff04984f164671df86c0247637c67b"

# INGREDIENT SEARCH RESPONSE #

ingredient = input("What ingredient do you need to use?")
recipe_url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)

response = requests.get(recipe_url)
results = response.json()
print(response)

# HITS COUNTER #

hits = results['hits']
print("We found {} hits for your search that use {}:".format(str(len(hits)), ingredient))

# PRINT RECIPE RESULTS #

for recipe in hits:
    recipe_no = hits.index(recipe)
    print(recipe_no, recipe['recipe']['label'])

def chooserecipe():
    chosen_recipe = input('Which recipe would you like to print? [enter number]: ')
    chosen_recipe_no = int(chosen_recipe)
    recipe_toprint = hits[chosen_recipe_no]['recipe']
    recipe_toprint_name = recipe_toprint['label']

    confirmation = input("Print recipe for {}? Confirm y or n:".format(recipe_toprint_name))

    if confirmation == 'n':
        chooserecipe()

    if confirmation == 'y':
        with open('print_recipe_file.doc', 'w+') as text_file:
            text_file.write(hits[chosen_recipe_no]['recipe']['label'].upper() + '\n' + '\n')
            ingredients_list = hits[chosen_recipe_no]['recipe']['ingredientLines']
            text_file.write('Ingredients:' + '\n')
            for ingredient in ingredients_list:
                text_file.write(ingredient + '\n')
            text_file.write(
                '\n' + "Link to instructions: " + hits[chosen_recipe_no]['recipe']['url'] + '\n' + '\n')

# PROGRAM RUN #

chooserecipe()
print("Printing complete. Enjoy!")















