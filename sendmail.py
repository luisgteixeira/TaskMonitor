#!/bin/python
# -*- coding: utf-8 -*-

# Para outras opcoes de email:
# https://blog.butecopensource.org/enviando-emails-com-o-python/

import smtplib

class SendMail:

    def send(self):
        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        smtp.login('logexecution@gmail.com', 'nossasenhaeessa')

        de = 'logexecution@gmail.com'
        para = ['luisguilherme.ufpi@gmail.com']
        msg = """From: %s
        To: %s
        Subject: Log de Execucao

        Email de teste do Log de Execucao.""" % (de, ', '.join(para))

        smtp.sendmail(de, para, msg)

        smtp.quit()
