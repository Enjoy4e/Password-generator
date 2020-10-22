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


def mypasswd_gen(length):
    psw = ''
    spec_amount = random.randint(1, length // 3)
    upper_amount = random.randint(1, (length - spec_amount) // 2)
    lower_amount = random.randint(1, (length - spec_amount - upper_amount) // 2)
    num_amount = length - spec_amount - upper_amount - lower_amount
    spec_pos = []
    lower_pos = []
    upper_pos = []
    num_pos = []
    for x in range(spec_amount):
        x = random.choice([i for i in range(0, length) if i not in spec_pos])
        spec_pos.append(x)
    for x in range(num_amount):
        x = random.choice([i for i in range(0, length) if i not in spec_pos and i not in num_pos])
        num_pos.append(x)
    for x in range(lower_amount):
        x = random.choice(
            [i for i in range(0, length) if i not in spec_pos and i not in num_pos and i not in lower_pos])
        lower_pos.append(x)
    for x in range(upper_amount):
        x = random.choice([i for i in range(0, length) if
                           i not in spec_pos and i not in num_pos and i not in lower_pos and i not in upper_pos])
        upper_pos.append(x)
    for x in range(0, length):
        if x in spec_pos:
            psw = psw + random.choice('_-,.?/`~!@#$%&*!')
        if x in lower_pos:
            psw = psw + random.choice('qwertyuiopasdfghjklzxcvbnm')
        if x in upper_pos:
            psw = psw + random.choice('QWERTYUIOPASDFGHJKLZXCVBNM')
        if x in num_pos:
            psw = psw + random.choice('0123456789')
    return psw


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


  for x in range(length):
        if x not in [flag_spec,flag_upper,flag_nums,flag_lower]:
            psw=psw+ random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_-,.?/`~!@#$%&*!'))
        if x==flag_spec:
            psw=psw+random.choice('_-,.?/`~!@#$%&*!')
        if x==flag_nums:
            psw=psw+random.choice('0123456789')
        if x==flag_lower:
            psw=psw+random.choice('qwertyuiopasdfghjklzxcvbnm')
        if x==flag_upper:
            psw=psw+random.choice('QWERTYUIOPASDFGHJKLZXCVBNM')


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
    while True:
        try:
            length = int(input())
            break
        except ValueError:
            print("Ошибка ввода длины пароля")
    print('Пароль для:', name)
    print('Сгенерированный пароль:', mypasswd_gen(length))
    # hech = int(input())
    print('Захешировать имеющиеся пароли?')
    print('1)Да      2)Нет')
    print('Отправить пароль на почту?')
    print('1)Да      2)Нет')
    # pochta = int(input())


if __name__ == '__main__':
    main()
