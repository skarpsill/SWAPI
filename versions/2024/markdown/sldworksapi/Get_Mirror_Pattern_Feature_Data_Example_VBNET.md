---
title: "Get Mirror Pattern Feature Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mirror_Pattern_Feature_Data_Example_VBNET.htm"
---

# Get Mirror Pattern Feature Data Example (VB.NET)

This example shows how to get data for a mirror pattern feature.

```
'--------------------------------------------------------------------
' Postconditions:
' 1. Verify that the specified part document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Creates Boss-Extrude2.
' 3. Mirrors Boss-Extrude2 to create LPattern1.
' 4. Mirrors Boss-Extrude1 and LPattern1 to create Mirror1.
' 5. Gets the patterned features of Mirror1.
' 6. Examine the FeatureManager design tree, the graphics area, and
'    the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'--------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchSegment As SketchSegment
        Dim swSketchManager As SketchManager
        Dim swFeature As Feature
        Dim swFeatureManager As FeatureManager
        Dim swMirrorPatternFeatureData As MirrorPatternFeatureData
        Dim swEntity As Entity
        Dim swFace As Face2
        Dim swSelData As SelectData = Nothing
        Dim status As Boolean
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer
        Dim faceArray() As Object
        Dim patternArray() As Object
        Dim i As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\beam with holes.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Create Boss-Extrude2
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("", "FACE", 0.0919322519657158, -0.0190749842767559, 0.0399999999999068, False, 0, Nothing, 0)
        swSketchManager = swModel.SketchManager
        swSketchSegment = swSketchManager.CreateCircle(0.092035, -0.020145, 0.0#, 0.093952, -0.029594, 0.0#)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
        swFeatureManager = swModel.FeatureManager
        swFeature = swFeatureManager.FeatureExtrusion3(True, False, False, 0, 0, 0.01, 0.01, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)

        'Create LPattern1
        status = swModelDocExt.SelectByID2("Boss-Extrude2", "BODYFEATURE", 0, 0, 0, False, 4, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.0441545689173921, -0.0398591118729428, 0.0402307394506352, True, 1, Nothing, 0)
        swFeature = swFeatureManager.FeatureLinearPattern4(3, 0.04, 1, 0.01, False, False, "NULL", "NULL", False, False, False, False, False, False, True, True, False, False, 0, 0)

        'Create Mirror1
        status = swModelDocExt.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", 0.232539736404746, -0.0399999999999068, 0.0224388980993808, True, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("LPattern1", "BODYFEATURE", 0, 0, 0, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, True, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", 0.232539736404746, -0.0399999999999068, 0.0224388980993808, True, 2, Nothing, 0)
        swFeature = swFeatureManager.InsertMirrorFeature2(False, False, False, False, swFeatureScope_e.swFeatureScope_AllBodies)

        'Get Mirror1 properties
        swMirrorPatternFeatureData = swFeature.GetDefinition
        Debug.Print("  " & swFeature.Name)
        Debug.Print("    Geometry pattern                                     = " & swMirrorPatternFeatureData.GeometryPattern)
        Debug.Print("    Number of mirrored faces                             = " & swMirrorPatternFeatureData.GetMirrorFaceCount)
        Debug.Print("    Type of mirrored plane (0 = face; 1 = plane)         = " & swMirrorPatternFeatureData.GetMirrorPlaneType)
        Debug.Print("    Number of patterned features                         = " & swMirrorPatternFeatureData.GetPatternFeatureCount)

        'Roll back to get to the faces and features
        status = swMirrorPatternFeatureData.AccessSelections(swModel, Nothing)
        swModel.ClearSelection2(True)

        If 1 = swMirrorPatternFeatureData.GetMirrorPlaneType Then
            swFeature = swMirrorPatternFeatureData.Plane
            'Cannot select a reference plane through Entity, so
            'use Feature
            Debug.Print("    Plane                  = " & swFeature.Name)
            status = swFeature.Select2(True, 0)
        Else
            'Select face through Entity
            swEntity = swMirrorPatternFeatureData.Plane
            status = swEntity.Select4(True, swSelData)
        End If

        faceArray = swMirrorPatternFeatureData.MirrorFaceArray
        If Not faceArray Is Nothing Then
            swModel.ClearSelection2(True)
            status = False
            For i = 0 To UBound(faceArray)
                swFace = faceArray(i)
                swEntity = swFace
                status = swEntity.Select4(True, swSelData)
            Next i
        End If

        patternArray = swMirrorPatternFeatureData.PatternFeatureArray
        If Not patternArray Is Nothing Then
            swModel.ClearSelection2(True)
            status = False
            For i = 0 To UBound(patternArray)
                swFeature = patternArray(i)
                Debug.Print("    Feature (" & i & ")                                          = " & swFeature.Name)
                status = swFeature.Select2(True, 0)
            Next i
        End If
        'Cancel changes
        swMirrorPatternFeatureData.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
