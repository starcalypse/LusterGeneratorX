import bpy


class LGX_OT_Generate(bpy.types.Operator):

    bl_idname = "lgx.generate"
    bl_label = "Generate"

    def execute(self, context):

        from .material_builder import MaterialBuilder

        MaterialBuilder.build(context)

        self.report(
        {'INFO'},
        "LGX Material Created"
        )

        return {'FINISHED'}