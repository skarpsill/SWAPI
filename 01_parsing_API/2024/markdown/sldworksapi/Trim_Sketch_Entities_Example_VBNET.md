---
title: "Trim Sketch Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Trim_Sketch_Entities_Example_VBNET.htm"
---

# Trim Sketch Entities Example (VB.NET)

This example shows how to trim a sketch to a corner.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Ensure the specified template exists.
 '
 ' Postconditions:
 ' 1. Opens a new part document.
 ' 2. Sketches some lines.
 ' 3. Examine the sketch, then press
 '    F5.
 ' 4. Selects two lines and trims them
 '    to a corner.
 ' 5. Examine the sketch to verify.
 '-----------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Public Sub Main()

         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swSketchMgr As SketchManager
         Dim swSketchSegment As SketchSegment
         Dim status As Boolean

         swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2018\templates\Part.prtdot", 0, 0, 0)
         swModelDocExt = swModel.Extension
         swSketchMgr = swModel.SketchManager

         ' Create sketch of lines
         status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
         swSketchMgr.InsertSketch(True)
         swModel.ClearSelection2(True)
         swSketchSegment = swSketchMgr.CreateLine(-0.055275, 0.03236, 0.0#, 0.027405, 0.03236, 0.0#)
         swSketchSegment = swSketchMgr.CreateLine(0.027405, 0.03236, 0.0#, 0.027405, -0.026476, 0.0#)
         swSketchSegment = swSketchMgr.CreateLine(0.027405, -0.026476, 0.0#, -0.055275, -0.026476, 0.0#)
         swSketchSegment = swSketchMgr.CreateLine(-0.055275, -0.026476, 0.0#, -0.055275, -0.070758, 0.0#)
         swSketchSegment = swSketchMgr.CreateLine(-0.055275, -0.070758, 0.0#, 0.027405, -0.070758, 0.0#)
         swSketchSegment = swSketchMgr.CreateLine(0.027405, -0.070758, 0.0#, 0.076642, 0.03236, 0.0#)
         swModel.ClearSelection2(True)

         Stop
         ' Examine the sketch before trimming
         ' the selected lines to a corner
         ' Press F5
         ' Select two lines to trim to a corner

         status = swModelDocExt.SelectByID2("Line6", "SKETCHSEGMENT", 0.0391723509933775, -0.0466042594822396, 0, True, 0, Nothing, 0)
         status = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0.0193539283564118, -0.0264761739915713, 0, True, 0, Nothing, 0)
         status = swSketchMgr.SketchTrim(swSketchTrimChoice_e.swSketchTrimCorner, 0, 0, 0)
         swModel.ClearSelection2(True)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
