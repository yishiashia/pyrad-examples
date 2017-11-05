import pyrad.packet
from pyrad.client import Client
from pyrad.dictionary import Dictionary
import six
import hmac
import hashlib

dicts=Dictionary("/tmp/dictionaries")

srv=Client(server='localhost',secret='adminsecret',dict=dicts)

req=srv.CreateAuthPacket(code=pyrad.packet.StatusServer)

# 1. set the default Message-Authenticator as 16-bytes zero.
req["Message-Authenticator"] = 16*six.b("\x00")

# 2. get the raw packet binary
raw_packet = req.RequestPacket()

# 3. calculate the hmac-md5 with shared secret
digest = hmac.new('adminsecret', raw_packet, hashlib.md5)

# 4. write back the Message-Authenticator
req["Message-Authenticator"] = digest.hexdigest().decode('hex')

reply=srv.SendPacket(req)

