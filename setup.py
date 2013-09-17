from setuptools import setup, find_packages
import os

version = '0.8.1'

setup(name='wheelcms_project',
      version=version,
      description="WheelCMS project package",
      long_description=open("README.md").read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Ivo van der Wijk',
      author_email='wheelcms@in.m3r.nl',
      url='http://github.com/wheelcms/wheelcms_project',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'dj-database-url',
          'setuptools',
          'pytest',
          'two.ol',
          'two.bootstrap',
          'twotest',
          'south',
          'django-haystack==1.2.7',
          'pysolr==2.1.0',
          'Pillow',
          'stracks_api',
          'wheelcms_axle',
          'wheelcms_spokes',
          'wheelcms_categories',
          'wheelcms_simplecontact',
          'wheelcms_theme_bootswatch',
          'django-userena',
          'django-guardian',
          'django-tinymce',
          'django-taggit',
      ],
      entry_points={
      },

      )

