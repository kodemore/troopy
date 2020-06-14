from dataclasses import dataclass
from typing import TypeVar

from troopy import CommandBus, MessageRouter

T = TypeVar("T")

message_router = MessageRouter()


class MyCommandHandler:
    def __call__(self, command: "MyCommand") -> None:
        print(command.message)


@dataclass
class MyCommand:
    message: str


message_router.attach(MyCommand, MyCommandHandler)
command_bus = CommandBus(message_router)
command_bus.dispatch(MyCommand("Hello!"))
