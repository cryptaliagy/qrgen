from setuptools import setup, find_packages


setup(
    name='qrgen',
    author='Natalia Maximo',
    author_email='iam@natalia.dev',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=['click'],
    tests_require=['mypy', 'flake8'],
    extras_require={
        'tests': ['mypy', 'flake8'],
    },
    entry_points={
        'console_scripts': ['qrgen = qrgen.main:main']
    },
)
