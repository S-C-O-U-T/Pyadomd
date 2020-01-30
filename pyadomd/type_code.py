from pyadomd import *
import clr
clr.AddReference('System')
from System import Decimal
from datetime import datetime
from functools import partial

#Types
F = Callable[[Any], Any]
class Type_code(NamedTuple):
    type_obj:F
    type_name:str


def _option_type(datatype, data):
    if data:
        return datatype(data)
    return None

adomd_type_map:Dict[str, Type_code] = {
    'System.Boolean': Type_code(partial(_option_type, bool), bool.__name__),
    'System.Decimal': Type_code(lambda x: Decimal.ToDouble(x) if x else None, float.__name__),
    'System.DateTime': Type_code(lambda x: datetime(x.Year, x.Month, x.Day, x.Hour, x.Minute, x.Second) if x else None, datetime.__name__),
    'System.Double': Type_code(partial(_option_type, float), float.__name__),
    'System.Int64': Type_code(partial(_option_type, int), int.__name__),
    'System.String': Type_code(partial(_option_type, str), str.__name__)
}

def convert(datatype:str, data:Any, type_map:Dict[str, Type_code]):
    type_to_convert = type_map[datatype]
    return type_to_convert.type_obj(data)
