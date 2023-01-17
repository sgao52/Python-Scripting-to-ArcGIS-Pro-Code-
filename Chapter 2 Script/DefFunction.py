import arcpy
arcpy.env.workspace = '.\shapefiles'

def listfieldnames (table):
    fields = arcpy.ListFields (table)
    namelist = []
    for field in fields:
        namelist.append (field.name)
    return namelist

fieldname = listfieldnames ('Libraries.shp')
print(fieldname)