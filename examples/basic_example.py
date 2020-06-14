from troopy import CommandBus, attach
from troopy.errors import NoHandlerAttachedError
from dataclasses import dataclass


class MyCommandHandler:
    def __call__(self, command: "MyCommand") -> None:
        assert isinstance(command, MyCommand)
        print(command.message)


@attach(MyCommandHandler)
@dataclass
class MyCommand:
    message: str


command_bus = CommandBus()

# will print Hello!
try:
    command_bus.dispatch(MyCommand("Hello!"))
except NoHandlerAttachedError:
    print("No handler")
