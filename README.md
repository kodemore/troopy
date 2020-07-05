# Troopy 
Command bus library for python. Makes using the message bus pattern in your application easy.

## What is a command/message?
Commands are objects, some kind of an imperative informing what behavior client expects from application. 
Commands can bear some information (client's input) required to fulfill the job. It is recommended to use dataclasses
when you declare a command for your own convenience.

## What is a command handler?
Command handler is a function or callable object, that accepts command as a parameter to perform specific task. 

## Advantages of using command bus/message bus

 - Command can be created anytime/anywhere by your client and as long as it is hand over to command bus it will be handled
 - You can slim your services layer and dependencies, as each handler perform one specific task
 - Testing your application can be more precise and easier

## Features

 - Fast and simple
 - Flexible solution which can be used everywhere
 - Works well with dataclasses
 - Custom factories for command handlers

## Installation

```
pip install troopy
```

# Basic Usage

```python
from troopy import CommandBus, command
from dataclasses import dataclass


class HelloHandler:
    def __call__(self, command: "SignUp") -> None:
        print("Hello user {command.username}!")


@command(HelloHandler)  # attach command to its handler
@dataclass
class SayHello:
    username: str


command_bus = CommandBus()
command_bus.dispatch(SayHello(username="Tom"))
```

`HelloHandler` is class which encapsulates our business logic (in this scenario welcomes user), any callable can be used
as a command handler, as long as it is a function or class declaration without `__init__` method.

`SayHello` is a command class which carries some data it is attached to `HelloHandler` with `@attach` decorator. 
`@attach` decorator allows the library to understand which handler is responsible for which command. It is also possible
to use `troopy.MessageRouter` directly to attach command to its handler ([example available here](/examples/custom_message_router_example.py))


The above example will print `Hello user Tom` as a result. 

# Setting factory for command handler
It is possible to use custom function for factoring command handlers, consider the following example:

```python
import sqlite3
from troopy import CommandBus, command
from dataclasses import dataclass

db = sqlite3.connect('example.db') 


class UserRegistrationHandler:
    def __init__(self, db):
        self.db = db
    def __call__(self, command: "RegisterUser") -> None:
        cursor = self.db.cursor()
        cursor.execute("INSER INTO users VALUES (?, ?)", (command.username, command.password))
        self.db.commit()


@command(UserRegistrationHandler)  # attach command to its handler
@dataclass
class RegisterUser:
    username: str
    password: str

def command_handler_factory(cls):
    return cls(db)

command_bus = CommandBus(handler_factory=command_handler_factory)
command_bus.dispatch(RegisterUser(username="Tom", password="secret"))
```

As you can probably tell `UserRegistrationHandler` requires sqlite db connection in order to work properly, with `command_handler_factory`
we are able to provide this connection to the object, so `RegisterUser` command can be handled properly.

For more examples please check [examples](/examples) directory
