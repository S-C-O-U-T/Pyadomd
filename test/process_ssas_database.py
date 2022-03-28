import json
from sys import path
#added to the path _before_ importing the pyadomd package
path.append("C:\\Program Files\\Microsoft.NET\\ADOMD.NET\\160")

from pyadomd import Pyadomd

exampleNonRowSetQuery = json.dumps({
    "refresh": {
        "type": "full",
        "objects": [
            {
                "database": "<YOUR-SSAS-MODEL>"
            }
        ]
    }
})

conn_str = "Provider=MSOLAP; Data Source=<YOUR-SSAS-SERVER>; Catalog=<YOUR-SSAS-MODEL>"
# This works very similar to the standard execute method, but it just
# executes any script against the ssas service that does not return
# data.
with Pyadomd(conn_str=conn_str) as conn:
    conn.cursor().executeNonQuery(exampleNonRowSetQuery)