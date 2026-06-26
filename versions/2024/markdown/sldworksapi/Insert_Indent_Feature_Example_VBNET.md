---
title: "Insert Indent Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Indent_Feature_Example_VBNET.htm"
---

# Insert Indent Feature Example (VB.NET)

This example shows how to insert and modify an indent feature.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part.
' 2. Selects the boss-extrude body and a face on the
'    extrude-thin body.
' 3. Inserts an indent feature.
' 4. Modifies the thickness of the indent feature.
' 5. Examine the Immediate window, FeatureManager design tree,
'    and graphics area.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatureMgr As FeatureManager
        Dim swSelectionMgr As SelectionMgr
        Dim swFeature As Feature
        Dim swIndentFeatureData As IndentFeatureData
        Dim targetBody As Body2
        Dim swFace As Face2
        Dim toolRegionBody As Body2
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim toolBodyRegions() As Object
        Dim toolBodyRegionType As Integer
        Dim nbrBodies As Integer
        Dim i As Integer

        'Open part where to insert indent feature
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Select solid body for target body,
        'select face for tool body region, and
        'and insert indent feature
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", -0.0371343422566497, -0.0149999999999864, 0.0883053842352979, True, 4, Nothing, 0)
        swFeatureMgr = swModel.FeatureManager
        swFeature = swFeatureMgr.InsertIndent(0.01, 0, True, True, False, False)

        'Access and modify indent feature
        Debug.Print("Indent feature name: " & swFeature.Name)
        swIndentFeatureData = swFeature.GetDefinition
        swIndentFeatureData.AccessSelections(swModel, Nothing)
        nbrBodies = swIndentFeatureData.GetBodiesCount
        Debug.Print("  Number of bodies: " & nbrBodies)
        targetBody = swIndentFeatureData.TargetBody
        Debug.Print("  Name of target body: " & targetBody.Name)
        toolBodyRegions = swIndentFeatureData.ToolBodyRegion
        Debug.Print("  Number of tool body regions: " & UBound(toolBodyRegions) + 1)
        For i = 0 To nbrBodies - 1
            swModel.ClearSelection2(True)
            swSelectionMgr = swModel.SelectionManager
            status = swSelectionMgr.AddSelectionListObject(toolBodyRegions(i), Nothing)
            toolBodyRegionType = swSelectionMgr.GetSelectedObjectType3(1, -1)
            Debug.Print("  Type of object selected for tool body region (2 = face; 3 = vertex): " & toolBodyRegionType)
            'If object selected for tool body region is a face,
            'then get the name of its body
            If toolBodyRegionType = 2 Then
                swFace = toolBodyRegions(i)
                toolRegionBody = swFace.GetBody
                Debug.Print("  Name of body of tool body region: " & toolRegionBody.Name)
            End If
        Next i
        Debug.Print("  Original thickness: " & swIndentFeatureData.Thickness)
        'Change thickness
        swIndentFeatureData.Thickness = 0.011
        Debug.Print("  Modified thickness: " & swIndentFeatureData.Thickness)
        status = swFeature.ModifyDefinition(swIndentFeatureData, swModel, Nothing)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
