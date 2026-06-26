---
title: "Get Reference Axis Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Reference_Axis_Data_Example_VBNET.htm"
---

# Get Reference Axis Data Example (VB.NET)

This example shows how to get reference axis data.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part, assembly, or drawing document.
 ' 2. Select a reference axis.
 '
 ' Postconditions: Inspect the Immediate window.
 '----------------------------------------------------------------------------
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
         Dim swRefAxis As RefAxis
         Dim swRefAxisData As RefAxisFeatureData
         Dim swMathAxis As Object

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swRefAxis = swFeat.GetSpecificFeature2
         swMathAxis = swRefAxis.GetRefAxisParams

         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("  " & swFeat.Name)
         Debug.Print("    Start point = (" & swMathAxis(0) * 1000.0# & ", " & swMathAxis(1) * 1000.0# & ", " & swMathAxis(2) * 1000.0# & ") mm")
         Debug.Print("    End point = (" & swMathAxis(3) * 1000.0# & ", " & swMathAxis(4) * 1000.0# & ", " & swMathAxis(5) * 1000.0# & ") mm")

         swRefAxisData = swFeat.GetDefinition
         Debug.Print("    Type = " & swRefAxisData.Type)

     End Sub

     Public swApp As SldWorks

 End  Class
```
