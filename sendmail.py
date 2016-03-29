#!/bin/python
# -*- coding: utf-8 -*-

# Para outras opcoes de email:
# https://blog.butecopensource.org/enviando-emails-com-o-python/

import smtplib

class SendMail(object):

    def __init__(self, mail_from, password, mail_to, execution_info, execution_info_largest):
        self.mail_from = mail_from
        self.password = password
        self.mail_to = mail_to.split(',')

        # Existe algo na string
        if execution_info:
            self.execution_info = ' (' + execution_info + ')'
        else:
            self.execution_info = execution_info

        self.execution_info_largest = execution_info_largest

    def send(self):
        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        smtp.login(self.mail_from, self.password)

        self.mail_from = 'Informação de Log<' + self.mail_from + '>'

        self.msg = """From: %s\nTo: %s\nSubject: Log de Execucao%s\n%s\n\nEmail de teste do Log de Execucao.""" % (self.mail_from, ', '.join(self.mail_to), self.execution_info, self.execution_info_largest)

        smtp.sendmail(self.mail_from, self.mail_to, self.msg)

        smtp.quit()
