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
    def __init__(self,positions = [], texture_coordinates = [], normals= [],layouts=[],face_vertex_layouts=[]):
        self.positions = positions
        self.texture_coordinates = texture_coordinates
        self.normals = normals
        self.layouts = layouts
        self.face_vertex_layouts = face_vertex_layouts

class BlendShape:
    def __init__(self,channel=None,deltas={}):
        self.channel = channel
        self.deltas = deltas

class SkinWeightsData:
    def __init__(self,maximum_influence_per_vertex = None, values = [], joint_indices= []):
        self.maximum_influence_per_vertex = maximum_influence_per_vertex
        self.values = values
        self.joint_indices = joint_indices


class Mesh:
    def __init__(self,name = None,topology = Topology(), skin_weights = SkinWeightsData(), blend_shapes = []):
        self.name = name
        self.topology = topology
        self.skin_weights = skin_weights
        self.blend_shapes = blend_shapes

class Geometry:
    def __init__(self,meshes={}):
        self.meshes = meshes

