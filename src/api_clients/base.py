from abc import ABC, abstractmethod
from src.dto import Vacancy


class VacancyAPIClient(ABC):
    """
    Создание базового, абстрактного клиента. abstractmethod принимает ключевое слово для поиска
    """

    @abstractmethod
    def get_vacancies(self, search_text: str) -> list[Vacancy]:
        pass