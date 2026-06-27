---
title: "Replace View Model Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Replace_View_Model_Example_VB.htm"
---

# Replace View Model Example (VBA)

This example shows how to replace a model in a drawing view.

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDrawingDoc As SldWorks.DrawingDoc
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swDrawingComponent As SldWorks.DrawingComponent
Dim views(0) As Object
Dim swView As SldWorks.View
Dim instances(0) As Object
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDrawingDoc = swModel
```

```
    status = swModel.ActivateView("Drawing View1")
```

```
    'Select the view in which to replace the model
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swView = swSelectionMgr.GetSelectedObject6(1, -1)
    Set views(0) = swView
```

```
    ' Select the instance of the model to replace
    status = swModelDocExt.SelectByID2("Assem20-3@Drawing View1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swDrawingComponent = swSelectionMgr.GetSelectedObject6(1, -1)
    Set instances(0) = swDrawingComponent.Component
    status = swDrawingDoc.ReplaceViewModel("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\bagel.sldprt", (views), (instances))
```

```
End Sub
```
