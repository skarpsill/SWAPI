---
title: "Get Sketch Arc Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Arc_Data_Example_VBNET.htm"
---

# Get Sketch Arc Data Example (VB.NET)

This example shows how to get sketch arc data.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Verify that the specified document template exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
  ' 1. Creates a new model document with a sketch of an open arc.
 ' 2. Inspect the Immediate window.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes.
  ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim skArcSegment As SketchArc
     Dim Part As ModelDoc2
     Dim centerPt As SketchPoint
     Dim startPt As SketchPoint
     Dim vNormalVector As Object
     Dim endPt As SketchPoint
     Dim boolstatus As Boolean

     Sub main()

         Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
         Part = swApp.ActiveDoc

         Part.SketchManager.InsertSketch(True)
         boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -0.0405700227306837, 0.02417279486491, 0.00498560798672921, False, 0, Nothing, 0)
         Part.ClearSelection2(True)

         skArcSegment = Part.SketchManager.CreateArc(-0.017822, 0.012246, 0.0#, 0.010653, 0.040124, 0.0#, -0.011244, -0.027057, 0.0#, -1)
         Part.ClearSelection2(True)
         Part.SketchManager.InsertSketch(True)

         centerPt = skArcSegment.GetCenterPoint2
         Debug.Print("Center point: " & centerPt.X & ", " & centerPt.Y & ", " & centerPt.Z)

         startPt = skArcSegment.GetStartPoint2
         Debug.Print("Start point: " & startPt.X & ", " & startPt.Y & ", " & startPt.Z)

         endPt = skArcSegment.GetEndPoint2
         Debug.Print("End point: " & endPt.X & ", " & endPt.Y & ", " & endPt.Z)

         vNormalVector = skArcSegment.GetNormalVector
         Debug.Print("Normal vector: " & vNormalVector(0) & ", " & vNormalVector(1) & ", " & vNormalVector(2))

         Debug.Print("Radius in mm: " & skArcSegment.GetRadius * 1000.0#)
         Debug.Print("Rotation direction (1 = counterclockwise, -1 = clockwise): " & skArcSegment.GetRotationDir)
         Debug.Print("Complete circle (1 = complete, 0 = partial arc): " & skArcSegment.IsCircle)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
