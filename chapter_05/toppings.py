requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
    print("Hold the anchovies!")

requested_toppings = ['mushrooms', 'onions', 'pineapple']

if 'pineapple' in requested_toppings:
    print("So, you're a monster?")

if 'anchovies' not in requested_toppings:
    print("Hold the anchovies!")

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

requested_toppings = []
if requested_toppings:
    print("You've selected some toppings.")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives',
                      'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print(f"\nFinished making your pizza.")
