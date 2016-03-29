#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sendmail import *

def main():

    from_mail = 'logexecution@gmail.com'
    password = 'nossasenhaeessa'
    to = 'luisguilherme.ufpi@gmail.com'
    #info_execution = 'execucao 1'
    info_execution = ''

    sendmail = SendMail(from_mail, password, to, info_execution)

    # Envia email
    sendmail.send()

if __name__ == '__main__':
    main()
