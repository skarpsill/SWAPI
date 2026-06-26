---
title: "Create Coordinate System Feature (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Coordinate_System_Feature_Example_VB.htm"
---

# Create Coordinate System Feature (VBA)

This example creates a coordinate system feature. The example then accesses
the feature and edits it.

```vb
'-----------------------------------------
' Precondition: Model document is open.
'
' Postconditions: Coordinate system feature is created.
'-----------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As SldWorks.Feature
Dim swFeatMgr As SldWorks.FeatureManager
Dim cSysData As SldWorks.CoordinateSystemFeatureData
Dim component As SldWorks.Component2
Dim boolstatus As Boolean
Dim vo As Variant
Dim vx As Variant
Dim vy As Variant
Dim vz As Variant
Dim evo As Variant
Dim evx As Variant
Dim evy As Variant
Dim evz As Variant
Dim so(0) As Object
Dim sx(1) As Object
Dim sy(1) As Object
Dim sz(1) As Object
Dim eso(0) As Object
Dim esx(1) As Object
Dim esy(1) As Object
Dim esz(1) As Object
Dim xEnt kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}As Object

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
Set swModelDocExt = swModel.Extension
Set swFeatMgr = swModel.FeatureManager
boolstatus = swModelDocExt.SelectByID2("", "VERTEX", 0, 0.00635, 0, False, 0, Nothing, 0)
boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.0308159564126, 0.006349999999827, 0.01220751949762, True, 0, Nothing, 0)
boolstatus = swModelDocExt.SelectByID2("", "VERTEX", 0.0762, 0.00635, 0.01905, True, 0, Nothing, 0)
boolstatus = swModelDocExt.SelectByID2("", "VERTEX", 0.0762, 0.00635, 0, True, 0, Nothing, 0)

' Assume a vertex was selected for the origin
Set so(0) = swSelMgr.GetSelectedObject6(1, -1)
' Assume one entity (point, line/edge, plane/face) was selected for the x axis
Set sx(0) = swSelMgr.GetSelectedObject6(2, -1)
' Assume two entities (point, line/edge, plane/face) were selected for the y axis
Set sy(0) = swSelMgr.GetSelectedObject6(3, -1)
Set sy(1) = swSelMgr.GetSelectedObject6(4, -1)
' Try getting additional selected entities for the z axis
Set sz(0) = swSelMgr.GetSelectedObject6(5, -1)
Set sz(1) = swSelMgr.GetSelectedObject6(6, -1)

vo = so
vx = sx
vy = sy
vz = sz

swModel.ClearSelection2 True

' Create coordinate system
Set swFeat = swFeatMgr.CreateCoordinateSystem(so(0), (vx), (vy), (vz))
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
If swFeat Is Nothing Then
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Did not create a coordinate system feature!"
Else
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set cSysData = swFeat.GetDefinition
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = cSysData.AccessSelections(swModel, component)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get and output the transform
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swXform kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}As SldWorks.MathTransform
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swXform = cSysData.Transform
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Origin = (" & -1# * swXform.ArrayData(9) * 1000# & ", " & -1# * swXform.ArrayData(10) * 1000# & ", " & -1# * swXform.ArrayData(11) * 1000# & ") mm"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Rot1 kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}= (" & swXform.ArrayData(0) & ", " & swXform.ArrayData(1) & ", " & swXform.ArrayData(2) & ")"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Rot2 kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}= (" & swXform.ArrayData(3) & ", " & swXform.ArrayData(4) & ", " & swXform.ArrayData(5) & ")"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Rot3 kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}= (" & swXform.ArrayData(6) & ", " & swXform.ArrayData(7) & ", " & swXform.ArrayData(8) & ")"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Trans kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}= (" & swXform.ArrayData(9) * 1000# & ", " & swXform.ArrayData(10) * 1000# & ", " & swXform.ArrayData(11) * 1000# & ") mm"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Scale kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}= " & swXform.ArrayData(12)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "XFlipped? " & cSysData.XFlipped
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}cSysData.XFlipped = True
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Select new entities for editing the coordinate system feature
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "VERTEX", 0, 0.00635, 0.01905, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.03505266269053, -6.420391980555E-05, 0.01914079805448, True, 2, Nothing, 0) ' Assume a vertex was selected for the origin
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.0308159564126, 0.006349999999827, 0.01220751949762, True, 3, Nothing, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Edit the origin
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set eso(0) = swSelMgr.GetSelectedObject6(1, -1)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Edit the y axis
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Assume two entities (point, line/edge, plane/face) were selected for the y axis
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set esy(0) = swSelMgr.GetSelectedObject6(2, -1)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set esz(0) = swSelMgr.GetSelectedObject6(3, -1)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}evo = eso
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}evy = esy
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}evz = esz
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swModel.ClearSelection2 True
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}cSysData.OriginEntity = eso(0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}cSysData.YAxisEntities = evy
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Try appending z-axis entities to see if they replace x-axis entity
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' If this happens, then y and z are the active axes,
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' and x-axis entity is inaccessible
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}cSysData.ZAxisEntities = evz
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get the origin entity
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim entType As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Stop
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim geo As SldWorks.Entity
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set geo = cSysData.OriginEntity
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}entType = geo.GetType
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get the x-axis entities; there shouldn't be any, because x is not active
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim gv As Variant
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vCount As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}vCount = cSysData.GetXAxisEntitiesCount
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}gv = cSysData.XAxisEntities
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim i As Long
kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get the y-axis entities
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}vCount = cSysData.GetYAxisEntitiesCount
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}gv = cSysData.YAxisEntities
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}For i = 0 To UBound(gv)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set xEnt = gv(i)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}entType = xEnt.GetType
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Next i
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swFeat.ModifyDefinition(cSysData, swModel, Nothing)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}cSysData.ReleaseSelectionAccess
End If

swModel.EditRebuild3

End Sub
```
