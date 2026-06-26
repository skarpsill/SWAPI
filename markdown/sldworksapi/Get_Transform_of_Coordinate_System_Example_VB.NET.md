---
title: "Get Transform of Coordinate System Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Transform_of_Coordinate_System_Example_VB.NET.htm"
---

# Get Transform of Coordinate System Example (VB.NET)

This example shows how to get the transform of a coordinate system.

NOTE:Because VB.NET does not
directly support VARIANTs, you must cast the returned objects to the appropriate
data types.

'-------------------------------------

Private Sub API_Test2()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swApp As SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModel As SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgr As SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFeat As SldWorks.feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vXformArr() As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vXform As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
sAxisName As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRet As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp
= CType(CreateObject("SldWorks.Application"), SldWorks.SldWorks)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel
= swApp.IActiveDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelMgr
= swModel.ISelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFeat
= CType(swSelMgr.GetSelectedObject6(1,
0), SldWorks.feature)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}System.Diagnostics.Debug.WriteLine("File
= " & swModel.GetPathName)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}System.Diagnostics.Debug.WriteLine("kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Current
coordinate system = " & swModel.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swFileSaveAsCoordinateSystem))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}System.Diagnostics.Debug.WriteLine("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sAxisName
= swFeat.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vXformArr
= CType(swModel.GetCoordinateSystemXformByName(sAxisName),
Double())

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}System.Diagnostics.Debug.WriteLine("kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
& sAxisName)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Each vXform In vXformArr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}System.Diagnostics.Debug.WriteLine("kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Origin
= (" + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(-1.0#
* vXformArr(9) * 1000.0#) + "," + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(-1.0#
* vXformArr(10) * 1000.0#) + "," + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Str(-1.0#
* vXformArr(11) * 1000.0#) + _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}")
mm")

End Sub

'-------------------------------------
