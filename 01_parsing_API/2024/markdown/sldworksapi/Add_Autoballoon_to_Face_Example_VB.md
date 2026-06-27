---
title: "Add Auto Balloons to Drawing Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Autoballoon_to_Face_Example_VB.htm"
---

# Add Auto Balloons to Drawing Example (VBA)

This example shows how to automatically add BOM balloons to a drawing view.

```vb
 '------------------------------------------------------------------------------
 ' Preconditions: Open a drawing with a bill of materials (BOM) table.
 '
 ' Postconditions: The specified BOM balloons are added to the view.
 '------------------------------------------------------------------------------
 Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim vNotes As Variant
 Dim autoballoonParams As SldWorks.AutoBalloonOptions
 Dim boolstatus As Boolean
Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
     boolstatus = Part.ActivateView("Drawing View1")
     boolstatus = Part.Extension.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
    Set autoballoonParams = Part.CreateAutoBalloonOptions()
     autoballoonParams.Layout = swDetailingBalloonLayout_Square
     autoballoonParams.ReverseDirection = False
     autoballoonParams.IgnoreMultiple = True
     autoballoonParams.InsertMagneticLine = True
     autoballoonParams.LeaderAttachmentToFaces = True
     autoballoonParams.Style = swBS_Circular
     autoballoonParams.Size = swBF_5Chars
     autoballoonParams.UpperTextContent = swBalloonTextItemNumber
     autoballoonParams.Layername = "-None-"
     autoballoonParams.ItemNumberStart = 1
     autoballoonParams.ItemNumberIncrement = 1
     autoballoonParams.ItemOrder = swBalloonItemNumbers_DoNotChangeItemNumbers
     autoballoonParams.EditBalloons = True
     autoballoonParams.EditBalloonOption = swEditBalloonOption_Resequence
    vNotes = Part.AutoBalloon5(autoballoonParams)

End Sub
```
