---
title: "Mirror View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Mirror_View_Example_VB.htm"
---

# Mirror View Example (VBA)

This example shows how to mirror a view.

```
'-------------------------------------------------------------------
' Preconditions:
' 1. Verify that the drawing to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the drawing.
' 2. Mirrors the drawing view.
' 3. Examine the drawing and Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'-------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swDrawing As SldWorks.DrawingDoc
Dim swView As SldWorks.View
Dim fileName As String
Dim errors As Long
Dim warnings As Long
Dim mirrored As Boolean
Dim orientation As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\clamp1.slddrw"
    Set swDrawing = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swView = swDrawing.GetFirstView 'This is the drawing template
    Set swView = swView.GetNextView 'This is the first drawing view in the drawing
    swView.SetMirrorViewOrientation True, swMirrorViewPositions_e.swMirrorViewPosition_Horizontal
    swView.GetMirrorViewOrientation mirrored, orientation
    Debug.Print "Mirrored? " & mirrored
    Debug.Print "Orientation (0 = horizontal)? " & orientation
```

```
End Sub
```
