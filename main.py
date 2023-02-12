stats = {
    'facebook': 59995, 'yandex': 1111111111120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98
}

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]
       }


def status(stat):
    stat = max(stats, key=stats.get)

    return stat


def cout_words(query):
    all_query = len(queries)
    dct = {}
    for query in queries:
        count = len(query.split())
        dct[count] = dct.get(count, 0) + 1

    for key in dct:
        percent_of_queries = round(dct[key] / all_query * 100)

    return f'Кол-во слов в запросе {key}  - {percent_of_queries}%'


def get_id(id):
    data = []
    for user, id in ids.items():
        for i in id:
            data.append(i)

    sets = set(data)
    return list(sets)
