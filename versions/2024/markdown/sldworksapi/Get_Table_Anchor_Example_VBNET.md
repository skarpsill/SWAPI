---
title: "Get Table Anchor Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Table_Anchor_Example_VBNET.htm"
---

# Get Table Anchor Example (VB.NET)

This example shows how to get the anchor for a selected bill of materials table.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing document that has a bill of materials.
 ' 2. Expand the Sheet Format node in the FeatureManager design tree and
 '    select the bill of materials anchor feature.
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
     Dim swFeat As Feature
     Dim swSelMgr As SelectionMgr
     Dim swTableAnchor As TableAnchor

     Sub main()

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swFeat = swSelMgr.GetSelectedObject6(1, 0)
         swTableAnchor = swFeat.GetSpecificFeature2

         ' Type of table anchor as defined in swTableAnnotationType_e
         Debug.Print("Type of table anchor = " & swTableAnchor.Type)

     End Sub

     Public swApp As SldWorks

 End  Class
```
