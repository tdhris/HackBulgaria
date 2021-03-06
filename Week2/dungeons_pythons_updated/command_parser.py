class CommandParser:
    def __init__(self):
        self.functions = {}

    def add_function(self, command, function):
        self.functions[command] = function

    def take_command(self, unparsed_command):
        unparsed_command = unparsed_command.split()
        command = unparsed_command[0]
        arguments = unparsed_command[1:]
        if command in self.functions:
            return self.functions[command](arguments)
