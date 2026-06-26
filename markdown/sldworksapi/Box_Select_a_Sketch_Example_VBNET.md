---
title: "Box Select a Sketch Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Box_Select_a_Sketch_Example_VBNET.htm"
---

# Box Select a Sketch Example (VB.NET)

This example shows how to box select all of the entities in a sketch
block.

'----------------------------------------------------------------------------- ' Preconditions: Open public_documents \samples\tutorial\blocks\piston_mechanism.sldblk . ' ' Postconditions: ' 1. Opens and box selects Sketch1 . ' 2. Examine the list of selected entities ' in the PropertyManager page. ' 3. Interactively quit editing the sketch without ' saving any changes. ' 4. Close the document. '--------------------------------------

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System

Partial Class SolidWorksMacros

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Select the sketch and open it
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.EditSketch()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ViewZoomtofit2()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Box select the sketch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SketchBoxSelect("-0.663893", "1.322001", "0.000000", "-0.395073", "0.698568", "0.000000")

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
