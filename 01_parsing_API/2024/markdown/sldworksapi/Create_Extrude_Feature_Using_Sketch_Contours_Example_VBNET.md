---
title: "Create Extrude Feature Using Sketch Contours Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Extrude_Feature_Using_Sketch_Contours_Example_VBNET.htm"
---

# Create Extrude Feature Using Sketch Contours Example (VB.NET)

This example shows how to create an extrude feature using sketch contours.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Creates a sketch containing sketch contours.
' 3. Creates a boss extrude feature using the sketch of sketch
'    contours.
' 4. Selects the boss extrude feature and accesses
'    its data.
' 5. Gets the sketch contours.
' 6. Get whether each sketch contour is open or closed.
' 7. Examine the FeatureManager design tree, graphics area, and
'    the Immediate window.
'--------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swSketchMgr As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swModelDocExtension As ModelDocExtension
        Dim swSelectionMgr As SelectionMgr
        Dim swFeatureMgr As FeatureManager
        Dim swFeature As Feature
        Dim swExtrudeFeatureData As ExtrudeFeatureData2
        Dim status As Boolean
        Dim skcontours() As Object
        Dim skcontour As SketchContour = Nothing
        Dim nbrContours As Integer
        Dim i As Integer

        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2016\templates\Part.prtdot", 0, 0, 0)
        swModelDocExtension = swModel.Extension
        swSketchMgr = swModel.SketchManager
        swSelectionMgr = swModel.SelectionManager
        swFeatureMgr = swModel.FeatureManager

        'Create sketch containing sketch contours
        swSketchMgr.InsertSketch(True)
        swSketchSegment = swSketchMgr.CreateCircle(0.0#, 0.0#, 0.0#, 0.010564, -0.041843, 0.0#)
        swModel.ClearSelection2(True)
        swSketchSegment = swSketchMgr.CreateCircle(0.043155, 0.0#, 0.0#, 0.048428, -0.01221, 0.0#)
        swModel.ClearSelection2(True)
        swSketchSegment = swSketchMgr.CreateCircle(-0.043155, 0.0#, 0.0#, -0.043214, -0.014954, 0.0#)
        swModel.ClearSelection2(True)
        swSketchMgr.InsertSketch(True)

        'Create boss extrude feature
        status = swModelDocExtension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        status = swModelDocExtension.SelectByID2("Sketch1", "SKETCHCONTOUR", -0.047096875714166, 0.00724922083273226, 0.018531938896921, True, 0, Nothing, 0)
        status = swModelDocExtension.SelectByID2("Sketch1", "SKETCHCONTOUR", 0.0473122625955432, -0.015948285832011, -0.0155264330079864, True, 0, Nothing, 0)
        status = swModelDocExtension.SelectByID2("Sketch1", "SKETCHCONTOUR", -0.00880361157802517, -0.0246473508312897, 0.0199951653548178, True, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        swSelectionMgr.EnableContourSelection = True
        status = swModelDocExtension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
        status = swModelDocExtension.SelectByID2("Sketch1", "SKETCHCONTOUR", -0.047096875714166, 0.00724922083273226, 0.018531938896921, True, 4, Nothing, 0)
        status = swModelDocExtension.SelectByID2("Sketch1", "SKETCHCONTOUR", 0.0473122625955432, -0.015948285832011, -0.0155264330079864, True, 4, Nothing, 0)
        status = swModelDocExtension.SelectByID2("Sketch1", "SKETCHCONTOUR", -0.00880361157802517, -0.0246473508312897, 0.0199951653548178, True, 4, Nothing, 0)
        swFeature = swFeatureMgr.FeatureExtrusion3(True, False, False, 0, 0, 0.01016, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)
        swSelectionMgr.EnableContourSelection = False

        'Select the boss extrude feature
        status = swModelDocExtension.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, swSelectOption_e.swSelectOptionDefault)
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swExtrudeFeatureData = swFeature.GetDefinition

        'Access the boss extrude feature data
        swExtrudeFeatureData.AccessSelections(swModel, Nothing)

        'Get the number of sketch contours in the extrude feature
        nbrContours = swExtrudeFeatureData.GetContoursCount
        Debug.Print("Number of sketch contours in the extrude feature: " & nbrContours)

        'Get the sketch contours in the extrude feature
        skcontours = swExtrudeFeatureData.Contours

        'Get each sketch contour and whether it is open or closed
        For i = 0 To (nbrContours - 1)
            skcontour = skcontours(i)
            Debug.Print("  Sketch contour " & i & " is closed? " & skcontour.IsClosed)
        Next i

        'Release selection access
        swExtrudeFeatureData.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
