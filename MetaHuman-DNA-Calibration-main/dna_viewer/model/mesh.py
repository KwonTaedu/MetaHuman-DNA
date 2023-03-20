from ..model.geometry import Point3

class Mesh:
    def __init__(self,dna_vertex_positions = [], dna_vertex_layout_positions = [],dna_vertex_layout_normals = [], polygon_faces = [], polygon_connects = [],
                 vertex_normals= [],derived_mesh_names=[]):
        self.dna_vertex_positions = dna_vertex_positions
        self.dna_vertex_layout_positions = dna_vertex_layout_positions
        self.dna_vertex_layout_normals = dna_vertex_layout_normals
        self.polygon_faces = polygon_faces
        self.polygon_connects = polygon_connects
        self.vertex_normals = vertex_normals
        self.derived_mesh_names = derived_mesh_names

