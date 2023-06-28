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


def test_dev_version_number(bake_examples_compiled_dev_version):
    cj = bake_examples_compiled_dev_version
    path = str(cj.project_path)

    subprocess.call(["git", "init", path])
    subprocess.call(["git", "commit", "-m", "initial", "."])
    subprocess.call(["pip", "install", "-e", path])

    import packagename

    # assert it hasn't fallen back to missing
    assert packagename.__version__ != "0.0.0"
    # assert it's actually correct
    assert packagename.__version__ == "0.1.dev0"

    with open(cj.project_path / "test", "w") as fobj:
        fobj.write("add untracked file to repo")

    # assert it's actually correct
    assert packagename.__version__ != "0.1.dev0"
    breakpoint()

    subprocess.call(["pip", "uninstall", "-y", "packagename"])
