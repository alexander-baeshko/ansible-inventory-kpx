#!/usr/bin/env python

import os
from xml.etree.ElementTree import fromstring
from json import dumps
from xmljson import badgerfish as bf
import libkeepass


class KpxInventory(object):
    """
    Ansible KPX inventory implementation
    """
    def __init__(self):
        self.kpx_db_path = os.environ.get('KPX_DB_PATH', None)
        self.kpx_db_password = os.environ.get('KPX_DB_PASSWORD', None)

        if self.kpx_db_path is None or self.kpx_db_password is None:
            print("Script wasn't able to load environment variables")
            raise Exception

    def inventory_template(self):
        """
        Ansible inventory template
        """
        return {
            'all': {
                'hosts': [],
                'vars': {},
            },
            '_meta': {
                'hostvars': {}
            }
        }

    def filter_raw_data(self, data):
        """
        Transform KPX DB data to Ansible format
        """
        try:
            output = self.inventory_template()

            for item in data['pwlist']['pwentry']:
                group = item['group']['$']
                title = item['title']['$']
                username_key = "kpx_%s_%s_username" % (group, title)
                password_key = "kpx_%s_%s_password" % (group, title)
                output['all']['vars'][username_key] = item['username']['$']
                output['all']['vars'][password_key] = item['password']['$']
        except Exception:
            print("Script wasn't able to generate inventory output")
            raise
        else:
            return output

    def load_kpx_db(self):
        """
        Returns KPX DB data
        """
        try:
            with libkeepass.open(self.kpx_db_path,
                                 password=self.kpx_db_password) as kpx_db:
                data = bf.data(fromstring(kpx_db.pretty_print()))
        except Exception:
            print("Script wasn't able to read KPX DB")
            raise
        else:
            return data

    def export(self):
        """
        Returns KPX DB data in Ansible format
        """
        kpx_raw_data = self.load_kpx_db()
        output = self.filter_raw_data(kpx_raw_data)
        print(dumps(output, sort_keys=True, indent=2))
        return output


if __name__ == '__main__':
    KpxInventory().export()
