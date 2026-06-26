---
title: "Replace View Model Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Replace_View_Model_Example_VBNET.htm"
---

# Replace View Model Example (VB.NET)

This example shows how to replace a model in drawing views.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\assem20.slddrw.
 ' 2. Verify that the specified replacement model exists.
 '
 ' Postconditions: Replaces the specified component in Drawing View1
 ' with the specified model.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes
 ' when closing it.
 '---------------------------------------------------------------------------
```

```
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swModelDocExt As ModelDocExtension
    Dim swDrawingDoc As DrawingDoc
    Dim swSelectionMgr As SelectionMgr
    Dim swDrawingComponent As DrawingComponent
    Dim swView As View
    Dim swComponent As Component2
    Dim views(0) As Object
    Dim instances(0) As Object
    Dim viewsIn(0) As DispatchWrapper
    Dim instancesIn(0) As DispatchWrapper
    Dim status As Boolean

    Sub main()

        swModel = swApp.ActiveDoc
        swDrawingDoc = swModel
        status = swModel.ActivateView("Drawing View1")

        'Select the view in which to replace the model
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swView = swSelectionMgr.GetSelectedObject6(1, -1)
        views(0) = swView
        viewsIn(0) = New DispatchWrapper(views(0))

        ' Select the instance of the model to replace
        status = swModelDocExt.SelectByID2("Assem20-3@Drawing View1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        swDrawingComponent = swSelectionMgr.GetSelectedObject6(1, -1)
        swComponent = swDrawingComponent.Component
        instances(0) = swComponent
        instancesIn(0) = New DispatchWrapper(instances(0))
        status = swDrawingDoc.ReplaceViewModel("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\bagel.sldprt", (viewsIn), (instancesIn))

    End Sub

    Public swApp As SldWorks

End Class
```
