import re
import json
import argparse
import os
from collections import Counter


# Возможность в командной строке указать директорию для поиска лог файлов
def arg_parser():
    parser = argparse.ArgumentParser(description='Parser for *.log files')
    parser.add_argument('path_to_filename', type=str, help='Enter path *.log file or directory of files.')
    args = parser.parse_args()
    return args


# Ищем в переданной директории *.log файлы
def find_log_files(path_to_filename: str):
    files_list = os.listdir(path_to_filename)
    log_files_list = list(filter(lambda x: x.endswith('.log'), files_list))
    return log_files_list


# Считываем данные из файла
def reader(path_to_filename: str):
    with open(path_to_filename) as f:
        log = f.read()
    return log


# Создать пустой файл parsing_results.json
def create_json():
    json_data = []
    with open('parsing_results.json', 'w') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))


# Добавляем данные в формате json в созданный ранее файл parsing_results.json
def add_to_json(json_data: object):
    data = json.load(open("parsing_results.json"))
    data.append(json_data)
    with open("parsing_results.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def count_requests_by_type(path_to_filename: str, param: str):
    """ Считаем кол-во разных запросов в 1 файле
    (доп.параметры: 'all_requests', 'get_requests', 'post_requests', 'head_requests')"""

    # Считаем общее кол-во выполненных запросов
    if param == 'all_requests':
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s-'
        requests_list = re.findall(regexp, reader(path_to_filename))
        all_req_quant = len(requests_list)
        json_data = {"Общее кол-во выполненных запросов из файла " + path_to_filename: all_req_quant}
        # Записываем найденные данные в json файл
        add_to_json(json_data)
        # Выводим в терминал данные об общем количестве выполненных запросов
        print('Общее кол-во выполненных запросов из файла ' + path_to_filename + " -", all_req_quant)
        return all_req_quant
    # Считаем общее кол-во выполненных GET запросов
    elif param == 'get_requests':
        regexp = r'"GET\s'
        requests_list = re.findall(regexp, reader(path_to_filename))
        get_req_quant = len(requests_list)
        json_data = {"Кол-во запросов типа GET из файла " + path_to_filename: get_req_quant}
        # Записываем найденные данные в json файл
        add_to_json(json_data)
        # Выводим в терминал данные о количестве GET запросов
        print('Кол-во запросов типа "GET" из файла ' + path_to_filename + " -", get_req_quant)
        return get_req_quant
    # Считаем общее кол-во выполненных POST запросов
    elif param == 'post_requests':
        regexp = r'"POST\s'
        requests_list = re.findall(regexp, reader(path_to_filename))
        post_req_quant = len(requests_list)
        json_data = {"Кол-во запросов типа POST из файла " + path_to_filename: post_req_quant}
        # Записываем найденные данные в json файл
        add_to_json(json_data)
        # Выводим в терминал данные о количестве POST запросов
        print('Кол-во запросов типа "POST" из файла ' + path_to_filename + " -", post_req_quant)
        return post_req_quant
    # Считаем общее кол-во выполненных HEAD запросов
    elif param == 'head_requests':
        regexp = r'"HEAD\s'
        requests_list = re.findall(regexp, reader(path_to_filename))
        head_req_quant = len(requests_list)
        json_data = {"Кол-во запросов типа HEAD из файла " + path_to_filename: head_req_quant}
        # Записываем найденные данные в json файл
        add_to_json(json_data)
        # Выводим в терминал данные о количестве GET запросов
        print('Кол-во запросов типа "HEAD" из файла ' + path_to_filename + " -", head_req_quant, "\n")
        return head_req_quant
    else:
        print('Enter valid searching value/parameter..', "\n")


# Обрабатываем запросы в искомом файле директории или всех файлах директории
def get_requests_quantity(path_to_filename: str):
    # Если передан путь до файла, обрабатываем только этот файл
    if os.path.isfile(path_to_filename):
        count_requests_by_type(path_to_filename, 'all_requests')
        count_requests_by_type(path_to_filename, 'get_requests')
        count_requests_by_type(path_to_filename, 'post_requests')
        count_requests_by_type(path_to_filename, 'head_requests')
    # Если передана директория (не файл!), обрабатываем все файлы *.log внутри этой директории
    else:
        if os.path.isdir(path_to_filename):
            log_files_list = find_log_files(path_to_filename)
            i = 0
            while i < len(log_files_list):
                count_requests_by_type(path_to_filename + log_files_list[i], 'all_requests')
                count_requests_by_type(path_to_filename + log_files_list[i], 'get_requests')
                count_requests_by_type(path_to_filename + log_files_list[i], 'post_requests')
                count_requests_by_type(path_to_filename + log_files_list[i], 'head_requests')
                i += 1
        else:
            print('No files were found in the directory. Check the sent path or mistakes in it.', "\n")


# Считаем запросы и выбираем топ 3 наиболее частых
def count_requests_frequency(path_to_filename: str):
    data = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', reader(path_to_filename))
    counter = Counter(data)
    most_freq_list = counter.most_common(3)
    i = 0
    ips_list = []
    while i < len(most_freq_list):
        ips_list.append(most_freq_list[i][0])
        i += 1
    json_data = {
        "Топ 3 IP адресов, с которых были сделаны самые частые запросы из файла " + path_to_filename: {
            "1 место": ips_list[0],
            "2 место": ips_list[1],
            "3 место": ips_list[2],
        }
    }
    # Записываем найденные данные в json файл
    add_to_json(json_data)
    # Выводим в терминал данные 3х IP, с которых было сделано наибольшее кол-во запросов
    print('Топ 3 IP адресов, с которых были сделаны самые частые запросы из файла ' + path_to_filename)
    print('1 место: ', ips_list[0])
    print('2 место: ', ips_list[1])
    print('3 место: ', ips_list[2], "\n")
    return ips_list


# Обрабатываем запросы в искомом файле директории или всех файлах директории
def get_frequent_requests(path_to_filename: str):
    if os.path.isfile(path_to_filename):
        count_requests_frequency(path_to_filename)
    # Если передана директория (не файл!), обрабатываем все файлы *.log внутри этой директории
    else:
        if os.path.isdir(path_to_filename):
            log_files_list = find_log_files(path_to_filename)
            i = 0
            while i < len(log_files_list):
                count_requests_frequency(path_to_filename + log_files_list[i])
                i += 1
        else:
            print('No files were found in the directory. Check the sent path or mistakes in it.', "\n")


# Считаем запросы и выбираем топ 3 наиболее длительных
def count_requests_speed(path_to_filename: str):
    time_regex = r'\" .\d{3,4}'
    data = re.findall(time_regex, reader(path_to_filename))
    i = 0
    time_list = []
    for elem in data:
        time_list.append(int(re.sub("[^0-9]", "", elem)))
        i += 1
    time_list.sort()
    slowest_request_time = time_list[-1].__str__()
    file_data = open(path_to_filename).readlines()
    requests_list = []
    for elem in iter(file_data):
        if slowest_request_time in elem:
            requests_list.append(elem)
    json_data = {
        "Топ 3 наиболее длительных запроса из файла " + path_to_filename: {
            "1 место": requests_list[0],
            "2 место": requests_list[1],
            "3 место": requests_list[2]
        }
    }
    # Записываем найденные данные в json файл
    add_to_json(json_data)
    # Выводим в терминал данные топ 3х самых долгих запросов
    print('Топ 3 наиболее длительных запроса из файла ' + path_to_filename)
    print('1 место: ', requests_list[0])
    print('2 место: ', requests_list[1])
    print('3 место: ', requests_list[2])
    return requests_list


# Обрабатываем запросы в искомом файле директории или всех файлах директории
def get_slow_requests(path_to_filename: str):
    if os.path.isfile(path_to_filename):
        count_requests_speed(path_to_filename)
    # Если передана директория (не файл!), обрабатываем все файлы *.log внутри этой директории
    else:
        if os.path.isdir(path_to_filename):
            log_files_list = find_log_files(path_to_filename)
            i = 0
            while i < len(log_files_list):
                count_requests_speed(path_to_filename + log_files_list[i])
                i += 1
        else:
            print('No files were found in the directory. Check the sent path or mistakes in it.', "\n")
