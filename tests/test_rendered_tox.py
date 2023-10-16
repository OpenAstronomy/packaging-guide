"""
Test that tox runs inside a rendered template.
"""
import subprocess


def test_tox_runs(cookiejar_examples, tox_project):
    """
    Test that tox runs for all the configs.
    """
    cj = cookiejar_examples
    # We have to git init so that setuptools_scm and it's generated manifest
    path = str(cj.project_path)

    subprocess.call(["git", "config", "--global", "init.defaultBranch", "main"])
    subprocess.call(["git", "init", path])
    subprocess.call(["git", "-C", path, "add", "."])
    subprocess.call(["git", "-C", path, "commit", "-m", "initial"])

    project = tox_project({}, prj_path=cj.project_path)
    # workdir not inherited project path, defaulting to local tox
    # therefore workdir needs to be specified on run call
    res = project.run("--skip-missing-interpreters", "true",
                      "--workdir", path)
    res.assert_success()
