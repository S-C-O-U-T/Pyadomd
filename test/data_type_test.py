from sys import path
path.append('\\Program Files\\Microsoft.NET\\ADOMD.NET\\150')
path.append('..\\')
from datetime import datetime

from pyadomd import Pyadomd

localhost = input('Localhost: ')

conn_str = f'Provider=MSOLAP;Data Source={localhost}'
query = """EVALUATE Table1"""

with Pyadomd(conn_str) as conn:
    with conn.cursor().execute(query) as cur:
        test_data = cur.fetchall()

expected = [('Test', 42, 42.42, datetime(2020, 1, 1, 0, 0), 42.42, False, datetime(2020, 1, 1, 0, 0), datetime(2020, 1, 1, 0, 0))
    ,('Test2', 0, 0.0, datetime(2020, 12, 31, 0, 0), 0.0, True, datetime(2020, 12, 31, 0, 0), datetime(2020, 12, 31, 0, 0)),
    ('Test3', None, None, datetime(2020, 12, 31, 0, 0), None, True, datetime(2020, 12, 31, 0, 0), datetime(2020, 12, 31, 0, 0))]

# test each element
for i, j in zip(test_data, expected):
    for z, w in zip(i, j):
        assert z == w
