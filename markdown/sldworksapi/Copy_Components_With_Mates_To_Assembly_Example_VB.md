---
title: "Copy Components With Mates to Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_Components_With_Mates_To_Assembly_Example_VB.htm"
---

# Copy Components With Mates to Assembly Example (VBA)

This example shows how to copy components with mates in an assembly.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\driveworksxpress\mobile gantry.SLDASM.
' 2. Inspect Leg<1> and Leg<2> in the assembly.
'
' Postconditions:
' 1. Replaces Leg<1> with a copy of Leg<2>.
' 2. Inspect Leg<2> and leg<3> in the assembly.
'
' NOTE: Because this assembly is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim SwApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim blRepeat(2) As Boolean
    Dim SelectedComps As Variant
    Dim RepeatOptions As Variant
    Dim MateRefs As Variant
    Dim InpValues As Variant
    Dim FlipValues As Variant
    Dim swAssy As AssemblyDoc
    Dim swItem As Object
    Dim arrMateEntities(2) As Object
    Dim arrCompsToCopy(0) As Object
    Dim boolstatus As Boolean
    Dim dValues(2) As Double
```

```
    Set SwApp = Application.SldWorks
    Set swModel = SwApp.ActiveDoc
```

```
    Set swAssy = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
    boolstatus = swModelDocExt.SelectByID2("Leg-1@mobile gantry", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    swModel.EditDelete
```

```
    swModel.ClearSelection2 True
```

```
    boolstatus = swModelDocExt.SelectByID2("Leg-2@mobile gantry", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swItem = swSelMgr.GetSelectedObject6(1, -1)
    Set arrCompsToCopy(0) = swItem
```

```
    swModel.ClearSelection2 True
```

```
    'Repeat all mates except the coincident mate with the "Right End@Universal Beam-1"
    Set arrMateEntities(0) = Nothing
    Set arrMateEntities(1) = Nothing
    boolstatus = swModelDocExt.SelectByID2("Left End@Universal Beam-1@mobile gantry", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set swItem = swSelMgr.GetSelectedObject6(1, -1)
    Set arrMateEntities(2) = swItem
```

```
    swModel.ClearSelection2 True
```

```
    blRepeat(0) = True
    blRepeat(1) = True
    blRepeat(2) = False
```

```
    SelectedComps = arrCompsToCopy
    RepeatOptions = blRepeat
    MateRefs = arrMateEntities
```

```
    dValues(0) = 0#
    dValues(1) = 0#
    dValues(2) = 0#
    InpValues = dValues
```

```
    blRepeat(0) = False
    blRepeat(1) = False
    blRepeat(2) = False
    FlipValues = blRepeat
```

```
    swAssy.CopyWithMates SelectedComps, RepeatOptions, MateRefs, InpValues, FlipValues
```

```
End Sub
```
