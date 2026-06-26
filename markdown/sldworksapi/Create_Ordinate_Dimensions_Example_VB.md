---
title: "Create Ordinate Dimensions Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Ordinate_Dimensions_Example_VB.htm"
---

# Create Ordinate Dimensions Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModelDoc As SldWorks.ModelDoc2
Dim swDrawingDoc As SldWorks.DrawingDoc
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swDisplayDimension As SldWorks.DisplayDimension
Dim status As Boolean
Dim errors As Long
Dim useDoc As Boolean
Dim arrowSize As Double
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModelDoc = swApp.ActiveDoc
    Set swDrawingDoc = swModelDoc
    Set swModelDocExt = swModelDoc.Extension
    status = swDrawingDoc.ActivateView("Drawing View1")

    'Create ordinate dimension
    status = swModelDocExt.SelectByID2("", "VERTEX", 8.76609155372049E-02, 0.255953076919585, -499.97349537912, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "VERTEX", 9.54286078448972E-02, 0.256322967029476, -499.97349537912, True, 0, Nothing, 0)
    errors = swModelDocExt.AddOrdinateDimension(swAddOrdinateDims_e.swHorizontalOrdinate, 0.094688827625117, 0.272968021978022, 0)

    'Add an ordinate dimension
    swModelDoc.ClearSelection2 True
    status = swModelDocExt.SelectByID2("", "VERTEX", 0.101346849603139, 0.257062747249256, -499.97349537912, False, 0, Nothing, 0)
    swModelDoc.ClearSelection2 True
    swModelDoc.SetPickMode

    'Change the diameter of the circle of the base ordinate dimension
    status = swModelDocExt.SelectByID2("D1@Sketch3@2012-sm.SLDDRW", "DIMENSION", 8.78551078448972E-02, 0.275113384615385, 0, False, 0, Nothing, 0)
    Set swSelMgr = swModelDoc.SelectionManager
    Set swDisplayDimension = swSelMgr.GetSelectedObject6(1, -1)
    swDisplayDimension.SetOrdinateDimensionArrowSize False, 0.00288
    swDisplayDimension.GetOrdinateDimensionArrowSize useDoc, arrowSize
    Debug.Print "Base ordinate dimension diameter of circle for arrow: " & arrowSize * 1000 & "mm"
```

```
End Sub
```
