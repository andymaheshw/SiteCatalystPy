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
        
    def __callapi(self, endpoint, verb = "POST", **kwargs):
        """
        Calls the Adobe Analytics API at a given endpoint and variable arguments
        """
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
        Retrieves the activation status for each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetActivation', rsid_list = rsid_list)
        
    def GetAxleStartDate(self, rsid_list):
        """
        Retrieves the date a report suite was migrated from SiteCatalyst 14 to axle processing (version 15).
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetAxleStartDate', rsid_list = rsid_list)
    
    def GetBaseCurrency(self, rsid_list):
        """
        Retrieves a list of supported currency codes for each of the specified report suites
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetBaseCurrency', rsid_list = rsid_list)
    
    def GetBaseURL(self, rsid_list):
        """
        Retrieves the base URL assigned to each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetBaseURL', rsid_list = rsid_list)
    
    def GetBookmarks(self, ):
        return self.__callapi('Bookmark.GetBookmarks', )
    
    def GetCalculatedMetrics(self, rsid_list):
        """
        Retrieves the calculated metrics assigned to each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetCalculatedMetrics', rsid_list = rsid_list)
    
    def GetClassifications(self, ):
        return self.__callapi('ReportSuite.GetClassifications', )
    
    def GetCustomCalendar(self, rsid_list):
        """
        Retrieves the custom calendar for each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetCustomCalendar', rsid_list = rsid_list)
    
    def GetDashboards(self, ):
        return self.__callapi('Bookmark.GetDashboards', )
    
    def GetDataWarehouseDisplay(self, rsid_list):
        """
        Returns if data warehouse is enabled for the requested report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetDataWarehouseDisplay', rsid_list = rsid_list)
    
    def GetDefaultPage(self, rsid_list):
        """
        Retrieves the default page for each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetDefaultPage', rsid_list = rsid_list)
    
    def GetDiscoverEnabled(self, rsid_list):
        """
        Returns whether ad hoc analysis (formerly Discover) is enabled for the requested report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetDiscoverEnabled', rsid_list = rsid_list)
    
    def GetEcommerce(self, rsid_list):
        """
        Retrieves the commerce level for each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetEcommerce', rsid_list = rsid_list)

    def GetElements(self, ):
        return self.__callapi('Report.GetElements', )
      
    def GetEndpoint(self, company): 
        """ 
        Calls Company.GetEndpoint to determine the appropriate endpoint for a give company 
              
        Keyword arguments: 
        company -- Company to retrieve endpoint for 
        """ 
        return self.__callapi('Company.GetEndpoint', "GET", company = company)
    
    def GetEvars(self, rsid_list):
        """
        Retrieves the commerce variables for each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetEvars', rsid_list = rsid_list)
    
    def GetFeed(self, ):
        return self.__callapi('DataFeed.GetFeed', )
    
    def GetFeeds(self, ):
        return self.__callapi('DataFeed.GetFeeds', )
    
    def GetFunctions(self, ):
        return self.__callapi('CalculatedMetrics.GetFunctions', )
    
    def GetGeoSegmentation(self, rsid_list):
        """
        Retrieves the geography segmentation for the requested report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetGeoSegmentation', rsid_list = rsid_list)
    
    def GetGroups(self, ):
        return self.__callapi('Permissions.GetGroups', )
    
    def GetInternalURLFilters(self, rsid_list):
        """
        Retrieves the internal URL filters for each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetInternalURLFilters', rsid_list = rsid_list)

    def GetIPAddressExclusions(self, rsid_list):
        """
        Returns a list of IP addresses excluded from website tracking for each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetIPAddressExclusions', rsid_list = rsid_list)

    def GetIPObfuscation(self, rsid_list):
        """
        Retrieves the IP Address Obfuscation setting for each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetIPObfuscation', rsid_list = rsid_list)
    
    def GetKeyVisitors(self, rsid_list):
        """
        Retrieves a list of key visitors for each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetKeyVisitors', rsid_list = rsid_list)
    
    def GetListVariables(self, rsid_list):
        """
        Retrieves the list variables for the requested report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetListVariables', rsid_list = rsid_list)
    
    def GetLocalization(self, rsid_list):
        """
        Retrieves the localization (multi-byte character) settings for each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetLocalization', rsid_list = rsid_list)
    
    def GetLogin(self, ):
        return self.__callapi('Permissions.GetLogin', )
    
    def GetLogins(self, ):
        return self.__callapi('Permissions.GetLogins', )
    
    def GetMarketingChannelCosts(self, rsid_list):
        """
        Returns the currently defined Marketing Channel costs for the specified report suite.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetMarketingChannelCosts', rsid_list = rsid_list)
    
    def GetMarketingChannelExpiration(self, rsid_list):
        """
        Returns the currently defined Marketing Channel expiration dates for the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetMarketingChannelExpiration', rsid_list = rsid_list)
    
    def GetMarketingChannelRules(self, rsid_list):
        """
        Returns the currently defined Marketing Channel rules for the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetMarketingChannelRules', rsid_list = rsid_list)
    
    def GetMarketingChannels(self, rsid_list):
        """
        Returns the currently defined Marketing Channels for the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetMarketingChannels',  rsid_list = rsid_list)
    
    def GetMetrics(self, ):
        return self.__callapi('Report.GetMetrics', )
    
    def GetMobileAppReporting(self, rsid_list):
        """
        Retrieves the Mobile Application Tracking settings for the requested report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetMobileAppReporting', rsid_list = rsid_list)
    
    def GetPaidSearchDetection(self, rsid_list):
        """
        Retrieves the paid search settings for each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetPaidSearchDetection', rsid_list = rsid_list)

    def GetPermanentTraffic(self, rsid_list):
        """
        Retrieves the permanent traffic settings for each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetPermanentTraffic', rsid_list = rsid_list)
        
    def GetProcessingStatus(self, rsid_list):
        """
        Returns processing status for the given report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetPermanentTraffic', rsid_list = rsid_list)
    
    
    def GetPrivacySettings(self, rsid_list):
        """
        Returns the activation date for the report suite(s) specified.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetPrivacySettings', rsid_list = rsid_list)
    
    def GetProps(self, rsid_list):
        """
        Retrieves the props (traffic variables) for the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetProps', rsid_list = rsid_list)
    
    def GetQueue(self ):
        return self.__callapi('Report.GetQueue')
    
    def GetRealTimeReport(self, ):
        return self.__callapi('Company.GetReportSuites', )
    
    def GetRealTimeSettings(self, rsid_list):
        """
        Returns the metrics that are configured to provide real time data.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetRealTimeSettings', rsid_list = rsid_list)
    
    def GetReportDescription(self, ):
        return self.__callapi('Bookmark.GetReportDescription', )
      
    def GetReportSuites(self):
        """Returns all report suites available to user from a given company."""
        return self.__callapi('Company.GetReportSuites')
    
    def GetScheduledSpike(self, rsid_list):
        """
        Retrieves the scheduled traffic increase settings for the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetScheduledSpike', rsid_list = rsid_list)

    def GetSegments(self, rsid_list):
        """
        Retrieves the segments that are available in one or more report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetSegments', rsid_list = rsid_list)
    
    def GetSiteTitle(self, rsid_list):
        """
        Retrieves the site title (friendly name) for each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetSiteTitle', rsid_list = rsid_list)
    
    def GetEvents(self, rsid_list):
        """
        Retrieves the success events for each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetEvents', rsid_list = rsid_list)
    
    def GetTemplate(self, rsid_list):
        """
        Retrieves the creation template for each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetTemplate', rsid_list = rsid_list)
    
    def GetTimeZone(self, rsid_list):
        """
        Retrieves the Time Zone setting for each of the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetTimeZone', rsid_list = rsid_list)
    
    def GetTrackingServer(self, rsid_list):
        """
        Returns the activation date for the report suite(s) specified.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('Company.GetTrackingServer', rsid_list = rsid_list)
    
    def GetTransactionEnabled(self, rsid_list):
        """
        Retrieves the transaction ids storage enable for the requested report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetTransactionEnabled', rsid_list = rsid_list)
    
    def GetUniqueVisitorVariable(self, rsid_list):
        """
        Retrieves the unique visitor variable setting for the specified report suites.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetUniqueVisitorVariable', rsid_list = rsid_list)
    
    def GetVersionAccess(self):
        return self.__callapi('Company.GetVersionAccess', )
    
    def GetVideoSettings(self, rsid_list):
        """
        Retrieves video measurement settings.
        
        Keyword arguments: 
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetVideoSettings', rsid_list = rsid_list)  

    def CancelReport(self, report_id):
        """
        Cancels a report

        Keyword arguments:
        report_id -- report to Cancel
        """
        js = '{"reportID": %s}' % (report_id)
        return self.__callapi('Report.Cancel', js)
    