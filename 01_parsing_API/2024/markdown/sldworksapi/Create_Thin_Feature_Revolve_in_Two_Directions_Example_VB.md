---
title: "Create Thin Feature Revolve in Two Directions Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Thin_Feature_Revolve_in_Two_Directions_Example_VB.htm"
---

# Create Thin Feature Revolve in Two Directions Example (VBA)

This example shows how to create a thin feature revolve in two directions.

```
'----------------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\api\Multiple Planar_Faces2.sldprt.
'
' Postconditions:
' 1. Creates a thin feature revolve in two directions.
' 2. Examine the graphics area and FeatureManager design tree.
'
' NOTE: Because the model is used elsewhere, do not save changes
'---------------------------------------------------------------------------

Option Explicit
```

```vb
Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim Part As SldWorks.ModelDoc2
     Dim boolstatus As Boolean

    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
    boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Axis1", "AXIS", -0.03249248386774, -0.008890295497245, -0.005457395402805, True, 16, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "FACE", -0.03948753408952, 0.1016773485926, -0.08343298757264, True, 32, Nothing, 0)

    Dim myFeature As SldWorks.Feature
     Set myFeature = Part.FeatureManager.FeatureRevolve2(False, True, True, False, False, True, 4, 5, 6.28318530718, 0, False, True, 0.01, 0.01, 0, 0.002, 0.01, True, True, True)
End Sub
```
