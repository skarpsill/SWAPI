---
title: "Select Multiple Splines for Loft Guide Curves Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Multiple_Splines_for_Loft_Guide_Curves_Example_VBNET.htm"
---

# Select Multiple Splines for Loft Guide Curves Example (VB.NET)

This example shows how to select multiple splines for the guide curves for a loft feature.

```
'---------------------------------------------------------------
' Preconditions: Verify that the specified part template exists.
'
' Postconditions:
' 1. Creates a new part.
' 2. Creates a profile sketch.
' 3. Creates a reference plane and another profile sketch on that
'    reference plane.
' 4. Creates two splines for the guide curves.
' 5. Selects the profile sketches.
' 6. Selects the splines and groups them as an object.
' 7. Creates a loft feature.
' 8. Examine the FeatureManager design tree and graphics area.
'---------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchSegment As SketchSegment
        Dim swSketchManager As SketchManager
        Dim swRefPlane As RefPlane
        Dim swFeatureManager As FeatureManager
        Dim status As Boolean

        'Create a new part
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2017\templates\Part.prtdot", 0, 0, 0)

        'Create a profile sketch
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        swSketchManager = swModel.SketchManager
        swSketchSegment = swSketchManager.CreateEllipse(0, 0, 0, 0.0706113079019074, 0, 0, 0, 0.0374944141689373, 0)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)

        'Create a reference plane and another profile sketch
        'on that reference plane
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        swFeatureManager = swModel.FeatureManager
        swRefPlane = swFeatureManager.InsertRefPlane(8, 0.07, 0, 0, 0, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchSegment = swSketchManager.CreateEllipse(0, 0, 0, 0.0527205722070845, 0, 0, 0, 0.0154164850136235, 0)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)

        'Create a spline
        status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        Dim pointArray As Object
        Dim points(14) As Double
        points(0) = -0.07
        points(1) = 0.0154164850136235
        points(2) = 0
        points(3) = -0.0531092941649547
        points(4) = 0.0280386111480766
        points(5) = 0
        points(6) = -0.0296934467839947
        points(7) = 0.0229795168190776
        points(8) = 0
        points(9) = -0.0112921067380967
        points(10) = 0.026354325474415
        points(11) = 0
        points(12) = 0
        points(13) = 0.0374944141689373
        points(14) = 0
        pointArray = points
        swSketchSegment = swSketchManager.CreateSpline((pointArray))
        swSketchManager.InsertSketch(True)
        swModel.ClearSelection2(True)

        'Create another spline
        status = swModelDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        ReDim points(8)
        points(0) = -0.07
        points(1) = -0.0154164850136235
        points(2) = 0
        points(3) = -0.0307689275649068
        points(4) = -0.0233694015292372
        points(5) = 0
        points(6) = 0
        points(7) = -0.0374944141689373
        points(8) = 0
        pointArray = points
        swSketchSegment = swSketchManager.CreateSpline((pointArray))
        swSketchManager.InsertSketch(True)
        swModel.ClearSelection2(True)

        'Select the profile sketches
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", -0.0585496337278505, 0.0209585732143712, 1, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", -0.0379093739088495, 0.0107136192740755, 1, True, 0, Nothing, 0)

        'Select the splines for the guide curves
        status = swModelDocExt.SelectByID2("Spline1@Sketch3", "EXTSKETCHSEGMENT", -0.00620659823337474, 0.0304187689522769, 2, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Spline1@Sketch4", "EXTSKETCHSEGMENT", -0.0402947949143199, -0.0206106896601265, 2, True, 0, Nothing, 0)
        'Group the selected splines as an object
        status = swModelDocExt.SelectByID2("Unknown", "SELOBJGROUP", 0, 0, 0, True, 2, Nothing, 0)

        'Create a loft
        swFeatureManager.InsertProtrusionBlend2(False, True, False, 1, 0, 0, 1, 1, True, True, False, 0, 0, 0, True, True, True, 0)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
