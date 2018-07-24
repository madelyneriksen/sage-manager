from setuptools import setup

setup(name="SageManager",
      version="0.1.0",
      description="SageManager, a gpg-based password manager.",
      author="Madelyn Eriksen",
      author_email="madelyn.eriksen@gmail.com",
      license="MIT",
      packages=["sagemanager"],
      entry_points={
          "console_scripts": [
              "sagemanager = sagemanager.cli:main"
          ]
      },
      zip_safe=False)
