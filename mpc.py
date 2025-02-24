#!/usr/bin/env python3

import os
import sys
import subprocess as sp

class MpcLauncher:
    def __init__(self, compiler):
        self.compiler = compiler

    def build(self):
        sp.run(["CC={} make -C mpc".format(self.compiler)], shell=True)

    def run(self):
        completed_process = sp.run(["CC={} make -C mpc test".format(self.compiler)], shell=True)
        if completed_process.returncode == 0:
            print("Mpc success")
        else:
            print("Fail")
            exit(1)

    def build_and_run(self):
        self.build()
        self.run()

    def clean(self):
        sp.run(["make -C mpc clean"], shell=True)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 mpc.py <compiler>")
        sys.exit(1)

    cc = sys.argv[1]
    mpc = MpcLauncher(cc)
    mpc.clean()
    mpc.build_and_run()
