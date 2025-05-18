#!/usr/bin/env python3

import os
import sys
import shutil
import subprocess as sp


class JsoncLauncher:
    def __init__(self, compiler):
        self.compiler = compiler

    def build(self):
        os.chdir("json-c")
        os.mkdir("build")
        os.chdir("build")
        sp.run(["CC={} cmake -DCMAKE_C_FLAGS=-O3 -DCMAKE_BUILD_TYPE=release ..".format(self.compiler)], shell=True)
        sp.run(["make"], shell=True)
        os.chdir("../..")

    def run(self):
        os.chdir("json-c/build")
        completed_process = sp.run(["make test"], shell=True)
        os.chdir("../..")

        if completed_process.returncode == 0:
            print("Json-C tests successful")
        else:
            print("Json-C tests failed")
            exit(1)

    def build_and_run(self):
        self.build()
        self.run()

    def clean(self):
        if os.path.exists("json-c/build"):
            shutil.rmtree("json-c/build")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 jsonc.py <compiler>")
        sys.exit(1)

    cc = sys.argv[1]
    jsonc = JsoncLauncher(cc)
    jsonc.clean()
    jsonc.build_and_run()
