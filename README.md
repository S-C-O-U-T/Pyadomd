# pyadomd

A pythonic approach to query SSAS data models.

![](https://img.shields.io/pypi/l/pyadomd)
![](https://img.shields.io/pypi/pyversions/pyadomd)
![](https://img.shields.io/badge/windows-10-blue)
[![Documentation Status](https://readthedocs.org/projects/pyadomd/badge/?version=latest)](https://pyadomd.readthedocs.io/en/latest/?badge=latest)

## Installation

```console
pip install pyadomd
```

## Query SSAS Tabular model

```python
from sys import path
path.append('\\Program Files\\Microsoft.NET\\ADOMD.NET\\150')

from pyadomd import Pyadomd

conn_str = 'Provider=MSOLAP;Data Source=localhost;Catalog=AdventureWorks;'
query = """EVALUATE Product"""

with Pyadomd(conn_str) as conn:
    with conn.cursor().execute(query) as cur:
        print(cur.fetchall())
```

## Integrates easily with pandas

```python

from pandas import DataFrame

with Pyadomd(conn_str) as conn:
    with conn.cursor().execute(query) as cur:
        df = DataFrame(cur.fetchone(), columns=[i.name for i in cur.description])
```

## FAQ

Q: I get the following exception?
```C#
System.IO.FileNotFoundException: Unable to find assembly 'Microsoft.AnalysisServices.AdomdClient'.
   at Python.Runtime.CLRModule.AddReference(String name)
```
A: This exception is most likely raised because you have'ent added the folder with the Microsoft.AnalysisServices.AdomdClient.dll to your path, before you import the pyadomd package.

Example:
```Python
from sys import path
path.append('\\Program Files\\Microsoft.NET\\ADOMD.NET\\150') #added to the path _before_ importing the pyadomd package

from pyadomd import Pyadomd
```

Q: When I try to connect the a Azure Analysis Servised instance I get an Authentication faild: User ID and Password are required when user interface is not available?

A: This exception is most likely raised due to you "app" is not registate in Azure.