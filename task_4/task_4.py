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
    создаёт словарь из данных.
    :param data: Собранные данные из файла - двумерный массив
    :return: сзданный словарь
    """
    res = {}
    for i in data:
        res[i[0]] = {"type": i[1], "date": int(i[2]), "creator": i[3], "count": int(i[4])}
    return res


def print_rating(res):
    """
    Функция считает рейтинг книги и выводит его на экран после названия книги
    :param res: словарь с данными о книге
    :return: None
    """
    for i in res:
        rating = res[i]["count"] / (2023 - res[i]["date"])
        print(f"{i}: {rating}")


def main():
    data = get_data()
    res = parse_data(data)
    print_rating(res)


if __name__ == "__main__":
    main()
