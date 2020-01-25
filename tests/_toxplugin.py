"""
The contents of this file are copied from tox/src/_pytestplugin.py under the
terms of the MIT license.
"""

import time


__all__ = ['reset_report', 'RunResult']


def reset_report(quiet=0, verbose=0):
    from tox.reporter import _INSTANCE

    _INSTANCE._reset(quiet_level=quiet, verbose_level=verbose)


class RunResult:
    def __init__(self, args, capfd):
        self.args = args
        self.ret = None
        self.duration = None
        self.out = None
        self.err = None
        self.session = None
        self.capfd = capfd

    def __enter__(self):
        self._start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.duration = time.time() - self._start
        self.out, self.err = self.capfd.readouterr()

    def _read(self, out, pos):
        out.buffer.seek(pos)
        return out.buffer.read().decode(out.encoding, errors=out.errors)

    @property
    def outlines(self):
        out = [] if self.out is None else self.out.splitlines()
        err = [] if self.err is None else self.err.splitlines()
        return err + out

    def __repr__(self):
        res = "RunResult(ret={}, args={!r}, out=\n{}\n, err=\n{})".format(
            self.ret, self.args, self.out, self.err
        )
        return res

    def output(self):
        return "{}\n{}\n{}".format(self.ret, self.err, self.out)

    def assert_success(self, is_run_test_env=True):
        msg = self.output()
        assert self.ret == 0, msg
        if is_run_test_env:
            assert any("  congratulations :)" == l for l in reversed(self.outlines)), msg

    def assert_fail(self, is_run_test_env=True):
        msg = self.output()
        assert self.ret, msg
        if is_run_test_env:
            assert not any("  congratulations :)" == l for l in reversed(self.outlines)), msg
