---
title: "Get Simple Fillet Feature Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Simple_Fillet_Feature_Data_Example_VBNET.htm"
---

# Get Simple Fillet Feature Data Example (VB.NET)

This example shows how to get simple fillet feature data.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document that contains a simple fillet feature.
 ' 2. Select the simple fillet feature.
 '
 ' Postconditions: Inspect the Immediate window.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swModelDocExt As ModelDocExtension
     Dim swSelMgr As SelectionMgr
     Dim swFeat As Feature
     Dim swFeatData As SimpleFilletFeatureData2
     Dim boolstatus As Boolean

     Sub main()

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension
         swSelMgr = swModel.SelectionManager

         boolstatus = swModelDocExt.SelectByID2("Fillet2", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)

         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swFeatData = swFeat.GetDefinition

         Debug.Print("Edge count: " & swFeatData.GetEdgeCount)

     End Sub

     Public swApp As SldWorks

 End  Class
```
