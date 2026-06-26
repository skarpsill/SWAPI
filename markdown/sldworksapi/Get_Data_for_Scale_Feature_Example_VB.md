---
title: "Get Data for Scale Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Data_for_Scale_Feature_Example_VB.htm"
---

# Get Data for Scale Feature Example (VBA)

This example shows how to get the data for the selected scale feature.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document with a scale feature.
 ' 2. Select the scale feature.
 '
 ' Postconditions: Inspect the Immediate window.
 '---------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swFeat                  As SldWorks.Feature
     Dim swScale                 As SldWorks.ScaleFeatureData
     Dim swCoordSys              As SldWorks.Feature
     Dim nX_Scale                As Double
     Dim nY_Scale                As Double
     Dim nZ_scale                As Double
     Dim bIsUniform              As Boolean
    Set swApp = CreateObject("SldWorks.Application")
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swScale = swFeat.GetDefinition
     Set swCoordSys = swScale.CoordinateSystem
    swScale.GetScale nX_Scale, nY_Scale, nZ_scale, bIsUniform
    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "Feature = " & swFeat.Name
     Debug.Print "   X scaling factor = " & nX_Scale
     Debug.Print "   Y scaling factor = " & nY_Scale
     Debug.Print "   Z scaling factor = " & nZ_scale
     Debug.Print "   Is uniform = " & bIsUniform
     Debug.Print "   Scaling type as defined in swScaleType_e = " & swScale.Type
     Debug.Print "   Bodies count = " & swScale.GetBodiesCount
     Debug.Print "   Is uniform = " & swScale.IsUniform
     Debug.Print "   Uniform scaling factor = " & swScale.ScaleUniform
     Debug.Print "   X scaling factor = " & swScale.ScaleX
     Debug.Print "   Y scaling factor = " & swScale.ScaleY
     Debug.Print "   Z scaling factor = " & swScale.ScaleZ
    If Not swCoordSys Is Nothing Then
         Debug.Print "   CoorSys = " & swCoordSys.Name
     End If
End Sub
```
