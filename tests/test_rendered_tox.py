"""
Test that tox runs inside a rendered template.
"""
import subprocess

def test_tox_runs(cookiejar_examples, tox_project):
    """
    Test that tox runs for all the configs.
    """
    cj = cookiejar_examples
    # We have to git init so that setuptools_scm works
    subprocess.call(["git", "init", str(cj.project_path)])


    project = tox_project({}, prj_path=cj.project_path)
    # res = project.run("--skip-missing-interpreters")
    # assert res.success
    print(list(cj.project_path.glob("**")))
    assert False
