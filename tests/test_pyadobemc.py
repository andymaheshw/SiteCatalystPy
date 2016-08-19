import os
import pyadobemc

def test_main():
	#assert pyadobemc  # use your library here
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

	assert aa.GetGroups()

	assert aa.GetInternalURLFilters(rsid_list = "zwitchdev")

	assert aa.GetIPAddressExclusions(rsid_list = "zwitchdev")

	assert aa.GetIPObfuscation(rsid_list = "zwitchdev")

	assert aa.GetKeyVisitors(rsid_list = "zwitchdev")

	assert aa.GetListVariables(rsid_list = "zwitchdev")

	assert aa.GetLocalization(rsid_list = "zwitchdev")

	assert aa.GetLogin()

	assert aa.GetLogins()

	assert aa.GetMarketingChannelExpiration(rsid_list = "zwitchdev")

	assert aa.GetMarketingChannelRules(rsid_list = "zwitchdev")

	#Fail
	#aa.GetMetrics(rsid_list = "zwitchdev")

	assert aa.GetMobileAppReporting(rsid_list = "zwitchdev")

	assert aa.GetPaidSearchDetection(rsid_list = "zwitchdev")

	assert aa.GetPermanentTraffic(rsid_list = "zwitchdev")

	assert aa.GetPrivacySettings(rsid_list = "zwitchdev")

	assert aa.GetProps(rsid_list = "zwitchdev")

	assert aa.GetQueue()

	#Fail
	#aa.GetRealTimeReport()

	assert aa.GetRealTimeSettings(rsid_list = "zwitchdev")

	#Fail
	#aa.GetReportDescription()

	assert aa.GetReportSuites()

	assert aa.GetScheduledSpike(rsid_list = "zwitchdev")

	assert aa.GetSegments(rsid_list = "zwitchdev")

	assert aa.GetSiteTitle(rsid_list = "zwitchdev")

	assert aa.GetEvents(rsid_list = "zwitchdev")

	assert aa.GetTemplate(rsid_list = "zwitchdev")

	assert aa.GetTimeZone(rsid_list = "zwitchdev")

	#Fail
	#aa.GetTrackingServer(rsid_list = "zwitchdev")

	assert aa.GetTransactionEnabled(rsid_list = "zwitchdev")

	assert aa.GetUniqueVisitorVariable(rsid_list = "zwitchdev")

	assert aa.GetVersionAccess()

	assert aa.GetVideoSettings(rsid_list = "zwitchdev")
