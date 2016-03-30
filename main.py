#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from sendmail import *
from logmonitor import *
from configuration_loader import *

def main():

    configuration_loader = ConfigurationLoader()
    configuration_loader.load_configurations()

    # Endereço do email remetente
    mail_from = configuration_loader.get_configuration("mail_from")
    # Senha do email remetente
    password = configuration_loader.get_configuration("password")
    # Endereços dos emails a serem enviadas as notificacoes
    mail_to = configuration_loader.get_configuration("mail_to")
    # Caminho do arquivo de Log
    log_path = configuration_loader.get_configuration("log_path")
    # Tempo de execucao em minutos
    notification_time = int(configuration_loader.get_configuration("notification_time"))
    notification_time *= 60
    # Informacao sobre a execucao (vai no assunto)
    execution_info = configuration_loader.get_configuration("execution_info")
    # Informacao maior sobre a execucao (vai no texto)
    execution_info_largest = configuration_loader.get_configuration("execution_info_largest")

    # Serve para repetir o envio dos email (temporario)
    running = 3

    logmonitor = LogMonitor("log.txt")

    while running > 0:

        print(logmonitor.get_message())

        notification_time = 60

        # Cria email a ser enviado
        # sendmail = SendMail(mail_from, password, mail_to, execution_info)
        #sendmail = SendMail(mail_from, password, mail_to, execution_info, execution_info_largest)

        # Envia email
        # sendmail.send()

        # Tempo entre o envio dos emails
        sleep(notification_time)
        running -= 1

if __name__ == '__main__':
    main()
