#!/usr/bin/python3
"""This module is for a locked class."""


class LockedClass:
    """Prevenst user from dynamically creating new instance."""

    __slots__ = ['first_name']
