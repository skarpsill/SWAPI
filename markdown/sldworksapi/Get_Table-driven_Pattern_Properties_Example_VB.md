---
title: "Get Table-driven Pattern Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Table-driven_Pattern_Properties_Example_VB.htm"
---

# Get Table-driven Pattern Properties Example (VBA)

This example shows how to get the properties of a table-driven pattern.

```
'------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\tablepattern.sldprt.
' 2. Select TPattern1.
' 3. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save
' changes.
'------------------------------------------------------------
```

```
Option Explicit
```

```
' TablePatternFeatureData::GetReferencePointType
'        0 = closed curve
'        1 = sketch point
'        2 = vertex
Sub ProcessCoordSys(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swCoordSys As SldWorks.Feature)
```

```
    Dim swDocExt As SldWorks.ModelDocExtension
    Dim swXform  As SldWorks.MathTransform
```

```
    Set swDocExt = swModel.Extension
    Set swXform = swDocExt.GetCoordinateSystemTransformByName(swCoordSys.Name)
```

```
    Debug.Print "  " & swCoordSys.Name
    Debug.Print "    Origin = (" & -1# * swXform.ArrayData(9) * 1000# & ", " & -1# * swXform.ArrayData(10) * 1000# & ", " & -1# * swXform.ArrayData(11) * 1000# & ") mm"
    Debug.Print "    Rot1   = (" & swXform.ArrayData(0) & ", " & swXform.ArrayData(1) & ", " & swXform.ArrayData(2) & ")"
    Debug.Print "    Rot2   = (" & swXform.ArrayData(3) & ", " & swXform.ArrayData(4) & ", " & swXform.ArrayData(5) & ")"
    Debug.Print "    Rot3   = (" & swXform.ArrayData(6) & ", " & swXform.ArrayData(7) & ", " & swXform.ArrayData(8) & ")"
    Debug.Print "    Trans  = (" & swXform.ArrayData(9) * 1000# & ", " & swXform.ArrayData(10) * 1000# & ", " & swXform.ArrayData(11) * 1000# & ") mm"
    Debug.Print "    Scale  = " & swXform.ArrayData(12)
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swTableFeatData  As SldWorks.TablePatternFeatureData
    Dim swRefPt As SldWorks.Vertex
    Dim swCoordSys As SldWorks.Feature 'Object
    Dim vBasePt  As Variant
    Dim vFace As Variant
    Dim vFeat As Variant
    Dim vPt As Variant
    Dim nPtType As Long
    Dim vRefPtParam As Variant
    Dim bRet As Boolean
    Dim i As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Set swTableFeatData = swFeat.GetDefinition
```

```
    ' Roll back to get the reference point
    bRet = swTableFeatData.AccessSelections(swModel, Nothing)
    Set swRefPt = swTableFeatData.ReferencePoint
    Set swCoordSys = swTableFeatData.CoordinateSystem
    vBasePt = swTableFeatData.GetBasePoint
    vFace = swTableFeatData.PatternFaceArray
    vFeat = swTableFeatData.PatternFeatureArray
    vPt = swTableFeatData.PointArray
```

```
    Debug.Print swFeat.Name
    Debug.Print "  Coord sys            = " & swCoordSys.Name
```

```
    ProcessCoordSys swApp, swModel, swCoordSys
```

```
    Debug.Print "  FaceCount            = " & swTableFeatData.GetPatternFaceCount
    Debug.Print "  FeatureCount         = " & swTableFeatData.GetPatternFeatureCount
    Debug.Print "  PointCount           = " & swTableFeatData.GetPointCount
    Debug.Print "  ReferencePointType   = " & swTableFeatData.GetReferencePointType
    Debug.Print "  BasePt               = (" & vBasePt(0) * 1000# & ", " & vBasePt(1) * 1000# & ", " & vBasePt(2) * 1000# & ") mm"
    Debug.Print "  GeometryPattern      = " & swTableFeatData.GeometryPattern
    Debug.Print "  UseCentroid          = " & swTableFeatData.UseCentroid
    If Not swRefPt Is Nothing Then
        ' Is null if centroid used
        vRefPtParam = swRefPt.GetPoint
        Debug.Print "  RefPt                = (" & vRefPtParam(0) * 1000# & ", " & vRefPtParam(1) * 1000# & ", " & vRefPtParam(2) * 1000# & ") mm"
    End If
    ' Roll forward
    swTableFeatData.ReleaseSelectionAccess
```

```
End Sub
```
