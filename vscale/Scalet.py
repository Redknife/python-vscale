from .baseapi import BaseAPI


class Scalet(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.status = None
        self.rplan = None
        self.locked = None
        self.keys = None
        self.private_address = None
        self.name = None
        self.ctid = None
        self.public_address = None
        self.hostname = None
        self.location = None
        self.active = None
        self.made_from = None

        super(Scalet, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, api_token, scalet_id):
        scalet = cls(token=api_token, ctid=scalet_id)
        scalet.load()
        return scalet

    @classmethod
    def get_object_from_data(cls, api_token, data):
        scalet = cls(token=api_token)
        for attr in data.keys():
            setattr(scalet, attr, data[attr])
        return scalet

    def load(self):
        data = self.get_data("scalets/{}".format(self.ctid))
        for attr in data.keys():
            setattr(self, attr, data[attr])

    def create(self, *args, **kwargs):

        for attr in kwargs.keys():
            setattr(self, attr, kwargs[attr])

        params = {
            'name': self.name,
            'make_from': self.made_from,
            'rplan': self.rplan,
            'do_start': self.active,
            'keys': self.keys,
            'location': self.location
        }

        data = self.get_data("scalets",
                             method='POST',
                             params=params)
        if data:
            for attr in data.keys():
                setattr(self, attr, data[attr])
        return data

    def restart(self):
        data = self.get_data("scalets/{}/restart".format(self.ctid),
                             method='PATCH')
        for attr in data.keys():
            setattr(self, attr, data[attr])
        return data

    def rebuild(self, root_pass):
        data = self.get_data("scalets/{}/rebuild".format(self.ctid),
                             method='PATCH',
                             params={'password': root_pass})
        for attr in data.keys():
            setattr(self, attr, data[attr])
        return data

    def stop(self):
        data = self.get_data("scalets/{}/stop".format(self.ctid),
                             method='PATCH')
        for attr in data.keys():
            setattr(self, attr, data[attr])
        return data

    def start(self):
        data = self.get_data("scalets/{}/start".format(self.ctid),
                             method='PATCH')
        for attr in data.keys():
            setattr(self, attr, data[attr])
        return data

    def upgrade(self, plan):
        data = self.get_data("scalets/{}/upgrade".format(self.ctid),
                             method='POST',
                             params={'rplan': plan})
        for attr in data.keys():
            setattr(self, attr, data[attr])
        return data

    def delete(self):
        data = self.get_data("scalets/{}".format(self.ctid), method='DELETE')
        for attr in data.keys():
            setattr(self, attr, data[attr])
        return data

    def add_sshkey(self, keys):
        data = self.get_data("scalets/{}".format(self.ctid),
                             method='PATCH', params={'keys': keys})
        for attr in data.keys():
            setattr(self, attr, data[attr])
        return data
