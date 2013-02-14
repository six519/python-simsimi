import python_simsimi

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name=python_simsimi.__app_name__,
    version=python_simsimi.__version__,
    description=python_simsimi.__description__,
    author=python_simsimi.__author__,
    author_email=python_simsimi.__author_email__,
    packages=['python_simsimi'],
    url=python_simsimi.__app_url__,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'License :: Freeware',
    ),
    download_url=python_simsimi.__download_url__,
)