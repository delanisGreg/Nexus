from setuptools import setup

setup(
        name='helloworls',
        inclide_package_data=True,
        version='1.0.2',
        description='Hello!',
        py_module=["hello"],
        packages=['src'],
        package_data={
        'src': ['Dockerfile'],
        },
        package_dir={'src':'src'},
)
