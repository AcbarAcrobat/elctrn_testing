import json
import requests
import urllib3
import logging
import os
from support.config import config
ENV = os.environ.get("CI_COMMIT_REF_SLUG")
#url = "https://{CI_COMMIT_REF_SLUG}.sphaera-cti-service.stage.sphaera.ru"
url = config.get('url')


class TestApi:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    LOGGER = logging.getLogger(__name__)

    def test_get_operators_list(self):
        r = requests.get(url + "/api/operators", verify=False, headers={"Content-Type": "application/json"})
        if 200 == r.status_code:
            pass
        else:
            raise AssertionError and print("test_get_operators_list doesn't have code status 200")
        print(TestApi.LOGGER.info(r.status_code))

    def test_post_login_with_extension(self):
        m = {'extension': '105'}
        r = requests.post(url + "/api/operators", verify=False, data=json.dumps(m), headers={"Content-Type": "application/json"})
        assert r.status_code == 200
        print(TestApi.LOGGER.info(r.status_code))
        if 'userName' in r.json() and r.json()['userName'] == 'Татьяна Сахарова':
            pass
        else:
            raise AssertionError and print('login with 105 extension doesnt get result Tatyana Saharova')

    def test_api_calls_time(self):
        m = {'extension': '105'}
        rj = {"status": "None"}
        r = requests.get(url + "/api/calls/regulatorytimestatus", verify=False, data=json.dumps(m), headers={"Content-Type": "application/json"})
        if 200 == r.status_code:
            pass
        else:
            raise AssertionError and print("test_api_calls_time doesn't have code status 200")
        if r.json() == rj:
            pass
        else:
            raise AssertionError and print("test_api_calls_time doesn't have {'status': 'None'}")
        print(TestApi.LOGGER.info(r.status_code))

    def test_api_checktraces(self):
        r = requests.get(url + "/api/checktraces", verify=False, headers={"Content-Type": "application/json"})
        if 200 == r.status_code:
            pass
        else:
            raise AssertionError and print("test_api_checktraces doesn't have code status 200")
        print(TestApi.LOGGER.info(r.status_code))

    def test_get_active_operators(self):
        r = requests.get(url + "/api/operators/active", verify=False, headers={"Content-Type": "application/json"})
        if 200 == r.status_code:
            pass
        else:
            raise AssertionError and print("test_get_active_operators doesn't have code status 200")
        print(TestApi.LOGGER.info(r.status_code))

    def test_get_calls_count(self):
        m = {'extension': '105'}
        r = requests.get(url + "/api/calls/count/105", verify=False, data=json.dumps(m), headers={"Content-Type": "application/json"})
        if 200 == r.status_code:
            pass
        else:
            raise AssertionError and print("test_api_calls_count doesn't have code status 200")
        print(TestApi.LOGGER.info(r.status_code))
        if r.text == '0':
            pass
        else:
            raise AssertionError and print("Calls Count is not correct")
