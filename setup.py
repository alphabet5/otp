import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="otp",
    version="0.0.1",
    author="John Burt",
    author_email="johnburt.jab@gmail.com",
    description="CLI application to enter OTP from secrets stored in your keychain.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alphabet5/otp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points={'console_scripts': ['otp=otp.cli:main']},
    include_package_data=True,
    package_data={'otp': ['*'], },
    install_requires=['pyotp',
                      'pyautogui',
                      'keyring'],
)
