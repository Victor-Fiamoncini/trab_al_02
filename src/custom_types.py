from typing import List, TypeVar, Union

Number = Union[float, int]

NumberInsideList = TypeVar('NumberInsideList', int, float)

Vector = List[NumberInsideList]

VectorBase = List[Vector]
