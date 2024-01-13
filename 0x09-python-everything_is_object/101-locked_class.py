#!/usr/bin/python3


class LockedClass:
    """
    Prevenst user from dynamically creating new instance
    """
    __slots__ = ['first_name']
