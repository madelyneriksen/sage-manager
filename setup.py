from setuptools import setup

setup(name="SageManager",
      version="0.1.0",
      description="SageManager, a gpg-based password manager.",
      long_description=open('README.md').read(),
      author="Madelyn Eriksen",
      author_email="madelyn.eriksen@gmail.com",
      license="MIT",
      packages=["sagemanager"],
      url='https://github.com/madelyneriksen/sage-manager/',
      entry_points={
          "console_scripts": [
              "sagemanager = sagemanager.cli:main"
          ]
      },
      install_requires=[
          "peewee >= 3.5.0",
          "pyperclip >= 1.6",
          "click >= 6.7",
          "gnupg >= 2.3.0",
      ],
      zip_safe=False)
