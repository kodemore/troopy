from dataclasses import dataclass
from typing import List, Type, TypeVar

from troopy import CommandBus, command

T = TypeVar("T")

message_log = []


def command_handler_factory(handler: Type[T]) -> T:
    return handler(message_log)


class MyCommandHandler:
    def __init__(self, message_log: List):
        self.log = message_log

    def __call__(self, command: "MyCommand") -> None:
        self.log.append(command.message)


@command(MyCommandHandler)
@dataclass
class MyCommand:
    message: str


command_bus = CommandBus(handler_factory=command_handler_factory)

command_bus.dispatch(MyCommand("Hello!"))


