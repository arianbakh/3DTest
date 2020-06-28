import os

from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3, Shader, Vec2

from settings import SHADERS_DIR


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.disableMouse()

        self.scene = self.loader.loadModel('models/environment')
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        self.taskMgr.add(self.spin_camera_task, 'SpinCameraTask')
        self.taskMgr.add(self.update_shader_inputs_task, 'UpdateShaderInputsTask')

        self.pandaActor = Actor('models/panda-model', {'walk': 'models/panda-walk4'})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        self.pandaActor.loop('walk')

        pos_interval1 = self.pandaActor.posInterval(13, Point3(0, -10, 0), startPos=Point3(0, 10, 0))
        pos_interval2 = self.pandaActor.posInterval(13, Point3(0, 10, 0), startPos=Point3(0, -10, 0))
        hpr_interval1 = self.pandaActor.hprInterval(3, Point3(180, 0, 0), startHpr=Point3(0, 0, 0))
        hpr_interval2 = self.pandaActor.hprInterval(3, Point3(0, 0, 0), startHpr=Point3(180, 0, 0))
        self.pandaPace = Sequence(pos_interval1, hpr_interval1, pos_interval2, hpr_interval2, name="pandaPace")
        self.pandaPace.loop()

        my_vertex_shader_path = os.path.join(SHADERS_DIR, 'my_shader.vert')
        my_fragment_shader_path = os.path.join(SHADERS_DIR, 'my_shader.frag')
        my_shader = Shader.load(Shader.SL_GLSL, vertex=my_vertex_shader_path, fragment=my_fragment_shader_path)

        tutorial_vertex_shader_path = os.path.join(SHADERS_DIR, 'tutorial_shader.vert')
        tutorial_fragment_shader_path = os.path.join(SHADERS_DIR, 'tutorial_shader.frag')
        tutorial_shader = Shader.load(Shader.SL_GLSL, vertex=tutorial_vertex_shader_path, fragment=tutorial_fragment_shader_path)

        self.pandaActor.setShaderInputs(**{
            'u_resolution': Vec2(self.win.getXSize(), self.win.getYSize()),
        })
        self.pandaActor.set_shader(tutorial_shader)

    def spin_camera_task(self, task):
        angle_degrees = task.time * 6.0
        angle_radians = angle_degrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angle_radians), -20 * cos(angle_radians), 3)
        self.camera.setHpr(angle_degrees, 0, 0)
        return Task.cont

    def update_shader_inputs_task(self, task):
        md = self.win.getPointer(0)
        self.pandaActor.setShaderInputs(**{
            'u_time': task.time,
            'u_mouse': Vec2(md.getX(), md.getY())
        })
        return Task.cont


app = MyApp()
app.run()
