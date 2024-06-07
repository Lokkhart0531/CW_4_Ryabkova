from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Salary:
    """
    Класс для работы с зарплатой
    currency - валюта
    salary_to и salary_from - диапазон зарплаты
    """
    currency: str
    salary_from: int | None = None
    salary_to: int | None = None

    def __lt__(self, other):
        """
        Сравнение зарплат с использованием магического метода __lt__
        """
        self_salary_from = self.salary_from or 0
        self_salary_to = self.salary_to or 0
        other_salary_from = other.salary_from or 0
        other_salary_to = other.salary_to or 0

        if 0 not in (self_salary_from, other_salary_from):
            if self_salary_from == other_salary_from:
                return self_salary_to < other_salary_to
            return self.salary_from < other.salary_from

        if  self_salary_from == 0 and other_salary_from == 0:
            return True
        if None in (self.salary_from, other.salary_from):
            return True
        return False

@dataclass(unsafe_hash=True)
class Vacancy:
    """
    Класс для работы с вакансией
    name - название
    url - ссылка на сайт
    employer_name - название компании или имя работадателя
    salary - зарплата
    """
    name: str
    url: str
    employer_name: str
    salary: Salary

    def __lt__(self, other):
        return self.salary < other.salary

