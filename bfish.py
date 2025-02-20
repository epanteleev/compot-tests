#!/usr/bin/env python3

import os
import sys
import subprocess as sp


class BfishLauncher:
    def __init__(self, compiler):
        self.compiler = compiler

    def build(self):
        sp.run(["CC={} make -C bfish".format(self.compiler), "bftest"], shell=True)

    def run(self):
        completed_process = sp.run(["./bfish/bftest"])
        if completed_process.returncode == 0:
            print("AES encryption successful")
        else:
            print("AES encryption failed")
            exit(1)

    def build_and_run(self):
        self.build()
        self.run()

    def clean(self):
        sp.run(["make -C bfish clean"], shell=True)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 bfish.py <compiler>")
        sys.exit(1)

    cc = sys.argv[1]
    bfish = BfishLauncher(cc)
    bfish.build_and_run()
