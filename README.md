[![CircleCI](https://circleci.com/gh/ansible-roles-mamono210/goaccess_systemd/tree/main.svg?style=svg)](https://circleci.com/gh/ansible-roles-mamono210/goaccess_systemd/tree/main)

Role Description
=========

Daemonize [GoAccess](https://goaccess.io) for CentOS Stream 8.

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
