---
title: "Insert Cut Extrude Feature (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Cut_Extrude_Example_VBNET.htm"
---

# Insert Cut Extrude Feature (VB.NET)

## Insert Cut Extrude Example (VB.NET)

This example shows how to insert a cut extrude feature.

```
'-------------------------------------------------------------
' Preconditions: Verify that the specified file to open exists.
'
' Postconditions:
' 1. Inserts a cut extrude feature in the model.
' 2. Examine the graphics area.
'
' NOTE: Because the part document is used elsewhere, do not save
' changes.
'--------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System

 Partial Class SolidWorksMacro

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub Main()

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSketchManager As SketchManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSketchSegment As SketchSegment
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeatureManager As FeatureManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeature As Feature
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim fileerror As Long, filewarning As Long

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Open part document
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\plate.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", fileerror, filewarning)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Select the face where to sketch a circle
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.02031412853728, 0.006977746007294, -0.008053400767039, False, 0, Nothing, 0)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchManager = swModel.SketchManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchManager.InsertSketch(True)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ClearSelection2(True)

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Sketch a circle
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchSegment = swSketchManager.CreateCircle(0.0#, 0.0#, 0.0#, 0.01708, -0.030458, 0.0#)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ClearSelection2(True)

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Create a cut-extrude feature using the circle
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeatureManager = swModel.FeatureManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeature = swFeatureManager.FeatureCut3(True, False, False, swEndConditions_e.swEndCondThroughAll, swEndConditions_e.swEndCondBlind, 0.01, 0.01, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False, False, False, False, True, True, False, False, False, swStartConditions_e.swStartSketchPlane, 0, False)

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

 End Class
```
