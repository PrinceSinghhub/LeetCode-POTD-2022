from typing import List


class Iterator:

    def __init__(self, nums: List[int]) -> None:
        """Initializes an iterator object to the beginning of a list."""

        self._nums = nums
        self._current = 0

    def hasNext(self) -> bool:
        """Returns true if the iteration has more elements."""

        return self._current < len(self._nums)

    def next(self) -> int:
        """Returns the next element in the iteration."""

        if not self.hasNext():
            raise StopIteration()

        value = self._nums[self._current]
        self._current += 1
        return value


class PeekingIterator:

    def __init__(self, iterator: Iterator):
        """Initialize your data structure here."""

        self._iterator = iterator
        self._buffer = None

    def peek(self) -> int:
        """Returns the next element in the iteration without advancing the iterator."""

        if self._buffer is None:
            self._buffer = self._iterator.next()

        return self._buffer

    def next(self) -> int:

        value, self._buffer = self._buffer, None

        if value is not None:
            return value
        else:
            return self._iterator.next()

    def hasNext(self) -> bool:

        return self._buffer is not None or self._iterator.hasNext()

