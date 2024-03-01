{% if cookiecutter.use_compiled_extensions == 'y' %}
def test_primes_c():
    from ..example_c import primes as primes_c
    assert primes_c(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
{% endif %}

def test_primes():
    from ..example_mod import primes
    assert primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
