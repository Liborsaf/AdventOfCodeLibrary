from abc import ABC, abstractmethod


class AdventOfCodeRegistry(ABC):
    @abstractmethod
    def setup(self):
        pass
