from setuptools import find_packages, setup


setup(
    author="",
    author_email="",
    description="",
    name="pinax-{{ app_name }}",
    version="0.1",
    url="http://github.com/pinax/pinax-{{ app_name }}/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "{{ app_name }}": []
    },
    test_suite="runtests.runtests",
    install_requires=[
        "Django>=1.8"
    ],
    tests_require=[
    ],
    extras_require={
        "pytest": ["pytest", "pytest-django"]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
