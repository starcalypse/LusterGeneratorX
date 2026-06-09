bl_info = {
    "name": "Luster Generator X",
    "author": "Starcalypse",
    "version": (0, 1, 0),
    "blender": (4, 2, 0),
    "location": "View3D > Sidebar > LGX",
    "description": "Modular procedural material framework",
    "category": "Material",
}

from .core.registration import register, unregister

if __name__ == "__main__":
    register()