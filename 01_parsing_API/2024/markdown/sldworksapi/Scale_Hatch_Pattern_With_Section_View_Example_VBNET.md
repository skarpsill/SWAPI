---
title: "Scale Hatch Pattern to Section View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Scale_Hatch_Pattern_With_Section_View_Example_VBNET.htm"
---

# Scale Hatch Pattern to Section View Example (VB.NET)

This example shows how to scale a hatch pattern to a section view.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\introsw\bolt-assembly.slddrw.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Scales the hatch pattern to the section view.
' 2. Examine the Immediate window.
'
' NOTE: Because this drawing is used elsewhere, do not save changes.
'--------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swDrawing As DrawingDoc
    Dim swView As View
    Dim swSectionView As DrSection

    Sub main()

        swModel = swApp.ActiveDoc
        swDrawing = swModel
        swDrawing.ActivateView("Drawing View5")
        swView = swDrawing.ActiveDrawingView
        swSectionView = swView.GetSection
        swSectionView.ScaleHatchPattern = True
        Debug.Print("  Scale hatch pattern to section view? " & swSectionView.ScaleHatchPattern)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
