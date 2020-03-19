#!/usr/bin/env python

import os
import shutil
import urllib.request


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


def copy_file(original_filepath, new_filepath):
    shutil.copyfile(os.path.join(PROJECT_DIRECTORY, original_filepath),
                    os.path.join(PROJECT_DIRECTORY, new_filepath))


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

license_files = {"BSD 3-Clause": 'BSD3.rst',
                 "GNU GPL v3+": 'GPLv3.rst',
                 "Apache Software License 2.0": 'APACHE2.rst',
                 "BSD 2-Clause": 'BSD2.rst'}


def process_license(license_name):
    if license_name in license_files:
        license_path = os.path.join(PROJECT_DIRECTORY, 'licenses', 'LICENSE.rst')
        shutil.copyfile(os.path.join(PROJECT_DIRECTORY, 'licenses', license_files[license_name]),
                        license_path)
        if not os.path.exists(os.path.join(PROJECT_DIRECTORY, 'LICENSE.rst')):
            os.symlink(license_path, os.path.join(PROJECT_DIRECTORY, 'LICENSE.rst'))

    if license_name != "Other":
        for license_file in license_files.values():
            os.remove(os.path.join(PROJECT_DIRECTORY, 'licenses', license_file))


if __name__ == '__main__':

    process_license('{{ cookiecutter.license }}')

    include_examples = '{{ cookiecutter.include_example_code }}' == 'y'
    use_compiled = '{{ cookiecutter.use_compiled_extensions }}' == 'y'

    if not(include_examples and use_compiled):
        remove_file('{{ cookiecutter.module_name }}/example_c.pyx')

    if not include_examples:
        remove_dir('{{ cookiecutter.module_name }}/example_subpkg/')
        remove_file('{{ cookiecutter.module_name }}/example_mod.py')
        remove_file('{{ cookiecutter.module_name }}/tests/test_example.py')
