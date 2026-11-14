import bpy, sys, json, base64, struct
bpy.ops.wm.open_mainfile(filepath=sys.argv[1])
NAMES = {'Cube':'hull','Cube.001':'rim','Cube.002':'dome','Cylinder':'log','Cylinder.001':'mast','Cylinder.002':'boom','Plane':'board','Plane.001':'sail'}
out = {}
dg = None
for o in bpy.data.objects:
    if o.type != 'MESH': continue
    smooth = any(p.use_smooth for p in o.data.polygons)
    for m in o.modifiers:
        if m.type == 'SUBSURF': m.levels = 2 if o.name in ('Cube','Cube.001','Cube.002') else 1
dg = bpy.context.evaluated_depsgraph_get()
for o in bpy.data.objects:
    if o.type != 'MESH': continue
    ev = o.evaluated_get(dg); me = ev.to_mesh()
    me.calc_loop_triangles()
    M = o.matrix_world
    pos = []
    for v in me.vertices:
        w = M @ v.co
        pos += [-w.y, w.z, -w.x]          # Blender (x, y, z) -> web (bow along +x, y up)
    idx = []
    for t in me.loop_triangles: idx += list(t.vertices)
    xs, ys, zs = pos[0::3], pos[1::3], pos[2::3]
    smooth = any(p.use_smooth for p in me.polygons)
    print(NAMES[o.name], 'verts', len(me.vertices), 'tris', len(idx)//3, 'smooth', smooth,
          'x[%.2f %.2f] y[%.2f %.2f] z[%.2f %.2f]' % (min(xs), max(xs), min(ys), max(ys), min(zs), max(zs)))
    out[NAMES[o.name]] = {'smooth': smooth,
        'p': base64.b64encode(struct.pack('<%df' % len(pos), *pos)).decode(),
        'i': base64.b64encode(struct.pack('<%dH' % len(idx), *idx)).decode()}
    ev.to_mesh_clear()
open(sys.argv[2], 'w').write('window.MEGALITH_BOAT = ' + json.dumps(out) + ';\n')
bpy.ops.export_scene.gltf(filepath=sys.argv[3], export_apply=True, export_format='GLB')
