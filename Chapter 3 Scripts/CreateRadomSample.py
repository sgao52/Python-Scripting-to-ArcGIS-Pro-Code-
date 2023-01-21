import arcpy
import random
inputfc = 'D:\GISDATA\Salzburg\Salzburg\City_of_Salzburg\Libraries.shp'
outputfc = 'D:\GISDATA\Salzburg\Salzburg\City_of_Salzburg\LibrariesRandom.shp'
outcount = 5 # random sample numbers
inlist = []
# list FIDs in the table and select random samples
with arcpy.da.SearchCursor(inputfc, 'OID@') as cursor:
    for row in cursor:
        id = row[0]
        inlist.append(id)
randomlist = random.sample(inlist, outcount)
# find a field for sql expression, also correspond to random FIDs selected.
desc = arcpy.da.Describe(inputfc)
fldname = desc['OIDFieldName']
# arcpy.AddFieldDelimiters adds field delimiters to a field name to allow for use in SQL expressions
# For instance, file geodatabase and .shp files use double quotation marks(""), personal geodatabases use square brackets([]), and enterprise geodatabases don not use field delimiters.
# This function can take away the guess work in ensuring that the field delimiters used with your SQL expression are the correct ones.
# I tried the "FID" in sql expression, it worked
sqlfield = arcpy.AddFieldDelimiters(inputfc, fldname)
# SQL expression, used in next step, in SQL, this list must be in a pair of parentheses, which is equivalent to a tuple in Python.
sqlexp = f'{sqlfield} IN {tuple(randomlist)}'
# arcpy.Select_analysis extracts features from an input feature class or input feature layer, typically using a select or SQL expression, and stores them in an output feature class.
arcpy.Select_analysis(inputfc, outputfc, sqlexp)
