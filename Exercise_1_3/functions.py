## function with no output / return
def bake():
    print("Baking with no output")

bake()

def bake_cookies(ingredients):
    for i in ingredients:
        print("adding %s to the bowl"% i)

bake_cookies(['eggs','butter'])


def bake_recipe(name, ingredients,cooking_time = 30):
    print("making %s takes %d minutes" % (name, cooking_time))
    for i in ingredients:
        print("adding %s to the bowl"% i)

bake_recipe(ingredients=['eggs','butter','sugar'],cooking_time=45,name="chocolate chip")

# variable length args don't knopw how many user cgives
def display_items(*items):
    for i in items:
        print(i)

display_items("python",'Javascript')

def path_ther(a, b):
    c_sqruare = int(a) ** 2 + int(b) **2
    print("c^2",c_sqruare)
    return c_sqruare ** .5

print(path_ther(4, 5))
print(path_ther(4,7))