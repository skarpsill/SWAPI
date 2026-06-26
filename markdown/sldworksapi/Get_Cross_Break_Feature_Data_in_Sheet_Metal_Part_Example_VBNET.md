---
title: "Get Cross Break Feature Data in Sheet Metal Part Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VBNET.htm"
---

# Get Cross Break Feature Data in Sheet Metal Part Example (VB.NET)

This example shows how to get cross break feature data in a sheet metal part.

```
'----------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a sheet metal part with a cross break feature.
' 2. Iterates over all features in the part and gets the
'    cross break feature.
' 3. Names the cross break feature's face.
' 4. Prints to the Immediate window this cross break
'    feature data:
'    * Name of the face
'    * Whether its direction is reversed
'    * Radius
'    * Angle
' 5. Examine the Immediate window.
'----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swPart As PartDoc
        Dim swModel As ModelDoc2
        Dim swSketchManager As SketchManager
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatureManager As FeatureManager
        Dim swCustomBendAllowance As CustomBendAllowance
        Dim swFeature As Feature
        Dim swCrossBreakFeatureData As CrossBreakFeatureData
        Dim swFace As Face2
        Dim swEntity As Entity
        Dim sketchLines As Object
        Dim features As Object
        Dim faceName As String
        Dim status As Boolean
        Dim i As Integer

        'Create sheet metal part with cross break feature
        swPart = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2016\templates\Part.prtdot", 0, 0, 0)
        swModel = swPart
        swSketchManager = swModel.SketchManager
        swSketchManager.InsertSketch(True)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
        status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
        sketchLines = swSketchManager.CreateCornerRectangle(0, 0, 0, 0.112582864792503, -0.0690084337349398, 0)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)
        swModel.ShowNamedView2("*Trimetric", 8)
        swFeatureManager = swModel.FeatureManager
        swCustomBendAllowance = swFeatureManager.CreateCustomBendAllowance()
        swCustomBendAllowance.KFactor = 0.5
        swFeature = swFeatureManager.InsertSheetMetalBaseFlange2(0.0007366, False, 0.01905, 0.00508, 0.00254, False, 0, 0, 1, swCustomBendAllowance, False, 0, 0.0001, 0.0001, 0.5, True, False, True, True)
        status = swModelDocExt.SelectByID2("Base-Flange1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("", "FACE", 0.0440948432654409, -0.0302769643316765, 0, True, 0, Nothing, 0)
        swFeature = swFeatureManager.InsertCrossBreak(1.5707963267949, 0.000635)
        swModel.ClearSelection2(True)

        'Get the cross break feature
        'by iterating over all features
        features = swFeatureManager.GetFeatures(True)
        For i = LBound(features) To UBound(features)
            swFeature = features(i)
            If swFeature.GetTypeName2 = "CrossBreak" Then
                swCrossBreakFeatureData = swFeature.GetDefinition()
                swCrossBreakFeatureData.AccessSelections(swModel, Nothing)
                swFace = swCrossBreakFeatureData.Face
                swEntity = swFace
                faceName = "CrossBreakFace"
                status = swPart.SetEntityName(swEntity, faceName)
                faceName = swModel.GetEntityName(swEntity)
                Debug.Print("Cross break feature data:")
                Debug.Print("  Name of face: " & faceName)
                Debug.Print("  Reverse direction: " & swCrossBreakFeatureData.ReverseDirection)
                Debug.Print("  Radius: " & swCrossBreakFeatureData.BreakRadius)
                Debug.Print("  Angle: " & swCrossBreakFeatureData.BreakAngle)
                swCrossBreakFeatureData.ReleaseSelectionAccess()
            End If
        Next

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
