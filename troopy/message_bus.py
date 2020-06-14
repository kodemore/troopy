from inspect import isclass
from typing import Any, Callable, Type, TypeVar, Union

from .message_router import MessageRouter, message_router

T = TypeVar("T")


def handler_default_factory(cls: Type[T]) -> T:
    return cls()


class MessageBus:
    def __init__(self, router: MessageRouter = message_router, handler_factory: Callable = handler_default_factory):
        self.router = router
        self.handler_factory = handler_factory

    def dispatch(self, message: Union[str, Any]) -> Any:
        handler = self.router.find_for(message)

        if isclass(handler):
            handler = self.handler_factory(handler)

        return handler(message)


__all__ = ["MessageBus"]
