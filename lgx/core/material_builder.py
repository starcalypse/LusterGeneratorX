import bpy

class MaterialBuilder:
    MATERIAL_NAME = "LGX Material"

    @classmethod
    def build(cls, context):
        obj = context.active_object

        if obj is None or obj.type != 'MESH':
            return None

        # Create new material
        material = bpy.data.materials.new(cls.MATERIAL_NAME)
        material.use_nodes = True

        # Assign material
        if len(obj.material_slots) == 0:
            obj.data.materials.append(material)
        else:
            obj.active_material = material

        return material