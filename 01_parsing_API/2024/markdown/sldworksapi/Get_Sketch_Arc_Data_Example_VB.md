---
title: "Get Sketch Arc Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Arc_Data_Example_VB.htm"
---

# Get Sketch Arc Data Example (VBA)

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
Dim swApp As SldWorks.SldWorks
 Dim skArcSegment As SldWorks.SketchArc
 Dim Part As SldWorks.ModelDoc2
 Dim centerPt As SldWorks.SketchPoint
 Dim startPt As SldWorks.SketchPoint
 Dim vNormalVector As Variant
 Dim endPt As SldWorks.SketchPoint
 Dim boolstatus As Boolean
 Option Explicit
Sub main()
    Set swApp = Application.SldWorks

    Set Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
     Set Part = swApp.ActiveDoc

    Part.SketchManager.InsertSketch True
     boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -4.05700227306837E-02, 0.02417279486491, 4.98560798672921E-03, False, 0, Nothing, 0)
     Part.ClearSelection2 True
    Set skArcSegment = Part.SketchManager.CreateArc(-0.017822, 0.012246, 0#, 0.010653, 0.040124, 0#, -0.011244, -0.027057, 0#, -1)
     Part.ClearSelection2 True
     Part.SketchManager.InsertSketch True

    Set centerPt = skArcSegment.GetCenterPoint2
     Debug.Print "Center point: " & centerPt.X & ", " & centerPt.Y & ", " & centerPt.Z

    Set startPt = skArcSegment.GetStartPoint2
     Debug.Print "Start point: " & startPt.X & ", " & startPt.Y & ", " & startPt.Z

    Set endPt = skArcSegment.GetEndPoint2
     Debug.Print "End point: " & endPt.X & ", " & endPt.Y & ", " & endPt.Z

    vNormalVector = skArcSegment.GetNormalVector
     Debug.Print "Normal vector: " & vNormalVector(0) & ", " & vNormalVector(1) & ", " & vNormalVector(2)

    Debug.Print "Radius in mm: " & skArcSegment.GetRadius * 1000#
     Debug.Print "Rotation direction (1 = counterclockwise, -1 = clockwise): " & skArcSegment.GetRotationDir
     Debug.Print "Complete circle (1 = complete, 0 = partial arc): " & skArcSegment.IsCircle

End Sub
```
