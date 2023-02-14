MENU = {
    'espresso' :{
        "water": 50,
        "cost": 1.5,
        "coffe_amount": 18
    },
    'latte' :{
        "water": 200,
        "cost": 2.5,
        "coffe_amount": 24,
        "milk": 150
    },
    'cappuccino' :{
        "water": 250,
        "cost": 3,
        "coffe_amount": 24,
        "milk": 100
    },
}

RESOURCES = {
    'water': 300,
    'milk': 200,
    'coffe_amount': 100
}

is_profit = False

def check_resource(coffe_type):
    coffe = MENU[coffe_type]
    for res in coffe:
        if res != 'cost':
            if RESOURCES[res] < coffe[res]:
                return res
    
    for res in coffe:
        if res != 'cost':
            if RESOURCES[res] >= coffe[res]:
                RESOURCES[res] -= coffe[res]

    return ''

def print_resources():
    for res in RESOURCES:
        if res == 'Money: $':
            print(f"{res}{RESOURCES[res]}")
        else:
            print(f"{res}: {RESOURCES[res]}")
    game()

def check_is_enough_payment(total_payment, coffe_type):
    if total_payment < MENU[coffe_type]["cost"]:
        return False
    else:
        return True

def game():
    coffe_type = input('​What would you like? (espresso/latte/cappuccino): ')
    if coffe_type == 'report':
        return print_resources()
    if coffe_type == 'off':
        return

    if coffe_type == 'espresso' or coffe_type == 'latte' or coffe_type == 'cappuccino':
        
        res = check_resource(coffe_type)

        if res == '':
            print('Please insert coins.')
            # COINS
            # Quarter: 25Cent, Dime: 10Cent, Nickel: 5Cent, Penny: 1cent
            quarter = float(input('How many quarters?: '))
            dimes = float(input('How many dimes?: '))
            nickles = float(input('How many nickes?: '))
            pennies = float(input('How many pennies?: '))

            total_payment = (0.25*quarter) + (0.10*dimes) + (0.05*nickles) + (0.01* pennies)
            coffe_cost =  MENU[coffe_type]['cost']
            if check_is_enough_payment(total_payment, coffe_type):
                global is_profit
                if is_profit == False:
                    RESOURCES['Money: $'] = 0
                is_profit = True
                money_chage = round(total_payment -coffe_cost,2)
                print(f'Here is {money_chage}$ in change.')
                print(f'Here is your {coffe_type}.Enjoy!')
                if is_profit:
                    RESOURCES['Money: $'] += coffe_cost
                
                game()
            else:
                print('Sorry that is not enough money. Money refunded.')
                game()
        else:
            print(f"Sorry there is not enough {res}")
            game()
    else:
        print('Try typing one of the three coffe types or two other instructions!!')
        return

game()











