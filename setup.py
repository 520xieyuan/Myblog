from distutils.core import setup

setup(name='Myblog',
      version='1.0',
      description='this is my first blog web',
      author='Eric',
      author_email='xie525@sina.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['article', 'myblog', 'user', 'utils'],
      py_modules=['manage'],
      data_files=['requirements']
     )