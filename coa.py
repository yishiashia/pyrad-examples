from pyrad.client import Client, Timeout
from pyrad.dictionary import Dictionary

dicts = Dictionary("/tmp/dictionaries")

srv = Client(server='localhost',secret='adminsecret',dict=dicts)
srv.timeout = 30

attributes = {
  "Alc-Subsc-ID-Str":"00:00:00:00:00:00",
  "Interim-Interval":14400
}

req = srv.CreateCoAPacket(**attributes)
result = client.SendPacket(req)

print result
print result.code
