class Point3:
    def __init__(self,x=0.0,y=0.0,z=0.0):
        self.x = x
        self.y = y
        self.z = z


class UV:
    def __init__(self,u=0.0,v=0.0):
        self.u = u
        self.v = v

class Layout:
    def __init__(self,position_index=0,texture_coordinate_index=0,normal_index=0):
        self.position_index = position_index
        self.texture_coordinate_index = texture_coordinate_index
        self.normal_index = normal_index

class Topology:
    def __init__(self,positions = None, texture_coordinates = None, normals= None, layouts=None ,face_vertex_layouts=None):
        self.positions = positions if positions else []
        self.texture_coordinates = texture_coordinates if texture_coordinates else []
        self.normals = normals if normals else []
        self.layouts = layouts if layouts else []
        self.face_vertex_layouts = face_vertex_layouts if face_vertex_layouts else []

class BlendShape:
    def __init__(self,channel=None,deltas=None):
        self.channel = channel
        self.deltas = deltas if deltas else {}

class SkinWeightsData:
    def __init__(self,maximum_influence_per_vertex = None, values = None, joint_indices= None):
        self.maximum_influence_per_vertex = maximum_influence_per_vertex
        self.values = values if values else []
        self.joint_indices = joint_indices if joint_indices else []


class Mesh:
    def __init__(self,name = None,topology = Topology(), skin_weights = SkinWeightsData(), blend_shapes = None):
        self.name = name
        self.topology = topology
        self.skin_weights = skin_weights
        self.blend_shapes = blend_shapes if blend_shapes else []

class Geometry:
    def __init__(self,meshes=None):
        self.meshes = meshes if meshes else {}

