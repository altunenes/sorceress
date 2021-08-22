from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='sorceress',
    version='1.0',
    description='Optical Illusions with Python',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/emportent/sorceress',
    author='Enes Altun',
    author_email='enesaltun2@gmail.com',
    license='MIT',
    classifiers=classifiers,
    python_requires='>=3.7',
    keywords='Optical-Illusion,illusions,optical',
    packages=['sorceress'],
    install_requires=['opencv-python',"numpy","colour-science","Pillow",],
    extras_require={
        'dev': [
            'Pillow',
            'pytest',
            'pytest-cov',
            'flake8',
        ]
    }
)
