from setuptools import setup

setup(
        name='helloworls',
        version='0.0.3',
        description='Hello!',
        py_module=["hello"],
        packages=['src'],
        package_dir={'src':'src'},
)
