---
title: "Create Ordinate Dimensions Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Ordinate_Dimensions_Example_VBNET.htm"
---

# Create Ordinate Dimensions Example (VB.NET)

This example shows how to create ordinate dimensions in a drawing.

```
'--------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\2012-sm.slddrw.
' 2. Click Tools > Options > Document Properties, expand Dimensions,
'    click Ordinate, change Base ordinate dimension standard to DIN,
'    and click OK.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Creates ordinate dimensions.
' 2. Click a blank area in the drawing.
' 3. Examine the base ordinate dimension in the drawing and the
'    Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'--------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModelDoc As ModelDoc2
        Dim swDrawingDoc As DrawingDoc
        Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
        Dim swDisplayDimension As DisplayDimension
        Dim status As Boolean
        Dim errors As Integer
        Dim useDoc As Boolean
        Dim arrowSize As Double

        swModelDoc = swApp.ActiveDoc
        swDrawingDoc = swModelDoc
        swModelDocExt = swModelDoc.Extension
        status = swDrawingDoc.ActivateView("Drawing View1")

        'Create ordinate dimension
        status = swModelDocExt.SelectByID2("", "VERTEX", 0.0876609155372049, 0.255953076919585, -499.97349537912, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "VERTEX", 0.0954286078448972, 0.256322967029476, -499.97349537912, True, 0, Nothing, 0)
        errors = swModelDocExt.AddOrdinateDimension(swAddOrdinateDims_e.swHorizontalOrdinate, 0.094688827625117, 0.272968021978022, 0)

        'Add an ordinate dimension
        swModelDoc.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("", "VERTEX", 0.101346849603139, 0.257062747249256, -499.97349537912, False, 0, Nothing, 0)
        swModelDoc.ClearSelection2(True)
        swModelDoc.SetPickMode()

        'Change the diameter of the circle of the base ordinate dimension
        status = swModelDocExt.SelectByID2("D1@Sketch3@2012-sm.SLDDRW", "DIMENSION", 0.0878551078448972, 0.275113384615385, 0, False, 0, Nothing, 0)
        swSelMgr = swModelDoc.SelectionManager
        swDisplayDimension = swSelMgr.GetSelectedObject6(1, -1)
        swDisplayDimension.SetOrdinateDimensionArrowSize(False, 0.00288)
        swDisplayDimension.GetOrdinateDimensionArrowSize(useDoc, arrowSize)
        Debug.Print("Base ordinate dimension diameter of circle for arrow: " & arrowSize * 1000 & "mm")

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
