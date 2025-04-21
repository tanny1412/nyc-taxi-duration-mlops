from setuptools import find_packages, setup

setup(
    name='taxitime',  # pip package name matching repository
    packages=find_packages(),
    version='0.1.0',
    description='End-to-end MLOps pipeline for predicting New York City taxi trip durations',
    author='Tanish Kandivlikar',
    author_email='tkandivlikar@wpi.edu',
    license='MIT',
)
