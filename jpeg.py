#!/usr/bin/env python3

import os
import sys
import subprocess as sp


class JpegLauncher:
    def __init__(self, compiler):
        self.compiler = compiler

    def build(self):
        os.chdir("jpeg-9f")
        sp.run(["CC={} CFLAGS=\"-fPIC -O3\" ./configure".format(self.compiler)], shell=True)
        sp.run(["make"], shell=True)
        os.chdir("..")

    def run(self):
        os.chdir("jpeg-9f")
        completed_process = sp.run(["make test"], shell=True)
        os.chdir("..")

        if completed_process.returncode == 0:
            print("jpeg-9f tests successful")
        else:
            print("jpeg-9f tests failed")
            exit(1)

    def build_and_run(self):
        self.build()
        self.run()

    def clean(self):
        os.chdir("jpeg-9f")
        sp.run(["make clean"], shell=True)
        os.chdir("..")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 jpeg.py <compiler>")
        sys.exit(1)

    cc = sys.argv[1]
    png = JpegLauncher(cc)
    png.clean()
    png.build_and_run()