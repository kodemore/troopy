from dataclasses import dataclass
from typing import List, Type, TypeVar

from troopy import CommandBus, attach

T = TypeVar("T")

message_log = []


def command_handler_factory(handler: Type[T]) -> T:
    return handler(message_log)


class MyCommandHandler:
    def __init__(self, log: List):
        self.log = log

    def __call__(self, command: "MyCommand") -> None:
        self.log.append(command.message)


@attach(MyCommandHandler)
@dataclass
class MyCommand:
    message: str


command_bus = CommandBus(handler_factory=command_handler_factory)
command_bus.dispatch(MyCommand("Hello!"))

print(message_log)

