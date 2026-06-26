---
title: "Create and Modify Dome Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Modify_Dome_Feature_Example_VB.htm"
---

# Create and Modify Dome Feature Example (VBA)

This example shows how to create and modify a dome feature.

```
'---------------------------------------------------------
' Preconditions:
' 1. Verify that the part document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Edits Sketch1, sketches an ellipse, and creates a boss feature.
' 3. Selects a face on the boss feature and
'    inserts a dome feature.
' 4. Prints to the Immediate window some
'    dome feature data.
' 5. Reverses the direction of the dome feature.
' 6. Examine the Immediate window, graphics area,
'    and FeatureManager design tree.
'
' NOTE: Because the part is used elsewhere, do not
' save changes.
'----------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchMgr As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swFeature As SldWorks.Feature
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swDomeFeatureData As SldWorks.DomeFeatureData2
Dim faces As Variant
Dim aFace As Variant
Dim swFace As SldWorks.Face2
Dim oneBody As SldWorks.Body2
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open model document to which to add a dome feature
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Open sketch to which to add a sketch of an ellipse
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    swModel.EditSketch
    swModel.ClearSelection2 True
```

```
    'Sketch an ellipse
    swModel.ShowNamedView2 "*Top", 5
    Set swSketchMgr = swModel.SketchManager
    Set swSketchSegment = swSketchMgr.CreateEllipse(-7.61501034873036E-02, 4.90523248480422E-02, 0, -5.13492425103863E-02, 4.90523248480422E-02, 0, -7.61501034873036E-02, 5.45451329838695E-02, 0)
    swModel.ClearSelection2 True
    swSketchMgr.InsertSketch True
    swModel.ViewZoomtofit2
    swModel.ShowNamedView2 "*Dimetric", 9
```

```
    'Insert dome feature
    status = swModelDocExt.SelectByID2("", "FACE", -9.30732824141103E-02, 2.99999999999727E-02, -4.82299571224303E-02, True, 0, Nothing, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("", "FACE", -9.30732824141103E-02, 2.99999999999727E-02, -4.82299571224303E-02, False, 1, Nothing, 0)
    swModel.InsertDome 0.01, False, True
```

```
    'Get and modify dome feature data
    status = swModelDocExt.SelectByID2("Dome1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swDomeFeatureData = swFeature.GetDefinition
    status = swDomeFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print "Is dome feature elliptical? " & swDomeFeatureData.Elliptical
        Debug.Print "Height of dome: " & swDomeFeatureData.Height
        Debug.Print "Number of faces on dome feature: " & swDomeFeatureData.GetFaceCount
        faces = swDomeFeatureData.faces
        For Each aFace In faces
            Set swFace = aFace
            Set oneBody = swFace.GetBody
            Debug.Print "Name of body for this dome feature face: " & oneBody.Name
        Next
        'Change direction of dome feature to concave
        swDomeFeatureData.ReverseDir = True
```

```
   status = swFeature.ModifyDefinition(swDomeFeatureData, swModel, Nothing)
```

```
End Sub
```
