---
title: "Create Temporary Extruded Body Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Temporary_Extruded_Body_Example_VBNET.htm"
---

# Create Temporary Extruded Body Example (VB.NET)

This example shows how to create a temporary extruded body.

```
'------------------------------------------------
' Preconditions: Verify that the specified part document
' template exists.
'
' Postconditions.
' 1. Opens a new part document.
' 2. Creates and selects a sheet (also called a surface) body.
' 3. Creates a temporary extruded body.
' 4. Examine the graphics area.
'------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatureManager As FeatureManager
        Dim swSketchManager As SketchManager
        Dim swSelectionManager As SelectionMgr
        Dim sketchSegment As SketchSegment
        Dim swModeler As Modeler
        Dim swMath As MathUtility
        Dim profileBody As Body2
        Dim extrudedBody As Body2
        Dim dirVector As MathVector
        Dim planeSurf As Surface
        Dim trimCurves(3) As Curve
        Dim points(11) As Double
        Dim pointArray As Object
        Dim halfWidth As Double
        Dim halfLength As Double
        Dim startArr(2) As Double
        Dim endArr(2) As Double
        Dim ptArr(2) As Double
        Dim dirArr(2) As Double
        Dim slotWidth As Double
        Dim slotLength As Double
        Dim slotDepth As Double
        Dim slotThruAll As Boolean
        Dim status As Boolean

        swModeler = swApp.GetModeler
        swMath = swApp.GetMathUtility
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2014\templates\Part.prtdot", 0, 0, 0)
        swFeatureManager = swModel.FeatureManager
        swSketchManager = swModel.SketchManager
        swModelDocExt = swModel.Extension
        swSelectionManager = swModel.SelectionManager

        'Create and select extruded surface body
        points(0) = -0.0720746414289124
        points(1) = -0.0283600245263074
        points(2) = 0
        points(3) = -0.0514715593755
        points(4) = -0.00345025084396866
        points(5) = 0
        points(6) = 0
        points(7) = 0
        points(8) = 0
        points(9) = 0.0872558597840225
        points(10) = 0.0521037067517796
        points(11) = 0
        pointArray = points
        sketchSegment = swSketchManager.CreateSpline((pointArray))
        swSketchManager.InsertSketch(True)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
        swFeatureManager.FeatureExtruRefSurface2(True, False, False, 0, 0, 0.0508, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, False, False, False, False)
        swSelectionManager.EnableContourSelection = False
        status = swModelDocExt.SelectByID2("Surface-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)

        slotDepth = 0.01
        slotWidth = 0.04
        slotLength = 0.09
        slotThruAll = False
        halfWidth = slotWidth / 2
        halfLength = slotLength / 2
        ptArr(0) = 0.0#
        ptArr(1) = 0.0#
        ptArr(2) = 0.0#
        dirArr(0) = 0.0#
        dirArr(1) = 0.0#
        dirArr(2) = 1.0#
        startArr(0) = 1.0#
        startArr(1) = 0.0#
        startArr(2) = 0.0#
        planeSurf = swModeler.CreatePlanarSurface2((ptArr), (dirArr), (startArr))

        ptArr(0) = -halfLength
        ptArr(1) = halfWidth
        ptArr(2) = 0.0#
        dirArr(0) = 1.0#
        dirArr(1) = 0.0#
        dirArr(2) = 0.0#
        trimCurves(0) = swModeler.CreateLine((ptArr), (dirArr))
        trimCurves(0) = trimCurves(0).CreateTrimmedCurve2(-halfLength, halfWidth, 0.0#, halfLength, halfWidth, 0.0#)

        ptArr(0) = halfLength
        ptArr(1) = 0.0#
        ptArr(2) = 0.0#
        startArr(0) = halfLength
        startArr(1) = halfWidth
        startArr(2) = 0.0#
        endArr(0) = halfLength
        endArr(1) = -halfWidth
        endArr(2) = 0.0#
        dirArr(0) = 0.0#
        dirArr(1) = 0.0#
        dirArr(2) = -1.0#
        trimCurves(1) = swModeler.CreateArc((ptArr), (dirArr), halfWidth, (startArr), (endArr))
        trimCurves(1) = trimCurves(1).CreateTrimmedCurve2(halfLength, halfWidth, 0.0#, halfLength, -halfWidth, 0.0#)

        ptArr(0) = halfLength
        ptArr(1) = -halfWidth
        ptArr(2) = 0.0#
        dirArr(0) = -1.0#
        dirArr(1) = 0.0#
        dirArr(2) = 0.0#
        trimCurves(2) = swModeler.CreateLine((ptArr), (dirArr))
        trimCurves(2) = trimCurves(2).CreateTrimmedCurve2(halfLength, -halfWidth, 0.0#, -halfLength, -halfWidth, 0.0#)

        ptArr(0) = -halfLength
        ptArr(1) = 0.0#
        ptArr(2) = 0.0#
        startArr(0) = -halfLength
        startArr(1) = -halfWidth
        startArr(2) = 0.0#
        endArr(0) = -halfLength
        endArr(1) = halfWidth
        endArr(2) = 0.0#
        dirArr(0) = 0.0#
        dirArr(1) = 0.0#
        dirArr(2) = -1.0#
        trimCurves(3) = swModeler.CreateArc((ptArr), (dirArr), halfWidth, (startArr), (endArr))
        trimCurves(3) = trimCurves(3).CreateTrimmedCurve2(-halfLength, -halfWidth, 0.0#, -halfLength, halfWidth, 0.0#)
        profileBody = planeSurf.CreateTrimmedSheet((trimCurves))

        dirArr(0) = 0.0#
        dirArr(1) = 0.0#
        dirArr(2) = -1.0#
        dirVector = swMath.CreateVector((dirArr))
        extrudedBody = swModeler.CreateExtrudedBody(profileBody, dirVector, slotDepth)
        extrudedBody.Display3(swModel, RGB(1, 0, 0), swTempBodySelectOptions_e.swTempBodySelectOptionNone)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
