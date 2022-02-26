import setuptools

with open('readme.md', 'r') as file:
  long_description = file.read()

setuptools.setup(

   name = 'preprocess_kgftalkie',
   version = '0.0.1',
   author = 'vainu',
   author_email= 'prraju@srkrec.ac.in',
   description = 'this i s preprocessing package',
   long_description_content_type = 'text/markdown',
   packages = setuptools.find_packages(),
   classifers = ['Programming lanugage'::Python::3]
   'License:: OSI Aproved :: MIT License'
   "Operating System:: OS Independent"],
   python_requires = '>=3.5'

  )