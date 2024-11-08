from host import hookimpl

class GreetPlugin:
    @hookimpl
    def add_command(self, subparsers):
        parser = subparsers.add_parser("nam", help="Greet the user")
        parser.add_argument("name", help="Name of the user")
        parser.set_defaults(func=self.greet_command)

    def greet_command(self, args):
        print(f"Namaste, {args.name}!")

nam_plugin = GreetPlugin()