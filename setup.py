from setuptools import setup, find_packages

version = '4.3.0.1'

setup(name='plugins.zope.zthreads',
      version=version,
      description='Debug the threads of zope to find deadlocks',
      long_description=open("README.md").read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "Intended Audience :: Other Audience",
          "Intended Audience :: System Administrators",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking",
        ],
      keywords='zope plone threads debug deadlock',
      author='Kai Hoppert',
      author_email='kai.hoppert@online.de',
      url='https://github.com/hoka/plugins.zope.zthreads.git',
      license='GNU General Public License version 2',
      packages=find_packages(),
      namespace_packages=['plugins','plugins.zope'],
      include_package_data=True,
      install_requires=[
        'setuptools',
        'threadframe',
      ],
      extras_require={'test': [
        'collective.testcaselayer',
      ]},
      platforms='Any',
      zip_safe=False,
      entry_points='''
[z3c.autoinclude.plugin]
target = plone
''',
)