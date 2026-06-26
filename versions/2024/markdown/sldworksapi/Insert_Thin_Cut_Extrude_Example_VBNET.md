---
title: "Insert Thin Cut Extrude Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Thin_Cut_Extrude_Example_VBNET.htm"
---

# Insert Thin Cut Extrude Example (VB.NET)

This example shows how to insert a thin cut extrude feature.

```
'------------------------------------------------------
' Preconditions: Verify that the specified part exists.
'
' Postconditions:
' 1. Opens the part.
' 2. Inserts a thin cut extrude feature in the part.
' 3. Examine the FeatureManager design tree and
'    graphics area.
'
' NOTE: Because this part document is used elsewhere,
' do not save changes.
'-----------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public
 Sub main()
```

```vb
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSketchManager As SketchManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSketchSegment As SketchSegment
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeatureManager As FeatureManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeature As Feature
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim longstatus As Integer, longwarnings As Integer

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Open part
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\water.sldprt", 1, 0, "", longstatus,
 longwarnings)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Select face on which to sketch a circle
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.0001655362220845, -0.0477671348753, 0.072, False, 0, Nothing, 0)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ShowNamedView2("*Normal To", swStandardViews_e.swBackView)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ClearSelection2(True)

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Sketch a circle
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchManager = swModel.SketchManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchSegment = swSketchManager.CreateCircle(0.0#, 0.0#, 0.0#, 0.030255, -0.042492, 0.0#)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ClearSelection2(True)

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Create the thin cut extrude
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeatureManager = swModel.FeatureManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeature = swFeatureManager.FeatureCutThin2(True, False, False, swEndConditions_e.swEndCondBlind,
 swEndConditions_e.swEndCondBlind, 0.01, 0.01, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False,
 False, False, 0.01, 0.01, 0.01, 0, 0, False, 0.005, True, True, swStartConditions_e.swStartSketchPlane, 0, False)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ShowNamedView2("*Isometric", swStandardViews_e.swIsometricView)

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

 End Class
```
