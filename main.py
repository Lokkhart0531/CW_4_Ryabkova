from src.api_clients.hh import HeadHunterAPI
from src.api_clients.base import VacancyAPIClient
from src.file_connector.json_connector import JSONConnector
from src.file_connector.base import FileConnector
from pathlib import Path
from prettytable import PrettyTable


BASE_PATH = Path(__file__).parent
VACANCIES_PATH_FILE = BASE_PATH.joinpath('vacancies.json')

api_client: VacancyAPIClient = HeadHunterAPI()
json_connector: FileConnector = JSONConnector(VACANCIES_PATH_FILE)
def main():
    """
    Работа с пользователем
    :return:
    """
    while True:
        print("""
Добро пожаловать в программу, выберите действие:
1.Загрузить вакансии в файл по ключевому слову
2.Вывести топ 10 вакинсий из файла
0.Выйти
        """)
        user_input = input()
        if not user_input.isdigit():
            continue

        user_choice = int(user_input)
        if user_choice == 1:
            search_word = input("Введите ключевое слово для поиска ")
            vacancies = api_client.get_vacancies(search_word.lower())
            for vac in vacancies:
                json_connector.add_vacancy(vac)
        elif user_choice == 2:
            vacancies = json_connector.get_vacancies()
            t = PrettyTable(['name', 'url', 'employer_name', 'salary'])

            for vac in sorted(vacancies, key=lambda x: x.salary, reverse=True)[:10]:
                salary = '{_from} -> {_to}, {currency}'.format(
                    _from=vac.salary.salary_from or 0,
                    _to=vac.salary.salary_to or 0,
                    currency=vac.salary.currency
                )
                t.add_row([vac.name, vac.url, vac.employer_name, salary])
            print(t)
        elif user_choice == 0:
            break


if __name__ == '__main__':
    main()

