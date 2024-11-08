from setuptools import setup, find_packages

setup(
    name="example_plugin",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "example.plugins": [
            "greet = example_plugin.plugin:greet_plugin",
        ],
    },
)
