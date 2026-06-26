---
title: "Get the Direction of a Bend Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Direction_of_a_Bend_Example_VBNET.htm"
---

# Get the Direction of a Bend Example (VB.NET)

This example shows how to get the direction of a bend in sheet metal.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a sheet metal part with a bend feature.
 ' 2. Select the bend feature.
 '
 ' Postconditions: Inspect the Immediate window.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim f As Feature
     Dim obe As OneBendFeatureData

     Sub main()

         swModel = swApp.ActiveDoc
         f = swModel.ISelectionManager.GetSelectedObject6(1, -1)
         obe = f.GetDefinition
         If obe.BendDirection = 1 Then
             Debug.Print("Direction of the selected bend is up.")
         ElseIf obe.BendDirection = 2 Then
             Debug.Print("Direction of the selected bend is down.")
         Else
             Debug.Print("Error getting the direction of the selected bend.")
         End If
     End Sub

     Public swApp As SldWorks

 End  Class
```
