from inspect import isclass
from typing import Any, Callable, Dict, Type, TypeVar

from .errors import HandlerAlreadyAttachedError, NoHandlerAttachedError

T = TypeVar("T")


class MessageRouter:
    def __init__(self):
        self.routes: Dict[Any, Callable] = {}

    def attach(self, message: Any, handler: Callable) -> None:
        if message in self.routes:
            raise HandlerAlreadyAttachedError(f"Only one handler can be attached to message {message}")
        self.routes[message] = handler

    def find_for(self, message: Any) -> Callable:
        if message.__class__ not in self.routes:
            raise NoHandlerAttachedError(f"Handler for message {message} could not be found")

        return self.routes[message.__class__]


message_router = MessageRouter()


def create_attach_decorator(router: MessageRouter):
    def decorator(message_handler: Type[T]) -> Callable[[Any], Any]:
        def _decorator(message):
            if not isclass(message):
                raise TypeError("Message must be valid class declaration")

            router.attach(message, message_handler)

            return message

        return _decorator

    return decorator


command = create_attach_decorator(message_router)

__all__ = ["MessageRouter", "message_router", "command", "create_attach_decorator"]
