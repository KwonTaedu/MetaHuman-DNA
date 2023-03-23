from ..model.geometry import Point3


class Mesh:
    def __init__(self,dna_vertex_positions = None,
                dna_vertex_layout_positions = None,
                dna_vertex_layout_normals = None, 
                polygon_faces = None,
                polygon_connects =None,
                 vertex_normals=None,
                 derived_mesh_names=None
        ):
        self.dna_vertex_positions = dna_vertex_positions if dna_vertex_positions else []
        self.dna_vertex_layout_positions = dna_vertex_layout_positions if dna_vertex_layout_positions else []
        self.dna_vertex_layout_normals = dna_vertex_layout_normals if dna_vertex_layout_normals else []
        self.polygon_faces = polygon_faces if polygon_faces else []
        self.polygon_connects = polygon_connects if polygon_connects else []
        self.vertex_normals = vertex_normals if vertex_normals else []
        self.derived_mesh_names = derived_mesh_names if derived_mesh_names else []