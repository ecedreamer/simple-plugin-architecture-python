from lib.processors import initialize_processors
from plugin_core.plugin_interface import PluginInterface


def process_data(processor_class: type, *args, **kwargs):
    if processor_class:
        processor: PluginInterface = processor_class()
        result = processor.run(*args, **kwargs)
        result["status"] = "success"
        return result
    else:
        return {"status": "failure"}


def main() -> None:
    print("Starting main...")
    processors: dict = initialize_processors()
    print(processors)
    processor_name = "first_plugin"
    processor_cls = processors.get(processor_name)
    t1 = process_data(processor_cls)

    print("Processed by first_plugin", t1)
    processor_name = "second_plugin"
    processor_cls = processors.get(processor_name)
    t2 = process_data(processor_cls)
    print("Processed by first_plugin", t2)


if __name__ == '__main__':
    main()
