from main import status, stats, cout_words, queries, get_id, ids
import pytest


def test_get_dict():
    res = status(stats)
    assert isinstance(res, str)


def test_line_number():
    res = cout_words(queries)
    assert '2' in res


def test_get_id():
    res = get_id(ids)
    assert isinstance(res, list)
