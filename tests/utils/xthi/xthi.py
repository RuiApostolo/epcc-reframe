#!/usr/bin/env python
"""Test of download and build of xthi from repository master"""

import reframe
import reframe.utility.sanity as sn

REPOURL = "https://github.com/ARCHER2-HPC/xthi.git"


@reframe.simple_test
class XthiCompilationTest(reframe.CompileOnlyRegressionTest):
    """Compile xthi via make"""

    maintainers = ["k.straford@epcc.ed.ac.uk"]
    descr = "xthi compilation test"
    valid_systems = ["archer2:login", "cirrus:login"]
    valid_prog_environs = [
        "PrgEnv-cray",
        "PrgEnv-gnu",
        "PrgEnv-aocc",
        "gcc",
        "intel",
    ]
    build_system = "Make"
    build_system_max_concurrency = 1
    sourcesdir = REPOURL
    sourcepath = "src"

    @sanity_function
    def sanity_check_build(self):
        """Ensure build completed without errors"""
        return sn.assert_not_found("error", self.stderr)
