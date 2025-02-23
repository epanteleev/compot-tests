#!/usr/bin/env python3

import os
import sys
import subprocess as sp


class YxmlLauncher:
    def __init__(self, compiler):
        self.compiler = compiler

    def build(self):
        sp.run(["CC={} make -C yxml".format(self.compiler)], shell=True)

    def run(self):
        completed_process = sp.run(["CC={} make -C yxml test".format(self.compiler)], shell=True)
        if completed_process.returncode == 0:
            print("Yxml success")
        else:
            print("Fail")
            exit(1)

    def build_and_run(self):
        self.build()
        self.run()

    def clean(self):
        sp.run(["make -C yxml clean"], shell=True)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 yxml.py <compiler>")
        sys.exit(1)

    cc = sys.argv[1]
    yxml = YxmlLauncher(cc)
    yxml.clean()
    yxml.build_and_run()
