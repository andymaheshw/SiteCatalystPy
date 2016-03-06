# -*- coding: utf-8 -*-
"""
Created on Sun Mar 06 00:27:21 2016

@author: maheshwa
"""

from datetime import date, timedelta
from collections import defaultdict
import urllib2, time, binascii, sha, json, urllib
import pandas as pd

# Authentication
class sitecatalyst:

    def __init__(self, user_name, shared_secret, company):
        self.user_name = user_name
        self.shared_secret = shared_secret
        self.company = company
    
    def omni_api(values):
        data = urllib.urlencode(values)
        req = urllib2.Request('https://api.omniture.com/admin/1.4/rest/?method=Report.Queue' , json.dumps(values))
        nonce = str(time.time())
        base64nonce = binascii.b2a_base64(binascii.a2b_qp(nonce))
        created_date = time.strftime("%Y-%m-%dT%H:%M:%SZ",  time.gmtime())
        sha_object = sha.new(nonce + created_date + '11927fbf7a71177c88610a00acf8eb50')
        password_64 = binascii.b2a_base64(sha_object.digest())
        X_str = 'UsernameToken Username="%s", PasswordDigest="%s", Nonce="%s", Created="%s"' % ('anirudh.maheshwari:mtv', password_64.strip(), base64nonce.strip(), created_date)
        req.add_header('X-WSSE', X_str)
        response = urllib2.urlopen(req)
        the_page = json.loads(response.read())
        return the_page