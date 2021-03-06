# Builtins stub used in dictionary-related test cases.

from typing import TypeVar, Generic, Iterable, Iterator, Tuple

T = TypeVar('T')
S = TypeVar('S')

class object:
    def __init__(self) -> None: pass

class type: pass

class dict(Iterable[T], Generic[T, S]):
    def __init__(self, arg: Iterable[Tuple[T, S]] = None) -> None: pass
    def __setitem__(self, k: T, v: S) -> None: pass
    def __iter__(self) -> Iterator[T]: pass
    def update(self, a: 'dict[T, S]') -> None: pass
class int: pass # for convenience
class str: pass # for keyword argument key type
class list(Iterable[T], Generic[T]): # needed by some test cases
    def __iter__(self) -> Iterator[T]: pass
    def __mul__(self, x: int) -> list[T]: pass

class tuple: pass
class function: pass
class float: pass
