# -*- coding: utf-8 -*-
"""
Setup file for Vector.
"""

import setuptools

with open("README.md") as f:
    __readme__ = f.read()

with open("LICENSE") as f:
    __license__ = f.read()


def setup_package():
    setuptools.setup(
        name="Vector",
        version="0.0",
        description="Tool to work with vectors.",
        long_description=__readme__,
        long_description_content_type="text/markdown",
        author="Mig Ver",
        license="MIT",
        author_email="",
        url="https://github.com/mig-ver/Vector",
        package_dir={"vector": "src"},
        # packages=["vector"],
        #   package_data={[]},
        include_package_data=True,
        extras_require={"test":["pytest",]},
        install_requires=[],
        classifiers=[
            "Programming Language :: Python :: 3.7",
            "Operating System :: OS Independent",
            "Intended Audience :: Science/Research",
        ],
    )


if __name__ == "__main__":
    setup_package()
