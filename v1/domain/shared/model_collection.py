from __future__ import annotations	
from typing import Callable, List
from collections.abc import Iterator
from uuid import uuid4
from domain.shared.model import Model

class ModelCollection(Iterator, Model):
    """Class to implement a collection for entities"""

    def __init__(self, collection: List[Model] = []):
        self._buffer: List[Model] = collection

    def __iter__(self) -> ModelCollection:
        self._index: int = 0

        return self
 
    def __next__(self) -> Model:
        try:
            model = self._buffer[self._index]
            self._index += 1
            return model
        except:
            raise StopIteration
    
    def append(self, model: Model) -> None:
        self._buffer.append(model)

    def remove(self, model: Model) -> None:
        self._buffer = list(filter(lambda buffer_model: buffer_model.id != model.id, self._buffer))

    def change(self, fn: Callable) -> None:
        self._buffer = list(map(fn, self._buffer))


