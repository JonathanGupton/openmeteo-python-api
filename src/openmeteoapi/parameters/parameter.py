"""Module containing the Parameter base class"""

from abc import ABC
from abc import abstractmethod
from typing import Optional
from typing import Any


class URLParameter(ABC):
    _default: Optional[Any] = None
    _description: str = ""

    def __init__(self, value=None):
        if value:
            self.value = value
        elif self._default is not None:
            self.value = self._default
        else:
            raise ValueError("No parameter value provided")

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @property
    def default(self):
        return self._default

    @property
    def description(self):
        return self._description

    @abstractmethod
    def formatted(self) -> str:
        raise NotImplementedError


class HourlyParameter(ABC):
    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    def formatted(self) -> str:
        return self.name


class DailyParameter(ABC):
    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    def formatted(self) -> str:
        return self.name
