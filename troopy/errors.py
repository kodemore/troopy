class NoHandlerAttachedError(ValueError):
    pass


class HandlerAlreadyAttachedError(ValueError):
    pass


__all__ = ["NoHandlerAttachedError", "HandlerAlreadyAttachedError"]
