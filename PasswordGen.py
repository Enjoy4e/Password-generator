import random


def password_gen(length, spec):
    psw = ''
    randoms = 0
    if spec == 1:
        randoms = random.randint(1, 2)
        for i in range(randoms):
            psw = psw + random.choice(list('_-,.?/`~!@#$%&*!'))
        for x in range(length - randoms):
            psw = psw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    else:
        for x in range(length - randoms):
            psw = psw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    psw = list(psw)
    random.shuffle(psw)
    result = ''.join(psw)
    return result


'''def send_mail(self, text):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # указываем уникальный пароль веб приложения
    server.login('Свой токен')
    body = text
    message = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'Адрес почты',
        message
    )

    # загатовка для быстрого ввода какого-либо второго мейла для демонстрации отправки писем
    # server.sendmail(
    #     'admin@itproger.com',
    #     '@mail.ru',
    #     message
    # )

    print("\nthe email has been sent")
    server.quit()'''


def main():
    print('Пароль для:')
    name = input()
    print('Длина пароля:')
    length = int(input())
    print('Нужно ли использовать спец. символы ~`!@#$%^&*()_-+=')
    print('1)Да      2)Нет')
    spec = int(input())
    print('Пароль для:', name)
    print('Сгенерированный пароль:', password_gen(length, spec))
    # hech = int(input())
    print('Захешировать имеющиеся пароли?')
    print('1)Да      2)Нет')
    print('Отправить пароль на почту?')
    print('1)Да      2)Нет')
    # pochta = int(input())


if __name__ == '__main__':
    main()
