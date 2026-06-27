---
title: "Change Pitch of Helix Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Pitch_of_Helix_Example_VB.htm"
---

# Change Pitch of Helix Example (VBA)

This example shows how to change the pitch of a helix.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open a part that contains a helix feature.
' 2. Select the helix feature.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Modifies the pitch of selected helix feature.
' 2. Gets the name of helix feature, original pitch, and
'    modified pitch values.
' 3. Examine the Immediate window and graphics area.
'--------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swHelix As SldWorks.HelixFeatureData
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set swHelix = swFeat.GetDefinition
```

```
    Debug.Print "Feature = " & swFeat.Name
    Debug.Print "  Original pitch = " & swHelix.Pitch * 1000# & " mm"
```

```
    ' Change the pitch value
    swHelix.Pitch = 1.25 * swHelix.Pitch
    Debug.Print "  Modified pitch = " & swHelix.Pitch * 1000# & " mm"
```

```
    ' Apply the change
    bRet = swFeat.ModifyDefinition(swHelix, swModel, Nothing): Debug.Assert bRet
```

```
End Sub
```
