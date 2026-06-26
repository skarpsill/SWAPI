---
title: "Is There a Projection Arrow and Is It Visible Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Is_There_a_Projection_Arrow_and_Is_It_Visible_Example_VBNET.htm"
---

# Is There a Projection Arrow and Is It Visible Example (VB.NET)

This example shows how to find out if:

- the selected drawing view is a projected view
- a projection arrow exists in the projected view
- the projected arrow is visible

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
' 2. Double-click the projected view (i.e., the upper-right drawing view).
' 3. In the PropertyManager page, click the Arrow check box and
'    type a label for the projection arrow.
' 4. Click OK to close the PropertyManager page.
'
' Postconditions:
' 1. Creates a visible projection arrow for Drawing View2, which is
'    a projected view.
' 2. Examine the graphics area and Immediate window.
'
' NOTE: Because this drawing document is used elsewhere, do not save
' changes.
'--------------------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDrawing As DrawingDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swView As View
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swProjectionArrow As ProjectionArrow
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim typeDrawingView As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDrawing = swModel
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swDrawing.ActivateView("Drawing View2")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Drawing View2", "DRAWINGVIEW", 0.4426278247583, 0.3837831481976, 0, False, 0, Nothing, 0)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swView = swDrawing.ActiveDrawingView
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}typeDrawingView = swView.Type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If typeDrawingView = 4 Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Type of selected drawing view is projected.")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Type of selected drawing view is not projected. Exiting macro.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swProjectionArrow = swView.GetProjectionArrow
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Not swProjectionArrow Is Nothing Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Projection arrow visible: " & swProjectionArrow.Visible)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("No projection arrow in projected view.")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
