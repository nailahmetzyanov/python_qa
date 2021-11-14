from src.parser import *

if __name__ == '__main__':
    """Создаем пустой файл parsing_results.json"""
    create_json()

    """Считаем общее количество выполненных запросов/GET запросов/POST запросов/HEAD запросов
    и дописываем в parsing_results.json"""
    get_requests_quantity(arg_parser().path_to_filename)

    """Ищем топ 3 IP адресов, с которых было сделано наибольшее количество запросов
    и дописываем в parsing_results.json"""
    get_frequent_requests(arg_parser().path_to_filename)

    """Ищем топ 3х самых долгих запросов и дописываем в parsing_results.json"""
    get_slow_requests(arg_parser().path_to_filename)
