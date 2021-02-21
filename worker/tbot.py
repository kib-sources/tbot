"""
worker.tbot

Запускаемый файл
created by pavel in pavel as 2/21/21
Проект tbot
"""

import datetime

__author__ = 'pavelmstu'
__maintainer__ = 'pavelmstu'
__credits__ = ['pavelmstu', ]
__copyright__ = "LGPL, kib.su 2021"
__status__ = 'Development'

__version__ = '20210221'

from time import sleep

import signal

# TODO
#   https://docs.python.org/3/library/argparse.html
import argparse

parser = argparse.ArgumentParser(
    description='Чат бот, который ....',
)

'''
parser.add_argument(
    '-t',
    dest='...',
    help='...',
    default=None,
)
# '''


_is_get_SIGINT = False


def signal_handler(sig, frame):
    global _is_get_SIGINT
    print("STOP all processes")
    _is_get_SIGINT = True


def is_end():
    global _is_get_SIGINT
    if _is_get_SIGINT:
        return True
    # TODO
    # ...
    return False


def main(args):
    print(datetime.datetime.now())

    while not is_end():

        # ...
        sleep(0.1)
        continue

    # Действия после остановки
    #  TODO
    #   ...
    return


if __name__ == "__main__":
    # TODO +SIGTERM, + ???
    signal.signal(signal.SIGINT, signal_handler)

    args = parser.parse_args()
    main(args)
else:
    raise Exception("Данный модуль может быть только запускаем!")