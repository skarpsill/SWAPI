---
title: "Get Mirror Pattern Feature Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mirror_Feature_Data_Example_VB.htm"
---

# Get Mirror Pattern Feature Data Example (VBA)

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
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchSegment As SldWorks.SketchSegment
Dim swSketchManager As SldWorks.SketchManager
Dim swFeature As SldWorks.Feature
Dim swFeatureManager As SldWorks.FeatureManager
Dim swMirrorPatternFeatureData As SldWorks.MirrorPatternFeatureData
Dim swEntity As SldWorks.Entity
Dim swFace As SldWorks.Face2
Dim swSelData As SldWorks.SelectData
Dim status As Boolean
Dim fileName As String
Dim errors As Long
Dim warnings As Long
Dim faceArray As Variant
Dim patternArray As Variant
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\beam with holes.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Create Boss-Extrude2
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("", "FACE", 9.19322519657158E-02, -1.90749842767559E-02, 3.99999999999068E-02, False, 0, Nothing, 0)
    Set swSketchManager = swModel.SketchManager
    Set swSketchSegment = swSketchManager.CreateCircle(0.092035, -0.020145, 0#, 0.093952, -0.029594, 0#)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeatureManager = swModel.FeatureManager
    Set swFeature = swFeatureManager.FeatureExtrusion3(True, False, False, 0, 0, 0.01, 0.01, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)
```

```
    'Create LPattern1
    status = swModelDocExt.SelectByID2("Boss-Extrude2", "BODYFEATURE", 0, 0, 0, False, 4, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 4.41545689173921E-02, -3.98591118729428E-02, 4.02307394506352E-02, True, 1, Nothing, 0)
    Set swFeature = swFeatureManager.FeatureLinearPattern4(3, 0.04, 1, 0.01, False, False, "NULL", "NULL", False, False, False, False, False, False, True, True, False, False, 0, 0)
```

```
    'Create Mirror1
    status = swModelDocExt.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", 0.232539736404746, -3.99999999999068E-02, 2.24388980993808E-02, True, 0, Nothing, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("LPattern1", "BODYFEATURE", 0, 0, 0, False, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, True, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", 0.232539736404746, -3.99999999999068E-02, 2.24388980993808E-02, True, 2, Nothing, 0)
    Set swFeature = swFeatureManager.InsertMirrorFeature2(False, False, False, False, swFeatureScope_e.swFeatureScope_AllBodies)
```

```
    'Get Mirror1 properties
    Set swMirrorPatternFeatureData = swFeature.GetDefinition
    Debug.Print "  " & swFeature.Name
    Debug.Print "    Geometry pattern                                     = " & swMirrorPatternFeatureData.GeometryPattern
    Debug.Print "    Number of mirrored faces                             = " & swMirrorPatternFeatureData.GetMirrorFaceCount
    Debug.Print "    Type of mirrored plane (0 = face; 1 = plane)         = " & swMirrorPatternFeatureData.GetMirrorPlaneType
    Debug.Print "    Number of patterned features                         = " & swMirrorPatternFeatureData.GetPatternFeatureCount
```

```
    'Roll back to get to the faces and features
    status = swMirrorPatternFeatureData.AccessSelections(swModel, Nothing)
    swModel.ClearSelection2 True
```

```
    If 1 = swMirrorPatternFeatureData.GetMirrorPlaneType Then
        Set swFeature = swMirrorPatternFeatureData.Plane
        'Cannot select a reference plane through Entity, so
        'use Feature
        Debug.Print "    Plane                  = " & swFeature.Name
        status = swFeature.Select2(True, 0)
    Else
        'Select face through Entity
        Set swEntity = swMirrorPatternFeatureData.Plane
        status = swEntity.Select4(True, swSelData)
    End If
```

```
    faceArray = swMirrorPatternFeatureData.MirrorFaceArray
    If Not IsEmpty(faceArray) Then
        swModel.ClearSelection2 True
        status = False
        For i = 0 To UBound(faceArray)
            Set swFace = faceArray(i)
            Set swEntity = swFace
            status = swEntity.Select4(True, swSelData)
        Next i
    End If
```

```
    patternArray = swMirrorPatternFeatureData.PatternFeatureArray
    If Not IsEmpty(patternArray) Then
        swModel.ClearSelection2 True
        status = False
        For i = 0 To UBound(patternArray)
            Set swFeature = patternArray(i)
            Debug.Print "    Feature (" & i & ")                                          = " & swFeature.Name
            status = swFeature.Select2(True, 0)
        Next i
    End If
```

```
    'Cancel changes
    swMirrorPatternFeatureData.ReleaseSelectionAccess
```

```
End Sub
```
