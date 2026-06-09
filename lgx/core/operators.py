import bpy

from .material_builder import MaterialBuilder


class LGX_OT_Generate(bpy.types.Operator):

    bl_idname = "lgx.generate"
    bl_label = "Generate"

    def execute(self, context):

        material = MaterialBuilder.build(context)

        if material is None:

            self.report(
                {'WARNING'},
                "No active object selected"
            )

            return {'CANCELLED'}

        self.report(
            {'INFO'},
            f"{material.name} created"
        )

        return {'FINISHED'}