from troopy import CommandBus, attach
from troopy.errors import NoHandlerAttachedError
from dataclasses import dataclass


def my_command_handler(command: "MyCommand") -> None:
    print(command.message)


@attach(my_command_handler)
@dataclass
class MyCommand:
    message: str


command_bus = CommandBus()

# will print Hello!
try:
    command_bus.dispatch(MyCommand("Hello!"))
except NoHandlerAttachedError:
    print("No handler")
