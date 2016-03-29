#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from sendmail import *

def main():

    running = 3

    '''
    mail_from = 'logexecution@gmail.com'
    password = 'nossasenhaeessa'
    mail_to = 'luisguilherme.ufpi@gmail.com'
    #execution_info = 'execucao 1'
    execution_info = ''

    # Tempo de execucao em minutos
    notification_time = 1
    '''

    while running > 0:
        # Cria email a ser enviado
        sendmail = SendMail(mail_from, password, mail_to, execution_info)

        # Envia email
        sendmail.send()

        # Tempo entre o envio dos emails
        time.sleep(notification_time * 60)
        running -= 1

if __name__ == '__main__':
    main()
