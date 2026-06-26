---
title: "Modify Plane by Editing Its Definition Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Plane_by_Editing_Its_Definition_Example_VB.htm"
---

# Modify Plane by Editing Its Definition Example (VBA)

This example shows how to modify a plane by editing its definition.

```
'----------------------------------------------
' Preconditions:
' 1. Open a model document with an offset plane
'    named Plane1.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Changes the the offset distance of Plane1 to
'    100mm.
' 2. Examine the Immediate window.
'-----------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swPart As SldWorks.PartDoc
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swRefPlane As SldWorks.RefPlaneFeatureData
Dim Feature As SldWorks.Feature
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
```

```
    boolstatus = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
    Set Feature = swSelMgr.GetSelectedObject5(1)
    Set swRefPlane = Feature.GetDefinition
    swRefPlane.AccessSelections swPart, Nothing
    Debug.Print "Original offset distance: " & swRefPlane.Distance
    swRefPlane.Distance = 0.1
    Debug.Print "Modified offset distance: " & swRefPlane.Distance
    Feature.ModifyDefinition swRefPlane, swPart, Nothing
```

```
End Sub
```
