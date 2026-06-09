import bpy


class LGX_PT_MainPanel(bpy.types.Panel):

    bl_label = "Luster Generator X"
    bl_idname = "LGX_PT_MainPanel"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "LGX"

    def draw(self, context):

        layout = self.layout

        layout.label(text="LGX Foundation")