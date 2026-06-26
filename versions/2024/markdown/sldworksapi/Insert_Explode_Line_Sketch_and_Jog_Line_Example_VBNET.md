---
title: "Insert Explode Line Sketch and Jog Line Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Explode_Line_Sketch_and_Jog_Line_Example_VBNET.htm"
---

# Insert Explode Line Sketch and Jog Line Example (VB.NET)

This example shows how to insert a jog line in an explode line sketch,
a type of 3D sketch.

```
'--------------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\floxpress\ball valve\ball_valve.sldasm.
'
' Postconditions:
' 1. Creates an exploded view of the assembly.
' 2. Adds a jog line, which is a type of explode line.
' 3. Examine the graphics area.
' 4. Locate 3DExplode1, the explode line sketch, on the
'    ConfigurationManager tab (click the ConfigurationManager tab and
'    expand default and ExplView1.)
'
' NOTE: Because this assembly is used elsewhere, do not save changes.
'--------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
```

```vb
Partial Class SolidWorksMacro

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swAssembly As AssemblyDoc
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSketchMgr As SketchManager
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSketchSegment As SketchSegment

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = SwApp.ActiveDoc
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swAssembly = swModel
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchMgr = swModel.SketchManager

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Explode the assembly
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swAssembly.AutoExplode()

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.EditRebuild3()

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ViewZoomtofit2()

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Insert an explode line sketch
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchMgr.InsertExplodeLineSketch()

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Create a line
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchSegment = swSketchMgr.CreateLine(0, 0.1, 0, 0, 0.3, 0)

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ViewZoomtofit2()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Create a jog line using the line
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchSegment.JogLine(0, 0.2, 0, 0.04, 0.25, 0)

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Close the 3D sketchkadov_tag{{<spaces>}}
         kadov_tag{{</spaces>}}swSketchMgr.Insert3DSketch(True)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

 End Class
```
