import arcpy
import river
arcpy.env.workspace = ".\shapefiles"
fc = 'Streams.shp'
with arcpy.da.SearchCursor (fc, ['OID@', 'SHAPE@']) as cursor:
    for row in cursor:
        oid = row[0]
        shape = row[1]
        segment = river.River(shape) # or row[1]
        si = round(segment.sinuosity(), 3)
        print(f'stream ID {oid} has a sinuosity of {si}')
