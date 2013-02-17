from setuptools import setup, find_packages

setup(
    name = 'paversion',
    version = '0.0.1',
    description = 'Paver tasks for bumping setup.py version metadata',
    author = 'Brian Lauber',
    author_email = 'constructible.truth@gmail.com',
    packages = find_packages(exclude = ["tests.*", "tests"]),
    install_requires = ["paver>=1.1.0"],
    test_suite = 'tests',
)

