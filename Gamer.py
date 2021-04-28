class Gamer:
    def __init__(self, command):
        self.__command = command

    def execute(self):
        self.__command.execute()