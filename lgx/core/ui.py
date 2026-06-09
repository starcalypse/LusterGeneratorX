import bpy


class LGX_PT_MainPanel(bpy.types.Panel):

    bl_label = "Luster Generator X"
    bl_idname = "LGX_PT_MainPanel"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "LGX"

    def draw(self, context):

        layout = self.layout

        props = context.scene.lgx

        layout.prop(props, "preset")

        box = layout.box()
        box.label(text="Pattern")

        box.prop(props, "pattern_scale")
        box.prop(props, "pattern_seed")
        box.prop(props, "pattern_detail")

        layout.separator()

        layout.operator(
            "lgx.generate",
            text="Generate",
            icon="SHADING_RENDERED",
        )