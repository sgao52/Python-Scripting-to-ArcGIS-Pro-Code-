import arcpy
import math
arcpy.env.workspace = '.\shapefiles'
fc = 'Streams.shp'

def sinuosity (shape):   # geometry object 'shape'
    channel = shape.length
    deltaX = shape.firstPoint.X - shape.lastPoint.X
    deltaY = shape.firstPoint.Y - shape.lastPoint.Y
    valley = math.sqrt(pow(deltaX,2) + pow(deltaY, 2))
    return channel/valley

with arcpy.da.SearchCursor(fc, ['OID@', 'SHAPE@']) as cursor:
    for row in cursor:
        oid = row[0]
        shape = row[1]
        si = round(sinuosity(shape), 3)
        print (f'Stream ID {oid} has a sinuosity index of {si}')

