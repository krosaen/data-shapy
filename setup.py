from setuptools import setup, find_packages

setup(
    name="Data Shapy",
    version="0.1",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages(exclude=['tests']),
    install_requires=[],
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'json-shape = data_shapy.json_shape:main',
        ],
    },
)
