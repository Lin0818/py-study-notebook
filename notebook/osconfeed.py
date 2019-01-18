# osconfeed.py
from urllib.request import urlopen
import warnings
import os
import json
import ssl

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL, context=gcontext) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())
            
        with open(JSON) as fp:
            return json.load(fp)

feed = load()
print(feed)
#sorted(feed['Schedule'].keys())
