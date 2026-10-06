import bpy
import random
import math

def purge_scene():
    for obj in list(bpy.data.objects):
        if obj.type == 'MESH':
            bpy.data.objects.remove(obj, do_unlink=True)

def generate_asteroid_field(count=30, field_radius=15.0, min_clearance=4.0):
    spawned_positions = []
    
    for i in range(count):
        x = random.uniform(-field_radius, field_radius)
        y = random.uniform(-field_radius, field_radius)
        z = random.uniform(-field_radius, field_radius)
        current_pos = (x, y, z)
        
        is_position_safe = True
        
        for existing_pos in spawned_positions:
            distance = math.dist(current_pos, existing_pos)
            if distance < min_clearance:
                is_position_safe = False
                break
                
        if is_position_safe:
            spawned_positions.append(current_pos)
            
            bpy.ops.mesh.primitive_ico_sphere_add(radius=1.0, location=current_pos)
            rock = bpy.context.active_object
            
            calculated_scale = 1.0 + (z * 0.05)
            clamped_scale = max(0.1, calculated_scale)
            
            rock.scale = (clamped_scale, clamped_scale, clamped_scale)
            
            rock.rotation_euler = (
                random.uniform(0, math.pi),
                random.uniform(0, math.pi),
                random.uniform(0, math.pi)
            )

purge_scene()
generate_asteroid_field(count=50, field_radius=20.0, min_clearance=3.5)
