pasta = ("pasta arrabiata","Italian",20,"medium")
biryani = ("Chicken Biryani","Indian",45,"Hard")
print("recipe1 :",pasta)
print("Name:",pasta[0])
print("cusine :",pasta[1])
print("Time:",pasta[2])
print("Difficulty:",pasta[3])

all_recipies = (pasta,biryani)
print("First recipe name:",all_recipies[0][0])
print("Second Recipe time :", all_recipies[1][2])
print("pasta recipe sliced:",pasta[1:3])

print("pasta in detail")
for i in pasta:
    print("-",i)

pasta_ingredients = {"tomato","garlic","olive oil","chilli","pasta","garlic"}
biryani_ingredients = {"rice","chicken","garlic","onion","tomato","spices"}
print("pasta ingredients",pasta_ingredients)
print("biryani ingredients",biryani_ingredients)
print("length of pasta ingredients",len(pasta_ingredients))

pasta_ingredients.add('parmesan')
pasta_ingredients.discard('chilli')
print("updated pasta ingredients",pasta_ingredients)

all_ingredients = print(pasta_ingredients.union(biryani_ingredients))
common = print(pasta_ingredients.intersection(biryani_ingredients))
only_pasta = print(pasta_ingredients.difference(biryani_ingredients))
unique = print(pasta_ingredients.symmetric_difference(biryani_ingredients))


