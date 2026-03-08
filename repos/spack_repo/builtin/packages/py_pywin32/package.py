# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPywin32(PythonPackage):
    """Python for Window Extensions."""

    homepage = "https://github.com/mhammond/pywin32"
    url = "https://github.com/mhammond/pywin32/archive/refs/tags/b306.tar.gz"

    license("PSF-2.0")

    version("311", sha256="4ae3f0d4adacc331733fe1204f7f93b8654615ca325adfc9eb6c67198246a91b")
    version("306", sha256="16e5ad3efbbf997080f67c3010bd4eb0067d499bbade9be1b240b7e85325c167")

    depends_on("cxx", type="build")  # generated

    with default_args(type="build"):
        depends_on("py-setuptools")
        depends_on("py-setuptools@77.0.3:", when="@311: ^python@3.9:")
        depends_on("py-setuptools@76.0", when="@311: ^python@:3.8")
