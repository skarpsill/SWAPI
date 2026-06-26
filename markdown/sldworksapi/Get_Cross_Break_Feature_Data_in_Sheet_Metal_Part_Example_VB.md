---
title: "Get Cross Break Feature Data in Sheet Metal Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VB.htm"
---

# Get Cross Break Feature Data in Sheet Metal Part Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swPart As SldWorks.PartDoc
Dim swModel As SldWorks.ModelDoc2
Dim swSketchManager As SldWorks.SketchManager
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureManager As SldWorks.FeatureManager
Dim swCustomBendAllowance As SldWorks.CustomBendAllowance
Dim swFeature As SldWorks.Feature
Dim swCrossBreakFeatureData As SldWorks.CrossBreakFeatureData
Dim swFace As SldWorks.Face2
Dim swEntity As SldWorks.Entity
Dim sketchLines As Variant
Dim features As Variant
Dim faceName As String
Dim status As Boolean
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Create sheet metal part with cross break feature
    Set swPart = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2016\templates\Part.prtdot", 0, 0, 0)
    Set swModel = swPart
    Set swSketchManager = swModel.SketchManager
    swSketchManager.InsertSketch True
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
    status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
    sketchLines = swSketchManager.CreateCornerRectangle(0, 0, 0, 0.112582864792503, -6.90084337349398E-02, 0)
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
    swModel.ShowNamedView2 "*Trimetric", 8
    Set swFeatureManager = swModel.FeatureManager
    Set swCustomBendAllowance = swFeatureManager.CreateCustomBendAllowance()
    swCustomBendAllowance.KFactor = 0.5
    Set swFeature = swFeatureManager.InsertSheetMetalBaseFlange2(0.0007366, False, 0.01905, 0.00508, 0.00254, False, 0, 0, 1, swCustomBendAllowance, False, 0, 0.0001, 0.0001, 0.5, True, False, True, True)
    status = swModelDocExt.SelectByID2("Base-Flange1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("", "FACE", 4.40948432654409E-02, -3.02769643316765E-02, 0, True, 0, Nothing, 0)
    Set swFeature = swFeatureManager.InsertCrossBreak(1.5707963267949, 0.000635)
    swModel.ClearSelection2 True
```

```
    'Get the cross break feature
    'by iterating over all features
    features = swFeatureManager.GetFeatures(True)
    For i = LBound(features) To UBound(features)
        Set swFeature = features(i)
        If swFeature.GetTypeName2 = "CrossBreak" Then
            Set swCrossBreakFeatureData = swFeature.GetDefinition()
            swCrossBreakFeatureData.AccessSelections swModel, Nothing
                Set swFace = swCrossBreakFeatureData.Face
                Set swEntity = swFace
                faceName = "CrossBreakFace"
                status = swPart.SetEntityName(swEntity, faceName)
                  faceName = swModel.GetEntityName(swEntity)
                  Debug.Print "Cross break feature data:"
                  Debug.Print "  Name of face: " & faceName
                  Debug.Print "  Reverse direction: " & swCrossBreakFeatureData.ReverseDirection
                  Debug.Print "  Radius: " & swCrossBreakFeatureData.BreakRadius
                  Debug.Print "  Angle: " & swCrossBreakFeatureData.BreakAngle
            swCrossBreakFeatureData.ReleaseSelectionAccess
        End If
    Next
End Sub
```
