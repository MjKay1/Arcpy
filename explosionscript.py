import arcpy
import sys
import traceback

Explosive = arcpy.GetParameterAsText(0)

Area = arcpy.GetParameterAsText(1)

Blast_Zone_Name = arcpy.GetParameterAsText(2)
if Blast_Zone_Name == '#' or not Blast_Zone_Name:
    Blast_Zone_Name = "M:\\Documents\\Programming2\\Prac1\\Intersect.shp" # provide a default value if unspecified

Blast_Range = arcpy.GetParameterAsText(3)

try:
	try:
		arcpy.ImportToolbox("m:/Documents/Programming2/Prac1/Models.tbx","models")
	except arcpy.ExecuteError as e:
		print("Import toolbox error", e)
		tb = sys.exc_info()[2]
		tbinfo = traceback.format_tb(tb)[0]
		print(tbinfo)
		# or
		arcpy.AddError(tbinfo)
	if arcpy.Exists("TEST.shp"):
		arcpy.Delete_management("TEST.shp")
	if arcpy.Exists("buffer.shp"):
		arcpy.Delete_management("buffer.shp")
	try:
		arcpy.Explosion_models(Explosive,Area,Blast_Zone_Name,Blast_Range,"buffer.shp")
	except arcpy.ExecuteError as e:
		print("Model run error", e)
		tb = sys.exc_info()[2]
		tbinfo = traceback.format_tb(tb)[0]
		print(tbinfo)
		# or
		arcpy.AddError(tbinfo)
except Exception as e:
	print(e)
	tb = sys.exc_info()[2]
	tbinfo = traceback.format_tb(tb)[0]
	print(tbinfo)
	# or
	arcpy.AddError(tbinfo)

