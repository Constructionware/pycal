from setuptools import find_packages, setup

setup(
    name='pycal',
    author='csware',
    author_email='csware.ware@gmail.com",
    description="A Builder's Companion."
    keywords="calculate calculator build construction",
    url="https://csware.pythonanywhere.com/pycal",
    project_urls={
        "Bug Tracker": "https://github.com/Constructionware/pycal.bugs/",
        "Documentation": "https://github.com/Constructionware/pycal/readme.md/",
        "Source Code": "https://github.com/Constructionware/pycal.git/",
    },
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
    'StringGenerator',
    ],
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
    ]
)
