# coding: utf8
#!/usr/bin/env python

import os

from caster import PolicyCaster
from policy_caster.daemon import Daemon


class CasterDaemon(Daemon):

    policy_path = os.path.abspath('policy.xml')

    def run(self):
        policy_caster = PolicyCaster(843, self.policy_path)
        policy_caster.run()


def main():
    daemon = CasterDaemon('/tmp/PolicyCaster.pid',
                          stderr=os.path.abspath('err.log'))
    if daemon.process_argv():
        pass
    else:
        daemon.run()


if __name__ == '__main__':
    main()

