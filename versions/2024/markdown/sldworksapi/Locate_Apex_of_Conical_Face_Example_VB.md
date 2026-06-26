---
title: "Locate Apex of Conical Face Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Locate_Apex_of_Conical_Face_Example_VB.htm"
---

# Locate Apex of Conical Face Example (VBA)

This example shows how to locate the apex of a conical face.

'----------------------------------------------
' Preconditions:
' 1. Open a part or assembly containing a conical face.
'kadov_tag{{<spaces>}}2. Select the conical face.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Creates a 3D sketch with a single point
at the apex of
'kadov_tag{{</spaces>}}the
conical face.
' 2. Examine the Immediate window.
'
' NOTE: Conical face can be truncated.
'------------------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swMathUtilkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathUtility

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFacekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.face2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSurfkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.surface

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vConekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nAxis(2)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vAxiskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAxiskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathVector

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nOrigin(2)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vOriginkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swOriginkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swApexkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swApexPtkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SketchPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMathUtil = swApp.GetMathUtility

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFace = swSelMgr.GetSelectedObject5(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSurf = swFace.GetSurface: Debug.Assert
swSurf.IsCone

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vCone
= swSurf.ConeParams

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nOrigin(0)
= vCone(0):kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nOrigin(1)
= vCone(1):kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nOrigin(2)
= vCone(2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vOrigin
= nOrigin

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swOrigin = swMathUtil.CreatePoint((vOrigin))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nAxis(0)
= vCone(3):kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nAxis(1)
= vCone(4):kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nAxis(2)
= vCone(5)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vAxis
= nAxis

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swAxis = swMathUtil.CreateVector((vAxis))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swAxis = swAxis.Scale(vCone(6)
/ Tan(vCone(7)))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApex = swOrigin.AddVector(swAxis)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}originkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & vCone(0) * 1000# & ", " & vCone(1) * 1000#
& ", " & vCone(2) * 1000# & ") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}axiskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & vCone(3) & ", " & vCone(4) & ",
" & vCone(5) & ")"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}radiuskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vCone(6) * 1000# & " mm"

' 1 radian = 180º/ p = 57.295779513º or approximately 57.3º

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}half
anglekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vCone(7) * 57.3 & " deg"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Apexkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swApex.ArrayData(0)
* 1000# & ", " & swApex.ArrayData(1)
* 1000# & ", " & swApex.ArrayData(2)
* 1000# & ") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.Insert3DSketch2False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.SetAddToDBTrue

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApexPt = swModel.CreatePoint2(swApex.ArrayData(0), swApex.ArrayData(1),
swApex.ArrayData(2))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.SetAddToDBFalse

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.Insert3DSketch2True

End Sub
