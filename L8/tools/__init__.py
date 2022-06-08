'''
Package tools: Beispiel eines Package
'''

# Die Anwesenheit dieses Files sagt Python, dass
# dieser Ordner ein Python-Package ist

# Enthaelt diese File Python-Code, so wird dieser ausgefuehrt.
# z.B.

from tools.tools_for_this.tools import PI
from tools.tools_for_that.tools import E
print('tools/__init__.py executed')
