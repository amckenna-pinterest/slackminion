from slackminion.tests.fixtures import *


class TestSlackIM(object):
    def setup(self):
        self.object = SlackConversation(conversation=test_channel, api_client=test_payload.get('api_client'))

    def teardown(self):
        self.object = None

    def test_init(self):
        assert self.object.id == test_user_id
        assert self.object.is_im is True

    def test_name(self):
        assert self.object.name == test_user_id

    def test_channel(self):
        assert self.object.channel == test_user_id
