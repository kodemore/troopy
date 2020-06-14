import pytest

from troopy import attach, message_router
from troopy.errors import HandlerAlreadyAttachedError


def test_attach_to_class() -> None:
    def test_handler(message) -> None:
        pass

    @attach(test_handler)
    class TestMessage:
        pass

    assert message_router.find_for(TestMessage())


def test_attach_to_nonclass() -> None:
    def test_handler(message) -> None:
        pass

    with pytest.raises(TypeError):
        @attach(test_handler)
        def message() -> None:
            pass


def test_fail_when_attaching_already_existing_handler() -> None:

    class TestMessage:
        pass

    def test_handler(message) -> None:
        pass

    def another_handler(message) -> None:
        pass

    message_router.attach(TestMessage, test_handler)

    with pytest.raises(HandlerAlreadyAttachedError):
        message_router.attach(TestMessage, another_handler)
