from setuptools import setup, find_packages

setup(
    name='apiverve_vpnproxydetector',
    version='1.1.9',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='VPN Detector is a simple tool for detecting VPN usage. It returns a boolean value indicating whether the IP address is using a VPN or not.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
