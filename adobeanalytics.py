# -*- coding: utf-8 -*-
"""
Created on Sun Mar 06 00:27:21 2016

@author: maheshwa
"""

from datetime import date, timedelta
from collections import defaultdict
import requests, time, binascii, sha, json, urllib #adding hashlib
import pandas as pd

# Authentication
class AdobeAnalytics:
    # Define all variables
    def __init__(self, user_name, shared_secret, company, endpoint='https://api.omniture.com/admin/1.4/rest/'):
        self.__user_name = user_name
        self.__shared_secret = shared_secret
        self.company = company
        self.api_url = endpoint
    
    # Method call to get API Endpoint
    def get_endpoint(self):
        values = {}
        self.api_url = self.omni_api(values, 'Company.GetEndpoint')
             
    #Core Method, Actually runs the JSON request    
    def omni_api(self, json_values, endpoint):
        req = requests.get('%s?method=%s' % (self.api_url, endpoint), json.dumps(json_values))       
        nonce = str(time.time())
        base64nonce = binascii.b2a_base64(binascii.a2b_qp(nonce))
        created_date = time.strftime("%Y-%m-%dT%H:%M:%SZ",  time.gmtime())
        sha_object = sha.new(nonce + created_date + '%s' % (self.__shared_secret))
        password_64 = binascii.b2a_base64(sha_object.digest())
        X_str = 'UsernameToken Username="%s", PasswordDigest="%s", Nonce="%s", Created="%s"' % ('%s:%s' % (self.__user_name, self.company), password_64.strip(), base64nonce.strip(), created_date)
        req.add_header('X-WSSE', X_str)
        response = req.json()
        the_page = response
        return the_page
     
     def ReportRun():
         print "in progress"