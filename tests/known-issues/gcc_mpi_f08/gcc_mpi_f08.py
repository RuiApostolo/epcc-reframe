#!/usr/bin/env python3

"""
Known issue mpi_f08 on gcc test

This test is designed to check if the programming environment is affected by the bug described at:
https://stackoverflow.com/questions/63824065/lbound-of-an-array-changes-after-call-to-mpi-gatherv-when-using-mpi-f08-module
https://gcc.gnu.org/pipermail/fortran/2020-September/055068.html

This issue prevents the mpi_f08 interface being used.
We expect GCC to potentially be affected and other compilers to not be affected.
Errors will be reported if gcc passes the test, or another type of compiler fails the test.
"""

import reframe as rfm
import reframe.utility.sanity as sn


@rfm.simple_test
class InterfaceBoundsTest(rfm.RegressionTest):
    """Test to check interface bounds -- gcc mpi_f08 known issue"""

    lang = parameter(["f90"])

    valid_systems = ["archer2:login", "cirrus:login"]
    valid_prog_environs = ["Default", "PrgEnv-cray", "PrgEnv-gnu", "gcc", "intel"]
    tags = {"functionality", "short", "issues"}
    maintainers = ["a.turner@epcc.ed.ac.uk"]

    @run_after("init")
    def setup_path(self):
        """Sets up path"""
        self.sourcepath = f"gcc_mpi_f08.{self.lang}"

    @sanity_function
    def assert_result(self):
        """Checks that issue was not found for non-gcc compilers"""
        # Expect gcc to fail check
        if self.current_environ.name in ["PrgEnv-gnu", "gcc"]:
            return sn.assert_found(r"F", self.stdout)
        # Expect other compilers to pass check
        return sn.assert_not_found(r"F", self.stdout)
