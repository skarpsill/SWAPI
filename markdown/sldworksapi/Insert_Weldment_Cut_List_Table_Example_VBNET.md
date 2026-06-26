---
title: "Insert Weldment Cut List Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weldment_Cut_List_Table_Example_VBNET.htm"
---

# Insert Weldment Cut List Table Example (VB.NET)

This example shows how to insert a weldment cut list table in a drawing.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified cut list template exists.
 ' 2. Open public_documents\samples\tutorial\weldments\weldment_box2.sldprt.
 ' 3. Click File > Make Drawing from Part > OK > drag a view onto
 '    the sheet > OK.
 ' 4. Expand the drawing view in the FeatureManager design tree.
 ' 5. Right-click weldment_box2 and select Open Part(weldment_box2.sldprt).
 ' 6. Right-click the Cut list folder and click Update Automatically.
 ' 7. Click Window > weldment_box2 - Sheet1*.
 '
 ' Postconditions:
 ' 1. Inserts a weldment cut list table.
 ' 2. Examine the FeatureManager design tree and graphics area.
 '
 ' NOTE: Because this part is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System

 Partial Class SolidWorksMacro

     Const WeldmentTableTemplate As String = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\cut list.sldwldtbt"

     Sub Main()

         Dim oDrawing As DrawingDoc
         Dim swView As View
         Dim WMTable As WeldmentCutListAnnotation

         oDrawing = swapp.ActiveDoc
         swView = oDrawing.GetFirstView
         swView = swView.GetNextView

         ' Insert the weldment cut list table
         WMTable = swView.InsertWeldmentTable(False, 0.1996662889191, 0.1013905859662, swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft,  "Default<As Welded>", WeldmentTableTemplate)

     End Sub

     Public swApp As SldWorks

 End  Class
```
