from plugin_core.plugin_interface import PluginInterface


class FirstPlugin(PluginInterface):
    def run(self):
        print("Running second plugin")
        return {"processed_by": "second plugin"}
