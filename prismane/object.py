from .components import Component
from .panels import MasterControlPanel
import pygame as pg


class Object():
    def __init__(self, idx: int, name: str, components: list[Component], z_index:int=1):
        self.idx = idx
        self.name = name
        self.z_index = z_index
        self.components = components

    def update(self, master_panel: MasterControlPanel, other_objects: list):
        pass

    def draw(self, surface: pg.Surface, master_panel: MasterControlPanel):
        pass


class ObjectArray():
    def __init__(self):
        self.objects: list[Object] = set()

    def append(self, object: Object):
        self.objects.append(object)

    def sort(self):
        self.objects.sort(key=lambda x: x.z_index)
    
    def remove(self, objects: list):
        for obj in objects:
            if obj in self.objects:
                self.objects.remove(obj)
    
    def filter(self, components: list[Component]) -> list[Object]:
        filtered = []
        for obj in self.objects:
            satisfies = True
            for component in components:
                if component not in obj.components:
                    satisfies = False
                    break
            if satisfies:
                filtered.append(obj)
        return filtered

    def __len__(self):
        return len(self.objects)

    def __iter__(self):
        for obj in self.objects:
            yield obj

    def __add__(self, other):
        if isinstance(other, ObjectArray):
            self.objects += other.objects
            return self
        else:
            raise TypeError(f"{other} is not an instance of 'ObjectArray'")