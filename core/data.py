"""
core.data

Содержит в себе все датаклассы и другие параметры, необходимые для работы с данными

created by pavelmstu in 2/21/21
Проект tbot
"""

import datetime

from enum import Enum

from dataclasses import dataclass

from typing import Optional, List, Tuple, Dict, Union

__author__ = 'pavelmstu'
__maintainer__ = 'pavelmstu'
__credits__ = ['pavelmstu', ]
__copyright__ = "LGPL, kib.su, 2021"
__status__ = 'Development'

__version__ = '20210221'

# TODO когда этот файл разрастётся, то нужно будет его разбить
#   core/data/__init__.py
#   core/data/......py
#   ....


class Position(Enum):
    """
    >> Participant.position
    """

    # студент МГТУ или другого ВУЗ-а
    Student = "student"

    # Активист СКИБ-а, имеющий привелегии при поступлении/правил отчисления и т.д
    KibStudent = 'kib_student'

    # Активист КИБ-а, читающий спецкурсы, мастер-классы, проводящий открытые лекции
    Mentor = 'mentor'

    # TODO
    #   подумать какие ещё есть позиции


@dataclass
class Participant:

    # ник в телеграмме
    # TODO сделать проверку, что начинается всегда с "@"
    telegram_nick: str

    # фамилия
    soname: str

    # имя
    name: str

    # отчество
    patronym: Optional[str] = None

    # университет
    university: str = 'bmstu'

    # Стастус слушателя.
    position:  Position = Position.Student.value


@dataclass
class Event:
    """
    Некое разовое событие, на которое можно подписатся
    """

    # название
    title: str

    # краткое описание
    theses: str

    # Дата события
    data: datetime.date

    # время начала и окончания события по Московскому времени
    t1: datetime.datetime
    t2: datetime.datetime

    # TODO аналогично Position сделать EventType
    # eventType: EventType = EventType.Default.value

    def subscribe(self, participant: Participant):
        """
        добавить участника
        :param participant:
        :return:
        """
        return NotImplemented


@dataclass
class Course:

    # TODO написать поля
    # ...

    @property
    def Events(self) -> List[Event]:
        """
        Список всех событий данного курса
        :return:
        """
        # return list()
        return NotImplemented

    def add(self, event: Event) -> type(None):
        """
        добавить событие к данному курсу
        :param Event:
        :return:
        True
        False
        """

        # поместить Event в базу данных если его ещё нет в базе данных
        # поместить self в базу данных, если его ещё нет в базе данных
        # сделать связь между Event и self

        return NotImplemented

    def subscribe(self, participant: Participant):
        """
        добавить участника
        :param participant:
        :return:
        """
        return NotImplemented


@dataclass
class TMessage:
    """
    Одно сообщение в телеграмме
    :return:
    """

    # TODO
    text: str


