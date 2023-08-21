from setuptools import setup, find_packages

setup(
    name="oj_proxy",
    version='0.1',
    description="a CLI that submits to Kattis, CodeForces",
    author="Muhammad Tanveer",
    packages= find_packages(),
    entry_points = {
        'console_scripts':["oj-proxy=cli.cli_main:main",],
    },
    install_requires=[
        "lxml==4.9.3",
        "requests==2.31.0"
    ]
)
