from setuptools import setup, find_packages

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setup(
    name="free-fire-emote-bot",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Free Fire Emote Bot API",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.9',
)