#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import setup, find_packages


setup(
    name='policy_caster',
    description='policy caster for flash clients',
    author='dsociative',
    author_email='admin@geektech.ru',
    packages=find_packages(),
    package_data={
        'policy_caster': ['policy.xml']
    },
    entry_points = {
    'console_scripts': [
        'policy_caster = policy_caster.caster:main',
        'policy_daemon = policy_caster.policy_daemon:main'
    ],
}
)