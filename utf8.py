#!/usr/bin/env python3

import os
import sys
import subprocess as sp


class Utf8Launcher:
    def __init__(self, compiler):
        self.compiler = compiler

    def build(self):
        sp.run(["CC={} make -C utf8.c test".format(self.compiler)], shell=True)

    def run(self):
        completed_process = sp.run(["./utf8.c/test"])
        if completed_process.returncode == 0:
            print("Success")
        else:
            print("Fail")
            exit(1)

    def build_and_run(self):
        self.build()
        self.run()

    def clean(self):
        sp.run(["make -C utf8.c clean"], shell=True)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 utf8.py <compiler>")
        sys.exit(1)

    cc = sys.argv[1]
    utf8 = Utf8Launcher(cc)
    utf8.clean()
    utf8.build_and_run()
