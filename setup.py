import setuptools


def load_requirements():
    with open("requirements.txt", "r") as fp:
        return [i for i in fp.readlines()]


setuptools.setup(
    name="app",
    packages=["app"],
    install_requires=load_requirements()
)
