from setuptools import setup, find_packages

exec(open('bar4py/version.py').read())

setup(
    name='bar4py',
    version=__version__,
    author='bxtkezhan-kk',
    author_email='bxtkezhan@qq.com',
    description='Augmented reality lib for Python3',
    url='https://bxtkezhan.github.io/BAR4Py',
    license='MIT License',
    keywords='AR OpenCV',
    packages=find_packages(),
    package_data={'bar4py': ['templates/index.tpl', 'static/js/*.js', 'static/model/mk.*']},
    install_requires= ['numpy', 'flask'],
)
