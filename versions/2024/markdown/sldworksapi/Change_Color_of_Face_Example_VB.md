---
title: "Change Color of Face Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Color_of_Face_Example_VB.htm"
---

# Change Color of Face Example (VBA)

This example shows how to change the color of the selected face to blue.

```
'-----------------------------------------------------
' Preconditions:
' 1. Open a part and select a face.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Changes the color of the selected face to blue.
' 2. Examine the Immediate window.
'------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFace As SldWorks.Face2
    Dim vFaceProp As Variant
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
```

```
    vFaceProp = swFace.MaterialPropertyValues
```

```
    If IsEmpty(vFaceProp) Then
        ' Is empty if face-level colors were not specified,
        ' so get them from underlying model
        vFaceProp = swModel.MaterialPropertyValues
    End If
```

```
    'Current color
    Debug.Print "RGB            = [" & vFaceProp(0) * 255# & ", " & vFaceProp(1) * 255# & ", " & vFaceProp(2) * 255# & "]"
    Debug.Print "Ambient        = " & vFaceProp(3)
    Debug.Print "Diffuse        = " & vFaceProp(4)
    Debug.Print "Specular       = " & vFaceProp(5)
    Debug.Print "Shininess      = " & vFaceProp(6)
    Debug.Print "Transparency   = " & vFaceProp(7)
    Debug.Print "Emission       = " & vFaceProp(8)
```

```
    ' New color
    bRet = swModel.SelectedFaceProperties(RGB(0, 0, 255), vFaceProp(3), vFaceProp(4), vFaceProp(5), vFaceProp(6), vFaceProp(7), vFaceProp(8), False, "")
```

```
    ' Deselect face to see new color
    swModel.ClearSelection2 True
```

```
End Sub
```
