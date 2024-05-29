import time

class CoffeeMachineCore:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin):
        self.plugins[name] = plugin

    def list_plugins(self):
        print(f'Available preparations are: ')
        for plugin in self.plugins:
            print(plugin)

    def execute(self, name, **kwargs):
        if name in self.plugins:
            return self.plugins[name].run(self, **kwargs)
        else:
            print(f"No plugin registered under the name: {name}")
            return None

    def power_on(self):
        print("Coffee machine powered on.")
        self.list_plugins()

    def power_off(self):
        print("Coffee machine powered off.")

    #services offered for brewing actual coffee drinks
    def grind_beans(self, grams_of_beans):
        print(f"Grinding {grams_of_beans} beans")

    def heat_water(self, mls_water):
        print(f"Heating {mls_water} [ml] water")

    def brew_coffee(self, delay):
        print(f"Brewing coffee for {delay} [s]")
        time.sleep(delay)

    def heat_milk(self, mls_of_milk, delay):
        print(f"Heating {mls_of_milk} [ml] of milk for {delay} [s]")
        time.sleep(delay)