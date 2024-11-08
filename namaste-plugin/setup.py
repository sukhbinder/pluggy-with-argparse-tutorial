from setuptools import setup, find_packages

setup(
    name="namaste_plugin",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "example.plugins": [
            "nam = namaste_plugin:nam_plugin",
        ],
    },
)
