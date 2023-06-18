from setuptools import find_packages, setup

setup(
    name='batchlib',
    packages=find_packages(include=['batchlib']),
    version='0.1.0',
    description='F-secure challenge solution',
    author='moneer',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner==6.0.0'],
    tests_require=['pytest==7.3.2'],
    test_suite='tests',
)

