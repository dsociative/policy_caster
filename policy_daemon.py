# coding: utf8
#!/usr/bin/env python

from daemon import Daemon
from policy_caster import PolicyCaster
import os


class CasterDaemon(Daemon):

    policy_path = os.path.abspath('policy.xml')

    def run(self):
        policy_caster = PolicyCaster(843, self.policy_path)
        policy_caster.run()


if __name__ == '__main__':
    daemon = CasterDaemon('/tmp/PolicyCaster.pid', stderr=os.path.abspath('err.log'))

    if daemon.process_argv():
        pass
    else:
        daemon.run()

