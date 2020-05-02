from typing import Any, cast, Callable, Dict, Iterator, List, NamedTuple, Optional, Tuple, TypeVar
import clr
clr.AddReference('System')
from System.IO import FileNotFoundException

from .pyadomd import Pyadomd