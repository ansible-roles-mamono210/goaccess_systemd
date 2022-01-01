[![](https://github.com/ansible-roles-mamono210/goaccess_systemd/workflows/build/badge.svg)](https://github.com/ansible-roles-mamono210/goaccess_sytemd/actions?query=workflow%3Abuild)

Role Description
=========

Daemonize [GoAccess](https://goaccess.io) for CentOS8.

Requirements
------------

Before running this role, Epel and [GoAccess](https://goaccess.io) installed on the target system.

Role Variables
--------------

None

Dependencies
------------

None

Example Playbook
----------------

```YAML
---
- hosts: all
  become: true
  roles:
    - geerlingguy.repo-epel
    - mamono210.goaccess_install
    - goaccess_systemd
```

License
-------

BSD
