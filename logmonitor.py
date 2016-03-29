#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import *
from time import time

class LogMonitor(object):
    """docstring for LogMonitor"""

    def __init__(self, log_path):
        """Construtor da classe LogMonitor"""
        super(LogMonitor, self).__init__()
        self.log_path = log_path        # Caminho do arquivo de log
        self.last_update_time = time()  # Inicializa tempo


    def modification_checker(self):
        """Verifica se o arquivo de log foi modificado."""
        # Obtem o tempo da ultima modificacao no arquivo de log
        last_modified_time = getmtime(self.log_path)

        # Verifica se o arquivo foi modificado desde a ultima verificacao
        if last_modified_time > self.last_update_time:
            self.last_update_time = last_modified_time
            #arquivo deve ser lido para obter alteracoes
        else:
            # deve ser enviada uma msg padrao
            pass
