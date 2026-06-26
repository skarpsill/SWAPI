---
title: "Get the Direction of a Bend Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Direction_of_a_Bend_Example_VB.htm"
---

# Get the Direction of a Bend Example (VBA)

This example shows how to get the direction of a bend in sheet metal.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a sheet metal part with a bend feature.
 ' 2. Select the bend feature.
 '
 ' Postconditions: Inspect the Immediate window.
 ' ---------------------------------------------------------------------------
 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim f As SldWorks.Feature
 Dim obe As SldWorks.OneBendFeatureData
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set f = swModel.ISelectionManager.GetSelectedObject6(1, -1)
     Set obe = f.GetDefinition
     If obe.BendDirection = 1 Then
         Debug.Print "Direction of the selected bend is up."
     ElseIf obe.BendDirection = 2 Then
         Debug.Print "Direction of the selected bend is down."
     Else
         Debug.Print "Error getting the direction of the selected bend."
     End If
 End Sub
```
