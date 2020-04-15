from contextlib import contextmanager

from decimal import getcontext


@contextmanager
def change_precision(precision):
    try:
        first_precision = getcontext().prec
        getcontext().prec = precision
        yield
    except Exception:
        raise
    finally:
        getcontext().prec = first_precision


class ChangePrecision:
    def __init__(self, precision):
        self.precision = precision

    def __enter__(self):
        self.first_precision = getcontext().prec
        getcontext().prec = self.precision

        return self

    def __exit__(self, *args):
        getcontext().prec = self.first_precision
