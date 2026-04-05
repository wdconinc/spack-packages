# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRestrictedpython(PythonPackage):
    """RestrictedPython is a defined subset of the Python language which
    allows to provide a program input into a trusted environment."""

    homepage = "https://github.com/zopefoundation/RestrictedPython"
    pypi = "restrictedpython/restrictedpython-8.1.tar.gz"
    git = "https://github.com/zopefoundation/RestrictedPython.git"

    maintainers("wdconinc")

    license("ZPL-2.1", checked_by="wdconinc")

    version("8.1", sha256="4a69304aceacf6bee74bdf153c728221d4e3109b39acbfe00b3494927080d898")

    depends_on("python@3.9:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@78.1.1:80")
