from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='csplookup',
    version='1.4',
    description='Client library for CSP Lookup API.',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Navid Zarepak',
    author_email='navid2zp@gmail.com',
    url='https://github.com/Navid2zp/csplookup-py',
    download_url='https://pypi.org/project/csplookup/',
    install_requires=[
        'requests',
    ],
)

if __name__ == '__main__':
    setup(**setup_args, )
