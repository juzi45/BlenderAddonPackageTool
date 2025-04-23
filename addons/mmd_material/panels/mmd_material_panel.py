import bpy

class MMD_MATERIAL_PT_merge_panel(bpy.types.Panel):
    bl_idname = "MMD_MATERIAL_PT_merge_panel"
    bl_label = "MMD材质合并"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MMD工具"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        # 添加启用开关
        layout.prop(scene, "mmd_material_merge_enabled", text="启用材质合并")
        
        # 添加阈值滑块
        if scene.mmd_material_merge_enabled:
            layout.prop(scene, "mmd_material_merge_threshold", slider=True)
            
            # 添加操作按钮
            layout.operator("mmd.material_merge", text="执行合并")


def register():
    bpy.utils.register_class(MMD_MATERIAL_PT_merge_panel)


def unregister():
    bpy.utils.unregister_class(MMD_MATERIAL_PT_merge_panel)