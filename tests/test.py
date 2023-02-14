from main import status, stats, cout_words, queries, get_id, ids
from yandex import TOKEN, YANDEX


def test_get_dict():
    res = status(stats)
    assert isinstance(res, str)


def test_line_number():
    res = cout_words(queries)
    assert '2' in res


def test_get_id():
    res = get_id(ids)
    assert isinstance(res, list)


ya = YANDEX(TOKEN)


# ТЕСТ С ОШИБОЙ
def test_deleted():
    status_code = '204'
    res = ya.check_folder_deleted()
    assert status_code in str(res)


# ТЕСТ БЕЗ ОШИБКИ
def test_created():
    status_code = '201'
    res = ya.check_folder_creation()
    assert status_code in str(res)
