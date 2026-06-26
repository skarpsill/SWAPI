---
title: "Get Reference Point Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Reference_Point_Data_Example_VBNET.htm"
---

# Get Reference Point Data Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swFeat As Feature
         Dim swRefPt As RefPoint
         Dim swRefPtData As RefPointFeatureData
         Dim swMathPt As MathPoint
         Dim vEntArr As Object
         Dim vEnt As Object
         Dim swEnt As Entity
         Dim swSkPt As SketchPoint
         Dim swSkSeg As SketchSegment
         Dim bRet As Boolean

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swRefPt = swFeat.GetSpecificFeature2
         swRefPtData = swFeat.GetDefinition
         swMathPt = swRefPt.GetRefPoint

         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("  " & swFeat.Name)
         Debug.Print("    Pt = (" & swMathPt.ArrayData(0) * 1000.0#   ", " & swMathPt.ArrayData(1) * 1000.0#   ", " & swMathPt.ArrayData(2) * 1000.0# & ") mm")
         Debug.Print("    AlongCurveOption   = " & swRefPtData.AlongCurveOption)
         Debug.Print("    Distance           = " & swRefPtData.Distance * 1000.0# & " mm")
         Debug.Print("    Type               = " & swRefPtData.Type)

         bRet = swRefPtData.AccessSelections(swModel,  Nothing)
         vEntArr = swRefPtData.Selections

         For Each vEnt In vEntArr
             If Not  Nothing  Is vEnt  Then
                 If TypeOf vEnt Is Entity Then
                     swEnt = vEnt
                     bRet = swEnt.Select4(True, Nothing)
                     Debug.Print("Entity used to create reference point selected.")
                     Stop
                 ElseIf TypeOf vEnt Is SketchPoint Then
                     swSkPt = vEnt
                     bRet = swSkPt.Select4(True, Nothing)
                     Debug.Print("SketchPoint used to create reference point selected.")
                     Stop
                 ElseIf TypeOf vEnt Is SketchSegment Then
                     swSkSeg = vEnt
                     bRet = swSkSeg.Select4(True, Nothing)
                     Debug.Print("SketchSegment used to create reference point selected.")
                     Stop
                 Else
                 End If
             End If
         Next

         swRefPtData.ReleaseSelectionAccess()

     End Sub

     Public swApp As SldWorks

 End  Class
```
