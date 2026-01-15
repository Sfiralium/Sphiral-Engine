import bpy
import math

def create_semicircle_sphiral():
    """
    Generates a physically accurate Sphiral coil for Blender.
    Based on the 'Semicircle Reference' model: R_arc = R_coil / 2.
    """
    name = "Sphiral_Reference_Model"
    R_coil = 50.0       
    R_arc = R_coil / 2.0 
    Height_Coil = 30.0  
    Height_S = 10.0     
    Turns = 1.0         
    Thickness = 2.0     
    Resolution = 1000   
    
    if bpy.context.scene.objects.get(name):
        bpy.data.objects.remove(bpy.context.scene.objects[name], do_unlink=True)

    right_points = []
    
    # 1. S-ARC (Semicircle)
    res_arc = int(Resolution * 0.3)
    for i in range(res_arc + 1):
        t = i / res_arc 
        phi = math.pi * (1 - t)
        x = R_arc + R_arc * math.cos(phi) 
        y = -R_arc * math.sin(phi)
        z = (Height_S / 2) * t
        right_points.append((x, y, z))
        
    # 2. COIL
    res_coil = int(Resolution * 0.7)
    z_start = Height_S / 2
    for i in range(1, res_coil + 1):
        t = i / res_coil
        theta = Turns * 2 * math.pi * t
        x = R_coil * math.cos(theta)
        y = R_coil * math.sin(theta)
        z = z_start + (Height_Coil * t)
        right_points.append((x, y, z))

    # 3. ANTI-SYMMETRY (Left Side)
    final_coords = []
    for p in reversed(right_points):
        if p[0] == 0 and p[1] == 0: continue
        p_anti = (-p[0], -p[1], -p[2])
        final_coords.append(p_anti)
    final_coords.extend(right_points)

    # 4. MESH GENERATION
    curveData = bpy.data.curves.new(name, type='CURVE')
    curveData.dimensions = '3D'
    curveData.bevel_depth = Thickness
    curveData.fill_mode = 'FULL'
    polyline = curveData.splines.new('POLY')
    polyline.points.add(len(final_coords) - 1)
    for i, p in enumerate(final_coords):
        polyline.points[i].co = (p[0], p[1], p[2], 1)

    obj = bpy.data.objects.new(name, curveData)
    bpy.context.collection.objects.link(obj)
    
    # Material for visualization
    mat = bpy.data.materials.new(name="Sphiral_Mat")
    mat.use_nodes = True
    obj.data.materials.append(mat)
    
    print("Sphiral generated successfully.")

if __name__ == "__main__":
    create_semicircle_sphiral()
