#!/bin/python
# -*- coding: utf-8 -*-

# Para outras opcoes de email:
# https://blog.butecopensource.org/enviando-emails-com-o-python/

import smtplib

class SendMail(object):

    def __init__(self, mail_from, password, mail_to, execution_info, execution_info_largest, message):
        self.mail_from = mail_from
        self.password = password
        self.mail_to = mail_to.split(',')

        # Existe algo na string
        if execution_info:
            self.execution_info = ' (' + execution_info + ')'
        else:
            self.execution_info = execution_info

        self.execution_info_largest = execution_info_largest
        self.message = message
        self.missing_send = False

    def send(self):
        try:
            smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)

            smtp.login(self.mail_from, self.password)

            self.mail_from = 'Informacao de Log<' + self.mail_from + '>'

            self.msg = """From: %s\nTo: %s\nSubject: Log de Execucao%s\n%s\n\n%s""" % (self.mail_from, ', '.join(self.mail_to), self.execution_info, self.execution_info_largest, self.message)

            smtp.sendmail(self.mail_from, self.mail_to, self.msg)

            smtp.quit()

            self.missing_send = False
        except smtplib.socket.error:
            print("Nao foi possivel enviar o email. Tentaremos daqui a 1 minuto!")
            self.missing_send = True
