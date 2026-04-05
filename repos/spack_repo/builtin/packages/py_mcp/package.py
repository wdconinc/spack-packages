# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMcp(PythonPackage):
    """Model Context Protocol SDK."""

    homepage = "https://modelcontextprotocol.io/docs/getting-started/intro"
    pypi = "mcp/mcp-1.26.0.tar.gz"
    git = "https://github.com/modelcontextprotocol/python-sdk.git"

    maintainers("wdconinc")

    license("MIT", checked_by="wdconinc")

    version("1.26.0", sha256="db6e2ef491eecc1a0d93711a76f28dec2e05999f93afd48795da1c1137142c66")

    depends_on("python@3.10:", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("py-anyio@4.5:")
        depends_on("py-httpx@0.27.1:")
        depends_on("py-httpx-sse@0.4:")
        depends_on("py-pydantic@2.11.0:2")
        depends_on("py-starlette@0.27:")
        depends_on("py-python-multipart@0.0.9:")
        depends_on("py-sse-starlette@1.6.1:")
        depends_on("py-pydantic-settings@2.5.2:")
        depends_on("py-uvicorn@0.31.1:")
        depends_on("py-jsonschema@4.20.0:")
        depends_on("py-pywin32@310:", when="platform=windows")
        depends_on("py-pyjwt@2.10.1: +crypto")
        depends_on("py-typing-extensions@4.9.0:")
        depends_on("py-typing-inspection@0.4.1:")
