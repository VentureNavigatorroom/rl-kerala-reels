# ---------- light, world, render ----------
bpy.ops.object.light_add(type='SUN'); sun = bpy.context.object; sun.rotation_euler = (math.radians(52), math.radians(8), math.radians(-28))
sun.data.energy = 4.2; sun.data.color = (1, 0.95, 0.85); sun.data.angle = math.radians(3)
w = bpy.data.worlds.new("w"); w.use_nodes = True; S.world = w
bg = w.node_tree.nodes["Background"]; bg.inputs[0].default_value = (0.38, 0.66, 1.0, 1); bg.inputs[1].default_value = 1.5
S.render.engine = "CYCLES"; S.cycles.device = "CPU"; S.cycles.samples = 12 if PREVIEW else 24; S.cycles.use_denoising = True; S.cycles.seed = 7
S.cycles.max_bounces = 4
S.view_settings.view_transform = "Standard"; S.view_settings.look = "None"
sc = 0.35 if PREVIEW else 1.0
S.render.resolution_x = int(1080 * sc); S.render.resolution_y = int(1920 * sc); S.render.image_settings.file_format = "PNG"
S.render.threads_mode = "FIXED"; S.render.threads = 2

def cam(name, loc, target, lens):
    bpy.ops.object.camera_add(location=loc); c = bpy.context.object; c.data.lens = lens
    c.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler(); return c
cams = dict(wide=cam("w", (0, -5.3, 1.55), (0, 0.3, 1.3), 34),
            A=cam("a", (0.2, -2.25, 1.62), (-1.0, 0.0, 1.5), 50),
            V=cam("v", (-0.2, -2.25, 1.62), (1.0, 0.0, 1.5), 50))
from bpy_extras.object_utils import world_to_camera_view
def shot(camname, a_open, v_open, tag):
    S.camera = cams[camname]
    S.render.use_border = bool(a_open or v_open); S.render.use_crop_to_border = False
    if S.render.use_border:
        bpy.context.view_layer.update()
        p = world_to_camera_view(S, S.camera, (A_o if a_open else V_o).matrix_world.translation)
        S.render.border_min_x, S.render.border_max_x = max(0, p.x - 0.09), min(1, p.x + 0.09)
        S.render.border_min_y, S.render.border_max_y = max(0, p.y - 0.05), min(1, p.y + 0.05)
        print("BORDER", camname, tag, round(p.x, 4), round(p.y, 4), flush=True)
    A_c.hide_render, A_o.hide_render, V_c.hide_render, V_o.hide_render = a_open, not a_open, v_open, not v_open
    S.render.filepath = f"{OUT}/{'prev_' if PREVIEW else ''}{camname}_{tag}.png"; bpy.ops.render.render(write_still=True); print("rendered", camname, tag, flush=True)
