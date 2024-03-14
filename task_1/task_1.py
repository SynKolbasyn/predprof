def get_data():
    """
    Собирает данные из csv файлика в двумерный массив и возвращает его
    :return: двумерный массив данных из файла
    """
    with open("languages.csv", "r", encoding="utf-8") as file:
        file.readline()
        data = [i.split(";") for i in file]
    return data


def parse_data(data):
    """
    создаёт словарь из данных. ключ - тип книги, значение - кол-во книг
    :param data: Собранные данные из файла - двумерный массив
    :return: сзданный словарь
    """
    res = {}
    for i in data:
        res[i[1]] = res.get(i[1], 0) + int(i[4])
    return res


def create_str_from_res(res):
    """
    создаёт строку из словаря данных, для удобства записи в файл
    :param res: словарь с данными
    :return: строка удовлетворяющая критериям задания
    """
    s = ""
    for i in res:
        s += f"Книг для изучения {i} в библиотеке нашлось: {res[i]}\n"
    return s


def save_result(res):
    """
    сохраняет словарь в нужном формате на компьютер
    :param res: словарь с данными для сохранения
    :return: None
    """
    with open("count_book.txt", "w", encoding="utf-8") as file:
        s = create_str_from_res(res)
        file.write(s)


def print_max_books_type(res):
    """
    выводит максимальное кол-во книг из всех тем
    :param res: словарь с данными о типах книг и их колличестве
    :return: None
    """
    print(f"Для изучения этой темы можно воспользоваться {max(res.values())} книгами")


def main():
    data = get_data()
    res = parse_data(data)
    save_result(res)
    print_max_books_type(res)


if __name__ == "__main__":
    main()
