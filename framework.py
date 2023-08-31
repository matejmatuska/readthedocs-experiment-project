"""
Lumache - Python library for cooks and food lovers.
"""

class Model:
    """Modules are messages containing dat. They can be produced and consumed."""

    def dump(self):
        """Dumps debug info about the Model"""


class Actor:
    """As the name suggests actors allow you to act on consumed messages. They also allow you to produce new messages."""

    def process(self):
        """Runs the actor code."""


class Repository:
    """Repository is a collection of Models and Actors"""
