from setuptools import setup, find_packages

setup(
    name="mkdocs-feather",
    version="0.1.0",
    description="Mkdocs plugin to enable live code examples in the documentation using feather",
    author="Anand Chitipothu",
    author_email="anand@pipal.in",
    install_requires=["mkdocs"],
    url="https://github.com/pipalacademy/mkdocs-feather",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.plugins': [
            'feather = mkdocs_feather:FeatherPlugin',
        ]
    }
)