class CommandRegistry:
    _commands = {}

    @classmethod
    def register(cls, name, command_cls):
        cls._commands[name] = command_cls

    @classmethod
    def get(cls, name):
        return cls._commands.get(name)