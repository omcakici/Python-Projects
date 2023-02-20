from menu import Menu, MenuItem
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine
from arts import logo

class Main:
    def __init__(self):
        self.show_menu_obj = Menu()
        self.coffe_maker_obj = CoffeeMaker()
        self.money_machine_obj = MoneyMachine()

    def coffe_making(self, coffe_make, drink):
        if coffe_make.is_resource_sufficient(drink):
            pay_enough = self.money_machine_obj.make_payment(drink.cost)

            if pay_enough:
                coffe_make.make_coffee(drink)
            else:
                self.main_process()

    def main_process(self):
        print(logo)
        
        coffe_type = input(f'​What would you like? ({self.show_menu_obj.get_items()}): ')

        if coffe_type == 'report':
            self.coffe_maker_obj.report()
            if self.money_machine_obj.profit > 0:
                self.money_machine_obj.report()
            self.main_process()

        elif coffe_type == 'off':
            return
        elif self.show_menu_obj.find_drink(coffe_type):
            if coffe_type == 'latte':
                drink = self.show_menu_obj.menu[0]
                self.coffe_making(self.coffe_maker_obj, drink)
                self.main_process()
            elif coffe_type == 'espresso':
                drink = self.show_menu_obj.menu[1]
                self.coffe_making(self.coffe_maker_obj, drink)
                self.main_process()
            else:
                drink = self.show_menu_obj.menu[2]
                self.coffe_making(self.coffe_maker_obj, drink)
                self.main_process()
        else:
            print('Typed wrong input try again later!')
            return        


start = Main()
print(start.main_process())