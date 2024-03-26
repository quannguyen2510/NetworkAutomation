#!/usr/bin/bash


cd VLAN
ansible-playbook VLAN_Create.yml
ansible-playbook AccessTrunkinConfig.yml
ansible-playbook CoreSwCfg.yml
ansible-playbook ServerSwCfg.yml

cd ../STP
ansible-playbook *

cd ../Interfaces/L3_interfaces
ansible-playbook *

cd ../../OSPF
ansible-playbook *

cd ../VRRP
ansible-playbook *

cd ../DHCP
ansible-playbook *

cd ../SMNP
ansible-playbook *

cd ..
ansible-playbook Save.yml
