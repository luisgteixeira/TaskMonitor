#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import *
from time import time

class LogMonitor(object):
    """docstring for LogMonitor"""

    def __init__(self, log_path):
        """Construtor da classe LogMonitor"""
        super(LogMonitor, self).__init__()
        self.log_path = log_path                        # Caminho do arquivo de log
        self.last_update_time = time() # Inicializa tempo
        self.log_readed_lines = 0                       # Numero de linhas do log ja enviadas
        self.finished = False


    def get_message(self, to_send=False):
        """"""
        modified = self.__modification_checker(to_send)
        if modified:
            # Obtem modificacoes do arquivo de log
            self.message = self.__get_log_info(to_send)
            self.__finish_checker()
        else:
            # deve ser enviada uma msg padrao
            self.message = "Ainda em execucao. Nao houve alteracoes desde a ultima verificacao."

        return self.message


    def __modification_checker(self, to_send):
        """Verifica se o arquivo de log foi modificado."""

        # Obtem o tempo da ultima modificacao no arquivo de log
        last_modified_time = getmtime(self.log_path)

        # Verifica se o arquivo foi modificado desde a ultima verificacao
        if last_modified_time > self.last_update_time:
            if to_send:
                self.last_update_time = last_modified_time
            return True
        else:
            return False


    def __get_log_info(self, to_send):
        """Obtem as modificacoes do log"""
        log_file = open(self.log_path)
        log = log_file.readlines()       # obtem as linhas do log em uma lista
        print("Log:", log)
        log_file.close()

        log = log[self.log_readed_lines:]  # obtem apenas as linhas que ainda nao foram lidas

        if to_send:
            self.log_readed_lines += len(log)  # atualiza o numero de linhas lidas

        log_info = ""

        for line in log:
            log_info += line

        return log_info


    def __finish_checker(self):
        """"""
        msg = self.message             # Copia a mensagem
        msg = msg.split("\n")          # Separa por linha
        last_line = msg[len(msg) - 1]  # Pega a ultima linha da mensagem
        if not last_line:
            last_line = msg[len(msg) - 2]
        if last_line.upper() == "END":
            self.finished = True
            msg[len(msg) - 1] = "\nExecucao finalizada!"
            self.message = "\n".join(msg)


    def is_finished(self):
        """"""
        return self.finished
















#
