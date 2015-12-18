from .baseapi import BaseAPI
from .Account import Account
from .Scalet import Scalet


class Manager(BaseAPI):
    def __init__(self, *args, **kwargs):
        super(Manager, self).__init__(*args, **kwargs)

    def get_account(self):
        return Account.get_object(api_token=self.token)

    def get_all_scalets(self):
        scalets_list = []
        scalets_data = self.get_data("scalets")
        for scalet_params in scalets_data:
            scalet = Scalet.get_object_from_data(self.token, scalet_params)
            scalets_list.append(scalet)

        return scalets_list

    def get_tasks(self):
        data = self.get_data("tasks")
        return data

    def get_images(self):
        data = self.get_data("images")
        return data

    def get_plans(self):
        data = self.get_data("rplans")
        return data

    def get_prices(self):
        data = self.get_data("billing/prices")
        return data

    def add_ssh_key(self, name, key):
        data = self.get_data("sshkeys", 'POST',
                             params={'key': key, 'name': name})
        return data

    def delete_ssh_key(self, id):
        data = self.get_data("sshkeys/{}".format(id), 'DELETE')
        return data

    def get_scalet(self, scalet_id):
        return Scalet.get_object(api_token=self.token, scalet_id=scalet_id)

    def create_scalet(self, name,
                      made_from='ubuntu_14.04_64_002_master',
                      rplan='small', active=True,
                      ssh_keys=[], location='spb0'):

        scalet = Scalet(token=self.token, name=name,
                        made_from=made_from, rplan=rplan,
                        active=active, keys=ssh_keys, location=location)
        scalet.create()
        return scalet

    def get_locations(self):
        data = self.get_data("locations")
        return data
