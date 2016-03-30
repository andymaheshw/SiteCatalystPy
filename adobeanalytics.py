# -*- coding: utf-8 -*-
"""
Created on Sun Mar 06 00:27:21 2016
@author: maheshwa
"""

from datetime import date, timedelta 
import requests, time, binascii, hashlib, json, urllib #adding hashlib 
import pandas as pd

# Authentication 
class AdobeAnalytics: 
  
    def __init__(self, user_name, shared_secret, endpoint='', debug = False): 
        """ 
        Entry point for making authenticated API calls to the Adobe Report API's 
        """ 
        self.__user_name = user_name 
        self.__shared_secret = shared_secret 
        self.__company = self.__user_name.split(":")[1] 
        self.__debug = debug
          
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
    def __callapi(self, endpoint, verb = "POST", **kwargs):
        header = self.__buildheader()
        if verb == "GET":
            req = requests.get('%s?method=%s' % (self.__api_url, endpoint), params=json.dumps(kwargs), headers=header)
            if self.__debug:
                print json.dumps(kwargs)
        else:
            req = requests.post('%s?method=%s' % (self.__api_url, endpoint), data=json.dumps(kwargs), headers=header)
            if self.__debug:
                print json.dumps(kwargs)
        return req.json()
    
    def GetActivation(self, rsid_list):
        """
        Returns the activation date for the report suite(s) specified.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetActivation', rsid_list = rsid_list)
        
    def GetAxleStartDate(self):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetBaseCurrency(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetBaseCurrency(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetBaseURL(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetBookmarks(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetCalculatedMetrics(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetClassification(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetCustomCalendar(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetDashboards(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetDataWarehouseDisplay(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetDefaultPage(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetDiscoverEnabled(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetEcommerce(self, ):
        return self.__callapi('Company.GetReportSuites', )

    def GetElements(self, ):
        return self.__callapi('Company.GetReportSuites', )
      
    def GetEndpoint(self, company): 
        """ 
        Calls Company.GetEndpoint to determine the appropriate endpoint for a give company 
              
        Keyword arguments: 
        company -- Company to retrieve endpoint for 
        """ 
        return self.__callapi('Company.GetEndpoint', "GET", company = company)
    
    def GetEvars(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetFeed(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetFeeds(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetFunctions(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetFunctions(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetGeoSegmentation(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetGroups(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetInternalURLFilters(self, ):
        return self.__callapi('Company.GetReportSuites', )

    def GetIPAddressExclusions(self, ):
        return self.__callapi('Company.GetReportSuites', )

    def GetIPObfuscation(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetKeyVisitors(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetListVariables(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetLocalization(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetLogin(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetLogins(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetMarketingChannelExpiration(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetMarketingChannelRules(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetMarketingChannels(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetMetrics(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetMobileAppReporting(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetPaidSearchDetection(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetPrivacySettings(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetProps(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetQueue(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetRealTimeReport(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetRealTimeSettings(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetReportDescription(self, ):
        return self.__callapi('Company.GetReportSuites', )
      
    def GetReportSuites(self):
        """Returns all report suites available to user from a given company."""
        return self.__callapi('Company.GetReportSuites')
    
    def GetScheduledSpike(self, ):
        return self.__callapi('Company.GetReportSuites', )

    def GetSegments(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetSiteTitle(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetSuccessEvents(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetTemplate(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetTimeZone(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetTrackingServer(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetTransactionEnabled(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetUniqueVisitorVariable(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetVersionAccess(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetVideoSettings(self, ):
        return self.__callapi('Company.GetReportSuites', )

