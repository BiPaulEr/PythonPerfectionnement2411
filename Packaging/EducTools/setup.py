from setuptools import setup, find_packages

setup(
    name="Eductools",
    version="0.0.0",
    description="A faire par le read me",
    packages=find_packages(),
    install_requires=["numpy", "click"],
    entry_points = {
        "console_scripts":[
            "math=eductools_cli.math_tools_cli:calcul_cli"
        ]
    },
    extras_require={
        "dev":["pytest"],
    }
)