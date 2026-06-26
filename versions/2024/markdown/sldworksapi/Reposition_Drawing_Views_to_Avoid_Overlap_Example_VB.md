---
title: "Reposition Drawing Views to Avoid Overlap Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Reposition_Drawing_Views_to_Avoid_Overlap_Example_VB.htm"
---

# Reposition Drawing Views to Avoid Overlap Example (VBA)

This example shows how to reposition drawing views to avoid overlap.

```
'-------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\introsw\bolt-assembly.slddrw.
' 2. Drag Drawing View3 so that it overlaps Drawing View2.
'
' Postconditions:
' 1. Repositions Drawing View2 and Drawing View2 so that they do
'    not overlap.
' 2. Examine the drawing and the Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'-----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swView  As SldWorks.View
    Dim vOutline() As Variant
    Dim vPos() As Variant
    Dim nNumView As Long
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
```

```
    nNumView = 0
```

```
    Set swView = swDraw.GetFirstView
    Do While Not swView Is Nothing
        ReDim Preserve vOutline(nNumView)
        ReDim Preserve vPos(nNumView)
        vOutline(nNumView) = swView.GetOutline
        vPos(nNumView) = swView.Position
        Debug.Print "View = " + swView.GetName2
        Debug.Print "  Pos = (" & vPos(nNumView)(0) * 1000# & ", " & vPos(nNumView)(1) * 1000# & ") mm"
        Debug.Print "  Min = (" & vOutline(nNumView)(0) * 1000# & ", " & vOutline(nNumView)(1) * 1000# & ") mm"
        Debug.Print "  Max = (" & vOutline(nNumView)(2) * 1000# & ", " & vOutline(nNumView)(3) * 1000# & ") mm"
        nNumView = nNumView + 1
        Set swView = swView.GetNextView
    Loop
```

```
    ' Sheet
    Set swView = swDraw.GetFirstView
```

```
    ' View 1
    Set swView = swView.GetNextView
```

```
    'View 2 - vertically aligned to view 1
    Set swView = swView.GetNextView
```

```
    vPos(2)(1) = vPos(1)(1) + (vOutline(1)(3) - vPos(1)(1)) + (vPos(2)(1) - vOutline(2)(1))
    swView.Position = vPos(2)
```

```
    swModel.GraphicsRedraw2
```

```
    'View 3 - horizontally aligned to view 2
    Set swView = swView.GetNextView
```

```
    vPos(3)(0) = vPos(1)(0) + (vOutline(1)(1) - vPos(0)(0)) + (vPos(3)(0) - vOutline(3)(0))
    swView.Position = vPos(3)
```

```
    swModel.GraphicsRedraw2
```

```
End Sub
```
