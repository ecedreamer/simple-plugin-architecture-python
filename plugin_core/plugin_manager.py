import importlib
import json
from pathlib import Path

from plugin_core.plugin_interface import PluginInterface


class PluginManager:
    pluggins = {}

    def load_plugins(self):
        print("Loading plugins...")
        self.discover_plugins()
        return self.pluggins

    def discover_plugins(self):
        plugin_folder = Path('plugins')
        for item in plugin_folder.iterdir():

            if item.is_dir() and not item.name.startswith(("_", ".")):
                with open(f"{item}/config.json") as file:
                    config = json.load(file)
                    plugin_main_module = config.get("plugin_main_module").split(".")[0]
                module = importlib.import_module(name=f"plugins.{item.name}.{plugin_main_module}", package="plugins")
                for name in dir(module):
                    obj = getattr(module, name)
                    if isinstance(obj, type) and issubclass(obj, PluginInterface) and obj != PluginInterface:
                        self.pluggins[item.name] = obj
