import bpy


class LGX_OT_Generate(bpy.types.Operator):

    bl_idname = "lgx.generate"
    bl_label = "Generate"

    def execute(self, context):

        self.report(
            {'INFO'},
            "LGX Generate pressed"
        )

        return {'FINISHED'}