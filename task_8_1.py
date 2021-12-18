import re

RE_EMAIL = re.compile(r'^(?P<username>[^@\s]+)@(?P<domain>[^@\s]+\.[^@\s]+)$')


def email_parse(email_address):
    if not re.match(RE_EMAIL, email_address):
        raise ValueError(f'wrong email: {email_address}')
    return re.search(RE_EMAIL, email_address).groupdict()


if __name__ == '__main__':
    print(email_parse('fs_.fgdfgdfg!@3&dfsdfs.fru'))

