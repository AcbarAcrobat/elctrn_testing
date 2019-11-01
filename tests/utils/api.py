# import configparser
# import logging
#
# from allure_commons._allure import step
# from tests.utils.http_manager import HttpManager
# # from tests.utils.json_fixture import JSONFixture
#
#
# class Api:
#     LOGGER = logging.getLogger(__name__)
#     parser = configparser.ConfigParser()
#     parser.read('simple_config.ini')
#
#     BASE_URL = parser.get('cti-service', 'url')
#     # CREATE_ISSUE = BASE_URL + "/rest/api/2/issue/"
#     # DELETE_ISSUE = BASE_URL + "/rest/api/2/issue/{0}/"
#
#     @staticmethod
#     def login():
#         with step("Login"):
#             url = Api.BASE_URL
#             userName = Api.parser.get('cti-service', 'userName')
#
#             result = HttpManager.auth(url, userName)
#             Api.LOGGER.info('TEST: Login with {0} credentials'.format(userName))
#             assert 200 == result.status_code
#
#     # @staticmethod
#     # def create_issue(project_key):
#     #     with step("Create issue"):
#     #         result = HttpManager.post(Api.CREATE_ISSUE,
#     #                                   JSONFixture.for_create_issue(project_key))
#     #         Api.LOGGER.info('TEST: Create issue. Method: {0}, Data: {1}'.format("POST", JSONFixture.for_create_issue(project_key)))
#     #         # TODO with this line allure report isn't generated - allure.attach("Create issue", JSONFixture.for_create_issue(project_key), AttachmentType.TEXT)
#     #         return result
#     #
#     # # @allure.step - will not work as expected. Returned value will be a link to memory
#     # @staticmethod
#     # def delete_issue(issue_id):
#     #     with step("Delete issue by ID"):
#     #         result = HttpManager.delete(Api.DELETE_ISSUE.format(issue_id))
#     #         Api.LOGGER.info('TEST: Delete issue. Method: {0}, URL : {1}'.format("DELETE", Api.DELETE_ISSUE.format(issue_id)))
#     #         return result