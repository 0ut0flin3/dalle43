import setuptools
setuptools.setup(name='dalle43',
    version='0.0.0.5',
    author='0ut0flin3',
    description='Use OpenAI DALL-E for free, unlimited and without politically correct restrictions',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        
                ],
    install_requires=['selenium==4.8.2'],
    python_requires='>=3'
        )
