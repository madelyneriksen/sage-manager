SageManager
====

A GPG-based, command line password creation and management utility for Python 3.

### Get Started

Download this git repository and install:
```
$ git clone https://github.com/madelyneriksen/sage-manager/
$ cd sage-manager
# Use of a Python3 virtual environment is recommended!
$ virtualenv .env
$ source .env/bin/activate
$ python install setup.py
```

To get started using SageManager is easy!
```
$ sagemanager --create hackernews
# Password:
# Retype Password:
# Password creation for hackernews success!
$ sagemanager --get hackernews
# Password:
# Retype Password:
# Password for hackernews copied to clipboard!
```

### FAQ/Why?

> No Python2?

Nope! Python 2 is end of life, and while there is legacy code out there to maintain in Python 2, this project uses typehints, Python3-only features, and will only ever be developed for Python3.

> If this is a password generator, why does it ask for a password?

Sagemanager encrypts passwords using GPG encryption. The password you enter on the first `--create` command will be the password sagemanager uses for encrypting passwords. Don't lose it!

> Why SageManager and not LastPass/Pass/$Other Manager?

No reason! This is a personal project first and foremost, built for fun and my own enjoyment.

> I'm a fugitive and wanted by international authorities. Will SageManager be enough to keep me secure?

SageManager is a small, personal project. For mission critial password management, I would recommend going with a more established open source solution.

### Development

Anyone is welcome to offer bug fixes, feature requests, or hack on the codebase for SageManager.

For pull request, please use `pylint` on your code, and write a few test cases!

#### Technology/Credits

* FSF for GPG
* [Peewee](https://github.com/coleifer/peewee), the ORM
* [Click](https://github.com/pallets/click)
* [Pytest](https://github.com/pytest-dev/pytest/)

#### Author

-- Madelyn Eriksen