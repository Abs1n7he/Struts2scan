#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from colorama import init
#from colorama import Fore, Back, Style, Cursor
from module.colorama import init
from module.colorama import Fore, Back, Style, Cursor
init(autoreset=True)

#Fore是针对字体颜色，Back是针对字体背景颜色，Style是针对字体格式
#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM 暗, NORMAL 正常, BRIGHT 亮, RESET_ALL
class Colored:
    @staticmethod
    def cyan(s):
        return Style.BRIGHT + Fore.CYAN    + s + Fore.RESET + Style.RESET_ALL
    @staticmethod
    def magenta(s):
        return Style.BRIGHT + Fore.MAGENTA + s + Fore.RESET + Style.RESET_ALL
    @staticmethod
    def red(s):
        return Style.BRIGHT + Fore.RED     + s + Fore.RESET + Style.RESET_ALL
    @staticmethod
    def red_twinkle(s):
        return Style.twinkle + Fore.RED     + s + Fore.RESET + Style.RESET_ALL

    @staticmethod
    def green(s):
        return Style.BRIGHT + Fore.GREEN+ s +   Fore.RESET + Style.RESET_ALL
    @staticmethod
    def white(s):
        return Fore.WHITE + s +                Fore.RESET + Style.RESET_ALL

    @staticmethod
    def cyan_fine(s):
        return Fore.CYAN + s +                 Fore.RESET + Style.RESET_ALL
    @staticmethod
    def yellow(s):
        return Style.BRIGHT + Fore.YELLOW + s +  Fore.RESET + Style.RESET_ALL

        
color = Colored()
