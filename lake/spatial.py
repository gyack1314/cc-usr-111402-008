"""空间资料形状读取和外包矩形。"""
def coordinates(geometry):
    kind=geometry['type']
    if kind=='Point':return [geometry['coordinates']]
    if kind=='LineString':
        if len(geometry['coordinates'])<2:raise ValueError('折线不足两个点')
        return geometry['coordinates']
    if kind=='Polygon':
        if not geometry['rings']:raise ValueError('区域没有外环')
        result=[]
        for ring in geometry['rings']:
            if len(ring)<4 or ring[0]!=ring[-1]:raise ValueError('区域环未闭合')
            result.extend(ring)
        return result
    raise ValueError('几何类型不支持')

def bounds(geometry):
    points=coordinates(geometry)
    if any(len(p)!=2 or any(type(v) is not int for v in p) for p in points):raise ValueError('坐标不是二维整数')
    return [min(p[0] for p in points),min(p[1] for p in points),max(p[0] for p in points),max(p[1] for p in points)]

def inspect(data,storage,root):
    return {'crs':data['crs'],'regions':{r['row_id']:bounds(r['geometry']) for r in data['regions']},'tracks':{r['row_id']:bounds(r['geometry']) for r in data['tracks']}}
