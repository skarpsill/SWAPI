---
title: "Create Section View at Specified Location Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Section_View_at_Specified_Location_Example_VB.htm"
---

# Create Section View at Specified Location Example (VBA)

This example shows how to create a section view at a specified location.

```
'-------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
'
' Postconditions:
' 1. Creates a section view created at the specified location.
' 2. Examine the graphics area.
'--------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swDrawing As SldWorks.DrawingDoc
Dim vChildComponents As Variant
Dim swFirstDrawingView As SldWorks.View
Dim swDrawingView As SldWorks.View
Dim swDrRootComponent As SldWorks.DrawingComponent
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swDrawing = swApp.ActiveDoc
    If swDrawing Is Nothing Then
        MsgBox "There is no active document"
        Exit Sub
    End If
```

```
    ' Always returns the drawing sheet first
    Set swFirstDrawingView = swDrawing.GetFirstView
```

```
    ' Get first drawing view
    Set swDrawingView = swFirstDrawingView.GetNextView
```

```
    ' Get  root drawing component
    Set swDrRootComponent = swDrawingView.RootDrawingComponent
    Dim iChild As Long
    If swDrRootComponent.GetChildrenCount > 0 Then
        vChildComponents = swDrRootComponent.GetChildren
        For iChild = 0 To UBound(vChildComponents)
        Next iChild
    End If
```

```
    ' Select the drawing view and create line for the section view
    Dim boolstatus As Boolean
    boolstatus = swDrawing.Extension.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
    swDrawing.ClearSelection2 True
    swDrawing.CreateLine2 0.091354, 0.284441, 0#, 0.253455, 0.140062, 0#
```

```
    ' Set arguments for call to create section view
    Dim x As Double, y As Double, z As Double
    Dim notAligned As Boolean, isOffsetSection As Boolean, chgdirection As Boolean, scwithmodel As Boolean, partial As Boolean, dispsurfcut As Boolean
    Dim label As String
    Dim sectionView As SldWorks.View
    x = 0.65
    y = 0.08908737704918
    z = 0
    notAligned = False
    isOffsetSection = False
    chgdirection = False
    scwithmodel = False
    partial = False
    dispsurfcut = False
    label = "A"
```

```
    ' Create section view
    Set sectionView = swDrawing.CreateSectionViewAt3(x, y, z, notAligned, isOffsetSection, label, chgdirection, scwithmodel, partial, dispsurfcut, (vChildComponents))
```

```
End Sub
```
