import pytest

from src.dto import Salary


class TestSalaryCompare:
    """
    Тест сравнения вакансий по зарпалте
    """
    def test_salary_are_equals_none_same(self):
        """
        Одинаковые зарплаты None
        """
        salary_1 = Salary(salary_from=None, salary_to=None, currency='RUB')
        salary_2 = Salary(salary_from=None, salary_to=None, currency='RUB')

        assert salary_1 == salary_2

    def test_salary_are_equals_not_none_same(self):
        """
        Одинаковые зарплаты not None
        """
        salary_1 = Salary(salary_from=100, salary_to=1_000, currency='RUB')
        salary_2 = Salary(salary_from=100, salary_to=1_000, currency='RUB')

        assert salary_1 == salary_2

    def test_from_lower_with_higher_salary(self):
        """
        Если указана только минимальная зарплата, то сравнение идет по ней
        """
        salary_lower = Salary(salary_from=100, salary_to=None, currency='RUB')
        salary_higher = Salary(salary_from=200, salary_to=None, currency='RUB')

        assert salary_lower < salary_higher

    def test_to_lower_with_higher_salary(self):
        """
        Если указана только максимальная зарплата, то сравнение идет по ней
        """
        salary_lower = Salary(salary_from=None, salary_to=100, currency='RUB')
        salary_higher = Salary(salary_from=None, salary_to=200, currency='RUB')

        assert salary_lower < salary_higher

    @pytest.mark.parametrize('not_none_salary', [
        {'salary_from': 100, 'salary_to': None},
        {'salary_from': None, 'salary_to': 200},
        {'salary_from': 100, 'salary_to': 200}
    ])
    def test_one_from_or_to_not_none(self, not_none_salary):
        """
        Если указана хотя бы одна из границ диапазона зарплат, а у другой None
        """
        salary_lower = Salary(salary_from=None, salary_to=None, currency='RUB')
        salary_higher = Salary(currency='RUB', **not_none_salary)

        assert salary_lower < salary_higher
