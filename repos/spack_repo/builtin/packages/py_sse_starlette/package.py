# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySseStarlette(PythonPackage):
    """SSE plugin for Starlette."""

    homepage = "https://github.com/sysid/sse-starlette"
    pypi = "sse_starlette/sse_starlette-3.3.4.tar.gz"
    git = "https://github.com/sysid/sse-starlette.git"

    maintainers("wdconinc")

    license("BSD-3-Clause", checked_by="wdconinc")

    version("3.3.4", sha256="aaf92fc067af8a5427192895ac028e947b484ac01edbc3caf00e7e7137c7bef1")

    depends_on("python@3.10:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("py-starlette@0.49.1:")
        depends_on("py-anyio@4.7:")
