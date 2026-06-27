---
title: "Get Reference Axis Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Reference_Axis_Data_Example_VB.htm"
---

# Get Reference Axis Data Example (VBA)

This example shows how to get reference axis data.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part, assembly, or drawing document.
 ' 2. Select a reference axis.
 '
 ' Postconditions: Inspect the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                       As SldWorks.SldWorks
     Dim swModel                     As SldWorks.ModelDoc2
     Dim swSelMgr                    As SldWorks.SelectionMgr
     Dim swFeat                      As SldWorks.Feature
     Dim swRefAxis                   As SldWorks.RefAxis
     Dim swRefAxisData               As SldWorks.RefAxisFeatureData
     Dim swMathAxis                  As Variant
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swRefAxis = swFeat.GetSpecificFeature2
     swMathAxis = swRefAxis.GetRefAxisParams
    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "  " & swFeat.Name
     Debug.Print "    Start point = (" & swMathAxis(0) * 1000# & ", " & swMathAxis(1) * 1000# & ", " & swMathAxis(2) * 1000# & ") mm"
     Debug.Print "    End point = (" & swMathAxis(3) * 1000# & ", " & swMathAxis(4) * 1000# & ", " & swMathAxis(5) * 1000# & ") mm"

    Set swRefAxisData = swFeat.GetDefinition
     Debug.Print "    Type = " & swRefAxisData.Type
End Sub
```
