import subprocess

import pytest


@pytest.fixture
def installed_cookiejar(cookiejar_examples):
    path = str(cookiejar_examples.project)

    subprocess.call(["git", "init", path])
    subprocess.call(["pip", "install", path])

    return cookiejar_examples


def test_examples_present(installed_cookiejar):
    cj = installed_cookiejar

    import packagename

    primes = packagename.do_primes(10)

    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    if cj.context['use_compiled_extensions']:
        cprimes = packagename.do_primes(10, usecython=True)

        assert primes == cprimes


