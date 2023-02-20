
class Main:
    def _init_(self, show_menu_obj, make_cofe_obj):
        self.show_menu_obj = show_menu_obj
        self.make_cofe_obj = make_cofe_obj

    def coffe_making(self, coffe_make, drink):
        if coffe_make.is_resource_sufficient(drink):
            coffe_make.make_coffee(drink)

    def main_process(self):
        print(logo)
        
        coffe_type = input(f'​What would you like? ({self.show_menu_obj.get_items()}): ')

        if self.show_menu_obj.find_drink(coffe_type):
            if coffe_type == 'latte':
                drink = self.show_menu_obj.menu[0]
                self.coffe_making(self.make_cofe_obj, drink)
                self.main_process()
            elif coffe_type == 'espresso':
                drink = self.show_menu_obj.menu[1]
                self.coffe_making(self.make_cofe_obj, drink)
                self.main_process()
            else:
                drink = self.show_menu_obj.menu[2]
                self.coffe_making(self.make_cofe_obj, drink)
                self.main_process()
        elif coffe_type == 'report':
            coffe_type.report()
            self.main_process()



menu_obj = Menu()
coffe_maker_obj = CoffeeMaker()
start = Main(menu_obj, coffe_maker_obj)
print(start.main_process())