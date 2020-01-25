import pytest

# This is probably ill advised
from tox._pytestplugin import *


@pytest.fixture(params=["bake_default",
                        "bake_examples_compiled",
                        "bake_examples"])
def cookiejar(request):
    """
    All the possible renders of the template.
    """
    return request.getfixturevalue(request.param)


@pytest.fixture(params=["bake_default",])
def cookiejar_no_examples(request):
    """
    Templates rendered without the examples
    """
    return request.getfixturevalue(request.param)


@pytest.fixture(params=["bake_examples_compiled",
                        "bake_examples"])
def cookiejar_examples(request):
    """
    Templates rendered with the examples
    """
    return request.getfixturevalue(request.param)


@pytest.fixture
def baked(request):
    """
    A specific render of the template
    """
    return request.getfixturevalue(request.param)


@pytest.fixture
def bake_default(cookies):
    """
    Render with the defaults.
    """
    return cookies.bake()


@pytest.fixture
def bake_examples(cookies):
    """
    Examples on.
    """
    return cookies.bake(extra_context={"include_example_code": "y"})


@pytest.fixture
def bake_examples_compiled(cookies):
    """
    Examples on.
    """
    return cookies.bake(extra_context={"include_example_code": "y",
                                       "use_compiled_extensions": "y"})
