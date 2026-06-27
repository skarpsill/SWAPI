---
title: "Make Part Transparent Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Make_Part_Transparent_Example_VB.htm"
---

# Make Part Transparent Example (VBA)

This example shows how to make a part transparent.

```
'----------------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Makes the part transparent.
' 2. Examine the graphics area and Immediate window.
'-----------------------------------------------------
```

```
Option Explicit
```

```
Function GetRValue(MyColour As Long) As Long
    GetRValue = MyColour Mod 256
End Function
```

```
Function GetGValue(MyColour As Long) As Long
    GetGValue = (MyColour \ 256) Mod 256
End Function
```

```
Function GetBValue(MyColour As Long) As Long
    GetBValue = (MyColour \ 65536) Mod 256
End Function
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim nDefaultColor As Long
    Dim vBodyArr As Variant
    Dim vBody As Variant
    Dim swBody As SldWorks.Body2
    Dim swFace As SldWorks.Face2
    Dim nMatProp(9) As Double
    Dim vMatProp As Variant
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
```

```
    nDefaultColor = swModel.GetUserPreferenceIntegerValue(swDocumentColorShading)
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Default Color = RGB(" & GetRValue(nDefaultColor) & ", " & GetGValue(nDefaultColor) & ", " & GetBValue(nDefaultColor) & ")"
```

```
    ' Set to sensible defaults
    ' Gray for default color
    nMatProp(0) = GetRValue(nDefaultColor) / 255#      ' red
    nMatProp(1) = GetRValue(nDefaultColor) / 255#      ' green
    nMatProp(2) = GetRValue(nDefaultColor) / 255#      ' blue
    nMatProp(3) = 1#                    ' Ambient
    nMatProp(4) = 1#                    ' Diffuse
    nMatProp(5) = 1#                    ' Specular
    nMatProp(6) = 0.31                  ' Shininess
    ' Increase transparency
    nMatProp(7) = 0.95                  ' Transparency
    nMatProp(8) = 0#                    ' Emmission
    vMatProp = nMatProp
```

```
    vBodyArr = swPart.GetBodies2(swAllBodies, True)
    For Each vBody In vBodyArr
        Set swBody = vBody
        Set swFace = swBody.GetFirstFace
        While Not swFace Is Nothing
            swFace.MaterialPropertyValues = vMatProp
            Set swFace = swFace.GetNextFace
        Wend
    Next
```

```
    ' Redraw to see new transparency
    swModel.GraphicsRedraw2
```

```
End Sub
```
