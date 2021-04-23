from setuptools import setup, find_packages
from db_helpers._version import VERSION

REQUIREMENTS = [
]
TEST_REQUIREMENTS = [
    'pep8>=1.7.0'
]
EXCLUDE_ITEMS = [
    '*.pyc', '__pycache__', '*.tests', '*.tests.*', 'tests.*', 'tests'
]

setup(
    name='db_helpers',
    version=VERSION,
    description='DB Helper Adapters',
    url='',
    author='Shiv Pratap Singh',
    packages=find_packages(exclude=EXCLUDE_ITEMS),
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    setup_requires=['pytest-runner'],
    include_package_data=True,
    zip_safe=False
)
