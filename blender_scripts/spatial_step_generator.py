import bpy
import math
cube_ref=bpy.data.objects["Cube"]
cube_ref.location=(5.0,-2.0,3.5)
cube_ref.rotation_euler=(0.0,math.radians(90),0.0)
def purge_scene():
    for obj in list(bpy.data.objects):
        if obj.type=="MESH":
            bpy.data.objects.remove(obj,do_unlink=True)
def generate_staircase(count=10):
    for i in range(count) :
        bpy.ops.mesh.primitive_cube_add(size=2.0)
        active_obj=bpy.context.active_object
        active_obj.location=(10.0+(2*i),10.0,10.0+(1*i))
        active_obj.rotation_euler=(0.0,0.0,math.radians(15*i))
purge_scene()
generate_staircase()

    





