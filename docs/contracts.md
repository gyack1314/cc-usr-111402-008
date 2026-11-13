# 资料及接口契约

坐标为整数平面格网，crs字段必须完全一致，不做经纬度或投影转换。几何为Point、LineString和Polygon，环首尾闭合，外环及孔洞简单且不相交。Polygon包含外边界与孔洞边界，但不包含孔洞内部；intersects表示两集合交非空，包括线仅碰边界，covers表示Polygon覆盖整个点或整条线。不支持的几何、坏环或不同crs先拒绝，不猜修复。spatial.py已有格式验证与外包矩形；精确关系及分片索引尚未实现。

所有记录为合成仓资料；data/source.json保存原始字段和身份。storage.py负责摘要读取，table.py保存独立关系版本，relations.py保留SQL三值和袋语义。inspect只调用现有基础接口，不提供新增查询或管理能力。
