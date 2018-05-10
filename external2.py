import arcpy

arcpy.env.workspace = "m:/Documents/Programming2/Prac1"

try:
	try:
		arcpy.ImportToolbox("m:/Documents/Programming2/Prac1/Models.tbx","models")
	except arcpy.ExecuteError as e:
		print("Import toolbox error", e)
	if arcpy.Exists("TEST.shp"):
		arcpy.Delete_management("TEST.shp")
	if arcpy.Exists("buffer.shp"):
		arcpy.Delete_management("buffer.shp")
	try:
		arcpy.Explosion_models("explosion0/point","build0/polygon","TEST.shp","50 Meters","buffer.shp")
	except arcpy.ExecuteError as e:
		print("Model run error", e)
except Exception as e:
	print(e)
	
