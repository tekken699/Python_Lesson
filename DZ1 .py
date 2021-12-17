import re

def email_pars(email):
    re_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not re_email.match(email):
        raise ValueError (f'Вы неверно указали ваш email! {email}')
    print(re_email.match(email).groupdict())


email = input('Введите пожалуйста ваш email: ')

try:
    email_pars(email)
except ValueError as error:
    print(error)

