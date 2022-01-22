"""
Copyright 2020 SCOUT

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from pyadomd import *
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
    if datatype in [bool, int, float] and data == 0:
        return datatype(data)
    return None

adomd_type_map:Dict[str, Type_code] = {
    'System.Boolean': Type_code(partial(_option_type, bool), bool.__name__),
    'System.DateTime': Type_code(lambda x: datetime(x.Year, x.Month, x.Day, x.Hour, x.Minute, x.Second) if x else None, datetime.__name__),
    'System.Decimal': Type_code(lambda x: Decimal.ToDouble(x) if x else None, float.__name__),
    'System.Double': Type_code(partial(_option_type, float), float.__name__),
    'System.Single': Type_code(partial(_option_type, float), float.__name__),
    'System.String': Type_code(partial(_option_type, str), str.__name__),
    'System.Guid': Type_code(partial(_option_type, str), str.__name__),
    'System.UInt16': Type_code(partial(_option_type, int), int.__name__),
    'System.UInt32': Type_code(partial(_option_type, int), int.__name__),
    'System.UInt64': Type_code(partial(_option_type, int), int.__name__),
    'System.Int16': Type_code(partial(_option_type, int), int.__name__),
    'System.Int32':  Type_code(partial(_option_type, int), int.__name__),
    'System.Int64': Type_code(partial(_option_type, int), int.__name__),
    'System.Object': Type_code(lambda x: x, 'System.Object'),
}

def convert(datatype:str, data:Any, type_map:Dict[str, Type_code]):
    type_to_convert = type_map[datatype]
    return type_to_convert.type_obj(data)
