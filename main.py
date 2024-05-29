from Plugins.Espresso import EspressoPlugin
from Plugins.Cappuccino import CappuccinoPlugin
from CoffeeMachineCore import CoffeeMachineCore

if __name__ == "__main__":
    coffee_machine = CoffeeMachineCore()
    coffee_machine.register_plugin("espresso", EspressoPlugin())
    coffee_machine.register_plugin("cappuccino", CappuccinoPlugin())
    coffee_machine.power_on()
    coffee_machine.execute("espresso")
    coffee_machine.execute("cappuccino")
    coffee_machine.power_off()