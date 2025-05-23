#!/usr/bin/env python3

import os
import sys
import subprocess as sp

expected_output = """21754 / 23019 bytes
OK
"""

excepted_output_bench = """412 / 412 bytes
OK
"""

class UmkaLauncher:
    def __init__(self, compiler):
        self.compiler = compiler

    def build(self):
        os.chdir("umka-lang")
        sp.run(["CC={} make".format(self.compiler)], shell=True)
        os.chdir("..")

    def run(self):
        self.run_tests()
        self.run_benchmarks()

    def run_tests(self):
        os.chdir("umka-lang/tests")
        
        # Build the library
        os.chdir("lib")
        sp.run(["./build_lib_linux.sh"], shell=True)
        os.chdir("..")

        # Run the tests
        sp.run(["../build/umka -warn all.um > actual.log"], shell=True)
        # Check the output
        result = sp.run(["../build/umka -warn compare.um actual.log expected.log"], shell=True, capture_output=True)

        os.chdir("../..")
        if result.stdout.decode() == expected_output:
            print("Umka tests successful")
        else:
            print("Umka tests failed")
            print("'" + result.stdout.decode() + "'")
            exit(1)

    def run_benchmarks(self):
        os.chdir("umka-lang/benchmarks")
        sp.run(["../build/umka -warn allbench.um > actual.log"], shell=True)
        # Check the output
        result = sp.run(["../build/umka -warn ../tests/compare.um actual.log expected.log"], shell=True, capture_output=True)

        os.chdir("../..")
        if result.stdout.decode() == excepted_output_bench:
            print("Umka benchmarks successful")
        else:
            print("Umka benchmarks failed")
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
    umka.clean()
    umka.build_and_run()
