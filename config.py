# -*- coding: utf-8 -*-
token = '594169097:AAEShVeDaukF2lx37P5i3rRSB5mUjJ-w4v4'

WEBHOOK_HOST = '82.200.130.16'
WEBHOOK_PORT = 443  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше

WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (token)

WelcomeMessageLine1 = 'Для использования сервиса нажмите на одну из следующих кнопок: «Создать обращение», «Посмотреть другие услуги» (кнопки отображены в нижней части экрана)'
WelcomeMessageLine2 = 'Для полноценной работы с сервисом требуется последняя версия приложения Telegram.'

WelcomeMessageLineAll = WelcomeMessageLine1+'\n\n'+WelcomeMessageLine2


RequestMessageLine1 = 'Вы выбрали услугу для отправки Обращения'
RequestMessageLine2 = 'Внимание, для возможности рассмотрения Вашего обращения просим отправлять достоверные контактные данные в тексте обращения (ФИО и контактный телефон).'
RequestMessageLine3 = 'После заполнения электронной формы Обращения, нажмите на кнопку «SEND» и дождитесь ответа'

RequestMessageLineAll = RequestMessageLine1+'\n\n'+RequestMessageLine2+'\n\n'+RequestMessageLine3


AddRequestMessageLine1 = 'Спасибо, Ваше обращение принято! Ожидайте ответа от менеджера по предоставленным Вами контактным данным. Благодарим за использование наших продуктов'
AddRequestMessageLine2 = 'В случае возникновения вопросов, просим обращаться в Call center по номерам 1440 или 8800 080 2017'

AddRequestMessageLineAll = AddRequestMessageLine1+'\n\n'+AddRequestMessageLine2

SendPhoneMessageLine = 'Для отправки обращения нажмите кнопку "Отправить номер телефона"'


SendPhoneRertyMessageLine1 = 'Для обработки Вашего Обращения требуется наличие номера, просим нажать на кнопку "Отправить номер телефона"'
SendPhoneRertyMessageLine2 = 'Либо, для перехода в Главное меню сервиса нажмите кнопку "Пeрeйти в Глaвнoе мeню"'

SendPhoneRertyMessageLineAll = SendPhoneRertyMessageLine1+'\n\n'+SendPhoneRertyMessageLine2