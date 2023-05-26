import importlib
import inspect
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
                module = importlib.import_module(name=f"plugins.{item.name}.{item.name}", package="plugins")
                for name in dir(module):
                    obj = getattr(module, name)
                    if isinstance(obj, type) and issubclass(obj, PluginInterface) and obj != PluginInterface:
                        self.pluggins[item.name] = obj
