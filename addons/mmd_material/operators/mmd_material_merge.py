import bpy

class MMD_MATERIAL_OT_merge(bpy.types.Operator):
    bl_idname = "mmd.material_merge"
    bl_label = "合并MMD材质"
    bl_description = "合并相似的MMD材质以减少材质数量"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.scene.mmd_material_merge_enabled

    def execute(self, context):
        threshold = context.scene.mmd_material_merge_threshold
        self.report({'INFO'}, f"正在合并材质，阈值: {threshold}")
        # 这里添加实际的材质合并逻辑
        return {'FINISHED'}


def register():
    bpy.utils.register_class(MMD_MATERIAL_OT_merge)


def unregister():
    bpy.utils.unregister_class(MMD_MATERIAL_OT_merge)