**Парсинг данных из файла .log формата по заранее заданным параметрам, вывод информации в терминал, запись данных в файл в формате .json**

1. Запуск осуществляется из командной строки терминала с указанием директории файлов или конкретного с помощью команды: "python main.py access.log"\

2. Логика для парсинга данных из файла "access.log" и сохранения их в нужном формате расположена в файле "parser.py"

   create_json() - создает пустой файл с заранее заданным именем "parsing_results.json" для дальнейшей записи полученных данных

   get_requests_quantity() - считает кол-во выполненных запросов (общее кол-во, GET, POST, HEAD)

   find_most_freq_requests() - ищет топ 3 IP адресов, с которых было сделано наибольшее кол-во запросов

   find_slowest_requests() - ищет топ 3 самых долгих запроса