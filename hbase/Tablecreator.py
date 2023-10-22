#!/usr/bin/env python3

import happybase

# Connect to HBase :
connection = happybase.Connection(host='localhost', port=16030)
   
table = connection.table('MyTable')

print(table.name)

table.put(b'row5', {b'amin:a': b'hello'})
