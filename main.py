#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sendmail import *

def main():

    sendmail = SendMail()

    # Envia email
    sendmail.send()

if __name__ == '__main__':
    main()
