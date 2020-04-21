def parse(query: str) -> dict:
    query = query.strip()
    d = {}

    if '?' in query:
        query = query.split('?')
        query = (query[1].split('&'))

        try:
            for i in query:
                key, value = i.split('=')
                d[key] = value
        except ValueError:
            pass

    return d


if __name__ == '__main__':
    assert parse(' https://example.com/path/to/page?name=ferret&color=purple ') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=f&color100purple') == {'name': 'f'}
    assert parse('https://example.com/path/to/page?name=DENI&color=blue&') == {'name': 'DENI', 'color': 'blue'}
    assert parse('https://example.com/path/TO/page?namE=123&color=purple&') == {'namE': '123', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=Андрей&color=pu%%%') == {'name': 'Андрей', 'color': 'pu%%%'}
    assert parse('https://example.com/path/to/page?name=ferret&color=p&&&') == {'name': 'ferret', 'color': 'p'}
    assert parse('https://example.com/path/to/page?name=123&color=77&&----&---') == {'name': '123', 'color': '77'}
    assert parse('https://example.com/path/to/page?name=ferret&color=') == {'name': 'ferret', 'color': ''}
    assert parse('https://example.com/path/to/page?name=') == {'name': ''}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('12345') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
