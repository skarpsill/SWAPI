---
title: "Get Data for Wrap Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Data_for_Wrap_Feature_Example_VB.htm"
---

# Get Data for Wrap Feature Example (VBA)

This example shows how to get data for a wrap feature.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document with a wrap feature.
 ' 2. Select the wrap feature.
 '
 ' Postconditions: Inspect the Immediate window.
 '---------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swFeat                  As SldWorks.Feature
     Dim swWrapSketch            As SldWorks.WrapSketchFeatureData
    Set swApp = CreateObject("SldWorks.Application")
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swWrapSketch = swFeat.GetDefinition
    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "Feature = " & swFeat.Name
     Debug.Print "   Reverse direction?  " & swWrapSketch.ReverseDirection
     Debug.Print "   Type of surface revolve =  " & swWrapSketch.Type
     Debug.Print "   Thickness =  " & swWrapSketch.Thickness
End Sub
```
