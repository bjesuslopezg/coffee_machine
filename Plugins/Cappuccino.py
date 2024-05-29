from Plugins.Plugin import PluginInterface

class CappuccinoPlugin(PluginInterface):
    def __init__(self):
        self.grams_of_beans = 200
        self.ml_of_water = 300
        self.ml_of_milk = 200
        self.brew_delay = 2
        self.heat_milk_delay = 4


    def run(self, coffee_machine):
        coffee_machine.grind_beans(self.grams_of_beans)
        coffee_machine.heat_water(self.ml_of_water)
        coffee_machine.heat_milk(self.ml_of_milk, self.heat_milk_delay)
        coffee_machine.brew_coffee(self.brew_delay)
        print(f"Enjoy your Cappuccino")