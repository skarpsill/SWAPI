---
title: "Create Variable-pitch Helix Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Variable_Pitch_Helix_Example_VBNET.htm"
---

# Create Variable-pitch Helix Example (VB.NET)

This example shows how to create a variable-pitch helix.

```
'--------------------------------------------------------------
' Preconditions: Verify that the specified part document
' template exists.
'
' Postconditions:
' 1. Creates a variable-pitch helix.
' 2. Examine the graphics area and FeatureManager design tree.
'--------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swSketchManager As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swFeatureManager As FeatureManager
        Dim swFeature As Feature
        Dim errors As Integer
        Dim status As Boolean

        ' Create part document
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
        swModel = swApp.ActiveDoc
        swSketchManager = swModel.SketchManager
        swFeatureManager = swModel.FeatureManager

        ' Sketch a circle
	swSketchSegment = swSketchManager.CreateCircle(0.0#, 0.0#, 0.0#, 0.045549, 0.013926, 0.0#)

        ' Create a variable-pitch helix using the sketched circle
        status = swFeatureManager.InsertVariablePitchHelix(False, True, 1, 4.712388980385)
        status = swFeatureManager.AddVariablePitchHelixFirstPitchAndDiameter(0.053, 0.05382625271268)
        status = swFeatureManager.AddVariablePitchHelixSegment(0.0265, 0.05382625271268, 0.5)
        status = swFeatureManager.AddVariablePitchHelixSegment(0.03975, 0.05382625271268, 0.75)
        status = swFeatureManager.AddVariablePitchHelixSegment(0.046375, 0.05382625271268, 0.875)
        status = swFeatureManager.AddVariablePitchHelixSegment(0.053, 0.05382625271268, 1)
        swFeature = swFeatureManager.EndVariablePitchHelix()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
