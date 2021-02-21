"""
core.errors -- перечисление ошибок в TBot проекте

Created at 11.12.2019 by pavelmstu.
"""

__author__ = 'pavelmstu'
__maintainer__ = 'pavelmstu'
__credits__ = ['pavelmstu', ]
__status__ = "Development"
__copyright__ = "LGPL, kib.su, 2021"

__version__ = '20210221'


class BaseCriticalTBotException(BaseException):
    """
    Абстрактный класс для всех критических ошибок
    """


class BaseTBotException(Exception):
    """
    Абстрактный класс для всех ошибок
    """


class ConfigException(BaseCriticalTBotException):
    """
    Errors in config env-s.
        For example uncorrect password
    """


class JsonTypeError(BaseTBotException):
    """
    Some error in core.json
    """