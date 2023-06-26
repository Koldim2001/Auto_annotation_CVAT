from setuptools import find_packages
from distutils.core import setup


setup(
    name="auto_annotate",
    version="1.0",
    packages=find_packages(),
    long_description="Производит создание файла аннотации YOLO 1.1 для CVAT",
    include_package_data=True,
    entry_points={
        "console_scripts": ["auto_annotate=main:main"],
    },
    install_requires=[
        "torch",
        "click",
        "ultralytics",
        "opencv-python",
        'gdown'
    ],
)