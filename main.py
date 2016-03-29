#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from sendmail import *

def main():

    configuration_file = open('configuration.txt', 'r')

    # Endereço do email remetente
    mail_from = configuration_file.readline().split('=')[1].replace('\n','')
    # Senha do email remetente
    password = configuration_file.readline().split('=')[1].replace('\n','')
    # Endereços dos emails a serem enviadas as notificacoes
    mail_to = configuration_file.readline().split('=')[1].replace('\n','')
    # Caminho do arquivo de Log
    log_path = configuration_file.readline().split('=')[1].replace('\n','')
    # Tempo de execucao em minutos
    notification_time = int(configuration_file.readline().split('=')[1].replace('\n',''))
    # Informacao sobre a execucao (vai no assunto)
    execution_info = configuration_file.readline().split('=')[1].replace('\n','')
    # Informacao maior sobre a execucao (vai no texto)
    execution_info_largest = configuration_file.readline().split('=')[1].replace('\n','')

    # Serve para repetir o envio dos email (temporario)
    running = 1

    while running > 0:
        # Cria email a ser enviado
        sendmail = SendMail(mail_from, password, mail_to, execution_info, execution_info_largest)

        # Envia email
        sendmail.send()

        # Tempo entre o envio dos emails
        time.sleep(notification_time * 60)
        running -= 1

if __name__ == '__main__':
    main()
