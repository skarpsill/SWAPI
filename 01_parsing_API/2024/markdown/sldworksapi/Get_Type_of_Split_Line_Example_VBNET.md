---
title: "Get Type of Split Line Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Type_of_Split_Line_Example_VBNET.htm"
---

# Get Type of Split Line Example (VB.NET)

This example shows how to get the type of split line.

```vb
 '----------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part document with a split line feature.
 ' 2. Select the split line feature.
 ' 3. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Gets the type of split line.
 ' 2. Examine the Immediate window.
 '-----------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swSelMgr As SelectionMgr
     Dim swFeat As Feature
     Dim swSplitLineFeat As SplitLineFeatureData
     Dim splittype As Integer

     Sub main()

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swSplitLineFeat = swFeat.GetDefinition

         splittype = swSplitLineFeat.GetType
         Debug.Print("Split line type (swSplitLineFeatureType_e): " & splittype)

     End Sub

     Public swApp As SldWorks

 End  Class
```
