#!/usr/bin/env python3

import chibicc
import bfish
import umka
import utf8
import yxml
import mpc
import lua
import cczlib

import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 run_all.py <compiler>")
        sys.exit(1)

    cc = sys.argv[1]

    tests = [
        chibicc.ChibiccLauncher,
        bfish.BfishLauncher,
        umka.UmkaLauncher,
        utf8.Utf8Launcher,
        yxml.YxmlLauncher,
        lua.LuaLauncher,
        cczlib.ZlibLauncher,
        mpc.MpcLauncher,
    ]
    for test in tests:
        site = test(cc)
        site.clean()
        site.build_and_run()
        
        print("-----------------------------------")
        print("|")
        print("|")
        print("-----------------------------------")

