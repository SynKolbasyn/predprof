def generate_hash(s):
    """
    Функция генерации хэша
    :param s: строка из которой будет сгенерирован хэш
    :return: хеш
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    d = {l: i for i, l in enumerate(s, 1)}
    p = 67
    m = 1e9 + 9
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + d[c] * p_pow) % m
        p_pow = (p_pow * p) % m
    return int(hash_value)


def generate_hash_table(res):
    """
    Создаёт хэш таблицу из массива
    :param res: массив из которогу будет создана хэш таблица
    :return: хэш таблица
    """
    hash_table = {}
    for i in res:
        hash_table[generate_hash(i)] = res[i]
    return hash_table


def print_hash_table(hash_table):
    """
    Выводит на экран хэш таблицу
    :param hash_table: хэш таблица
    :return:
    """
    for h, e in zip(hash_table.keys(), hash_table.values()):
        print(f"Hash: {h} -> Value: {e}")
