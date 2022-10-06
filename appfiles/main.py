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
    print(recipe['recipe']['label'], recipe['recipe']['url'])










