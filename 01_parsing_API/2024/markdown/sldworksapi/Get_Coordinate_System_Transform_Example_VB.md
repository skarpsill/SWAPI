---
title: "Get Coordinate System Transform Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Coordinate_System_Transform_Example_VB.htm"
---

# Get Coordinate System Transform Example (VBA)

This example shows how to get the default coordinate system transform
for the selected feature.

'------------------------------------------

'

' Preconditions: Model document is open and a feature
is selected.

'

' Postconditions: None

'

'-------------------------------------------

Option Explicit

Public Enum swUserPreferenceStringValue_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFileSaveAsCoordinateSystem
= 16

End Enum

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDocExtkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDocExtension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFeatkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swXformkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathTransform

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
sAxisNamekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDocExt = swModel.Extension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeat = swSelMgr.GetSelectedObject5(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Current
coordinate system = " & swModel.GetUserPreferenceStringValue(swFileSaveAsCoordinateSystem)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}sAxisName
= swFeat.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swXform = swDocExt.GetCoordinateSystemTransformByName(sAxisName)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
& sAxisName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Originkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & -1# * swXform.ArrayData(9)
* 1000# & ", " & -1# * swXform.ArrayData(10)
* 1000# & ", " & -1# * swXform.ArrayData(11)
* 1000# & ") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Rotational
sub-matrix 1kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & swXform.ArrayData(0)
& ", " & swXform.ArrayData(1)
& ", " & swXform.ArrayData(2)
& ")"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Rotational
sub-matrix 2kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & swXform.ArrayData(3)
& ", " & swXform.ArrayData(4)
& ", " & swXform.ArrayData(5)
& ")"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Rotational
sub-matrix 3kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & swXform.ArrayData(6)
& ", " & swXform.ArrayData(7)
& ", " & swXform.ArrayData(8)
& ")"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Translation
vectorkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & swXform.ArrayData(9)
* 1000# & ", " & swXform.ArrayData(10)
* 1000# & ", " & swXform.ArrayData(11)
* 1000# & ") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Scalekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swXform.ArrayData(12)

End Sub

'------------------------------------------
