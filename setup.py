import io

from setuptools import setup

PACKAGE_ROOT = 'thirdrail'

with open('README.md') as readme_file:
    readme = readme_file.read()

about = dict()
with io.open(f'{PACKAGE_ROOT}/__version__.py', 'r', encoding='utf-8') as f:
    exec(f.read(), about)

requirements = [
]

setup(
    name="third-rail",
    version=about['__version__'],
    description='Python web framework on rolling stock.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Tyler Green',
    author_email='greent@tyleragreen.com',
    url='https://github.com/tyleragreen/third-rail',
    packages=[
        f'{PACKAGE_ROOT}',
    ],
    license='MIT license',
    install_requires=requirements,
)
