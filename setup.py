from setuptools import setup

setup(
        name='helloworls',
        inclide_package_data=True,
        version='0.0.4',
        description='Hello!',
        py_module=["hello"],
        packages=['src'],
        package_data={
        'src': ['dockerfile'],
        },
        package_dir={'src':'src'},
)
