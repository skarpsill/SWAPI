---
title: "Create Plane thru 3 Points In-context Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Plane_Thru_3_Points_In-context_Example_VB.htm"
---

# Create Plane thru 3 Points In-context Example (VBA)

This example shows how to create a plane through 3 points in-context.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a fully resolved assembly.
' 2. Select a component.
' 3. Expand the selected component in the FeatureManager
'    design tree.
'
' Postconditions:
' 1. Creates a plane, passing through three points,
'    in the selected component.
' 2. Examine the selected component in the FeatureManager
'    design tree to verify that a 3D sketch and plane
'    were created.
'--------------------------------------------------
Option Explicit
```

```
'  Possible status values for AssemblyDoc::EditPart2
Public Enum swEditPartCommandStatus_e
    swEditPartFailure = -1
    swEditPartAsmMustBeSaved = -2
    swEditPartCompMustBeSelected = -3
    swEditPartCompMustBeResolved = -4
    swEditPartCompMustHaveWriteAccess = -5
    swEditPartSuccessful = 0
    swEditPartCompNotPositioned = &H1
End Enum
```

```
Sub main()
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swEditModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelData As SldWorks.SelectData
    Dim swPart As SldWorks.PartDoc
    Dim swSketchPt1 As SldWorks.SketchPoint
    Dim swSketchPt2 As SldWorks.SketchPoint
    Dim swSketchPt3 As SldWorks.SketchPoint
    Dim swPlane As SldWorks.RefPlane
    Dim nRetVal As Long
    Dim nInfo As Long
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    Set swAssy = swModel
```

```
    ' Start in-context edit
    nRetVal = swAssy.EditPart2(True, False, nInfo)
    Debug.Assert swEditPartSuccessful = nRetVal
```

```
    Set swEditModel = swModel
```

```
    ' Turn off snapping
    swEditModel.SetAddToDB True
```

```
    ' Insert part/component 3D sketch in-context
    swEditModel.Insert3DSketch2 True
```

```
    ' Create points in part
    Set swSketchPt1 = swEditModel.CreatePoint2(0#, 0.02123307340457, 0.005485856156458)
    Set swSketchPt2 = swEditModel.CreatePoint2(0.04415646169588, 0.01166034702997, -0.00770979679615)
    Set swSketchPt3 = swEditModel.CreatePoint2(0#, -0.006247647329005, 0.007641244473859)
```

```
    ' Exit sketch but in assembly
    ' This gets you to editing part/component in-context
    swModel.Insert3DSketch2 True
```

```
    ' Restore snapping
    swEditModel.SetAddToDB False
```

```
    swModel.ClearSelection2 True

    bRet = swSketchPt1.Select4(True, swSelData): Debug.Assert bRet
    bRet = swSketchPt2.Select4(True, swSelData): Debug.Assert bRet
    bRet = swSketchPt3.Select4(True, swSelData): Debug.Assert bRet
```

```
    ' Create plane in part/component
    Set swPlane = swModel.CreatePlaneThru3Points3(True)
    Debug.Assert Not swPlane Is Nothing
```

```
    ' Go back to assembly
    ' End in-context edit
    swAssy.EditAssembly
```

```
End Sub
```
