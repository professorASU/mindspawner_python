from setuptools import setup, find_packages

setup(
    name='mindspawner',
    version='0.1.0',
    description='A Python library to interact with the MindSpawner agent server',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Tomoyoshi Yamamoto',
    author_email='karolus@sfc.wide.ad.jp',
    url='https://github.com/professorASU/mindspawner-python',
    packages=find_packages(),
    install_requires=[
        'socketio',
        'numpy',
        'python-socketio',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
