from Plugins.Plugin import PluginInterface

class EspressoPlugin(PluginInterface):
    def __init__(self):
        self.grams_of_beans = 100
        self.ml_of_water = 100
        self.brew_delay = 5

    def run(self, coffee_machine):
        coffee_machine.grind_beans(self.grams_of_beans)
        coffee_machine.heat_water(self.ml_of_water)
        coffee_machine.brew_coffee(self.brew_delay)
        print(f"Enjoy your Espresso")