import smtplib
from dotenv import load_dotenv
import os 
site_name="https://dvmn.org/profession-ref-program/id627628409/IVxXh/"
friend_name="Елена"
sander_name="Максим"
sender_email="devmanorg@yandex.ru"
recipient_email="rassolenko.maxim@yandex.ru"
letter="""/
From: devmanorg@yandex.ru
To: rassolenko.maxim@yandex.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8

Привет,%friend_name%!.%my_name% приглашает тебя на сайт %website%!
%website% — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".replace("%friend_name%",friend_name).replace("%my_name%",sander_name).replace("%website%",site_name).replace("devmanorg@yandex.ru",sender_email).replace("rassolenko.maxim@yandex.ru",recipient_email)
letter = letter.encode("UTF-8")
load_dotenv()
login= os.getenv('LOGIN')
password= os.getenv('TOKEN')
server = smtplib.SMTP_SSL("smtp.yandex.ru:465")
server.login(login,password)
server.sendmail(sender_email,recipient_email, letter)
server.quit()

