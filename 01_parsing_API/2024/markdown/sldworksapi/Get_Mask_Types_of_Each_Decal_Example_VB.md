---
title: "Get Mask Types of Each Decal Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mask_Types_of_Each_Decal_Example_VB.htm"
---

# Get Mask Types of Each Decal Example (VBA)

This example shows how to get a decal and its mask type.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a model that has at least one decal applied
'    to it in the Default configuration.
' 2. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'-----------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDecal As SldWorks.Decal
Dim lNbrDecals As Long, i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    lNbrDecals = swModelDocExt.GetDecalsCount
    Debug.Print "Number of decals: " & lNbrDecals
    For i = 1 To lNbrDecals
        ' Get the decal with the corresponding decal ID in the
        ' the Default configuration
        Set swDecal = swModelDocExt.GetDecal(i, "Default")
        Debug.Print "Mask type: " & swDecal.MaskType
    Next i
```

```
End Sub
```
