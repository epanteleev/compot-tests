#!/usr/bin/env python3

import os
import sys
import subprocess as sp

class LuaLauncher:
    def __init__(self, compiler):
        self.compiler = compiler

    def build(self):
        sp.run(["CC={} make -C lua".format(self.compiler)], shell=True)

    def run(self):
        os.chdir("lua/testes")
        completed_process = sp.run(['../lua -e"_U=true" all.lua'], shell=True)
        os.chdir("../..")

        if completed_process.returncode == 0:
            print("Lua tests successful")
        else:
            print("Lua tests failed")
            exit(1)

    def build_and_run(self):
        self.build()
        self.run()

    def clean(self):
        sp.run(["make -C lua clean"], shell=True)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 lua.py <compiler>")
        sys.exit(1)

    cc = sys.argv[1]
    lua = LuaLauncher(cc)
    lua.clean()
    lua.build_and_run()