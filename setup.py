
# Add setuptools helpers

import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="lancedb",
        version="0.1.0",        
        description="Python client for LanceDB",
        long_description=open('README.md').read(),
        url="https://github.com/lancedb/lancedb-python",
        author="LanceDB",
        license='Apache-2.0',
        packages=setuptools.find_packages(),
        install_requires=[
            'pyarrow',
            'pandas',
            'lance @ git+https://github.com/quickwit-inc/lance.git',
        ],
        extras_require={
            'test': ['pytest']
        }
    )
