from .panels import MasterControlPanel
from .object import ObjectGroup


class Scene():
    def __init__(self):
        self.objects: ObjectGroup = ObjectGroup()

        self.update_z_sorting = False

        self.change_scenes = False
        self.next_scene = None
    
    def queue_next_scene(self, next_scene_name):
        self.change_scenes = True
        self.next_scene = next_scene_name
    
    def unload(self):
        pass

    def update(self, master_panel: MasterControlPanel):
        for obj in self.objects:
            obj.update(master_panel, self.objects)

        master_panel.sound_panel.play_sound_queue()

    def draw(self, surface, game_data):
        if self.update_z_sorting:
            self.objects.sort()

        for obj in self.objects:
            obj.draw(surface, game_data)
