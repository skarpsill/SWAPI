---
title: "Change Sketch Plane Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Sketch_Plane_Example_VB.htm"
---

# Change Sketch Plane Example (VBA)

This example shows how to change which plane a sketch is on.

```
'-------------------------------------------------
' Preconditions: Open a part document that
' contains:
' * Sketch1 sketched on the Front Plane.
' * Plane named Plane1.
'
' Postconditions:
' 1. Moves Sketch1 to Plane1.
' 2. Examine the graphics area.
'-------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim vConfigNames As Variant
Dim boolstatus As Boolean
```

```
Sub main()
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
```

```
    boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    If (1) Then
        boolstatus = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
    End If
    If (0) Then
        boolstatus = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
    End If
```

```
    vConfigNames = swModel.GetConfigurationNames()
    boolstatus = swModelDocExt.ChangeSketchPlane(swThisConfiguration, vConfigNames(0))
```

```
    boolstatus = swModel.EditRebuild3()
End Sub
```
