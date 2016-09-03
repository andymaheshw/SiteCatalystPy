import os
import pyadobemc

def test_main():

	'''
	Tests generally test for the presense of a specific key, which tests not
	only that the API was accessed but the expected answer structure was returned.
	Tests don't test that a certain answer was returned, as this can vary based
	on changing admin settings.
	'''

	aa = pyadobemc.AdobeAnalytics(user_name=os.environ['USER'], shared_secret=os.environ['SECRET'])

	assert isinstance(aa.GetActivation(rsid_list = "zwitchdev"), list)

	assert aa.GetAxleStartDate(rsid_list = "zwitchdev")[0]["axle_start_date"] == '2014-02-20'

	assert aa.GetBaseCurrency(rsid_list = "zwitchdev")[0]["base_currency"] == 'USD'

	assert aa.GetBaseURL(rsid_list = "zwitchdev")[0]["base_url"] == 'http://www.randyzwitch.com'

	assert isinstance(aa.GetBookmarks(1,2), dict)

	assert "calculated_metrics" in aa.GetCalculatedMetrics(rsid_list = "zwitchdev")[0]

	#aa.GetClassifications(rsid_list = "zwitchdev")

	assert aa.GetCustomCalendar(rsid_list = "zwitchdev")[0]["calendar_type"] == 'gregorian'

	assert isinstance(aa.GetDashboards(), dict)

	assert aa.GetDataWarehouseDisplay(rsid_list = "zwitchdev")[0]["data_warehouse_display"] == 'all-logins-have-access'

	assert "default_page" in aa.GetDefaultPage(rsid_list = "zwitchdev")[0]

	assert "discover_enabled" in aa.GetDiscoverEnabled(rsid_list = "zwitchdev")[0]

	assert aa.GetEcommerce(rsid_list = "zwitchdev")[0]["ecommerce"]

	#aa.GetElements(reportSuiteID = "zwitchdev")

	assert "evars" in aa.GetEvars(rsid_list = "zwitchdev")[0]

	#aa.GetFeed()
	#aa.GetFeeds()

	assert aa.GetFunctions()[0]["description"]

	assert aa.GetGeoSegmentation(rsid_list = "zwitchdev")[0]["geo_segmentation"]

	assert "group_description" in aa.GetGroups()[0]

	assert "randyzwitch.com" in aa.GetInternalURLFilters(rsid_list = "zwitchdev")[0]["internal_url_filters"]

	assert "ip_address_exclusions" in aa.GetIPAddressExclusions(rsid_list = "zwitchdev")[0]

	assert "ip_obfuscation" in aa.GetIPObfuscation(rsid_list = "zwitchdev")[0]

	assert "key_visitors" in aa.GetKeyVisitors(rsid_list = "zwitchdev")[0]

	assert "list_variables" in aa.GetListVariables(rsid_list = "zwitchdev")[0]

	assert aa.GetLocalization(rsid_list = "zwitchdev")[0]["localization"]

	assert (aa.GetLogin()["first_name"] == "Randy") or (aa.GetLogin()["first_name"] == "Andy")

	assert "email" in aa.GetLogins()[0]

	assert "days" in aa.GetMarketingChannelExpiration(rsid_list = "zwitchdev")[0]

	assert "marketing_channel_rules" in aa.GetMarketingChannelRules(rsid_list = "zwitchdev")[0]

	#Fail
	#aa.GetMetrics(rsid_list = "zwitchdev")

	assert aa.GetMobileAppReporting(rsid_list = "zwitchdev")["allow_configuration"]

	assert "paid_search_detection" in aa.GetPaidSearchDetection(rsid_list = "zwitchdev")[0]

	assert "permanent_traffic" in aa.GetPermanentTraffic(rsid_list = "zwitchdev")[0]

	assert "privacy_settings" in aa.GetPrivacySettings(rsid_list = "zwitchdev")[0]

	assert "props" in aa.GetProps(rsid_list = "zwitchdev")[0]

	assert isinstance(aa.GetQueue(), list)

	#Fail
	#aa.GetRealTimeReport()

	assert "real_time_settings" in aa.GetRealTimeSettings(rsid_list = "zwitchdev")[0]

	#Fail
	#aa.GetReportDescription()

	assert "report_suites" in aa.GetReportSuites()

	assert "scheduled_spike" in aa.GetScheduledSpike(rsid_list = "zwitchdev")[0]

	assert "segments" in aa.GetSegments(rsid_list = "zwitchdev")[0]

	assert "site_title" in aa.GetSiteTitle(rsid_list = "zwitchdev")[0]

	assert  "events" in aa.GetEvents(rsid_list = "zwitchdev")[0]

	assert "template" in aa.GetTemplate(rsid_list = "zwitchdev")[0]

	assert "time_zone" in aa.GetTimeZone(rsid_list = "zwitchdev")[0]

	#Fail
	#aa.GetTrackingServer(rsid_list = "zwitchdev")

	assert "transaction" in aa.GetTransactionEnabled(rsid_list = "zwitchdev")[0]

	assert "unique_visitor_variable" in aa.GetUniqueVisitorVariable(rsid_list = "zwitchdev")[0]

	assert "sc15" in aa.GetVersionAccess()

	assert "video_settings" in aa.GetVideoSettings(rsid_list = "zwitchdev")[0]
