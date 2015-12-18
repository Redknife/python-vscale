import responses

import vscale

from .BaseTest import BaseTest


class TestManager(BaseTest):
    def setUp(self):
        super(TestManager, self).setUp()
        self.manager = vscale.Manager(token=self.token)

    @responses.activate
    def test_get_account(self):
        data = self.load_from_file('account.json')
        url = self.end_point + 'account'

        responses.add(responses.GET,
                      url,
                      body=data,
                      status=200,
                      content_type='application/json')

        account = self.manager.get_account()

        self.assertEqual(responses.calls[0].request.url, url)
        self.assertEqual(account.token, self.token)
        self.assertEqual(account.email, 'username@mail.com')
        self.assertEqual(account.actdate, '2015-03-16 07:30:38.195103')
        self.assertEqual(account.country, 'Russia')
        self.assertEqual(account.face_id, "1")
        self.assertEqual(account.id, "6523")
        self.assertEqual(account.is_blocked, False)
        self.assertEqual(account.locale, 'ru')
        self.assertEqual(account.middlename, 'Usermiddlename')
        self.assertEqual(account.mobile, "79226961269")
        self.assertEqual(account.name, "Username")
        self.assertEqual(account.state, "1")
        self.assertEqual(account.surname, "Usersurname")
        self.assertEqual(account.status_message, "ok")
