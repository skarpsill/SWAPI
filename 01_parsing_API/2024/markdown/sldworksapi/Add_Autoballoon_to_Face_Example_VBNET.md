---
title: "Add Auto Balloons to Drawing Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Autoballoon_to_Face_Example_VBNET.htm"
---

# Add Auto Balloons to Drawing Example (VB.NET)

This example shows how to automatically add BOM balloons to a drawing view.

```vb
 '------------------------------------------------------------------------------
 ' Preconditions: Open a drawing with a bill of materials (BOM) table.
 '
 ' Postconditions: BOM balloons are added to the view.
 '------------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim vNotes As Object
     Dim autoballoonParams As AutoBalloonOptions
     Dim boolstatus As Boolean

     Sub main()

         Part = swApp.ActiveDoc
         boolstatus = Part.ActivateView("Drawing View1")
         boolstatus = Part.Extension.SelectByID2("Drawing View1",  "DRAWINGVIEW", 0, 0, 0,  False, 0,  Nothing, 0)

         autoballoonParams = Part.CreateAutoBalloonOptions()
         autoballoonParams.Layout = swBalloonLayoutType_e.swDetailingBalloonLayout_Square
         autoballoonParams.ReverseDirection =  False
         autoballoonParams.IgnoreMultiple = True
         autoballoonParams.InsertMagneticLine = True
         autoballoonParams.LeaderAttachmentToFaces = True
         autoballoonParams.Style = swBalloonStyle_e.swBS_Circular
         autoballoonParams.Size = swBalloonFit_e.swBF_5Chars
         autoballoonParams.UpperTextContent = swBalloonTextContent_e.swBalloonTextItemNumber
         autoballoonParams.Layername = "-None-"
         autoballoonParams.ItemNumberStart = 1
         autoballoonParams.ItemNumberIncrement = 1
         autoballoonParams.ItemOrder = swBalloonItemNumbersOrder_e.swBalloonItemNumbers_DoNotChangeItemNumbers
         autoballoonParams.EditBalloons = True
         autoballoonParams.EditBalloonOption = swEditBalloonOption_Resequence

         vNotes = Part.AutoBalloon5(autoballoonParams)

     End Sub

     Public swApp As SldWorks

 End  Class
```
