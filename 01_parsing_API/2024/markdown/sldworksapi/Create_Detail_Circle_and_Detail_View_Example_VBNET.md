---
title: "Create Detail Circle and Detail View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Detail_Circle_and_Detail_View_Example_VBNET.htm"
---

# Create Detail Circle and Detail View Example (VB.NET)

This example shows how to create a detail circle and a detail view.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the drawing to open exists.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the specified drawing.
 ' 2. Activates Drawing View4.
 ' 3. Creates a detail circle and a detail view using the visible
 '    corner of Drawing View4.
 ' 4. Activates the detail view.
 ' 5. Gets and sets some properties of the detail circle and detail view.
 ' 6. Examine the drawing document and Immediate window.
 '
 ' NOTE: Because the drawing is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub Main()

         Dim swModel As ModelDoc2
         Dim swDrawing As DrawingDoc
         Dim swSketchManager As SketchManager
         Dim swSketchSegment As SketchSegment
         Dim swView As View
         Dim swDetailCircle As DetailCircle
          Dim swSelMgr As SelectionMgr
         Dim swSelData As SelectData
         Dim fileName As String
         Dim status As Boolean
         Dim errors As Integer, warnings As Integer

         ' Open drawing
         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\replaceview.slddrw"
         swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         swDrawing = swModel
         swSelMgr = swModel.SelectionManager
         swSelData = swSelMgr.CreateSelectData
         swApp.ActivateDoc3("replaceview - Sheet1", False, swRebuildOnActivation_e.swDontRebuildActiveDoc, errors)

         ' Activate Drawing View4 and create detail circle and detail view
         status = swDrawing.ActivateView("Drawing View4")
         swSketchManager = swModel.SketchManager
         swSketchSegment = swSketchManager.CreateCircle(0.007581, 0.053509, 0.0#, 0.013533, 0.016475, 0.0#)
         swView = swDrawing.CreateDetailViewAt4(0.22305342706156, 0.0762140266484527, 0, swDetViewStyle_e.swDetViewSTANDARD, 1, 1, "A", swDetCircleShowType_e.swDetCircleCIRCLE, True, True, False, 5)

         swModel.ClearSelection2(True)

         ' Activate detail view
         status = swDrawing.ActivateView("Drawing View5")

         ' Get and some properties of detail circle and detail view
         swDetailCircle = swView.GetDetail
         Debug.Print("Detail circle:")
         Debug.Print("  Selected: " & swDetailCircle.Select(True, Nothing))
         Debug.Print("  Label: " & swDetailCircle.GetLabel)
         Dim xpos as Double
         Dim ypos as Double
         swDetailCircle.GetLabelPosition(xpos, ypos)
          Debug.Print("  Label X position: " & xpos)
         Debug.Print("  Label Y position: " & ypos)
         Debug.Print("  Type of circle: " & swDetailCircle.GetDisplay)
         Debug.Print("  Name: " & swDetailCircle.GetName)
         Debug.Print("  Style: " & swDetailCircle.GetStyle)
         Debug.Print("  Default document text formatting? " & swDetailCircle.GetUseDocTextFormat)
         If (swDetailCircle.NoOutline =  Then
             Debug.Print("  No outline? False")
             If swDetailCircle.JaggedOutline Then
                 swDetailCircle.ShapeIntensity = 2
                 Debug.Print("  Jagged outline and shape intensity? True and 2")
             End If
         End If

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
