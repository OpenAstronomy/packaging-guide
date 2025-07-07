{% if cookiecutter.use_compiled_extensions == 'y' %}
def test_primes_c():
    from {{ cookiecutter.module_name }}.example_c import primes as primes_c  # noqa: PLC0415
    assert primes_c(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
{% endif %}

def test_primes():
    from {{ cookiecutter.module_name }}.example_mod import primes  # noqa: PLC0415
    assert primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
