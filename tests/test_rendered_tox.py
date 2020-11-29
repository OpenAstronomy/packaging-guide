"""
Test that tox runs inside a rendered template.
"""
import subprocess



def test_tox_runs(cookiejar, cmd):
    """
    Test that tox runs for all the configs.
    """
    # We have to git init so that setuptools_scm works
    subprocess.call(["git", "init", str(cookiejar.project)])

    # The cmd fixture is imported from tox._pytestplugins and runs tox with the
    # given CLI args.
    result = cmd("-c", str(cookiejar.project))

    # Validate that we actually ran all the sub toxs
    assert "SKIPPED" not in result.output()
