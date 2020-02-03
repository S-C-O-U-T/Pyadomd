Getting Started
===============

A pythonic approach to query SSAS data models.

.. image:: https://img.shields.io/pypi/l/pyadomd.svg
    :target: https://pypi.org/project/pyadomd/

.. image:: https://img.shields.io/pypi/pyversions/pyadomd.svg
    :target: https://pypi.org/project/pyadomd/

.. image:: https://readthedocs.org/projects/pyadomd/badge/?version=latest
    :target: https://pyadomd.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Installation
------------
``pip install pyadomd``

Query SSAS Tabular model
------------------------

.. code-block:: python
    
    from sys import path
    path.append('\\Program Files\\Microsoft.NET\\ADOMD.NET\\150')

    from pyadomd import Pyadomd
    
    conn_str = 'Provider=MSOLAP;Data Source=localhost;Catalog=AdventureWorks;'
    query = """EVALUATE Product"""
    
    with Pyadomd(conn_str) as conn:
        with conn.cursor().execute(query) as cur:
            print(cur.fetchall())

Integrates easily with pandas
-----------------------------

.. code-block:: python

    from pandas import DataFrame

    with Pyadomd(conn_str) as conn:
        with conn.cursor().execute(q) as cur:
            df = DataFrame(cur.fetchone(), 
            columns=[i.name for i in cur.description])