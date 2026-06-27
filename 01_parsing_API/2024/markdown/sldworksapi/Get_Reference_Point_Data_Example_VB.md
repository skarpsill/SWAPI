---
title: "Get Reference Point Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Reference_Point_Data_Example_VB.htm"
---

# Get Reference Point Data Example (VBA)

This example shows how to get reference point data.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a part, assembly, or drawing document that has a
'    reference point.
' 2. Select the reference point.
'
' Postconditions:
' 1. Selects the feature used to create the reference point.
' 2. Press F5 after each feature selection to continue.
' 3. Inspect the Immediate window.
'----------------------------------------------------------------------------
```

```vb
Option Explicit
Sub main()
    Dim swApp                       As SldWorks.SldWorks
     Dim swModel                     As SldWorks.ModelDoc2
     Dim swSelMgr                    As SldWorks.SelectionMgr
     Dim swFeat                      As SldWorks.Feature
     Dim swRefPt                     As SldWorks.RefPoint
     Dim swRefPtData                 As SldWorks.RefPointFeatureData
     Dim swMathPt                    As SldWorks.MathPoint
     Dim vEntArr                     As Variant
     Dim vEnt                        As Variant
     Dim swEnt                       As SldWorks.Entity
     Dim swSkPt                      As SldWorks.SketchPoint
     Dim swSkSeg                     As SldWorks.SketchSegment
     Dim bRet                        As Boolean
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swRefPt = swFeat.GetSpecificFeature2
     Set swRefPtData = swFeat.GetDefinition
     Set swMathPt = swRefPt.GetRefPoint
    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "  " & swFeat.Name
     Debug.Print "    Pt = (" & swMathPt.ArrayData(0) * 1000# & ", " & swMathPt.ArrayData(1) * 1000# & ", " & swMathPt.ArrayData(2) * 1000# & ") mm"
     Debug.Print "    AlongCurveOption   = " & swRefPtData.AlongCurveOption
     Debug.Print "    Distance           = " & swRefPtData.Distance * 1000# & " mm"
     Debug.Print "    Type               = " & swRefPtData.Type
    bRet = swRefPtData.AccessSelections(swModel, Nothing)
     vEntArr = swRefPtData.Selections
    For Each vEnt In vEntArr
         If Not Nothing Is vEnt Then
             If TypeOf vEnt Is SldWorks.Entity Then
                 Set swEnt = vEnt
                 bRet = swEnt.Select4(True, Nothing)
                 Debug.Print "Entity used to create reference point selected."
                 Stop
             ElseIf TypeOf vEnt Is SldWorks.SketchPoint Then
                 Set swSkPt = vEnt
                 bRet = swSkPt.Select4(True, Nothing)
                 Debug.Print "SketchPoint used to create reference point selected."
                 Stop
             ElseIf TypeOf vEnt Is SldWorks.SketchSegment Then
                 Set swSkSeg = vEnt
                 bRet = swSkSeg.Select4(True, Nothing)
                 Debug.Print "SketchSegment used to create reference point selected."
                 Stop
             Else
             End If
         End If
     Next
    swRefPtData.ReleaseSelectionAccess
End Sub
```
