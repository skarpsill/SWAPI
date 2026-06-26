---
title: "Modify Move/Copy Body Using Vertex Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_and_Copy_Body_Using_Vertex_Example_VBNET.htm"
---

# Modify Move/Copy Body Using Vertex Example (VB.NET)

This example shows how to modify a move/copy body feature using a vertex.

```
'---------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Selects a solid body and two vertices.
' 3. Inserts a move/copy body feature and gets and sets some of its feature data.
' 4. Examine the FeatureManager design tree, the graphics area, and
'    the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatureManager As FeatureManager
        Dim swFeature As Feature
        Dim swMoveCopyBodyFeatureData As MoveCopyBodyFeatureData
        Dim swVertexFrom As Vertex
        Dim swVertexTo As Vertex
        Dim swSelectionMgr As SelectionMgr
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String

        'Open part document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        swFeatureManager = swModel.FeatureManager

        'Select solid body and vertices for move/copy body feature
        status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, 0, 0.065, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, -0.09, 0.065, True, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, 0, 0.065, True, 4, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, -0.09, 0.065, True, 8, Nothing, 0)

        'Insert move/copy body feature
        swFeature = swFeatureManager.InsertMoveCopyBody2(0, 0, 0, 0, -0.085, 0, 0.065, 0, 0, 0, True, 1)

        'Roll forward the feature and get and set move/copy body feature data
        swMoveCopyBodyFeatureData = swFeature.GetDefinition
        status = swMoveCopyBodyFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("Move/copy body feature data:")
        Debug.Print("  Number of bodies to move or rotate and copy: " & swMoveCopyBodyFeatureData.GetBodiesCount)
        Debug.Print("  Number of copies: " & swMoveCopyBodyFeatureData.NumberOfCopies)
        Debug.Print("  Transform type (0 = None, 1 = Translation, 2 = Rotation): " & swMoveCopyBodyFeatureData.TransformType)

        'Change translation vertex
        status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, -0.09, 0.065, True, 8, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swVertexFrom = swSelectionMgr.GetSelectedObject6(1, -1)
        swMoveCopyBodyFeatureData.TransformReferenceEntity = swVertexFrom
        swMoveCopyBodyFeatureData.TranslateToVertex = swVertexFrom
        status = swModelDocExt.SelectByID2("", "VERTEX", 0, -0.065, 0, False, 0, Nothing, 0)
        swVertexTo = swSelectionMgr.GetSelectedObject6(1, -1)
        swMoveCopyBodyFeatureData.TranslateToVertex = swVertexTo
        swMoveCopyBodyFeatureData.TransformX = 0.05

        'Apply the changes and roll back the feature
        swFeature.ModifyDefinition(swMoveCopyBodyFeatureData, swModel, Nothing)

        swModel.ViewZoomtofit2()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
