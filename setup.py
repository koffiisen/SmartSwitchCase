from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    setup(
        name='smartswitchcase',
        version='1.0',
        author="Joel Koffi ONIPOH",
        author_email="koffi_joel.onipoh@isen.yncrea.fr",
        description="Python libraries of implementation of Switch Case",
        long_description=long_description,
        long_description_content_type='text/markdown',
        url="https://github.com/koffiisen/SmartSwitchCase",
        keywords=['Switch', "Case", "Switch Case", "switch case", "switch", "case",
                  "python switch case", "Python switch case", "python switch",
                  "python library", "python libraries", "python switch case library",
                  "Python Switch Case example"],
        packages=find_packages(),
        python_requires='>=2.7',
        include_package_data=False,
        classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.1",
            "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    )
