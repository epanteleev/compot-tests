#!/usr/bin/env python3

import os
import sys
import shutil
import subprocess as sp


class PngLauncher:
    def __init__(self, compiler):
        self.compiler = compiler

    def build(self):
        os.chdir("libpng")
        sp.run(["CC={} CFLAGS=-O3 ./configure".format(self.compiler)], shell=True)
        sp.run(["make"], shell=True)
        os.chdir("..")

    def run(self):
        os.chdir("libpng")
        completed_process = sp.run(["make test"], shell=True)
        os.chdir("..")

        if completed_process.returncode == 0:
            print("Libpng tests successful")
        else:
            print("Libpng tests failed")
            exit(1)

    def build_and_run(self):
        self.build()
        self.run()

    def clean(self):
        os.chdir("libpng")
        sp.run(["make clean"], shell=True)
        os.chdir("..")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 png.py <compiler>")
        sys.exit(1)

    cc = sys.argv[1]
    png = PngLauncher(cc)
    png.clean()
    png.build_and_run()
