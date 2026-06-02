from typing import Literal, Optional, Self, Union


class _MissingSentinel:
  def __bool__(self) -> Literal[False]:
    return False


MISSING = _MissingSentinel()


class Element[T]:
  def __init__(self, value: T, *, index: int) -> None:
    if not isinstance(index, int):
      raise TypeError(f"index: Must be an instance of {int}; not {index.__class__}")
    if index < 0:
      raise ValueError("index: Must be greater than or equal to 0")
    self.index: int = index
    self.value: T = value


class Array[T]:
  def __bool__(self) -> bool:
    return bool(self.__elements)
  
  
  def __call__(self, *, size: int) -> Self[T]:
    if not isinstance(size, int):
      raise TypeError(f"size: Must be an instance of {int}; not {size.__class__}")
    if size < 0:
      raise ValueError("size: Must be greater than or equal to 0")
    self.__elements: list[Element[T]] = list()
    self.__index: Optional[int] = None
    self.__length: int = 0
    self.__size: int = size
    return self


  def __class_getitem__(cls, type_: T) -> Self[T]:
    if not isinstance(type_, type):
      raise TypeError(f"type_: Must be an instance of {type}; not {type_.__class__}")
    instance: Self[T] = cls()
    instance._element_type: T = type_
    return instance


  def __delitem__(self, index: int) -> None:
    if not isinstance(index, int):
      raise TypeError(f"index: Must be an instance of {int}; not {index.__class__}")
    if index < 0:
      index += self.size
    if self.size <= index:
      raise IndexError(f"index: Exceeded array size of {self.size}; given {index}")
    for i, element in enumerate(self):
      if element.index == index:
        self.__elements.pop(i)
        break


  def __getitem__(self, index: int) -> T:
    return self.get(index)


  def __iter__(self) -> Self:
    self.__index: int = -1
    return self


  def __next__(self) -> Element[T]:
    if self.__index is None:
      raise StopIteration
    if not self:
      self.__index = None
      raise StopIteration
    if self.__index + 1 == self.length:
      self.__index = None
      raise StopIteration
    self.__index += 1
    return self.__elements[self.__index]


  def __repr__(self) -> str:
    s: str = "["
    for element in self:
      if element is MISSING: continue
      s += f"{element.value!s}{", " if element.index + 1 < self.length else ""}"
    s += "]"
    return s


  def __setitem__(self, index: int, value: Any) -> None:
    self.set(index, value)


  def get(self, index: int) -> Union[T, MISSING]:
    if not isinstance(index, int):
      raise TypeError(f"index: Must be an instance of {int}; not {index.__class__}")
    if index < 0:
      index += self.size
    if self.size <= index:
      raise IndexError(f"index: Exceeded array size of {self.size}; given {index}")
    for element in self.__elements:
      if element.index == index:
        return element.value
    return MISSING


  @property
  def length(self) -> int:
    return len(self.__elements)


  def pop(self, index: int) -> Optional[T]:
    if not isinstance(index, int):
      raise TypeError(f"index: Must be an instance of {int}; not {index.__class__}")
    if index < 0:
      index += self.size
    if self.size <= index:
      raise IndexError(f"index: Exceeded array size of {self.size}; given {index}")
    for i, element in enumerate(self):
      if i == index:
        del self[i]
        return element.value


  def set(self, index: int, value: T) -> None:
    if not isinstance(index, int):
      raise TypeError(f"index: Must be an instance of {int}; not {index.__class__}")
    if index < 0:
      index += self.size
    if self.size <= index:
      raise IndexError(f"index: Exceeded array size of {self.size}; given {index}")
    if not isinstance(value, self._element_type):
      raise TypeError(f"value: Must be an instance of {self._element_type}; not {value.__class__}")
    e: Element = Element(value, index = index)
    if self:
      for i, element in enumerate(self):
        if element.index == index:
          self.__elements[i] = e
          return
        if index < element.index:
          self.__elements.insert(i - 1, e)
          return
      self.__elements.insert(index, e)
    else:
      self.__elements.insert(0, e)


  @property
  def size(self) -> int:
    return self.__size


class DynamicArray(Array):
  def __init__(self) -> None:
    super().__call__(size = 0)


static_array = Array[int](size = 3)
static_array[0] = 1
static_array[1] = 2
static_array[2] = 3
print(f"{static_array = }")   # [1, 2, 3]

dynamic_array = DynamicArray()
print(f"{dynamic_array = }")  # []