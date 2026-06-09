import bpy

from .ui import LGX_PT_MainPanel
from .properties import LGXProperties

classes = (
    LGXProperties,
    LGX_PT_MainPanel,
)


def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.lgx = bpy.props.PointerProperty(
        type=LGXProperties
    )


def unregister():

    del bpy.types.Scene.lgx

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)