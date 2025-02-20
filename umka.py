#!/usr/bin/env python3

import os
import sys
import subprocess as sp

expected_output = """21754 / 23019 bytes
OK
412 / 412 bytes
OK
"""

class UmkaLauncher:
    def __init__(self, compiler):
        self.compiler = compiler

    def build(self):
        os.chdir("umka-lang")
        sp.run(["CC={} ./build_linux.sh".format(self.compiler)], shell=True)
        os.chdir("..")

    def run(self):
        os.chdir("umka-lang")
        result = sp.run(["./test_linux.sh"], shell=True, stdout=sp.PIPE)
        os.chdir("..")
        if result.stdout.decode() == expected_output:
            print("Umka tests successful")
        else:
            print("Umka tests failed")
            print("'" + result.stdout.decode() + "'")
            exit(1)

    def build_and_run(self):
        self.build()
        self.run()

    def clean(self):
        os.chdir("umka-lang")
        sp.run(["make clean"], shell=True)
        os.chdir("..")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 umka.py <compiler>")
        sys.exit(1)

    cc = sys.argv[1]
    umka = UmkaLauncher(cc)
    umka.build_and_run()
