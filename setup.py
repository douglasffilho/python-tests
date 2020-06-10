from setuptools import setup, find_packages

setup(
    name='python-tests',
    version='1.0.0',
    packages=find_packages('src', include=['src/*', '*']),
    package_dir={'': 'src'},
    url='',
    license='MIT',
    author='Douglas Filho',
    author_email='douglasf.filho@gmail.com',
    description='Another Flask App',
    scripts=['bin/run_application.py']
)
