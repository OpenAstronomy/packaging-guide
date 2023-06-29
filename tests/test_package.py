import io
import sys
import subprocess

import pytest


@pytest.fixture
def installed_cookiejar(cookiejar_examples):
    path = str(cookiejar_examples.project_path)

    subprocess.call(["git", "init", path])
    subprocess.call(["pip", "install", path])

    yield cookiejar_examples

    subprocess.call(["pip", "uninstall", "-y", "packagename"])


def test_examples_present(installed_cookiejar):
    cj = installed_cookiejar

    import packagename

    primes = packagename.do_primes(10)

    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    if cj.context['use_compiled_extensions']:
        cprimes = packagename.do_primes(10, usecython=True)

        assert primes == cprimes


def test_dev_version_number(virtualenv, bake_examples_compiled_dev_version):
    cj = bake_examples_compiled_dev_version
    path = str(cj.project_path)

    subprocess.run(["git", "init", path], check=True)
    with open(cj.project_path / ".gitignore", "w") as fobj:
        fobj.writelines([
            "packagename/_compiler.c\n",
            "packagename/_version.py\n",
            "packagename/example_c.c\n",
            "*.so\n",
            "*.egg-info\n",
            "__pycache__\n",
        ])
    subprocess.run(["git", "-C", path, "config", "author.name", "'Test User'"], check=True)
    subprocess.run(["git", "-C", path, "config", "author.email", "'test@openastronomy.org'"], check=True)
    subprocess.run(["git", "-C", path, "config", "-l"], check=True)
    subprocess.run(["git", "-C", path, "add", "."], check=True)
    subprocess.run(["git", "-C", path, "commit", "-m", "initial"], check=True)
    subprocess.run(["git", "-C", path, "tag", "v0.1"], check=True)

    # Create a new virtualenv with the package installed
    virtualenv.run(f"pip install setuptools_scm")
    virtualenv.run(f"pip install -e {path}")

    # assert it's actually correct
    dynamic_version = virtualenv.run('python -c "import packagename; print(packagename.__version__)"', capture=True).strip()
    assert dynamic_version == "0.1"

    with open(cj.project_path / "README.md", "a") as fobj:
        fobj.seek(0, io.SEEK_END)
        fobj.write("add untracked file to repo")

    subprocess.run(["git", "-C", path, "add", "."], check=True)
    subprocess.run(["git", "-C", path, "commit", "-m", "second"], check=True)

    # assert it's actually correct
    dynamic_version = virtualenv.run('python -c "import packagename; print(packagename.__version__)"', capture=True).strip()
    assert dynamic_version.startswith("0.2.dev1")
