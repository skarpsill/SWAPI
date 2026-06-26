---
title: "Create Relative Drawing View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Relative_Drawing_View_Example_VBNET.htm"
---

# Create Relative Drawing View Example (VB.NET)

This example shows how to create a relative drawing view.

```
' ******************************************************************************
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\maingrip.sldprt.
' 2. Select File > Make Drawing from Part.
' 3. Run the macro.
'
' Postconditions:
' 1. Iterates through the drawing views
'    in the View Palette and drops
'    *Current drawing view in the drawing.
' 2. Activates the part.
' 3. Selects two faces for the relative drawing view.
' 4. Activates the drawing.
' 5. Creates and inserts a relative drawing
'    view using the selected faces.
'
' NOTE: Because the part document is used elsewhere, do not
' save any changes when closing it.
' ******************************************************************************

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swDrawing As DrawingDoc
    Dim swView As View
    Dim swModelDocExt As ModelDocExtension
    Dim fileName As String
    Dim status As Boolean
    Dim errors As Integer
    Dim warnings As Integer
    Dim numViews As Integer
    Dim viewNames As Object
    Dim viewName As Object
    Dim viewPaletteName As String

    Sub main()

        swDrawing = swApp.ActiveDoc

        ' Get number of views on View Palette
        numViews = 0
        viewNames = swDrawing.GetDrawingPaletteViewNames

        ' Iterate through views on View Palette
        ' When view name equals *Current, drop
        ' that view in drawing
        If (Not (IsNothing(viewNames))) Then
            numViews = (UBound(viewNames) - LBound(viewNames) + 1)
            For Each viewName In viewNames
                viewPaletteName = viewName
                If (viewPaletteName = "*Current") Then
                    swView = swDrawing.DropDrawingViewFromPalette2(viewPaletteName, 0.0#, 0.0#, 0.0#)
                End If
            Next viewName
        End If

        ' Activate the part document and
        ' select two faces for the relative drawing view
        swApp.ActivateDoc3("maingrip.sldprt", False, swRebuildOnActivation_e.swUserDecision, errors)
        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("", "FACE", 0.0466263268498324, 0.00558799999987514, -0.00617351393179888, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", 0.0504738910727269, 0.00167315253537481, -0.00496149996774875, True, 2, Nothing, 0)

        ' Activate the drawing document
        ' Create and insert the relative drawing view using
        ' the selected faces
        ' Activate the relative drawing view
        swApp.ActivateDoc3("maingrip - Sheet1", False, swRebuildOnActivation_e.swUserDecision, errors)
        swDrawing = swApp.ActiveDoc
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\maingrip.sldprt"
        swView = swDrawing.CreateRelativeView(fileName, 0.203608914116486, 0.493530187561698, swRelativeViewCreationDirection_e.swRelativeViewCreationDirection_FRONT, swRelativeViewCreationDirection_e.swRelativeViewCreationDirection_RIGHT
```

```
)
        status = swDrawing.ActivateView("Drawing View2")

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
