from __future__ import annotations
from pyadomd import *

#Types
T = TypeVar('T')
class Description(NamedTuple):
    name:str
    type_code:str

import clr
clr.AddReference('Microsoft.AnalysisServices.AdomdClient')
from Microsoft.AnalysisServices.AdomdClient import AdomdConnection, AdomdCommand # type: ignore

from pyadomd.type_code import adomd_type_map, convert

class Cursor:
    
    def __init__(self, connection:AdomdConnection):
        self._conn = connection
        self._description:Optional[Description] = None

    def close(self) -> None:
        if self.is_closed:
            return
        self._reader.Close()

    def execute(self, query:str) -> Cursor:
        self._cmd = AdomdCommand(query, self._conn)
        self._reader = self._cmd.ExecuteReader()
        self._field_count = self._reader.FieldCount
        
        for i in range(self._field_count):
            self._description = Description(
                    self._reader.GetName(i), 
                    adomd_type_map[self._reader.GetFieldType(i).ToString()].type_name
                    )
                
        return self

    def fetchone(self) -> Iterator[Tuple[T, ...]]:
        while(self._reader.Read()):
            yield tuple(convert(self._reader.GetFieldType(i).ToString(), self._reader[i], adomd_type_map) for i in range(self._field_count))

    @property
    def is_closed(self) -> bool:
        try:
            state = self._reader.IsClosed
        except AttributeError:
            return True        
        return state

    @property
    def description(self) -> Optional[Description]:
        return self._description

    def __enter__(self) -> Cursor:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()

class Pyadomd:

    def __init__(self, conn_str:str):
        self.conn = AdomdConnection()
        self.conn.ConnectionString = conn_str

    def close(self) -> None:
        self.conn.Close()
    
    def open(self) -> None:
        self.conn.Open()

    def cursor(self) -> Cursor:
        c = Cursor(self.conn)
        return c
    
    @property
    def state(self) -> int:
        return self.conn.State
    
    def __enter__(self) -> Pyadomd:
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()