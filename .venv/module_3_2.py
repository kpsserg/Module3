def send_email(message, recipient, *, sender = "university.help@gmail.com"):

    #Проверка адреса отправителя
    if not is_correct_email(sender):
        print_error(recipient, sender)
        return False

    # Проверка адреса получателя
    if not is_correct_email(recipient):
        print_error(recipient, sender)
        return False

    if recipient.upper() == sender.upper():
        print('Нельзя отправить письмо самому себе!')
        return False

    if sender.upper() == "university.help@gmail.com".upper():
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        return True

    if sender.upper() != "university.help@gmail.com".upper():
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        return True


def print_error(recipient, sender):
    print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')


def is_correct_email(email):
    if is_email_have_at(email):
        return True
    else:
        return False


def is_email_have_at(email):
    email_parts = []
    email_parts = email.split('@')
    if len(email_parts) == 2:
        if is_valid_email_zone(email_parts[-1]):
            return True
        else:
            return False
    else:
        return False

#Проверка доменной зоны почты
def is_valid_email_zone(zone):
    zone = zone.split('.')
    allow_zone = ['ru'.upper(), 'com'.upper(), 'net'.upper()]
    if zone[-1].upper() in allow_zone:
        return True
    else:
        return False


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'Urban.teacher@mail.ru', sender='Urban.Teacher@mail.Ru')
#The End!