#!/usr/bin/python3
# -*- coding: utf-8 -*-

from savings import Savings

from qt_savings import QtSavingsObserver

if __name__ == '__main__':
    qt_savings_observer = QtSavingsObserver()
    savings = Savings(savings_observer=qt_savings_observer)
    savings.start()
