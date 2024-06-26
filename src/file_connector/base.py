from abc import ABC, abstractmethod
from src.dto import Vacancy

class FileConnector(ABC):
    """
    Работа с файлом: получение, запись, удаление c использованием абстрактоного метода
    """
    @abstractmethod
    def get_vacancies(self) -> list[Vacancy]:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass
