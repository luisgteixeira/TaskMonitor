#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from sendmail import *

def main():

    running = 3

    from_mail = 'logexecution@gmail.com'
    password = 'nossasenhaeessa'
    to = 'luisguilherme.ufpi@gmail.com'
    #info_execution = 'execucao 1'
    info_execution = ''

    # Tempo de execucao em minutos
    execution_time = 1

    while running > 0:
        # Cria email a ser enviado
        sendmail = SendMail(from_mail, password, to, info_execution)

        # Envia email
        sendmail.send()

        # Tempo entre o envio dos emails
        time.sleep(execution_time * 60)
        running -= 1

if __name__ == '__main__':
    main()
