# decorator for priming coroutine
# coroutil.py
from functools import wraps

def coroutine(func):
    """Decorator: primes 'func' by advancing to first 'yield'"""
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer
