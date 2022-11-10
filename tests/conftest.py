import py
import pytest

import tox
from _toxplugin import RunResult, reset_report


@pytest.fixture
def cmd(request, monkeypatch, capfd):
    """
    This fixture is copied from tox/src/_pytestplugin.py under the
    terms of the MIT license.
    """
    request.addfinalizer(py.path.local().chdir)

    def run(*argv):
        reset_report()
        with RunResult(argv, capfd) as result:
            _collect_session(result)

            # noinspection PyBroadException
            try:
                tox.session.main([str(x) for x in argv])
                assert False  # this should always exist with SystemExit
            except SystemExit as exception:
                result.ret = exception.code
            except OSError as e:
                traceback.print_exc()
                result.ret = e.errno
            except Exception:
                traceback.print_exc()
                result.ret = 1
        return result

    def _collect_session(result):
        prev_build = tox.session.build_session

        def build_session(config):
            result.session = prev_build(config)
            return result.session

        monkeypatch.setattr(tox.session, "build_session", build_session)

    yield run


@pytest.fixture(params=["bake_default",
                        "bake_examples_compiled",
                        "bake_examples"])
def cookiejar(request):
    """
    All the possible renders of the template.
    """
    return request.getfixturevalue(request.param)


@pytest.fixture(params=["bake_default", ])
def cookiejar_no_examples(request):
    """
    Templates rendered without the examples
    """
    return request.getfixturevalue(request.param)


@pytest.fixture(params=["bake_examples_compiled",
                        "bake_examples",
                        "bake_examples_compiled_dev_version"])
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


def _handle_cookiecutter_errors(result):
    if result.exception is not None:
        raise result.exception

    assert result.exit_code == 0

    return result


@pytest.fixture
def bake_default(cookies):
    """
    Render with the defaults.
    """
    result = cookies.bake()
    return _handle_cookiecutter_errors(result)


@pytest.fixture
def bake_examples(cookies):
    """
    Examples on.
    """
    result = cookies.bake(extra_context={"include_example_code": "y"})
    return _handle_cookiecutter_errors(result)


@pytest.fixture
def bake_examples_compiled(cookies):
    """
    Examples on.
    """
    result = cookies.bake(extra_context={"include_example_code": "y",
                                         "use_compiled_extensions": "y"})
    return _handle_cookiecutter_errors(result)


@pytest.fixture
def bake_examples_compiled_dev_version(cookies):
    """
    Examples on.
    """
    result = cookies.bake(extra_context={"include_example_code": "y",
                                         "use_compiled_extensions": "y",
                                         "enable_dynamic_dev_versions": "y"})
    return _handle_cookiecutter_errors(result)
