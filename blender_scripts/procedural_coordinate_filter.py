import bpy
import random
import math

def purge_scene():
    for obj in list(bpy.data.objects):
        if obj.type == 'MESH':
            bpy.data.objects.remove(obj, do_unlink=True)

def generate_random_field(count=20, field_radius=10.0):
    for i in range(count):
        x = random.uniform(-field_radius, field_radius)
        y = random.uniform(-field_radius, field_radius)
        z = random.uniform(-field_radius, field_radius)
        
        if x>=0:
            bpy.ops.mesh.primitive_ico_sphere_add(radius=1.0, location=(x, y, z))
        
            spawned_mesh = bpy.context.active_object
        
            calculated_scale = 1.0 + (z * 0.08)
            clamped_scale = max(0.1, calculated_scale)
        
            spawned_mesh.scale = (clamped_scale, clamped_scale, clamped_scale)

purge_scene()
generate_random_field(count=30, field_radius=15.0)
