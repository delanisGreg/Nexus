from setuptools import setup

setup(
        name='helloworls',
        version='0.0.1',
        description='Hello!',
        py_module=["hello"],
        package_dir={'':'src'},
        setup_requires=['wheel'],
)
