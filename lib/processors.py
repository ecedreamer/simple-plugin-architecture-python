from typing import Dict

from plugin_core.plugin_interface import PluginInterface
from plugin_core.plugin_manager import PluginManager


def initialize_processors() -> Dict[str, PluginInterface]:
    manager = PluginManager()
    return manager.load_plugins()
