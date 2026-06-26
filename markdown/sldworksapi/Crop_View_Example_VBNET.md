---
title: "Crop View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Crop_View_Example_VBNET.htm"
---

# Crop View Example (VB.NET)

This example shows how to crop a view.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Ensure the specified drawing document exists.
 '
 ' Postconditions: The view is cropped around the specified rectangle.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes when exiting.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim myView As View
     Dim boolstatus As Boolean
     Dim longstatus As Long, longwarnings As Long

     Sub main()

         Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw", 3, 0, "", longstatus, longwarnings)
         swApp.ActivateDoc2("foodprocessor - Sheet1",  False, longstatus)
         Part = swApp.ActiveDoc

         boolstatus = Part.Extension.SelectByID2("Drawing View1",  "DRAWINGVIEW", 0, 0, 0,  False, 0,  Nothing, 0)
         myView = Part.SelectionManager.GetSelectedObject6(1, -1)

         boolstatus = Part.ActivateView("Drawing View1")
         Dim vSkLines As Object
         vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0574722079408937, 0.0331536511827661, 0, 0.0371399698368841, -0.0373161088172339, 0)

         longstatus = myView.Crop
         Part.ClearSelection2(True)

     End Sub

     Public swApp As SldWorks

 End  Class
```
