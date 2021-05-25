from sys import path
path.append('\\Program Files\\Microsoft.NET\\ADOMD.NET\\150')
from pyadomd import Pyadomd

from azure.identity import ClientSecretCredential

scope = 'https://northeurope.asazure.windows.net/.default'

tenant_id = input('Tenant id: ')
client_id = input('Client id: ')
client_secret = input('Client secret: ')
authority = f'https://login.microsoftonline.com/'

credential = ClientSecretCredential(tenant_id, client_id, client_secret, authority=authority)
token = credential.get_token(scope)
serverName = 'asazure://northeurope.asazure.windows.net/aast'

connectionString = f'Provider=MSOLAP;Data Source={serverName};Initial Catalog=Test;User ID=;Password={token.token};Persist Security Info=True;Impersonation Level=Impersonate;'

query = "EVALUATE SUMMARIZECOLUMNS('Sample Data'[Value1])"

with Pyadomd(connectionString) as conn:
    with conn.cursor().execute(query) as cur:
        print(cur.fetchall())