def make_sandwish(*toppings):
    print("Make this sandwich with sause:")
    for topping in toppings:
        print(topping)

make_sandwish('cheese')
make_sandwish('ketchup','tomato')
make_sandwish('ketchup','cheese','tomato')
