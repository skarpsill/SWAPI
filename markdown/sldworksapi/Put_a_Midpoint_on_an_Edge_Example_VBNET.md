---
title: "Select the Midpoint of an Edge Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Put_a_Midpoint_on_an_Edge_Example_VBNET.htm"
---

# Select the Midpoint of an Edge Example (VB.NET)

This example shows how to select the midpoint of an edge.

```vb
 '-------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part document.
 ' 2. Select an edge.
 ' 3. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Puts a midpoint on the selected edge.
 ' 2. Place the cursor on the selected edge to see the
 '    midpoint.
 ' 3. Examine the Immediate window.
 '------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Const swSelEDGES As Long = 1
     Const swSelREFERENCECURVES As Long = 26
     Const swSelPOINTREFS As Long = 41
     Const swSelREFEDGES As Long = 51

     Sub main()

         Dim swModel As ModelDoc2
         Dim swPart As PartDoc
         Dim swSelMgr As SelectionMgr
         Dim nSelType As Long

         swModel = swApp.ActiveDoc
         swPart = swModel
         swSelMgr = swModel.SelectionManager

         nSelType = swSelMgr.GetSelectedObjectType3(1, -1)
         Debug.Print("SelType (before) = " + Str(nSelType))

         swModel.SelectMidpoint()

         nSelType = swSelMgr.GetSelectedObjectType3(1, -1)
         Debug.Print("SelType (after ) = " + Str(nSelType))

     End Sub

     Public swApp As SldWorks

 End  Class
```
