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
