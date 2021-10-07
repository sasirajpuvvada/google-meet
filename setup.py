from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()

  
setup(
        name ='google meet',
        version ='1.0.0',
        author ='Sasi Raj',
        author_email ='sasi@gmail.com',
        url ='',
        description ='opens google meet on the fly in your browser.',
        long_description_content_type ="text/markdown",
        # license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'google_meet = src.google_meet'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords ='google meet browser python package',
        install_requires = requirements,
        zip_safe = False
)