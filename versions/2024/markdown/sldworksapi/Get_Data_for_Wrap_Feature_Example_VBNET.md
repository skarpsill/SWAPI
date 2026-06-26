---
title: "Get Data for Wrap Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Data_for_Wrap_Feature_Example_VBNET.htm"
---

# Get Data for Wrap Feature Example (VB.NET)

This example shows how to get data for a wrap feature.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document with a wrap feature.
 ' 2. Select the wrap feature.
 '
 ' Postconditions: Inspect the Immediate window.
 '---------------------------------------------------------------------------
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
         Dim swWrapSketch As WrapSketchFeatureData

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swWrapSketch = swFeat.GetDefinition

         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("Feature = " & swFeat.Name)
         Debug.Print("   Reverse direction?  " & swWrapSketch.ReverseDirection)
         Debug.Print("   Type of surface revolve =  " & swWrapSketch.Type)
         Debug.Print("   Thickness =  " & swWrapSketch.Thickness)

     End Sub

     Public swApp As SldWorks

 End  Class
```
