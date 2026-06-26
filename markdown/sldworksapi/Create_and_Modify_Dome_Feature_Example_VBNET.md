---
title: "Create and Modify Dome Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Modify_Dome_Feature_Example_VBNET.htm"
---

# Create and Modify Dome Feature Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchMgr As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swFeature As Feature
        Dim swSelectionMgr As SelectionMgr
        Dim swDomeFeatureData As DomeFeatureData2
        Dim faces() As Object
        Dim aFace As Object
        Dim swFace As Face2
        Dim oneBody As Body2
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        'Open model document to which to add a dome feature
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Open sketch to which to add a sketch of an ellipse
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        swModel.EditSketch()
        swModel.ClearSelection2(True)

        'Sketch an ellipse
        swModel.ShowNamedView2("*Top", 5)
        swSketchMgr = swModel.SketchManager
        swSketchSegment = swSketchMgr.CreateEllipse(-0.0761501034873036, 0.0490523248480422, 0, -0.0513492425103863, 0.0490523248480422, 0, -0.0761501034873036, 0.0545451329838695, 0)
        swModel.ClearSelection2(True)
        swSketchMgr.InsertSketch(True)
        swModel.ViewZoomtofit2()
        swModel.ShowNamedView2("*Dimetric", 9)

        'Insert dome feature
        status = swModelDocExt.SelectByID2("", "FACE", -0.0930732824141103, 0.0299999999999727, -0.0482299571224303, True, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("", "FACE", -0.0930732824141103, 0.0299999999999727, -0.0482299571224303, False, 1, Nothing, 0)
        swModel.InsertDome(0.01, False, True)

        'Get and modify dome feature data
        status = swModelDocExt.SelectByID2("Dome1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swDomeFeatureData = swFeature.GetDefinition
        status = swDomeFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("Is dome feature elliptical? " & swDomeFeatureData.Elliptical)
        Debug.Print("Height of dome: " & swDomeFeatureData.Height)
        Debug.Print("Number of faces on dome feature: " & swDomeFeatureData.GetFaceCount)
        faces = swDomeFeatureData.Faces
        For Each aFace In faces
            swFace = aFace
            oneBody = swFace.GetBody
            Debug.Print("Name of body for this dome feature face: " & oneBody.Name)
        Next
        'Change direction of dome feature to concave
        swDomeFeatureData.ReverseDir = True
        status = swFeature.ModifyDefinition(swDomeFeatureData, swModel, Nothing)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
