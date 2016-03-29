# -*- coding: utf-8 -*-
"""
Created on Sun Mar 06 00:27:21 2016
@author: maheshwa
"""

from datetime import date, timedelta 
from collections import defaultdict 
import requests, time, binascii, hashlib, json, urllib #adding hashlib 
import pandas as pd 
  
# Authentication 
class AdobeAnalytics: 
  
    def __init__(self, user_name, shared_secret, endpoint=''): 
         """ 
         Entry point for making authenticated API calls to the Adobe Report API's 
         """ 
         self.__user_name = user_name 
         self.__shared_secret = shared_secret 
         self.__company = self.__user_name.split(":")[1] 
          
         #If user doesn't specify their own endpoint, call API to get proper endpoint 
         #Most users should never do this, but some have requested capability in RSiteCatalyst 
         self.__api_url = 'https://api.omniture.com/admin/1.4/rest/' 
         if endpoint != '': 
             self.__api_url = endpoint 
         else: 
             self.__api_url = self.GetEndpoint(company = self.__company) 
  
    def __buildheader(self): 
        """ 
        Returns required header for authenticating API calls. This is an internal method to be used 
        by other public method calls. 
        """ 
        nonce = str(time.time()) 
        base64nonce = binascii.b2a_base64(binascii.a2b_qp(nonce)) 
        created_date = time.strftime("%Y-%m-%dT%H:%M:%SZ",  time.gmtime()) 
        sha_object = hashlib.sha1(nonce + created_date + '%s' % (self.__shared_secret))  
        password_64 = binascii.b2a_base64(sha_object.digest()) 
        X_str = 'UsernameToken Username="%s", PasswordDigest="%s", Nonce="%s", Created="%s"' % ('%s:%s' % (self.__user_name, self.__company), password_64.strip(), base64nonce.strip(), created_date) 
        return {'X-WSSE':X_str} 
        
    #Core Method, Actually runs the JSON request     
    def __callapi(self, endpoint, **kwargs): 
        header = self.__buildheader() 
        req = requests.get('%s?method=%s' % (self.__api_url, endpoint), params=json.dumps(kwargs), headers=header) 
        return req.json() 
      
    def GetEndpoint(self, **kwargs): 
        """ 
        Calls Company.GetEndpoint to determine the appropriate endpoint for a give company 
              
        Keyword arguments: 
        company -- Company to retrieve endpoint for 
        """ 
        return self.__callapi('Company.GetEndpoint', **kwargs) 
       
    # def ReportRun(self): 
    #     # build JSON 
    #     values = {} 
    #     #define endpoint 
    #     endpoint = 'Report.Run' 
    #     __callapi(values, endpoint) 
      
    def GetReportSuites(self, **kwargs):
        """Returns all report suites available to user from a given company."""
        return self.__callapi('Company.GetReportSuites', **kwargs)