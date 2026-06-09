"""
Luster Generator X

Material Builder
"""

import bpy


class MaterialBuilder:

    MATERIAL_NAME = "LGX Material"

    @classmethod
    def build(cls, context):

        obj = context.active_object

        if obj is None:
            return None

        # Create material
        material = bpy.data.materials.new(cls.MATERIAL_NAME)

        # Enable nodes
        material.use_nodes = True

        # Assign material
        obj.active_material = material

        return material