# ansible-role-mongo-logrotate #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-mongo-logrotate/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-mongo-logrotate/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/ansible-role-mongo-logrotate.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-mongo-logrotate/alerts/)
[![CodeQL](https://github.com/cisagov/ansible-role-mongo-logrotate/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-mongo-logrotate/actions/workflows/codeql-analysis.yml)

An Ansible role for installing and configuring
[`logrotate`](https://github.com/logrotate/logrotate) for MongoDB hosts.

## Requirements ##

**IMPORTANT:** In order for this log rotation to work correctly, your
mongod configuration file (typically found in `/etc/mongod.conf`)
must contain the following settings:

```yaml
systemLog:
    logRotate: reopen
processManagement:
    pidFilePath: /var/run/mongodb/mongod.pid
```

## Role Variables ##

None.

<!--
| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| optional_variable | Describe its purpose. | `default_value` | No |
| required_variable | Describe its purpose. | n/a | Yes |
-->

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  tasks:
    - name: Configure logrotate for MongoDB
      ansible.builtin.include_role:
        name: mongo_logrotate
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

David Redmin <david.redmin@trio.dhs.gov>
