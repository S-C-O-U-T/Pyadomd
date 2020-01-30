from sys import path
path.append('C:\\Program Files\\Microsoft.NET\\ADOMD.NET\\150')

from configparser import ConfigParser
from pyadomd.pyadomd import Pyadomd

#from utils import get_acces_token

#q = r"""EVALUATE SUMMARIZECOLUMNS('Sample Data'[Value2], 'Sample Data'[Value3], "Sum of Value 1", [Sum of Value 1])"""
q = """EVALUATE SUMMARIZECOLUMNS('Table1'[Boolean], 'Table1'[Currency], 'Table1'[DateTime], 'Table1'[Date], 'Table1'[Floating Point], 'Table1'[Integer], 'Table1'[String], 'Table1'[Time])"""
source = 'https://northeurope.asazure.windows.net'

config = ConfigParser()
config.read('config.ini')
#token = get_acces_token(source,  config['AZURE']['tenantId'],  config['AZURE']['appId'],  config['AZURE']['appSecret'])

data_source = 'asazure://northeurope.asazure.windows.net/aast'
#conn_str = f'Provider=MSOLAP;Data Source={data_source};Initial Catalog=Test;User ID=;Password={token};Persist Security Info=True;Impersonation Level=Impersonate'
conn_str = 'Data Source=127.0.0.1:49959;'

l = []
with Pyadomd(conn_str) as conn:
    with conn.cursor().execute(q) as cur: 
        for i in cur.fetchone(): # type: ignore
            print(i)
            print('*'*10)
            print(type(i[3]))
            print('*'*10)
            l.append(i)

print(cur.description)