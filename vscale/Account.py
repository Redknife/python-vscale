from .baseapi import BaseAPI


class Account(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.actdate = None
        self.name = None
        self.state = None
        self.country = None
        self.mobile = None
        self.locale = None
        self.id = None
        self.is_blocked = None
        self.surname = None
        self.face_id = None
        self.middlename = None
        self.email = None
        self.status_message = None

        super(Account, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, api_token):
        account = cls(token=api_token)
        account.load()
        return account

    def load(self):
        data = self.get_data("account")
        account_data = data['info']

        setattr(self, 'status_message', data['status'])
        for attr in account_data.keys():
            setattr(self, attr, account_data[attr])

    def __str__(self):
        return "{}".format(self.email)