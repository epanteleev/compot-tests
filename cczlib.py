#!/usr/bin/env python3

import os
import sys
import subprocess as sp


class ZlibLauncher:
    def __init__(self, compiler):
        self.compiler = compiler

    def build(self):
        os.chdir("zlib")
        sp.run(["CC={} CFLAGS=-O3 ./configure --static".format(self.compiler)], shell=True)
        sp.run(["CC={} make".format(self.compiler)], shell=True)
        os.chdir("..")

    def run(self):
        os.chdir("zlib")
        completed_process = sp.run(["CC={} make test".format(self.compiler)], shell=True)
        os.chdir("..")
        if completed_process.returncode == 0:
            print("Zlib success")
        else:
            print("Fail")
            exit(1)

    def build_and_run(self):
        self.build()
        self.run()

    def clean(self):
        sp.run(["make -C zlib clean"], shell=True)

    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 zlib.py <compiler>")
        sys.exit(1)

    cc = sys.argv[1]
    zlib = ZlibLauncher(cc)
    zlib.clean()
    zlib.build_and_run()