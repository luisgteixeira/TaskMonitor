#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from sendmail import *
from logmonitor import *
from configuration_loader import *

def main():
    print("Monitoramento iniciado.")

    print("Lendo configuracoes.")
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
    # Informacao sobre a execucao (vai no assunto)
    execution_info = configuration_loader.get_configuration("execution_info")
    # Informacao maior sobre a execucao (vai no texto)
    execution_info_largest = configuration_loader.get_configuration("execution_info_largest")
    print("Configuracoes lidas.")

    logmonitor = LogMonitor(log_path)

    print("Enviando notificacao inicial.")
    initial_msg = "Execucao iniciada."
    sendmail = SendMail(mail_from, password, mail_to, execution_info, execution_info_largest, initial_msg)
    sendmail.send()
    print("Notificacao inicial enviada.")

    minuto = 0

    while True:

        for n in range(1, notification_time):
            sleep(60)

            minuto += 1
            print("===========================================================")
            print("Minuto:", minuto)

            print("Obtendo mensagem.")
            msg = logmonitor.get_message(sendmail.missing_send)
            print("Verificando finalizacao da execucao.")

            if logmonitor.is_finished():
                print("Execucao finalizada.")
                print("Enviando notificacao de termino.")
                sendmail = SendMail(mail_from, password, mail_to, execution_info, execution_info_largest, msg)
                sendmail.send()
                # So encerra quando a ultima messagem tiver sido enviada
                if not sendmail.missing_send:
                    print("Notificacao de termino enviada.")
                    print("Finalizando monitoramento.")
                    exit(0)
                print("Ainda nao foi possivel finalizar o monitoramento. Tentaremos daqui a 1 minuto!")
            else:
                print("Execucao nao finalizada.")

        sleep(60)

        minuto += 1
        print("===========================================================")
        print("Minuto:", minuto)

        print("Enviando notificacao de andamento")
        # Cria email a ser enviado
        msg = logmonitor.get_message(sendmail.missing_send, True)
        print(msg)
        sendmail = SendMail(mail_from, password, mail_to, execution_info, execution_info_largest, msg)

        # Envia
        sendmail.send()
        # So mostra mensagem apos envio confirmado
        if not sendmail.missing_send:
            print("Notificacao de andamento enviada.")

if __name__ == '__main__':
    main()
