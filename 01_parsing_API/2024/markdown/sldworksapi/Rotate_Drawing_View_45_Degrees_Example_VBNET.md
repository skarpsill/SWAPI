---
title: "Rotate Drawing View 45 Degrees Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Drawing_View_45_Degrees_Example_VBNET.htm"
---

# Rotate Drawing View 45 Degrees Example (VB.NET)

This example shows how to rotate the selected drawing view 45º.

```vb
  '-------------------------------------------------------------
 ' Preconditions: Verify that the specified file to open exists.
 '
 ' Postconditions: Rotates the selected drawing view 45º.
 '-------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swDrawing As DrawingDoc
         Dim status As Boolean
         Dim errors As Long
         Dim warnings As Long

         swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\driveworksxpress\mobile gantry.slddrw", swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         swModelDocExt = swModel.Extension
         swModel.ViewZoomtofit2()
         swDrawing = swModel

         status = swDrawing.ActivateView("Drawing View4")
         status = swModelDocExt.SelectByID2("Drawing View4",  "DRAWINGVIEW", 0.1122300799499, 0.1471819585104, 0, False, 0, Nothing, 0)
        'Convert degrees to radians, the default system unit
         ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
         status = swDrawing.DrawingViewRotate(45 / 57.3)
  End Sub
     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End  Class
```
