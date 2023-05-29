from abc import ABC, abstractmethod


class TaskRepositoiry(ABC):
    @abstractmethod
    def create(self):
        raise NotImplementedError
