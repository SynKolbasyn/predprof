from hash_table import generate_hash_table, print_hash_table


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
        res[i[1]] = {"type": i[1], "date": int(i[2]), "creator": i[3], "count": int(i[4])}
    return res


def main():
    data = get_data()
    res = parse_data(data)
    hash_table = generate_hash_table(res)
    print_hash_table(hash_table)


if __name__ == "__main__":
    main()
