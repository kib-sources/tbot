"""
core.json -- основной json в TBot проете

ИСПОЛЬЗОВАНИЕ:
>> import core.json as json

(!) Не используйте более станрадрный json

"""

__author__ = 'pavelmstu'
__maintainer__ = 'pavelmstu'
__credits__ = ['pavelmstu', ]
__status__ = "Development"

# please, when change this file, set new data!
__version__ = "20211211"

import numpy
import datetime

import json as original_json

from core.errors import JsonTypeError

# Format for datetime when json serializable,
DATETIME_JSON_MESSAGE_FORMAT = '%Y.%m.%d %H:%M:%S'

# default indent in original json is None.
# in core.json default indent is 4, because it is useful for humanS
DEFAULT_INDENT = [None, 4][1]

ELLIPSIS_STR = "..."


def _default(obj):
    if isinstance(obj, datetime.datetime):
        return obj.strftime(DATETIME_JSON_MESSAGE_FORMAT)

    if isinstance(obj, set):
        return list(obj)

    if obj is ...:
        return ELLIPSIS_STR

    if isinstance(obj, dict):
        return obj

    if isinstance(obj, numpy.int64):
        return int(obj)

    to_json = getattr(obj, 'to_json', None)
    if to_json:
        return obj.to_json()

    raise JsonTypeError("type {} is not JSON serializable!".format(type(obj)))


def _load_further_processing(obj):
    if isinstance(obj, list):
        for i, obj_i in enumerate(obj):
            obj[i] = _load_further_processing(obj_i)

    if isinstance(obj, dict):
        for key in obj.keys():
            obj[key] = _load_further_processing(obj[key])

    if isinstance(obj, str):
        # check datetime.datetime
        try:
            obj_d = datetime.datetime.strptime(obj, DATETIME_JSON_MESSAGE_FORMAT)
        except ValueError as _:
            pass
        else:
            return obj_d

        if obj == ELLIPSIS_STR:
            return ...

    return obj


# TODO ПРОТЕСТИРОВАТЬ ЭТО БЕЗОБРАЗИЕ! :)))
#   возможно что-нибудь как-нибудь где-нибудь вдруг... отвалится.


def dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=DEFAULT_INDENT, separators=None,
        sort_keys=False, **kw):

    return original_json.dump(
        obj, fp,
        skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular,
        allow_nan=allow_nan, cls=cls, indent=indent, separators=separators,
        default=_default, sort_keys=sort_keys, **kw
    )


def dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=DEFAULT_INDENT, separators=None,
        sort_keys=False, **kw):

    return original_json.dumps(
        obj,
        skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular,
        allow_nan=allow_nan, cls=cls, indent=indent, separators=separators,
        default=_default, sort_keys=sort_keys, **kw
    )


def load(fp, *, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):

    return original_json.load(
        fp,
        cls=cls, object_hook=object_hook, parse_float=parse_float,
        parse_int=parse_int, parse_constant=parse_constant, object_pairs_hook=object_pairs_hook,
        **kw
    )


def loads(s, *, encoding=None, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):

    return original_json.loads(
        s,
        encoding=encoding, cls=cls, object_hook=object_hook, parse_float=parse_float,
        parse_int=parse_int, parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw
    )