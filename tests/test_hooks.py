from pathlib import Path

import pytest


def test_examples_removed(cookiejar_no_examples):
    cj = cookiejar_no_examples
    ctx = cj.context

    example_files = [
        "example_mod.py",
        "example_c.pyx",
        "example_subpkg/"
        "tests/"
    ]

    for afile in example_files:
        assert not (cj.project_path / ctx['package_name'] / afile).exists()


def test_examples_present(cookiejar_examples):
    cj = cookiejar_examples
    ctx = cj.context

    example_files = [
        "example_mod.py",
        "example_subpkg/",
        "example_subpkg/__init__.py",
        "example_subpkg/tests/__init__.py",
        "example_subpkg/data/.gitignore",
        "tests/",
        "tests/test_example.py",
        "tests/__init__.py",
    ]

    if ctx['use_compiled_extensions'] == 'y':
        example_files.append("example_c.pyx")

    for afile in example_files:
        assert (cj.project_path / ctx['package_name'] / afile).exists()


@pytest.mark.parametrize("license, lfile", [
    ("BSD 3-Clause", "BSD3.rst"),
    ("GNU GPL v3+", "GPLv3.rst"),
    ("Apache Software License 2.0", "APACHE2.rst"),
    ("BSD 2-Clause", "BSD2.rst")])
def test_licence(license, lfile, cookies):
    cj = cookies.bake(extra_context={'license': license})

    assert (cj.project_path / "licenses" / "TEMPLATE_LICENSE.rst").exists()
    assert (cj.project_path / "licenses" / "LICENSE.rst").exists()

    with open(cj.project_path / "licenses" / "LICENSE.rst") as fobj:
        license_content = fobj.readlines()

    base_path = Path(".") / "{{ cookiecutter.package_name }}"
    base_path /= "licenses"
    base_path = base_path.resolve()
    with open(base_path / lfile) as fobj:
        expected_content = fobj.readlines()

    assert expected_content[1:] == license_content[1:]


def test_other_licence(cookies):
    cj = cookies.bake(extra_context={'license': 'Other'})

    assert (cj.project_path / "licenses" / "TEMPLATE_LICENSE.rst").exists()

    assert not (cj.project_path / "licenses" / "LICENSE.rst").exists()

    license_files = {"BSD 3-Clause": 'BSD3.rst',
                     "GNU GPL v3+": 'GPLv3.rst',
                     "Apache Software License 2.0": 'APACHE2.rst',
                     "BSD 2-Clause": 'BSD2.rst'}

    for name, lfile in license_files.items():
        assert (cj.project_path / "licenses" / lfile).exists()


def test_cruft_update_exists(bake_examples_compiled_dev_version):
    cj = bake_examples_compiled_dev_version

    present_files = [
        ".github/workflows/sub_package_update.yml",
        ".github/workflows/ci.yml",
    ]

    for afile in present_files:
        assert (cj.project_path / afile).exists()


def test_cruft_update_absent(bake_examples_compiled):
    cj = bake_examples_compiled

    present_files = [
        ".github/workflows/ci.yml"
    ]

    absent_files = [
        ".github/workflows/sub_package_update.yml"
    ]

    for afile in present_files:
        assert (cj.project_path / afile).exists()

    for afile in absent_files:
        assert not (cj.project_path / afile).exists()
