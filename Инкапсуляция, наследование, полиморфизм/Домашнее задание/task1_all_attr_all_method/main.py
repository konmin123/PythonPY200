from typing import Optional

if __name__ == "__main__":
    class Parent:
        nationality = "rus"
        _religion = "christianity"
        __stratum = "the proletariat"

        def __init__(self, role: Optional[str] = None, age: Optional[int] = None, name: Optional[int] = None):
            self.role = role
            self._age = age
            self.__name = name
    pass
