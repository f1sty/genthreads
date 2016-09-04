"""
    genthreads
    ----------

    Genthreads is my attempt to implement elixir actors model in python.

"""

from setuptools import setup


setup(
    name='genthreads',
    version='0.01',
    url='http://github.com/f1sty/genthreads/',
    license='MIT',
    author='Yurii Skrynnykov',
    author_email='truef1s7@gmail.com',
    description='A package trying to implement elixir concurrancy model',
    long_description=__doc__,
    packages=['genthreads'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    # install_requires=[
    # ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
    # entry_points='''
    #     [console_scripts]
    # '''
)
