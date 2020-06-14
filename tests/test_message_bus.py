from typing import Callable, List, Type

import pytest

from troopy import CommandBus, MessageRouter
from troopy.errors import NoHandlerAttachedError


def test_dispatch_for_missing_handler() -> None:
    class TestMessage:
        message: str

        def __init__(self, message):
            self.message = message

    command_bus = CommandBus()

    with pytest.raises(NoHandlerAttachedError):
        command_bus.dispatch(TestMessage(message="Hello"))


def test_dispatch_for_function() -> None:
    class TestMessage:
        message: str

        def __init__(self, message):
            self.message = message

    dispatched = []
    message_router = MessageRouter()

    def message_handler(message: TestMessage) -> None:
        dispatched.append(message)

    message_router.attach(TestMessage, message_handler)
    command_bus = CommandBus(message_router)

    command_bus.dispatch(TestMessage("Hello"))
    assert dispatched


def test_dispatch_for_handler_class() -> None:
    class TestMessage:
        message: str

        def __init__(self, message):
            self.message = message

    dispatched = []
    message_router = MessageRouter()

    class TestMessageHandler:
        def __call__(self, message: TestMessage):
            dispatched.append(message)

    message_router.attach(TestMessage, TestMessageHandler)
    command_bus = CommandBus(message_router)

    command_bus.dispatch(TestMessage("Hello"))
    assert dispatched


def test_dispatch_for_handler_class_with_custom_factory() -> None:
    class TestMessage:
        message: str

        def __init__(self, message):
            self.message = message

    dispatched = []
    message_router = MessageRouter()

    class TestMessageHandler:
        def __init__(self, log: List):
            self.log = log

        def __call__(self, message: TestMessage):
            self.log.append(message)

    def handler_factory(handler: Type) -> Callable:
        return handler(dispatched)

    message_router.attach(TestMessage, TestMessageHandler)
    command_bus = CommandBus(message_router, handler_factory)

    command_bus.dispatch(TestMessage("Hello"))
    assert dispatched
