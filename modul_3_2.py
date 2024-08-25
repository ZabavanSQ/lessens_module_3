def send_email(message, recipient, sender = "university.help@gmail.com"):
    while recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        break
    if '@' in recipient and  '.com'in recipient or '.ru' in recipient or '.net' in recipient:
        if '@' in sender and  '.com'in sender or '.ru' in sender or '.net' in sender:
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
        else:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    else:
         print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")





send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

