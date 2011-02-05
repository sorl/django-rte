from setuptools import setup, find_packages


setup(
    name='django-rte',
    version='0.2',
    url='https://github.com/aino/django-rte',
    license='BSD',
    author='Mikko Hellsing',
    author_email='mikko@aino.se',
    description='Rich text editor for Django',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
    ],
    packages=find_packages(),
    platforms='any',
    zip_safe=False,
)

