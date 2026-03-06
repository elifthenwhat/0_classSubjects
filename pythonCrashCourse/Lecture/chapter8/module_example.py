# This file is used in conjuction with test_example.py (This is the module file)

def make_pizza(size, *toppings):
    # Summarize the pizza we are about to make.
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")