#!/usr/bin/env python3

"""Reframe test for Nektarplusplus"""

# Based on original work from:
#   Copyright 2016-2022 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
#   ReFrame Project Developers. See the top-level LICENSE file for details.
#   SPDX-License-Identifier: BSD-3-Clause

import reframe as rfm
import reframe.utility.sanity as sn


@rfm.simple_test
class TestModuleNektarpluslus(rfm.RunOnlyRegressionTest):
    """Nektarplusplus Test"""

    descr = "Test Nektarplusplus"

    valid_systems = ["archer2:compute"]
    valid_prog_environs = ["PrgEnv-cray"]

    tags = {"performance", "applications"}

    keep_files = ["rfm_job.out"]

    reference = {
        "archer2:compute": {
            "Computationtime": (953.0, -0.1, 0.1, "seconds"),
        },
    }

    num_nodes = 1
    num_tasks_per_node = 1
    num_cpus_per_task = 1
    num_tasks = num_nodes * num_tasks_per_node * num_cpus_per_task

    time_limit = "2h"

    modules = ["cpe/22.12", "nektar/5.5.0"]

    env_vars = {"CRAY_ADD_RPATH": "yes"}

    @run_before("run")
    def prepare_run(self):
        """Setup test execution"""

        self.executable = "IncNavierStokesSolver"

        self.executable_opts = ["TGV64_mesh.xml TGV64_conditions.xml"]

    @sanity_function
    def assert_finished(self):
        """Sanity check that simulation finished successfully"""
        return sn.assert_found(
            r"Total\s+Computation\s+Time\s+=\s+",
            self.keep_files[0],
            msg="test_module_nektarplusplus: Completion message not found",
        )

    @performance_function("seconds", perf_key="Computationtime")
    def extract_perf(self):
        """Extract performance value to compare with reference value"""
        return sn.extractsingle(
            r"Total\s+Computation\s+Time\s+=\s+(?P<Comptime>[0-9]+.[0-9]+)s",
            self.keep_files[0],
            "Comptime",
            float,
        )
