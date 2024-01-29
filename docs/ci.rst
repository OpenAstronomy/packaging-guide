.. _ci:
======================
Continuous Integration
======================

Continuous Integration (CI) is the method by which software is tested and built before deployment to users.
A set of 'jobs' are defined in a ``.yml`` file, roughly taking the flow build - test - deploy.
Each run is built from a clean environment.
Workflows can be set to begin on triggers for example, a ``git push`` or a new tag.

There are an array solutions for running CI, Open Astronomy recommends `GitHub Actions <https://docs.github.com/en/actions/>`__ for projects using GitHub.
GitHub Actions workflows are defined in the ``.github/workflows/`` folder at the root of the repo.
Open Astronomy maintains a `set of tools <https://github.com/OpenAstronomy/github-actions-workflow>`__ to make configuring GitHub Actions easier.

Examples
++++++++
Testing
-------
In order GitHub Actions to run your workflow, it requires; an event to trigger the workflow, one or more jobs to complete and all steps must either run a script or trigger an action.
Looking at this in context:

.. code-block:: yml
    on:
      push:
      pull_request:
      workflow_dispatch:

    jobs:
      test:
        uses: OpenAstronomy/github-actions-workflows/.github/workflows/tox.yml@v1
        with:
          envs: |
            - linux: py311

In this case the workflow is triggered on push to branch, a PR and a manual trigger of the workflow on GitHub actions.
The second line of the job defines the name, in this case ``test`` and uses instructs the virtual machine to use Open Astronomy's pre-defined test with tox.
The ``envs`` list, defines which environments the test set is going to be ran on.
Therefore the package will be built using tox, will then trigger the testing in the selected environment/s.

Publishing to PyPI
------------------

No Compiled Extensions
######################

Python packages should be published on `pypi <https://pypi.org/>`__, in which case GitHub actions can facilitate this.
The ``on`` command will need to be more selective in this case.
Publishing to pypi would only be desirable on merges to master, here the trigger for the flow will be on push to the main branch specifically.
We also need to pass a pypi key, associated with your pypi account.
`Instructions on creating up your key here <https://pypi.org/help/#apitoken>`__.
The secret can be stored at organisation or repo level in GitHub settings, and the secret defined earlier in the workflow.


.. code-block:: yml
    on:
      push:
      tag:

   jobs:
     publish:
       uses: OpenAstronomy/github-actions-workflows/.github/workflows/publish_pure_python.yml@v1
       with:
         test_extras: test
         test_command: pytest --pyargs test_package
     secrets:
       pypi_token: ${{ secrets.pypi_token }}

Replace references to test_package with the package to be published.

With Compiled Extensions
########################

Almost all packages on pypi also have environment specific binaries with all dependencies packaged.
It is expected that a package publishes both a pure python distribution and the binary, see `here for examples <https://pypi.org/project/sunpy/#files>`__.

In this case, in addition to the running the tests, the ``with`` block also includes targets.
'Targets' are the distributions which the binary will be built for, so in this case it would be linux and MacOS 64 bit.
The ``publish`` method from the Open Astronomy GitHub actions packages the module with the dependencies for the specific targets listed

.. code-block:: yml
    jobs:
      publish:
        uses: OpenAstronomy/github-actions-workflows/.github/workflows/publish.yml@v1
        with:
          test_extras: test
          test_command: pytest --pyargs test_package
          targets: |
            - linux
            - cp3?-macosx_x86_64
      secrets:
        pypi_token: ${{ secrets.pypi_token }}


.. sam, work your way to the full example use the sunkit example
.. https://github.com/sunpy/sunkit-instruments/blob/main/.github/workflows/ci.yml

Putting it all together
#######################

Combining the above steps reveals a total workflow, build, testing and publishing

.. code-block:: yml
    name: package_deployment

    on:
      push:
      tag:

    jobs:
      test:
        uses: OpenAstronomy/github-actions-workflows/.github/workflows/tox.yml@v1
        with:
          envs: |
            - linux: py311

      publish_python:
        uses: OpenAstronomy/github-actions-workflows/.github/workflows/publish_pure_python.yml@v1
          with:
            test_extras: test
            test_command: pytest --pyargs test_package
        secrets:
          pypi_token: ${{ secrets.pypi_token }}

      publish_binaries:
       publish:
         uses: OpenAstronomy/github-actions-workflows/.github/workflows/publish.yml@v1
         with:
           test_extras: test
           test_command: pytest --pyargs test_package
           targets: |
             - linux
             - cp3?-macosx_x86_64
       secrets:
         pypi_token: ${{ secrets.pypi_token }}

The ``.github/workflows/`` directory may contain several workflows such as the above.
Each file may contain different workflows, with different triggers dependent on requirements.
