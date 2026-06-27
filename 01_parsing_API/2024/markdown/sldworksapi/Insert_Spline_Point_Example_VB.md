---
title: "Insert Spline Point Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Spline_Point_Example_VB.htm"
---

# Insert Spline Point Example (VBA)

This example shows how to insert a spline point in a spline sketch.

```
'----------------------------------------------------------------------------
' Preconditions: Verify that the specified template exists.
'
' Postconditions:
' 1. Sketches a spline containing four spline points.
' 2. Inserts a fifth spline point.
' 3. Examine the graphics area.
'---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim skSegment As SldWorks.SketchSegment
```

```
Option Explicit
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2017\templates\Part.prtdot", 0, 0, 0)
```

```
    Dim pointArray As Variant
    Dim points() As Double
    ReDim points(0 To 11) As Double
    points(0) = -6.25070182577474E-02
    points(1) = 7.39156869269664E-03
    points(2) = 0
    points(3) = -4.20233044773113E-02
    points(4) = 3.50529989729012E-02
    points(5) = 0
    points(6) = 2.78754181857153E-02
    points(7) = -1.65377796333246E-02
    points(8) = 0
    points(9) = 4.03878396197683E-02
    points(10) = 4.06222157061507E-02
    points(11) = 0
    pointArray = points
```

```
    Set skSegment = Part.SketchManager.CreateSpline((pointArray))
    Part.InsertSplinePoint 3.82447809668287E-02, 7.81095184375528E-03, 0
    Part.SketchManager.InsertSketch True
```

```
End Sub
```

```vb
 -
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim skSegment As SldWorks.SketchSegment
Option Explicit
 Sub main()

    Set swApp = Application.SldWorks
     Set Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2012\templates\Part.prtdot", 0, 0, 0)

    Dim pointArray As Variant
     Dim points() As Double
     ReDim points(0 To 11) As Double
     points(0) = -6.25070182577474E-02
     points(1) = 7.39156869269664E-03
     points(2) = 0
     points(3) = -4.20233044773113E-02
     points(4) = 3.50529989729012E-02
     points(5) = 0
     points(6) = 2.78754181857153E-02
     points(7) = -1.65377796333246E-02
     points(8) = 0
     points(9) = 4.03878396197683E-02
     points(10) = 4.06222157061507E-02
     points(11) = 0
     pointArray = points

    Set skSegment = Part.SketchManager.CreateSpline((pointArray))
     Part.InsertSplinePoint 3.82447809668287E-02, 7.81095184375528E-03, 0
     Part.SketchManager.InsertSketch True

End Sub
```
