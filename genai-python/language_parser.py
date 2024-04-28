from abc import ABC, abstractmethod

class LanguageParser(ABC):
    @abstractmethod
    def parse(self, file_path):
        pass