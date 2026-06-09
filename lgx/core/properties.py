import bpy
from bpy.types import PropertyGroup
from bpy.props import (
    EnumProperty,
    FloatProperty,
    IntProperty,
)


class LGXProperties(PropertyGroup):

    preset: EnumProperty(
        name="Preset",
        items=[
            ("CASE_HARDENED", "Case Hardened", ""),
        ],
        default="CASE_HARDENED",
    )

    pattern_scale: FloatProperty(
        name="Scale",
        default=3.0,
        min=0.01,
        max=20.0,
    )

    pattern_seed: IntProperty(
        name="Seed",
        default=0,
        min=0,
    )

    pattern_detail: FloatProperty(
        name="Detail",
        default=8.0,
        min=0.0,
        max=16.0,
    )