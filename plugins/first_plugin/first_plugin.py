from plugin_core.plugin_interface import PluginInterface


class FirstPlugin(PluginInterface):
    def run(self, *args, **kwargs):
        print("Running first plugin")
        return {"processed_by": "first plugin"}
