from .panels import MasterControlPanel
from .object import ObjectArray


class Scene():
    def __init__(self, name: str, master_panel: MasterControlPanel, amnesia:bool=False):
        super().__init__([], 0)
        self.name = name
        self.objects = ObjectArray()

        self.update_z_sorting = False

        self.amnesia: bool = amnesia

        self.change_scenes = False
        self.next_scene = None
    
    def queue_next_scene(self, scene, master_panel: MasterControlPanel):
        if self.amnesia:
            self.forget(master_panel)

        self.change_scenes = True
        self.next_scene = scene

    def forget(self, master_panel: MasterControlPanel):
        self = Scene(self.name, master_panel, self.amnesia)

    def update(self, master_panel: MasterControlPanel):
        for obj in self.objects:
            obj.update(master_panel, self.objects)

        master_panel.sound_panel.play_sound_queue()

    def draw(self, surface, game_data):
        if self.update_z_sorting:
            self.objects.sort()

        for obj in self.objects:
            obj.draw(surface, game_data)