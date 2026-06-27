---
title: "Create and Modify Variable-pitch Helix Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Modify_Variable-pitch_Helix_Example_VBNET.htm"
---

# Create and Modify Variable-pitch Helix Example (VB.NET)

This example shows how to create and modify a variable-pitch helix.

```
'--------------------------------------------
' Preconditions:
' 1. Specified part template exits.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Selects Front Plane, creates a circle, and
'    and uses the circle to create a variable-pitch
'    helix feature named Helix/Spiral1.
' 3. Gets whether the Helix/Spiral1 feature is a
'    variable-pitch helix. If so:
'    a. Prints to the Immediate window the number
'       of regions.
'    b. Prints to the Immediate window
'       each region's diameter, pitch, height,
'       and revolution.
'    c. If region 2 of the variable-pitch helix
'       is defined by height and revolution:
'       1. Modifies region's diameter, height, and
'          revolution values.
'       2. Prints to the Immediate window the status
'          of modifications made in previous step.
'    d. Deletes the last region in the Helix/Spiral1 feature and
'       prints the status of the deletion to the Immediate window.
'    e. Adds a new last region to the Helix/Spiral1 feature and
'       prints the status of the addition to the Immediate window.
'    - or -
'    Prints to the Immediate window that the Helix/Spiral1
'    feature is not a variable-pitch helix.
' 4. Examine the Immediate window.
'--------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swPart As PartDoc
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchMgr As SketchManager
        Dim swFeatureMgr As FeatureManager
        Dim swFeat As Feature
        Dim swHelixFeatData As HelixFeatureData
        Dim status As Boolean
        Dim i As Integer
        Dim helixType As Integer
        Dim helixStatus As Integer
        Dim helixRegionArray(0) As Integer

        swPart = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
        swModel = swPart
        swModelDocExt = swModel.Extension

        'Select plane on which to create circle
        'for variable-pitch helix
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", -0.0571253507530972, 0.0536428819342089, 0.00349118658744337, False, 0, Nothing, 0)
        swSketchMgr = swModel.SketchManager
        swSketchMgr.InsertSketch(True)
        'Create circle for variable-pitch helix
        swSketchMgr.CreateCircle(0.007581, 0.053509, 0.0#, 0.013533, 0.016475, 0.0#)
        ' Create a variable-pitch helix using the just-sketched circle
        swFeatureMgr = swModel.FeatureManager
        status = swFeatureMgr.InsertVariablePitchHelix(False, True, swHelixDefinedBy_e.swHelixDefinedByHeightAndRevolution, 4.712388980385)
        status = swFeatureMgr.AddVariablePitchHelixFirstPitchAndDiameter(0.053, 0.05382625271268)
        status = swFeatureMgr.AddVariablePitchHelixSegment(0.0265, 0.05382625271268, 0.5)
        status = swFeatureMgr.AddVariablePitchHelixSegment(0.03975, 0.05382625271268, 0.75)
        status = swFeatureMgr.AddVariablePitchHelixSegment(0.046375, 0.05382625271268, 0.875)
        status = swFeatureMgr.AddVariablePitchHelixSegment(0.053, 0.05382625271268, 1)
        swFeat = swFeatureMgr.EndVariablePitchHelix()
        'Get variable-pitch helix
        swHelixFeatData = swFeat.GetDefinition
        If swHelixFeatData.VariablePitch Then
            Debug.Print("  Number of regions: " & swHelixFeatData.PitchCount)
            For i = 1 To swHelixFeatData.PitchCount
                Debug.Print("   Region " & i & ":")
                Debug.Print("      Diameter: " & swHelixFeatData.GetRegionParameterAtIndex(i, swVariablePitchHelixRegionParameter_e.swVariablePitchHelixRegionParameter_Diameter))
                Debug.Print("      Pitch: " & swHelixFeatData.GetRegionParameterAtIndex(i, swVariablePitchHelixRegionParameter_e.swVariablePitchHelixRegionParameter_Pitch))
                Debug.Print("      Height: " & swHelixFeatData.GetRegionParameterAtIndex(i, swVariablePitchHelixRegionParameter_e.swVariablePitchHelixRegionParameter_Height))
                Debug.Print("      Revolutions: " & swHelixFeatData.GetRegionParameterAtIndex(i, swVariablePitchHelixRegionParameter_e.swVariablePitchHelixRegionParameter_Revolution))
            Next i
            'Modify Region 2 of variable-pitch helix
            'defined by height and revolution
            helixType = swHelixFeatData.DefinedBy
            Select Case helixType
                Case swHelixDefinedBy_e.swHelixDefinedByHeightAndRevolution
                    If i >= 2 Then
                        'Cannot change pitch
                        'Can change diameter, height, and revolution
                        'Revolution must be smaller than previous region's
                        'revolution and less than next region's revolution
                        Debug.Print("")
                        Debug.Print("Helix defined by height and revolution:")
                        Debug.Print("   Region modified: 2")
                        helixStatus = swHelixFeatData.SetRegionParameterAtIndex(2, swVariablePitchHelixRegionParameter_e.swVariablePitchHelixRegionParameter_Diameter, 0.052)
                        Debug.Print("      Diameter modified (0 = success): " & helixStatus)
                        helixStatus = swHelixFeatData.SetRegionParameterAtIndex(2, swVariablePitchHelixRegionParameter_e.swVariablePitchHelixRegionParameter_Height, 0.025)
                        Debug.Print("      Height modified (0 = success): " & helixStatus)
                        helixStatus = swHelixFeatData.SetRegionParameterAtIndex(2, swVariablePitchHelixRegionParameter_e.swVariablePitchHelixRegionParameter_Revolution, 0.45)
                        Debug.Print("      Revolution modified (0 = success): " & helixStatus)
                    Else
                        Debug.Print("Less than three regions in Helix/Spiral1 feature.)")
                    End If

                Case swHelixDefinedBy_e.swHelixDefinedByHeightAndPitch
                    'Cannot change revolution
                    'TODO: Add code for variable-pitch helix defined by height and pitch

                Case swHelixDefinedBy_e.swHelixDefinedByPitchAndRevolution
                    'Cannot change height
                    'TODO: Add code for variable-pitch helix defined by pitch and revolution
            End Select

            'Delete last region in the Helix/Spiral1 feature
            helixRegionArray(0) = (i - 1)

            Debug.Print("")
            status = swHelixFeatData.DeleteRecord(helixRegionArray)
            Debug.Print("Last region in Helix/Spiral1 deleted; i.e., region " & i - 1 & " was deleted: " & status)

            'Add new region to end of Region parameters table
            Dim record(3) As Double
            'Height
            record(0) = 0.055
            'Number of revolutions
            record(1) = 1
            '0 indicates that this value cannot be specified
            'for this type of variable-pitch helix (Height and Revolution)
            'Instead, SOLIDWORKS calculates it
            record(2) = 0
            'Diameter
            record(3) = 0.05382625271268
            status = swHelixFeatData.AddLastRecord(record)
            Debug.Print("New region 5 added as last record to Helix/Spiral1: " & status)

            status = swFeat.ModifyDefinition(swHelixFeatData, swModel, Nothing)
        Else
            Debug.Print("Helix is not variable pitch.")
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
