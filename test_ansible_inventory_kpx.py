#!/usr/bin/local python

from collections import OrderedDict
import os
import ansible_inventory_kpx


class TestKpxInventory(object):
    """
    KpxInventory tests
    """
    def _setup_environment(self):
        code_path = os.path.dirname(os.path.realpath(__file__))
        kpx_db_path = code_path + "/tests/db/db.kdb"
        kpx_db_password = "test"

        os.environ['KPX_DB_PATH'] = kpx_db_path
        os.environ['KPX_DB_PASSWORD'] = kpx_db_password

        self.ki = ansible_inventory_kpx.KpxInventory()

    def test_load_kpx_db(self):
        self._setup_environment()
        data = self.ki.load_kpx_db()

        assert data is not None
        assert isinstance(data, OrderedDict)
        assert len(data['pwlist']['pwentry']) == 9

    def test_filter_raw_data(self):
        self._setup_environment()
        data = self.ki.load_kpx_db()

        output = self.ki.filter_raw_data(data)
        assert output is not None
        assert isinstance(output, dict)
        assert len(output['all']['vars']) == 18

    def test_export(self):
        self._setup_environment()
        output = self.ki.export()

        assert output is not None
        assert isinstance(output, dict)
        assert len(output['all']['vars']) == 18
