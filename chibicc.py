#!/usr/bin/env python3

import os
import sys
import subprocess as sp


class ChibiccLauncher:
    def __init__(self, compiler):
        self.compiler = compiler

    def build(self):
        sp.run(["CC={} make -C chibicc".format(self.compiler)], shell=True)

    def run(self):
        completed_process = sp.run(["make -C chibicc test".format(self.compiler)], shell=True)
        if completed_process.returncode == 0:
            print("Chibicc tests successful")
        else:
            print("Chibicc tests failed")
            exit(1)

    def build_and_run(self):
        self.build()
        self.run()

    def clean(self):
        sp.run(["make -C chibicc clean"], shell=True)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 chibicc.py <compiler>")
        sys.exit(1)

    cc = sys.argv[1]
    chibicc = ChibiccLauncher(cc)
    chibicc.clean()
    chibicc.build_and_run()
