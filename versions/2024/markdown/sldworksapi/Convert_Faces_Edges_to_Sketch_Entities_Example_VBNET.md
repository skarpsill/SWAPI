---
title: "Convert Faces' Edges to Sketch Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Convert_Faces_Edges_to_Sketch_Entities_Example_VBNET.htm"
---

# Convert Faces' Edges to Sketch Entities Example (VB.NET)

This example shows how to convert the edges of a face to sketch entities.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\cosmosxpress\aw_hook.sldprt.
' 2. If prompted to convert to appearances, click OK.
'
' Postconditions:
' 1. Converts the edges of the selected faces to sketch entities
'    onto Plane1, and creates Sketch3.
' 2. Examine the FeatureManager design tree.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'--------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSketchManager As SketchManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchManager = swModel.SketchManager

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Open sketch on Plane1
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchManager.InsertSketch(True)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Select disjoint faces
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.1098855514325, -0.05688720168837, 0.03453543805836, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.1161834220602, 0.002276177312467, 0.03345674799152, True, 0, Nothing, 0)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Convert edges of faces to sketch entities
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swSketchManager.SketchUseEdge2(False)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Clear the selections and close the sketch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ClearSelection2(True)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchManager.InsertSketch(True)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
