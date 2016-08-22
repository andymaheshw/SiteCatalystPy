# -*- coding: utf-8 -*-
"""
Created on Sun Mar 06 00:27:21 2016
@author: maheshwa
"""

from __future__ import print_function
import requests
import time
import binascii
import hashlib
import json


# Authentication
class AdobeAnalytics:

    def __init__(self, user_name, shared_secret, endpoint='', debug=False):
        """
        Entry point for making authenticated API calls to the Adobe Report API's
        """
        self.__user_name = user_name
        self.__shared_secret = shared_secret
        self.__company = self.__user_name.split(":")[1]
        self.__debug = debug

        # If user doesn't specify their own endpoint, call API to get proper endpoint
        # Most users should never do this, but some have requested capability in RSiteCatalyst
        self.__api_url = 'https://api.omniture.com/admin/1.4/rest/'
        if endpoint != '':
            self.__api_url = endpoint
        else:
            self.__api_url = self.GetEndpoint(company=self.__company)

    def __buildheader(self):
        """
        Returns required header for authenticating API calls. This is an internal method to be used
        by other public method calls.
        """
        nonce = str(time.time())
        base64nonce = binascii.b2a_base64(binascii.a2b_qp(nonce)).decode('utf-8')
        created_date = time.strftime("%Y-%m-%dT%H:%M:%SZ",  time.gmtime())
        sha_object = hashlib.sha1((nonce + created_date + '%s' % (self.__shared_secret)).encode('utf-8'))
        password_64 = binascii.b2a_base64(sha_object.digest()).decode('utf-8')
        X_str = 'UsernameToken Username="%s", PasswordDigest="%s", Nonce="%s", Created="%s"' % (
            '%s:%s' % (self.__user_name, self.__company), password_64, base64nonce, created_date)
        return {'X-WSSE': X_str}

    def __callapi(self, endpoint, verb="POST", **kwargs):
        """
        Calls the Adobe Analytics API at a given endpoint and variable arguments
        """

        # Automatically convert an rsid_list string type to list as required by API
        if "rsid_list" in kwargs and isinstance(kwargs["rsid_list"], str):
            kwargs["rsid_list"] = [kwargs["rsid_list"]]

        header = self.__buildheader()
        if verb == "GET":
            req = requests.get('%s?method=%s' % (self.__api_url, endpoint), params=json.dumps(kwargs), headers=header)
            if self.__debug:
                print(json.dumps(kwargs))
        else:
            req = requests.post('%s?method=%s' % (self.__api_url, endpoint), data=json.dumps(kwargs), headers=header)
            if self.__debug:
                print(json.dumps(kwargs))
        return req.json()

    def GetActivation(self, rsid_list):
        """
        Retrieves the activation status for each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetActivation', rsid_list=rsid_list)

    def GetAxleStartDate(self, rsid_list):
        """
        Retrieves the date a report suite was migrated from SiteCatalyst 14 to axle processing (version 15).

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetAxleStartDate', rsid_list=rsid_list)

    def GetBaseCurrency(self, rsid_list):
        """
        Retrieves a list of supported currency codes for each of the specified report suites

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetBaseCurrency', rsid_list=rsid_list)

    def GetBaseURL(self, rsid_list):
        """
        Retrieves the base URL assigned to each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetBaseURL', rsid_list=rsid_list)

    def GetBookmarks(self, folder_limit=None, folder_offset=None):
        """
        Retrieves a list of bookmarks for the authenticated user.

        Keyword arguments:
        folder_limit -- (optional) Limit the retrieval to the specified number of bookmarks.
        folder_offset -- (optional) Start the bookmark retrieval at the specified offset.
        """
        report_description = {}
        if folder_limit:
            report_description["folder_limit"] = folder_limit
        if folder_offset:
            report_description["folder_offset"] = folder_limit

        return self.__callapi('Bookmark.GetBookmarks', report_description=report_description)

    def GetCalculatedMetrics(self, rsid_list):
        """
        Retrieves the calculated metrics assigned to each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetCalculatedMetrics', rsid_list=rsid_list)

    def GetClassifications(self, rsid_list, element_list=[]):
        """
        Retrieves a list of classifications (associated with the specified element) for each of the
        specified report suites.

        Keyword arguments:
        rsid_list = Single report suite id or list of report suites
        """
        return self.__callapi('ReportSuite.GetClassifications', rsid_list=rsid_list, element_list=element_list)

    def GetCustomCalendar(self, rsid_list):
        """
        Retrieves the custom calendar for each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetCustomCalendar', rsid_list=rsid_list)

    def GetDashboards(self, ):
        return self.__callapi('Bookmark.GetDashboards', )

    def GetDataWarehouseDisplay(self, rsid_list):
        """
        Returns if data warehouse is enabled for the requested report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetDataWarehouseDisplay', rsid_list=rsid_list)

    def GetDefaultPage(self, rsid_list):
        """
        Retrieves the default page for each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetDefaultPage', rsid_list=rsid_list)

    def GetDiscoverEnabled(self, rsid_list):
        """
        Returns whether ad hoc analysis (formerly Discover) is enabled for the requested report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetDiscoverEnabled', rsid_list=rsid_list)

    def GetEcommerce(self, rsid_list):
        """
        Retrieves the commerce level for each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetEcommerce', rsid_list=rsid_list)

    def GetElements(self, rsid_list, elements=[], metrics=[]):
        """
       Get Valid Elements for a Report Suite

       Keyword arguments:
       rsid_list -- Single report suite id, or character vector of report suite ids
       metrics -- list of existing metrics you want to use in combination with an additional metric
       elements -- list of existing elements you want to use in combination with an additional metric

        """
        result = {}
        for report in rsid_list:
            result[report] = self.__callapi('Report.GetElements', reportSuiteID=report, existingElements=elements,
                                            existingMetrics=metrics)
        return result

    def GetEndpoint(self, company):
        """
        Calls Company.GetEndpoint to determine the appropriate endpoint for a give company

        Keyword arguments:
        company -- Company to retrieve endpoint for
        """
        return self.__callapi('Company.GetEndpoint', "GET", company=company)

    def GetEvars(self, rsid_list):
        """
        Retrieves the commerce variables for each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetEvars', rsid_list=rsid_list)

    def GetFeed(self, feed_id):
        """
        Get Data Feed Detail for a specific feed

        Keyword arguments:
        feed_id -- Data Feed ID
        """
        return self.__callapi('DataFeed.GetFeed', feed_id=feed_id)

    def GetFeeds(self, rsid_list, start_time="", end_time="", status=[]):
        """
        Get Data Feed Detail for a Report Suite(s)

        Keyword arguments:
        rsid_list -- Report suite id (or list of report suite ids)
        start_time -- Beginning of time period you want to check
        end_time -- End of time period you want to check
        status -- Character vector/list of statuses to filter by

        Example:
        feeds2 = GetFeeds("zwitchdev", "2014-12-02 05:00:00", "2014-12-03 05:00:00")
        """
        return self.__callapi('DataFeed.GetFeeds', rsid_list=rsid_list, status=status, start_time="", end_time="")

    def GetFunctions(self, ):
        return self.__callapi('CalculatedMetrics.GetFunctions', )

    def GetGeoSegmentation(self, rsid_list):
        """
        Retrieves the geography segmentation for the requested report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetGeoSegmentation', rsid_list=rsid_list)

    def GetGroups(self, ):
        return self.__callapi('Permissions.GetGroups', )

    def GetInternalURLFilters(self, rsid_list):
        """
        Retrieves the internal URL filters for each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetInternalURLFilters', rsid_list=rsid_list)

    def GetIPAddressExclusions(self, rsid_list):
        """
        Returns a list of IP addresses excluded from website tracking for each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetIPAddressExclusions', rsid_list=rsid_list)

    def GetIPObfuscation(self, rsid_list):
        """
        Retrieves the IP Address Obfuscation setting for each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetIPObfuscation', rsid_list=rsid_list)

    def GetKeyVisitors(self, rsid_list):
        """
        Retrieves a list of key visitors for each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetKeyVisitors', rsid_list=rsid_list)

    def GetListVariables(self, rsid_list):
        """
        Retrieves the list variables for the requested report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetListVariables', rsid_list=rsid_list)

    def GetLocalization(self, rsid_list):
        """
        Retrieves the localization (multi-byte character) settings for each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetLocalization', rsid_list=rsid_list)

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
        return self.__callapi('ReportSuite.GetMarketingChannelCosts', rsid_list=rsid_list)

    def GetMarketingChannelExpiration(self, rsid_list):
        """
        Returns the currently defined Marketing Channel expiration dates for the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetMarketingChannelExpiration', rsid_list=rsid_list)

    def GetMarketingChannelRules(self, rsid_list):
        """
        Returns the currently defined Marketing Channel rules for the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetMarketingChannelRules', rsid_list=rsid_list)

    def GetMarketingChannels(self, rsid_list):
        """
        Returns the currently defined Marketing Channels for the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetMarketingChannels',  rsid_list=rsid_list)

    def GetMetrics(self, rsid_list, elements=[], metrics=[]):
        """
        Get Valid Metrics for a Report Suite

       Keyword arguments:
       rsid_list -- Single report suite id, or character vector of report suite ids
       metrics -- list of existing metrics you want to use in combination with an additional metric
       elements -- list of existing elements you want to use in combination with an additional metric

        """
        result = {}
        for report in rsid_list:
            result[report] = self.__callapi('Report.GetMetrics', reportSuiteID=report, existingElements=elements,
                                            existingMetrics=metrics)
        return result

    def GetMobileAppReporting(self, rsid_list):
        """
        Retrieves the Mobile Application Tracking settings for the requested report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetMobileAppReporting', rsid_list=rsid_list)

    def GetPaidSearchDetection(self, rsid_list):
        """
        Retrieves the paid search settings for each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetPaidSearchDetection', rsid_list=rsid_list)

    def GetPermanentTraffic(self, rsid_list):
        """
        Retrieves the permanent traffic settings for each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetPermanentTraffic', rsid_list=rsid_list)

    def GetProcessingStatus(self, rsid_list):
        """
        Returns processing status for the given report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetPermanentTraffic', rsid_list=rsid_list)

    def GetPrivacySettings(self, rsid_list):
        """
        Returns the activation date for the report suite(s) specified.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetPrivacySettings', rsid_list=rsid_list)

    def GetProps(self, rsid_list):
        """
        Retrieves the props (traffic variables) for the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetProps', rsid_list=rsid_list)

    def GetQueue(self, ):
        return self.__callapi('Report.GetQueue')

    def GetRealTimeReport(self, rsid_list, metrics=[], elements=[], date_granularity=5,
                          date_from="1 hour ago", date_to="now", sort_algorithm="mostpopular",
                          floor_sensitivity=.25, first_rank_period=0,
                          algorithm_argument="linear", everything_else=True,
                          selected=[]):
        """
        Function to access the Adobe Analytics Real-Time API v1.4.
        This API provides the ability for reporting up to the most recent minute.
        This API is best used at 15-30 second intervals (or longer).

        keyword arguments:
        rsid_list -- Report Suite
        metrics -- Report metric
        elements -- Report breakdowns
        date_granularity -- Report Granularity. Defaults to 5 minutes
        date_from -- Report starting time. Defaults to "1 hour ago"
        date_to -- Report end time. Defaults to "now"
        sort_algorithm -- Sorting algorithm. Defaults to "mostpopular"
        floor_sensitivity -- Floor sensitivity. Defaults to .25
        first_rank_period -- First Ranking Period. Defaults to 0
        algorithm_argument -- Ranking algorithm. Defaults to "linear"
        everything_else -- Provide counts for elements not returned as 'top'
        selected -- Selected items for a given element (only works for a single element)
        """
        return self.__callapi('Report.Run', rsid_list=rsid_list, metrics=metrics, elements=[])

    def GetRealTimeSettings(self, rsid_list):
        """
        Returns the metrics that are configured to provide real time data.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetRealTimeSettings', rsid_list=rsid_list)

    def GetReportDescription(self, bookmark):
        """
        Get report description for a specific bookmark_id

        keyword arguments:
        bookmark -- Bookmark ID

        """

        return self.__callapi('Bookmark.GetReportDescription', bookmark_id=bookmark)

    def GetReportSuites(self):
        """Returns all report suites available to user from a given company."""
        return self.__callapi('Company.GetReportSuites')

    def GetScheduledSpike(self, rsid_list):
        """
        Retrieves the scheduled traffic increase settings for the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetScheduledSpike', rsid_list=rsid_list)

    def GetSegments(self, rsid_list):
        """
        Retrieves the segments that are available in one or more report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetSegments', rsid_list=rsid_list)

    def GetSiteTitle(self, rsid_list):
        """
        Retrieves the site title (friendly name) for each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetSiteTitle', rsid_list=rsid_list)

    def GetEvents(self, rsid_list):
        """
        Retrieves the success events for each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetEvents', rsid_list=rsid_list)

    def GetTemplate(self, rsid_list):
        """
        Retrieves the creation template for each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetTemplate', rsid_list=rsid_list)

    def GetTimeZone(self, rsid_list):
        """
        Retrieves the Time Zone setting for each of the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetTimeZone', rsid_list=rsid_list)

    def GetTrackingServer(self, rsid):
        """
        Returns the activation date for the report suite(s) specified.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('Company.GetTrackingServer', rsid=rsid)

    def GetTransactionEnabled(self, rsid_list):
        """
        Retrieves the transaction ids storage enable for the requested report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetTransactionEnabled', rsid_list=rsid_list)

    def GetUniqueVisitorVariable(self, rsid_list):
        """
        Retrieves the unique visitor variable setting for the specified report suites.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetUniqueVisitorVariable', rsid_list=rsid_list)

    def GetVersionAccess(self):
        return self.__callapi('Company.GetVersionAccess',)

    def GetVideoSettings(self, rsid_list):
        """
        Retrieves video measurement settings.

        Keyword arguments:
        rsid_list -- Report suites to evaluate
        """
        return self.__callapi('ReportSuite.GetVideoSettings', rsid_list=rsid_list)

    def CancelReport(self, report_id):
        """
        Cancels a report

        Keyword arguments:
        report_id -- report to Cancel
        """
        js = '{"reportID": %s}' % (report_id)
        return self.__callapi('Report.Cancel', js=js)

    def ValidateReport(self, report_description, interval_seconds=0, max_attempts=1):
        """
        Checks if report is valid

        Keyword arguments:
        report_description  -- json of the report
        interval_seconds -- how long to wait
        max_attempts -- how
        """
        return self.__callapi('Report.Validate', report_description=report_description)
