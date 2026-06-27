---
title: "Create Unfolded View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Unfolded_View_Example_VBNET.htm"
---

# Create Unfolded View Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim myView As View
     Dim boolstatus As Boolean

     Sub main()

         Part = swApp.ActiveDoc
         boolstatus = Part.Extension.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
         myView = Part.CreateUnfoldedViewAt3(0.379074752406062, 0.276482735105582, 0, False)

     End Sub

     Public swApp As SldWorks

 End  Class
```
