from setuptools import setup, find_packages

setup(
    name="futuristic-auth-system",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "bcrypt",
    ],
    entry_points={
        'console_scripts': [
            'futuristic-auth = src.auth:main',
        ],
    },
    include_package_data=True,
    author="",
    description="A futuristic authentication system with secure login/registration and cyberpunk interface.",
    license="MIT",
)
