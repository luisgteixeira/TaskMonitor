#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from sendmail import *
from logmonitor import *

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

    logmonitor = LogMonitor("log.txt")

    while running > 0:

        print(logmonitor.get_message())

        notification_time = 60

        # Cria email a ser enviado
        # sendmail = SendMail(mail_from, password, mail_to, execution_info)

        # Envia email
        # sendmail.send()

        # Tempo entre o envio dos emails
        sleep(notification_time)
        running -= 1

if __name__ == '__main__':
    main()
