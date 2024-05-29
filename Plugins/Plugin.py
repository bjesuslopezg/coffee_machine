class PluginInterface:
    def run(self, coffee_machine, **kwargs):
        raise NotImplementedError("Plugins must implement the run method.")