---
title: "Hide and Show Sketches Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_and_Show_Sketches_Example_VBNET.htm"
---

# Hide and Show Sketches Example (VB.NET)

This example shows how to hide and show sketches in a model.

```
'---------------------------------------
' Preconditions: Run the macro.
'
' Postconditions:
' 1. Opens a new part document and
'    creates two sketches.
' 2. Selects one sketch and hides it.
' 3. Examine the graphics area to verify
'    and press F5.
' 4. Selects the hidden sketch and shows
'    it.
'--------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchMgr As SketchManager
        Dim sketchLines As Object
        Dim swSketchSegment As SketchSegment
        Dim status As Boolean

        swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2013\templates\Part.prtdot", swDwgPaperSizes_e.swDwgPaperAsizeVertical, 0, 0)
        swModelDocExt = swModel.Extension
        swSketchMgr = swModel.SketchManager

        ' Sketch a rectangle
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        sketchLines = swSketchMgr.CreateCornerRectangle(-0.0684166678777842, 0.0376953152008355, 0, -0.0273535635019471, 0.00483994917499331, 0)
        swModel.ClearSelection2(True)
        swSketchMgr.InsertSketch(True)

        ' Sketch a circle
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        swSketchSegment = swSketchMgr.CreateCircle(0.044426, 0.079347, 0.0#, 0.057359, 0.06229, 0.0#)
        swModel.ClearSelection2(True)
        swSketchMgr.InsertSketch(True)

        swModel.ClearSelection2(True)

        ' Select a sketch and hide it
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        swModel.BlankSketch()

        Stop
        ' Examine the graphics area
        ' to verify that the selected sketch
        ' is hidden
        ' Press F5

        swModel.ClearSelection2(True)

        ' Select the just hidden sketch again
        ' and show it
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        swModel.UnblankSketch()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
