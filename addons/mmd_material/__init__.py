import bpy

from .config import __addon_name__
from .i18n.dictionary import dictionary
from ...common.class_loader import auto_load
from ...common.class_loader.auto_load import add_properties, remove_properties
from ...common.i18n.dictionary import common_dictionary
from ...common.i18n.i18n import load_dictionary

# Add-on info
bl_info = {
    "name": "Basic Add-on Sample",
    "author": "[You name]",
    "blender": (3, 5, 0),
    "version": (0, 0, 1),
    "description": "This is a template for building addons",
    "warning": "",
    "doc_url": "[documentation url]",
    "tracker_url": "[contact email]",
    "support": "COMMUNITY",
    "category": "3D View"
}

_addon_properties = {}

# MMD材质合并操作符
from .operators.mmd_material_merge import MMD_MATERIAL_OT_merge

# MMD材质合并相关属性
_mmd_material_properties = {
    bpy.types.Scene: {
        "mmd_material_merge_threshold": bpy.props.FloatProperty(
            name="材质合并阈值",
            description="材质相似度阈值，低于此值的材质将被合并",
            default=0.8,
            min=0.0,
            max=1.0
        ),
        "mmd_material_merge_enabled": bpy.props.BoolProperty(
            name="启用材质合并",
            description="是否启用MMD材质合并功能",
            default=True
        )
    }
}

# You may declare properties like following, framework will automatically add and remove them.
# Do not define your own property group class in the __init__.py file. Define it in a separate file and import it here.
# 注意不要在__init__.py文件中自定义PropertyGroup类。请在单独的文件中定义它们并在此处导入。
# _addon_properties = {
#     bpy.types.Scene: {
#         "property_name": bpy.props.StringProperty(name="property_name"),
#     },
# }

def register():
    # Register classes
    auto_load.init()
    auto_load.register()
    add_properties(_addon_properties)
    add_properties(_mmd_material_properties)

    # Internationalization
    load_dictionary(dictionary)
    bpy.app.translations.register(__addon_name__, common_dictionary)

    print("{} addon is installed.".format(__addon_name__))


def unregister():
    # Internationalization
    bpy.app.translations.unregister(__addon_name__)
    # unRegister classes
    auto_load.unregister()
    remove_properties(_addon_properties)
    remove_properties(_mmd_material_properties)
    print("{} addon is uninstalled.".format(__addon_name__))
