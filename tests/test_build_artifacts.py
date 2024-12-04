"""
This test file let's you render the examples we use in the tests to a given
directory for ease of inspection.
This means that you can check things like whitespace or other issues in a rendered example.
"""
import pytest
import shutil
from pathlib import Path


@pytest.mark.parametrize("bake_name",
                         ["bake_default",
                          "bake_examples",
                          "bake_examples_compiled",
                          "bake_examples_compiled_dev_version",
                          "bake_examples_url_extensions"])
def test_render_template(request, bake_name, pytestconfig):
    bake = request.getfixturevalue(bake_name)
    cached_dir = pytestconfig.getoption("--cookie-location")
    if not cached_dir:
        pytest.skip("No cookie location provided skipping render")

    target_dir = Path(cached_dir) / bake_name.removeprefix("bake_")
    if target_dir.exists():
        shutil.rmtree(target_dir)
    shutil.copytree(bake.project_path, target_dir)
