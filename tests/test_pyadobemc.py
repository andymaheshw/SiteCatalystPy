import os
import pyadobemc


def test_main():
	assert pyadobemc  # use your library here
	aa = pyadobemc.AdobeAnalytics(user_name=os.environ['USER'], shared_secret=os.environ['SECRET'], debug = True)
	assert isinstance(aa.GetActivation(rsid_list = "zwitchdev"), list) == True
