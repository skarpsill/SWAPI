---
title: "Create Hole Wizard Hole Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Hole_Wizard_Hole_Example_VBNET.htm"
---

# Create Hole Wizard Hole Example (VB.NET)

This example shows how to create a hole using the hole wizard.

```
'---------------------------------------------------------------
' Preconditions: Verify that the specified part template exists.
'
' Postconditions:
' 1. Creates a part.
' 2. Creates a hole using the hole wizard.
' 3. Examine the graphics area and FeatureManager
'    design tree.
'---------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatMgr As FeatureManager
        Dim swFeat As Feature
        Dim swSketchMgr As SketchManager
        Dim sketchLines As Object
        Dim status As Integer
        Dim boolstatus As Boolean
        Dim P1(2) As Double
        Dim P2(2) As Double
        Dim P3(2) As Double

        'Create the model for the wizard hole
        swApp.ResetUntitledCount(0, 0, 0)
        swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2020\templates\Part.prtdot", 0, 0, 0)
        swApp.ActivateDoc2("Part1", False, status)
        swModel = swApp.ActiveDoc
        swSketchMgr = swModel.SketchManager
        swModelDocExt = swModel.Extension
        swFeatMgr = swModel.FeatureManager
        sketchLines = swSketchMgr.CreateCornerRectangle(-0.05096498314664, 0.05060941349678, 0, 0.1021670127265, -0.05037236706354, 0)
        boolstatus = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
        boolstatus = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        boolstatus = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        boolstatus = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        swFeat = swFeatMgr.FeatureExtrusion2(True, False, False, 0, 0, 0.381, 0.381, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False, False, False, True, True, True, 0, 0, False)

        'Create three points for the reference plane
        P1(0) = -0.0141556764402858
        P1(1) = 0.00194061273859598
        P1(2) = 0
        P2(0) = -0.0141556764402858
        P2(1) = 0.00194061273859598
        P2(2) = 1
        P3(0) = -0.149976101832345
        P3(1) = -0.988792859011662
        P3(2) = 0

        'Create the reference plane
        swModel.CreatePlaneFixed2(P1, P2, P3, False)

        'Select the reference plane
        boolstatus = swModelDocExt.SelectByID2("Plane1", "PLANE", -0.0156784487003801, -0.00916715285390111, 0.0558270998665543, False, 0, Nothing, 0)

        'Create the hole wizard countersink hole
        swFeat = swFeatMgr.HoleWizard5(swWzdGeneralHoleTypes_e.swWzdCounterSink, swWzdHoleStandards_e.swStandardAnsiMetric, swWzdHoleStandardFastenerTypes_e.swStandardAnsiMetricFlatHead82, "M2", swEndConditions_e.swEndCondThroughAll, 0.0102, 0.010312189893273, 0, 0.0044, 1.57079632679489, 0.000152189893272978, 0, -1, -1, -1, -1, 1, -1, -1, -1, "", False, True, True, True, True, False)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
