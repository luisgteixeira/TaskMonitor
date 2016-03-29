#!/bin/python
# -*- coding: utf-8 -*-

# Para outras opcoes de email:
# https://blog.butecopensource.org/enviando-emails-com-o-python/

import smtplib

class SendMail(object):

    def __init__(self, from_mail, password, to, info_execution):
        self.from_mail = from_mail
        self.password = password
        self.to = [to]
        # Existe algo na string
        if info_execution:
            self.info_execution = ' (' + info_execution + ')'
        else:
            self.info_execution = info_execution

    def send(self):
        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        smtp.login(self.from_mail, self.password)

        self.from_mail = 'Informação de Log<' + self.from_mail + '>'

        self.msg = """From: %s\nTo: %s\nSubject: Log de Execucao%s

        Email de teste do Log de Execucao.""" % (self.from_mail, ', '.join(self.to), self.info_execution)

        smtp.sendmail(self.from_mail, self.to, self.msg)

        smtp.quit()
