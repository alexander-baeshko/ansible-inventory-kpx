ansible-inventory-kpx
=================
Example of Ansible dynamic inventory

Configuration and usage
=================
1. Set Keepassx DB path and password via environment variables
export KPX_DB_PATH="<KPX_DB_PATH>"
export KPX_DB_PASSWORD="<KPX_DB_PASSWORD>"

2. Keepassx DB items usernames and passwords are exported to Ansible as variables
and have kpx_<group_id>_<item_id>_username / kpx_<group_id>_<item_id>_password format

$ ansible -i ./ansible_inventory_kpx.py -m debug -a "var=hostvars[inventory_hostname]" localhost
 [WARNING]: Could not match supplied host pattern, ignoring: all

 [WARNING]: provided hosts list is empty, only localhost is available

localhost | SUCCESS => {
    "changed": false,
    "hostvars[inventory_hostname]": {
        "ansible_check_mode": false,
        "ansible_connection": "local",
        "ansible_playbook_python": "/home/ab/Virtualenv/ansible-inventory-kpx/bin/python",
        "ansible_python_interpreter": "/home/ab/Virtualenv/ansible-inventory-kpx/bin/python",
        "ansible_version": {
            "full": "2.4.2.0",
            "major": 2,
            "minor": 4,
            "revision": 2,
            "string": "2.4.2.0"
        },
        "group_names": [],
        "groups": {
            "all": [],
            "ungrouped": []
        },
        "inventory_hostname": "localhost",
        "inventory_hostname_short": "localhost",
        "kpx_group01_gr01_value01_password": "test",
        "kpx_group01_gr01_value01_username": "test",
        "kpx_group01_gr01_value02_password": "test",
        "kpx_group01_gr01_value02_username": "test",
        "kpx_group01_gr01_value03_password": "test",
        "kpx_group01_gr01_value03_username": "test",
        "kpx_group02_gr02_value01_password": "test",
        "kpx_group02_gr02_value01_username": "test",
        "kpx_group02_gr02_value02_password": "test",
        "kpx_group02_gr02_value02_username": "test",
        "kpx_group02_gr02_value03_password": "test",
        "kpx_group02_gr02_value03_username": "test",
        "kpx_group03_gr03_value01_password": "test",
        "kpx_group03_gr03_value01_username": "test",
        "kpx_group03_gr03_value02_password": "test",
        "kpx_group03_gr03_value02_username": "test",
        "kpx_group03_gr03_value03_password": "test",
        "kpx_group03_gr03_value03_username": "test",
        "omit": "__omit_place_holder__c181eb2fafcccb568b8140dd2f7c5037a3520b2f",
        "playbook_dir": "/home/ab/Workspace/Projects/ansible-inventory-kpx"
    }
}
