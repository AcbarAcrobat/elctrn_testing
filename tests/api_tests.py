import json
import requests
import urllib3
import logging
url = "https://ccng-563.sphaera-cti-service.stage.sphaera.ru"


class TestApi:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    LOGGER = logging.getLogger(__name__)

    def test_get_operators_list(self):
        r = requests.get(url + "/api/operators", verify=False, headers={"Content-Type": "application/json"})
        assert 200 == r.status_code
        print(TestApi.LOGGER.info(r.status_code))

    def test_post_login_with_extension(self):
        m = {'extension': '105'}
        r = requests.post(url + "/api/operators", verify=False, data=json.dumps(m), headers={"Content-Type": "application/json"})
        assert r.status_code == 200
        print(TestApi.LOGGER.info(r.status_code))
        if 'userName' in r.json() and r.json()['userName'] == 'Татьяна Сахарова':
            pass
        else:
            print('login_test_with_extension is not correct. ERROR')

    def test_api_calls_count(self):
        m = {'extension': '105'}
        r = requests.get(url + "/api/calls/count/105", verify=False, data=json.dumps(m), headers={"Content-Type": "application/json"})
        assert 200 == r.status_code
        print(TestApi.LOGGER.info(r.status_code))

    def test_api_calls_time(self):
        m = {'extension': '105'}
        rj = {"status": "None"}
        r = requests.get(url + "/api/calls/regulatorytimestatus", verify=False, data=json.dumps(m), headers={"Content-Type": "application/json"})
        assert 200 == r.status_code
        assert r.json() == rj
        print(TestApi.LOGGER.info(r.status_code))

    def test_api_checktraces(self):
        r = requests.get(url + "/api/checktraces", verify=False, headers={"Content-Type": "application/json"})
        assert 200 == r.status_code
        print(TestApi.LOGGER.info(r.status_code))

    def test_get_active_operators(self):
        r = requests.get(url + "/api/operators/active", verify=False, headers={"Content-Type": "application/json"})
        assert 200 == r.status_code
        print(TestApi.LOGGER.info(r.status_code))

    '''Not used'''
    # def test_get_values(self):
    #     r = requests.get(url + "/api/values", verify=False, headers={"Content-Type": "application/json"})
    #     assert 200 == r.status_code
    #     print(TestApi.LOGGER.info(r.status_code))

    # def test_get_users_submit_phon_numb(self):
    #     r = requests.get(url + "/api/users/submit/105", verify=False, data={}, headers={"Content-Type": "application/json"})
    #     assert 200 == r.status_code
    #     print(TestApi.LOGGER.info(r.status_code))

    def test_get_tatiana_saharova(self):
        r = requests.get(url, verify=False, data={}, headers={"Content-Type": "application/json"})
        assert r.status_code == 200
        print(TestApi.LOGGER.info(r.status_code))
        if 'userName' in r.json() and r.json()['userName'] == 'Татьяна Сахарова':
            pass
        else:
            print('test_get_ivan_asterisk is not correct. ERROR')
            print(TestApi.LOGGER.info(r.json))

    def test_get_calls_count(self):
        burl = 'https://tester.sphaera-cti-service.stage.sphaera.ru/api/calls/count/105'
        r = requests.get(url, verify=False, data={}, headers={"Content-Type": "application/json"})
        assert 200 == r.status_code
        print(TestApi.LOGGER.info(r.status_code))
        if r.text == '40':
            pass
        else:
            print('test_get_calls_count is not correct')
            print(r.json())

    def test_get_calls_time(self):
        burl = 'https://tester.sphaera-cti-service.stage.sphaera.ru/api/calls/time/105'
        r = requests.get(url, verify=False, data={}, headers={"Content-Type": "application/json"})
        assert r == "2019-10-23T10:34:35.837171"


