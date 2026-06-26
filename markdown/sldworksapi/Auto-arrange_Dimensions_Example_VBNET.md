---
title: "Auto-arrange Dimensions Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Auto-arrange_Dimensions_Example_VBNET.htm"
---

# Auto-arrange Dimensions Example (VB.NET)

This example shows how to auto-arrange the selected dimensions.

```vb
'------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
 ' 2. Box-select the dimensions in Drawing View1.
 '
 ' Postconditions:
 ' 1. Auto-arranges the selected dimensions.
 ' 2. Examine Drawing View1.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System

 Partial  Class SolidWorksMacro

     Public  Sub Main()

         Dim swModel  As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swDrawingDoc As DrawingDoc
         Dim status  As  Boolean

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension
         swDrawingDoc = swModel
         status = swModelDocExt.AlignDimensions(swAlignDimensionType_e.swAlignDimensionType_AutoArrange, 0.001)

     End  Sub

     '''  <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     '''  </summary>
     Public swApp As SldWorks

 End  Class
```
