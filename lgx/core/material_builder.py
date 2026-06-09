import bpy


class MaterialBuilder:

    MATERIAL_NAME = "LGX Material"

    @classmethod
    def build(cls, context):

        obj = context.active_object

        if obj is None:
            return None

        material = bpy.data.materials.get(cls.MATERIAL_NAME)

        if material:

            bpy.data.materials.remove(material)

        material = bpy.data.materials.new(cls.MATERIAL_NAME)

        material.use_nodes = True

        obj.active_material = material

        return material