import argparse
import pluggy
from pluggy import HookimplMarker
from pluggy import HookspecMarker



hookspec = HookspecMarker("example")
hookimpl = HookimplMarker("example")

class ExampleSpec:
    @hookspec
    def add_command(subparsers):
        """Add a command to the host parser"""

# Create a plugin manager and register hook specifications

plugin_manager = pluggy.PluginManager("example")

plugin_manager.add_hookspecs(ExampleSpec)

# Load plugins
def load_plugins():
    plugin_manager.load_setuptools_entrypoints("example.plugins")

def main():
    parser = argparse.ArgumentParser(description="Example host program")
    subparsers = parser.add_subparsers(dest="command")

    load_plugins()
    plugin_manager.hook.add_command(subparsers=subparsers)

    args = parser.parse_args()

    if args.command:
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
