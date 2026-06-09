import bpy
from .material_builder import MaterialBuilder

class LGX_OT_Generate(bpy.types.Operator):
    bl_idname = "lgx.generate"
    bl_label = "Generate"

    def execute(self, context):
        mat = MaterialBuilder.build(context)

        if mat is None:
            self.report({'WARNING'}, "Select a valid mesh object!")
            return {'CANCELLED'}

        self.report({'INFO'}, f"{mat.name} created and assigned")
        return {'FINISHED'}