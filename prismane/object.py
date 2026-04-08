from __future__ import annotations
from .panels import MasterControlPanel
import pygame as pg


class Object():
    def __init__(self, idx: int, name: str, z_index:int=1):
        self.idx = idx
        self.name = name
        self.z_index = z_index

    def update(self, master_panel: MasterControlPanel, other_objects: ObjectGroup):
        pass

    def draw(self, surface: pg.Surface, master_panel: MasterControlPanel):
        pass


class ObjectGroup():
    def __init__(self):
        self.objects: list[Object] = []

    def append(self, object: Object):
        self.objects.append(object)

    def sort(self):
        self.objects.sort(key=lambda x: x.z_index)
    
    def remove(self, objects: list):
        for obj in objects:
            if obj in self.objects:
                self.objects.remove(obj)
    
    def __len__(self):
        return len(self.objects)

    def __iter__(self):
        for obj in self.objects:
            yield obj

    def __add__(self, other):
        if isinstance(other, ObjectGroup):
            self.objects += other.objects
            return self
        else:
            raise TypeError(f"{other} is not an instance of 'ObjectArray'")
