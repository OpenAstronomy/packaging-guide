# Try to use setuptools_scm to get the current version; this is only used
# in development installations from the git repository.
from pathlib import Path

try:
    from setuptools_scm import get_version

    version = get_version(root=Path('../..'), relative_to=__file__)
except ImportError:
    raise
except Exception as e:
    raise ValueError('setuptools_scm can not determine version.') from e
