---
title: "Insert Weld Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weld_Table_Example_VBNET.htm"
---

# Insert Weld Table Example (VB.NET)

This example shows how to insert a weld table into a drawing view.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open the drawing of a part that contains a weld bead.
 ' 2. Verify that install_dir\lang\english\weldtable-standard.sldwldtbt exists.
 '
 ' Postconditions:
 ' 1. Inserts a weld table.
 ' 2. Examine the drawing and the FeatureManager design tree.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System

 Partial Class SolidWorksMacro

     Dim Draw As DrawingDoc
     Dim Part As ModelDoc2
     Dim swActiveView As View
     Dim boolstatus As Boolean

     Const WeldTableTemplate As String = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\weldtable-standard.sldwldtbt"
     Sub main()

         Part = swApp.ActiveDoc
         boolstatus = Part.Extension.SelectByID2("Drawing View1",  "DRAWINGVIEW", 0, 0, 0,  False, 0,  Nothing, 0)
         Draw = Part
        boolstatus = Draw.ActivateView("Drawing View1")
         swActiveView = Draw.ActiveDrawingView
         Dim boolResult As Boolean
         boolResult = swActiveView.InsertWeldTable(False,  True,  False, 0.0#, 0.0#, swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_BottomLeft,  "Default", WeldTableTemplate)

     End Sub

     Public swApp As SldWorks

 End  Class
```
