from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("version.txt", "r") as fh:
    version = fh.read()

setup(
    name='cltl.chat-backend',
    version=version,
    package_dir={'': 'src'},
    packages=find_namespace_packages(include=['cltl.*']),
    data_files=[('version.txt', ['version.txt'])],
    url="https://github.com/numblr/cltl-chat-backend",
    license='MIT License',
    author='CLTL',
    author_email='t.baier@vu.nl',
    description='Dummy component to connect to cltl-chat-ui',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.8',
    install_requires=['cltl.combot', 'cltl.chat-ui'],
)
