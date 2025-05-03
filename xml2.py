#!/usr/bin/env python3

import os
import sys
import shutil
import subprocess as sp


class Xml2Launcher:
    def __init__(self, compiler):
        self.compiler = compiler

    def build(self):
        os.chdir("libxml2")
        os.mkdir("build")
        os.chdir("build")
        sp.run(["CC={} cmake -DCMAKE_C_FLAGS=-O3 -DBUILD_SHARED_LIBS=OFF -DLIBXML2_WITH_THREADS=OFF -DCMAKE_BUILD_TYPE=release ..".format(self.compiler)], shell=True)
        sp.run(["make"], shell=True)
        os.chdir("../..")

    def run(self):
        os.chdir("libxml2/build")
        completed_process = sp.run(["make test"], shell=True)
        os.chdir("../..")

        if completed_process.returncode == 0:
            print("libxml2 tests successful")
        else:
            print("libxml2 tests failed")
            exit(1)

    def build_and_run(self):
        self.build()
        self.run()

    def clean(self):
        if os.path.exists("libxml2/build"):
            shutil.rmtree("libxml2/build")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 xml2.py <compiler>")
        sys.exit(1)

    cc = sys.argv[1]
    xml2 = Xml2Launcher(cc)
    xml2.clean()
    xml2.build_and_run()