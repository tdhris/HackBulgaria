class CommandParser:
    def __init__(self):
        self.functions = {}

    def on(self, command, function):
        self.functions[command] = function

    def take_command(self, unparsed_command):
        command_parts = unparsed_command.split(" ")
        arguments = command_parts[1:]
        command = command_parts[0]

        if command in self.functions:
            self.functions[command](arguments)
