import json

from .BaseTest import BaseTest

import vscale


class TestAccount(BaseTest):
    def setUp(self):
        super(TestAccount, self).setUp()

        json_str = self.load_from_file('account.json')
        data = json.loads(json_str)
        account = vscale.Account()

        setattr(account, 'status_message', data['status'])
        for attr in data['info'].keys():
            setattr(account, attr, data['info'][attr])

        self.account = account

    def test_str(self):
        self.assertEqual(self.account.__str__(), "username@mail.com")