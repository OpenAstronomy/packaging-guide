#!/usr/bin/env python

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
LICENSE_FILES = {"BSD 3-Clause": 'BSD3.rst',
                 "GNU GPL v3+": 'GPLv3.rst',
                 "Apache Software License 2.0": 'APACHE2.rst',
                 "BSD 2-Clause": 'BSD2.rst'}

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


def copy_file(original_filepath, new_filepath):
    shutil.copyfile(os.path.join(PROJECT_DIRECTORY, original_filepath),
                    os.path.join(PROJECT_DIRECTORY, new_filepath))

def process_license(license_name):
    if license_name in LICENSE_FILES:
        shutil.copyfile(os.path.join(PROJECT_DIRECTORY, 'licenses', LICENSE_FILES[license_name]),
                        os.path.join(PROJECT_DIRECTORY, 'licenses', 'LICENSE.rst'))

    if license_name != "Other":
        for license_file in LICENSE_FILES.values():
            os.remove(os.path.join(PROJECT_DIRECTORY, 'licenses', license_file))


def process_version(enable_dynamic_dev_versions):
    if enable_dynamic_dev_versions != "y":
        remove_dir(os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.module_name }}', '_dev'))
        remove_file(os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.module_name }}', 'version.py'))

if __name__ == '__main__':

    process_license('{{ cookiecutter.license }}')
    process_version('{{ cookiecutter.enable_dynamic_dev_versions }}')
    include_examples = '{{ cookiecutter.include_example_code }}' == 'y'
    use_compiled = '{{ cookiecutter.use_compiled_extensions }}' == 'y'

    if not(include_examples and use_compiled):
        remove_file('{{ cookiecutter.module_name }}/example_c.pyx')

    if not include_examples:
        print("Removing examples")
        remove_dir('{{ cookiecutter.module_name }}/example_subpkg/')
        remove_file('{{ cookiecutter.module_name }}/example_mod.py')
        remove_file('{{ cookiecutter.module_name }}/tests/test_example.py')
