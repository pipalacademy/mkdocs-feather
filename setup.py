from setuptools import setup, find_packages

setup(
    name="mkdocs-feather",
    description="Mkdocs plugin to enable live code examples in the documentation using feather",
    author="Anand Chitipothu",
    author_email="anand@pipal.in",
    install_requires=["mkdocs"],
    url="https://github.com/pipalacademy/mkdocs-feather",

    packages=find_packages(),

    entry_points={
        'mkdocs.plugins': [
            'feather = mkdocs_feather:FeatherPlugin',
        ]
    }
)