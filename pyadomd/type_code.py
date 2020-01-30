from pyadomd import *
import clr
clr.AddReference('System')
from System import Decimal
from datetime import datetime

class Type_code(NamedTuple):
    type_obj:Any
    type_name:str

adomd_type_map:Dict[str, Type_code] = {
    'System.Boolean': Type_code(bool, bool.__name__),
    'System.Decimal': Type_code(lambda x: float(Decimal.ToDouble(x)), float.__name__),
    'System.DateTime': Type_code(lambda x: datetime(x.Year, x.Month, x.Day, x.Hour, x.Minute, x.Second), datetime.__name__),
    'System.Double': Type_code(float, float.__name__),
    'System.Int64': Type_code(int, int.__name__),
    'System.String': Type_code(str, str.__name__)
}

def convert(datatype:str, data:Any, type_map:Dict[str, Any]):
    type_to_convert = type_map[datatype]
    return type_to_convert.type_obj(data)
