---
title: "Crop View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Crop_View_Example_VB.htm"
---

# Crop View Example (VBA)

This example shows how to crop a view.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Ensure the specified drawing document exists.
 '
 ' Postconditions: The view is cropped around the specified rectangle.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes when exiting.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim myView As SldWorks.View
 Dim boolstatus As Boolean
 Dim longstatus As Long, longwarnings As Long
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks

    Set Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw", 3, 0, "", longstatus, longwarnings)
     swApp.ActivateDoc2 "foodprocessor - Sheet1", False, longstatus
     Set Part = swApp.ActiveDoc

    boolstatus = Part.Extension.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
     Set myView = Part.SelectionManager.GetSelectedObject6(1, -1)

    boolstatus = Part.ActivateView("Drawing View1")
     Dim vSkLines As Variant
     vSkLines = Part.SketchManager.CreateCornerRectangle(-5.74722079408937E-02, 3.31536511827661E-02, 0, 3.71399698368841E-02, -3.73161088172339E-02, 0)

    longstatus = myView.Crop
     Part.ClearSelection2 True

End Sub
```
