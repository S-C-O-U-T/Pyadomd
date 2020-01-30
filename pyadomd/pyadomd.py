from __future__ import annotations
from typing import Iterator, TypeVar, Tuple, List, NamedTuple

#Types
T = TypeVar('T')
class Description(NamedTuple):
    name:str
    type_code:str

import clr # type: ignore
clr.AddReference('Microsoft.AnalysisServices.AdomdClient')
from Microsoft.AnalysisServices.AdomdClient import AdomdConnection, AdomdCommand # type: ignore

from collections import namedtuple

class Cursor:
    
    def __init__(self, connection:AdomdConnection):
        self._conn = connection
        self._description:List[Description] = []


    def close(self) -> None:
        if self.is_closed:
            return
        self._reader.Close()

    def execute(self, query:str) -> Cursor:
        self._cmd = AdomdCommand(query, self._conn)
        self._reader = self._cmd.ExecuteReader()
        self._field_count = self._reader.FieldCount
        
        for i in range(self._field_count):
            self._description.append(Description(self._reader.GetName(i), self._reader.GetFieldType(i).ToString()))

        return self

    def fetchone(self) -> Iterator[Tuple[T, ...]]:
        while(self._reader.Read()):
            yield tuple(self._reader[i] for i in range(self._field_count))

    @property
    def is_closed(self) -> bool:
        try:
            state = self._reader.IsClosed
        except AttributeError:
            return True        
        return state

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