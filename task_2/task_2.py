from quick_sort import quick_sort


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
        tmp = res.get(i[1], [])
        tmp.append({"title": i[0], "type": i[1], "creators": i[3]})
        res[i[1]] = tmp
    return res


def print_res(arr, res):
    """
    Функция выводит ответ на задание
    :param arr: отсортированный массив
    :param res: словарь с данными
    :return: None
    """
    for i1, i in enumerate(arr[:3]):
        print(f"{res[i][0]['type']} {i1 + 1}:")
        for j, e in enumerate(res[i]):
            print(f"{e['title']} {j + 1} - создатель {e['creators'] if e['creators'] != '' else 'неизвестен'}")
        print("…")


def main():
    data = get_data()
    res = parse_data(data)
    arr = [i for i in res.keys()]
    quick_sort(arr, 0, len(arr) - 1)
    print_res(arr, res)


if __name__ == "__main__":
    main()
