# pyadomd

A pythonic approach to query SSAS data models.

![](https://img.shields.io/pypi/l/pyadomd)
![](https://img.shields.io/pypi/pyversions/pyadomd)
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