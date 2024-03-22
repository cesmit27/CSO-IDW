import arcpy as a
from arcpy.sa import *

def IDW_Model():  # IDW_Model

    a.env.overwriteOutput = False

    a.CheckOutExtension("3D")
    a.CheckOutExtension("spatial")

    Sonde_Locations = r"D:\CSO GIS\Sonde_Data\Sonde_Data.gdb\Sonde_Locations"

#Replace DO with whatever water quality metric you need
    IDW_DO = r"D:\CSO GIS\Sonde_Data\Sonde_Data.gdb\IDW_DO"
    IDW_Model = IDW_DO
    with a.EnvManager(extent="-74.5796313262923 40.2655574760266 -73.5718087106604 41.1005995132686 GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", \
                          mask=r"D:\CSO GIS\Sonde_Data\Sonde_Data.gdb\Study_Area", outputCoordinateSystem="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"):
        IDW_DO = a.sa.Idw(Sonde_Locations, "DO__mg_L_", "3.34016814896799E-03", 2, "VARIABLE 12", "")
        IDW_DO.save(IDW_Model)

#DONT FORGET TO CHANGE THE FIELD, use this code to check correct name since the parantheses were causing issues
'''
fields = a.ListFields(r"D:\CSO GIS\Sonde_Data\Sonde_Data.gdb\Sonde_Locations")
for field in fields:
    print(field.name)
'''
#TRied to get to add direct to the map, but couldn't
'''
NewLayer= r'D:\CSO GIS\Sonde_Data\Sonde_Data.gdb\IDW_DO'
aprx = a.mp.ArcGISProject(r"D:\CSO GIS\Sonde_Data\Sonde_Data.aprx")
mapx = aprx.listMaps("Map")[0]
new_layer = mapx.addDataFromPath(NewLayer)
new_layer.name = "IDW_DO"
aprx.save()
'''
if __name__ == '__main__':
    with a.EnvManager(scratchWorkspace=r"D:\CSO GIS\Sonde_Data\Sonde_Data.gdb", workspace="D:\CSO GIS\Sonde_Data\Sonde_Data.gdb"):
        IDW_Model()

