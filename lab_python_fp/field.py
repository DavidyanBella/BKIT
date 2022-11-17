goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]


def field(items, *args):
    assert len(items) > 0
    for g in items:
        if 'title' in args:

           break
    else:
