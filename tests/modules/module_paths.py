#!/usr/bin/env python3
"""Reframe test to whether module locations are readable"""

import reframe as rfm
import reframe.utility.sanity as sn


class ModulePathTestBase(rfm.RunOnlyRegressionTest):
    """Checks if module file locations are readable"""

    descr = "Check that all module file locations are readable" ""
    valid_prog_environs = ["Default"]
    sourcesdir = None
    executable = "test -r"
    maintainers = ["r.apostolo@epcc.ed.ac.uk"]

    @sanity_function
    def assert_exists(self):
        """Checks exit code"""
        return sn.assert_eq(self.job.exitcode, 0)


class ARCHER2Paths(rfm.RegressionMixin):
    """Mixin class with ARCHER2 paths"""

    path = parameter(
        [
            "/work/y07/shared/archer2-lmod/utils/compiler/crayclang/10.0",  # Darshan
            "/work/y07/shared/archer2-lmod/python/core",  # python
            "/work/y07/shared/archer2-lmod/libs/core",  # cse libraries
            "/work/y07/shared/archer2-lmod/apps/core",  # cse apps
            "/work/y07/shared/archer2-lmod/utils/core",  # cse utils
            "/opt/cray/pe/lmod/modulefiles/mpi/crayclang/14.0/ofi/1.0/cray-mpich/8.0",  # cray parallel hdf5/netcdf
            "/opt/cray/pe/lmod/modulefiles/comnet/crayclang/14.0/ofi/1.0",  # cray mpich
            "/opt/cray/pe/lmod/modulefiles/compiler/crayclang/14.0",  # cray hdf5
            "/opt/cray/pe/lmod/modulefiles/mix_compilers",  # cray mixed compilers
            "/opt/cray/pe/lmod/modulefiles/perftools/22.12.0",  # cray performance tools
            "/opt/cray/pe/lmod/modulefiles/net/ofi/1.0",  # cray openshmem
            "/opt/cray/pe/lmod/modulefiles/cpu/x86-rome/1.0",  # cray fftw
            "/opt/cray/pe/lmod/lmod/modulefiles/Core",  # cray lmod
            "/opt/cray/pe/lmod/modulefiles/core",  # cray PrgEnvs and libsci
            "/opt/cray/pe/lmod/modulefiles/craype-targets/default",  # cray targets
            "/usr/local/share/modulefiles",  # epcc module
            "/opt/cray/modulefiles",  # cray lustre and rocm
        ]
    )


class CirrusPaths(rfm.RegressionMixin):
    """Mixin class with cirrus paths"""

    path = parameter(
        [
            "/work/y07/shared/cirrus-modulefiles",  # epcc modules
            "/usr/share/Modules/modulefiles",  # default
        ]
    )

class CirrusEXPaths(rfm.RegressionMixin):
    """Mixin class with Cirrus EX paths"""

    path = parameter(
        [
            "/work/y07/shared/cirrus-ex/cirrus-ex-lmod/apps/mpi/crayclang/16.0/ofi/1.0/x86-turin/1.0/cray-mpich/8.0",
            "/work/y07/shared/cirrus-ex/cirrus-ex-lmod/apps/mpi/gnu/10.0/ofi/1.0/x86-turin/1.0/cray-mpich/8.0",
            "/work/y07/shared/cirrus-ex/cirrus-ex-lmod/apps/mpi/aocc/4.1/ofi/1.0/x86-turin/1.0/cray-mpich/8.0",
            "/work/y07/shared/cirrus-ex/cirrus-ex-lmod/apps/mpi/intel/2023.2/ofi/1.0/x86-turin/1.0/cray-mpich/8.0", 
            "/work/y07/shared/cirrus-ex/cirrus-ex-software/spack-cirrus-ex/0.2/cirrus-ex-cse/modules/cce/19.0.0", 
            "/work/y07/shared/cirrus-ex/cirrus-ex-software/spack-cirrus-ex/0.2/cirrus-ex-cse/modules/gcc/14.2",
            "/work/y07/shared/cirrus-ex/cirrus-ex-software/spack-cirrus-ex/0.2/cirrus-ex-cse/modules/Core", 
            "/work/y07/shared/cirrus-ex/cirrus-ex-lmod/apps/core",
            "/work/y07/shared/cirrus-ex/cirrus-ex-lmod/utils/core",
            "/opt/cray/pe/lmod/modulefiles/mpi/crayclang/16.0/ofi/1.0/cray-mpich/8.0",
            "/opt/cray/pe/lmod/modulefiles/mpi/gnu/10.0/ofi/1.0/cray-mpich/8.0",
            "/opt/cray/pe/lmod/modulefiles/mpi/aocc/4.1/ofi/1.0/cray-mpich/8.0",
            "/opt/cray/pe/lmod/modulefiles/mpi/intel/2023.2/ofi/1.0/cray-mpich/8.0",
            "/opt/cray/pe/lmod/modulefiles/comnet/crayclang/16.0/ofi/1.0",
            "/opt/cray/pe/lmod/modulefiles/comnet/gnu/10.0/ofi/1.0",
            "/opt/cray/pe/lmod/modulefiles/comnet/aocc/4.1/ofi/1.0",
            "/opt/cray/pe/lmod/modulefiles/comnet/intel/2023.2/ofi/1.0",
            "/opt/cray/pe/lmod/modulefiles/compiler/crayclang/16.0",
            "/opt/cray/pe/lmod/modulefiles/compiler/gnu/10.0",
            "/opt/cray/pe/lmod/modulefiles/compiler/aocc/4.1",
            "/opt/cray/pe/lmod/modulefiles/compiler/intel/2023.2",
            "/opt/cray/pe/lmod/modulefiles/mix_compilers",
            "/opt/cray/pe/lmod/modulefiles/perftools/25.03.0", 
            "/opt/cray/pe/lmod/modulefiles/net/ofi/1.0",
            "/opt/cray/pe/lmod/modulefiles/cpu/x86-turin/1.0", 
            "/usr/share/Modules/modulefiles", 
            "/opt/cray/pe/lmod/lmod/modulefiles/Core",
            "/opt/cray/pe/lmod/modulefiles/core",
            "/opt/cray/pe/lmod/modulefiles/craype-targets/default",
            "/opt/modulefiles", 
            "/opt/cray/modulefiles"
        ]
    )


@rfm.simple_test
class ModulePathTestARCHER2(ModulePathTestBase, ARCHER2Paths):
    """ARCHER2 test class"""

    valid_systems = ["archer2:login"]

    @run_after("init")
    def setup_path(self):
        """add path to exe"""
        self.executable_opts = [self.path]


@rfm.simple_test
class ModulePathTestCirrus(ModulePathTestBase, CirrusPaths):
    """Cirrus test class"""

    valid_systems = ["cirrus:login"]

    @run_after("init")
    def setup_path(self):
        """add path to exe"""
        self.executable_opts = [self.path]

@rfm.simple_test
class ModulePathTestCirrusEX(ModulePathTestBase, CirrusEXPaths):
    """Cirrus test class"""

    valid_systems = ["cirrus-ex:login"]

    @run_after("init")
    def setup_path(self):
        """add path to exe"""
        self.executable_opts = [self.path]
