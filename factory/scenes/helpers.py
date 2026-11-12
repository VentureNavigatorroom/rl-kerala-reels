"""Low-poly Kerala tea-shop scene with two original characters. Renders shot stills with Cycles."""
import bpy, math, sys
from mathutils import Vector

OUT = "/home/claude/sample_work/stills"
PREVIEW = "--preview" in sys.argv
bpy.ops.wm.read_factory_settings(use_empty=True)
S = bpy.context.scene
_m = {}
def mat(rgb, rough=0.85, emit=0.0):
    key = (rgb, rough, emit)
    if key in _m: return _m[key]
    m = bpy.data.materials.new("m"); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*[c ** 2.2 for c in rgb], 1)
    b.inputs["Roughness"].default_value = rough
    if emit:
        b.inputs["Emission Color"].default_value = (*[c ** 2.2 for c in rgb], 1); b.inputs["Emission Strength"].default_value = emit
    _m[key] = m; return m

def fin(o, m, parent=None, rot=None, scale=None):
    o.data.materials.append(mat(*m) if isinstance(m[0], tuple) else mat(m))
    if rot: o.rotation_euler = [math.radians(a) for a in rot]
    if scale: o.scale = scale
    if parent: o.parent = parent
    return o
def box(size, loc, m, **k):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc); o = bpy.context.object; o.scale = size
    k.pop("scale", None); return fin(o, m, **k)
def cyl(r, h, loc, m, v=8, r2=None, **k):
    if r2 is None: bpy.ops.mesh.primitive_cylinder_add(vertices=v, radius=r, depth=h, location=loc)
    else: bpy.ops.mesh.primitive_cone_add(vertices=v, radius1=r, radius2=r2, depth=h, location=loc)
    return fin(bpy.context.object, m, **k)
def ico(r, loc, m, sub=1, **k):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=sub, radius=r, location=loc)
    return fin(bpy.context.object, m, **k)
def empty(loc, rotz=0):
    bpy.ops.object.empty_add(location=loc); e = bpy.context.object; e.rotation_euler = (0, 0, math.radians(rotz)); return e

# ---------- palette ----------
RED_OXIDE, CREAM, WOOD, DWOOD = (0.62, 0.17, 0.13), (0.96, 0.91, 0.78), (0.55, 0.36, 0.2), (0.36, 0.22, 0.12)
TERRA, GRASS, PADDY, WATER = (0.8, 0.36, 0.2), (0.36, 0.66, 0.25), (0.62, 0.8, 0.3), (0.25, 0.62, 0.78)
LEAF, TRUNK, WHITE, BLACK = (0.2, 0.55, 0.2), (0.5, 0.4, 0.28), (0.97, 0.97, 0.95), (0.06, 0.05, 0.05)
SKIN_A, SKIN_V = (0.72, 0.47, 0.32), (0.6, 0.38, 0.25)

