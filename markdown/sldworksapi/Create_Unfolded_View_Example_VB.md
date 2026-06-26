---
title: "Create Unfolded View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Unfolded_View_Example_VB.htm"
---

# Create Unfolded View Example (VBA)

This example shows how to create an unfolded view from an existing view.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open:
 '    public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw
 '
 ' Postconditions: A new unfolded view is created from Drawing View1.
 '
 ' NOTE: Because the model is used elsewhere,
 ' do not save changes when closing it.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim myView As SldWorks.View
 Dim boolstatus As Boolean
Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
     boolstatus = Part.Extension.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
     Set myView = Part.CreateUnfoldedViewAt3(0.379074752406062, 0.276482735105582, 0, False)
End Sub
```
