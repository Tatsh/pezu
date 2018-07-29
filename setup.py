"""Module with Portage helper commands."""
from setuptools import setup

setup(
    name='upkeep',
    version='0.0.2',
    author='Andrew Udvare',
    author_email='audvare@gmail.com',
    url='https://github.com/Tatsh/upkeep',
    license='LICENSE.txt',
    description='Portage update helper scripts.',
    long_description=open('README.md').read(),
    py_modules=['upkeep'],
    entry_points={
        'console_scripts': [
            'ecleans = upkeep:ecleans',
            'emerges = upkeep:emerges',
            'esync = upkeep:esync',
            'rebuild-kernel = upkeep:rebuild_kernel_command',
            'upgrade-kernel = upkeep:upgrade_kernel_command',
        ]
    }
)
