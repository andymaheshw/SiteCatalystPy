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
        return self.__callapi('ReportSuite.GetAxleStartDate', )
    
    def GetBaseCurrency(self, ):
        return self.__callapi('ReportSuite.GetBaseCurrency', )
    
    def GetBaseURL(self, ):
        return self.__callapi('ReportSuite.GetBaseURL', )
    
    def GetBookmarks(self, ):
        return self.__callapi('Bookmark.GetBookmarks', )
    
    def GetCalculatedMetrics(self, ):
        return self.__callapi('ReportSuite.GetCalculatedMetrics', )
    
    def GetClassifications(self, ):
        return self.__callapi('ReportSuite.GetClassifications', )
    
    def GetCustomCalendar(self, ):
        return self.__callapi('ReportSuite.GetCustomCalendar', )
    
    def GetDashboards(self, ):
        return self.__callapi('Bookmark.GetDashboards', )
    
    def GetDataWarehouseDisplay(self, ):
        return self.__callapi('ReportSuite.GetDataWarehouseDisplay', )
    
    def GetDefaultPage(self, ):
        return self.__callapi('ReportSuite.GetDefaultPage', )
    
    def GetDiscoverEnabled(self, ):
        return self.__callapi('ReportSuite.GetDiscoverEnabled', )
    
    def GetEcommerce(self, ):
        return self.__callapi('ReportSuite.GetEcommerce', )

    def GetElements(self, ):
        return self.__callapi('Report.GetElements', )
      
    def GetEndpoint(self, company): 
        """ 
        Calls Company.GetEndpoint to determine the appropriate endpoint for a give company 
              
        Keyword arguments: 
        company -- Company to retrieve endpoint for 
        """ 
        return self.__callapi('Company.GetEndpoint', "GET", company = company)
    
    def GetEvars(self, ):
        return self.__callapi('ReportSuite.GetEvars', )
    
    def GetFeed(self, ):
        return self.__callapi('DataFeed.GetFeed', )
    
    def GetFeeds(self, ):
        return self.__callapi('DataFeed.GetFeeds', )
    
    def GetFunctions(self, ):
        return self.__callapi('CalculatedMetrics.GetFunctions', )
    
    def GetGeoSegmentation(self, ):
        return self.__callapi('ReportSuite.GetGeoSegmentation', )
    
    def GetGroups(self, ):
        return self.__callapi('Permissions.GetGroups', )
    
    def GetInternalURLFilters(self, ):
        return self.__callapi('ReportSuite.GetInternalURLFilters', )

    def GetIPAddressExclusions(self, ):
        return self.__callapi('ReportSuite.GetIPAddressExclusions', )

    def GetIPObfuscation(self, ):
        return self.__callapi('ReportSuite.GetIPObfuscation', )
    
    def GetKeyVisitors(self, ):
        return self.__callapi('ReportSuite.GetKeyVisitors', )
    
    def GetListVariables(self, ):
        return self.__callapi('ReportSuite.GetListVariables', )
    
    def GetLocalization(self, ):
        return self.__callapi('ReportSuite.GetLocalization', )
    
    def GetLogin(self, ):
        return self.__callapi('Permissions.GetLogin', )
    
    def GetLogins(self, ):
        return self.__callapi('Permissions.GetLogins', )
    
    def GetMarketingChannelExpiration(self, ):
        return self.__callapi('ReportSuite.GetMarketingChannelExpiration', )
    
    def GetMarketingChannelRules(self, ):
        return self.__callapi('ReportSuite.GetMarketingChannelRules', )
    
    def GetMarketingChannels(self, ):
        return self.__callapi('ReportSuite.GetMarketingChannels', )
    
    def GetMetrics(self, ):
        return self.__callapi('Report.GetMetrics', )
    
    def GetMobileAppReporting(self, ):
        return self.__callapi('ReportSuite.GetMobileAppReporting', )
    
    def GetPaidSearchDetection(self, ):
        return self.__callapi('ReportSuite.GetPaidSearchDetection', )
    
    def GetPrivacySettings(self, ):
        return self.__callapi('ReportSuite.GetPrivacySettings', )
    
    def GetProps(self, ):
        return self.__callapi('ReportSuite.GetProps', )
    
    def GetQueue(self, ):
        return self.__callapi('Report.GetQueue', )
    
    def GetRealTimeReport(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetRealTimeSettings(self, ):
        return self.__callapi('ReportSuite.GetRealTimeSettings', )
    
    def GetReportDescription(self, ):
        return self.__callapi('Bookmark.GetReportDescription', )
      
    def GetReportSuites(self):
        """Returns all report suites available to user from a given company."""
        return self.__callapi('Company.GetReportSuites')
    
    def GetScheduledSpike(self, ):
        return self.__callapi('ReportSuite.GetScheduledSpike', )

    def GetSegments(self, ):
        return self.__callapi('ReportSuite.GetSegments', )
    
    def GetSiteTitle(self, ):
        return self.__callapi('ReportSuite.GetSiteTitle', )
    
    def GetEvents(self, ):
        return self.__callapi('ReportSuite.GetEvents', )
    
    def GetTemplate(self, ):
        return self.__callapi('ReportSuite.GetTemplate', )
    
    def GetTimeZone(self, ):
        return self.__callapi('ReportSuite.GetTimeZone', )
    
    def GetTrackingServer(self, ):
        return self.__callapi('Company.GetTrackingServer', )
    
    def GetTransactionEnabled(self, ):
        return self.__callapi('ReportSuite.GetTransactionEnabled', )
    
    def GetUniqueVisitorVariable(self, ):
        return self.__callapi('ReportSuite.GetUniqueVisitorVariable', )
    
    def GetVersionAccess(self, ):
        return self.__callapi('Company.GetVersionAccess', )
    
    def GetVideoSettings(self, ):
        return self.__callapi('ReportSuite.GetVideoSettings', )

