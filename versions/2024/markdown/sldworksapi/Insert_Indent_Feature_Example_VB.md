---
title: "Insert Indent Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Indent_Feature_Example_VB.htm"
---

# Insert Indent Feature Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swIndentFeatureData As SldWorks.IndentFeatureData
Dim targetBody As SldWorks.Body2
Dim swFace As SldWorks.Face2
Dim toolRegionBody As SldWorks.Body2
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim toolBodyRegions As Variant
Dim toolBodyRegionType As Long
Dim nbrBodies As Long
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open part where to insert indent feature
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Select solid body for target body,
    'select face for tool body region, and
    'and insert indent feature
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, False, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", -3.71343422566497E-02, -1.49999999999864E-02, 8.83053842352979E-02, True, 4, Nothing, 0)
    Set swFeatureMgr = swModel.FeatureManager
    Set swFeature = swFeatureMgr.InsertIndent(0.01, 0, True, True, False, False)
```

```
    'Access and modify indent feature
    Debug.Print "Indent feature name: " & swFeature.Name
    Set swIndentFeatureData = swFeature.GetDefinition
    swIndentFeatureData.AccessSelections swModel, Nothing
    nbrBodies = swIndentFeatureData.GetBodiesCount
    Debug.Print "  Number of bodies: " & nbrBodies
    Set targetBody = swIndentFeatureData.targetBody
    Debug.Print "  Name of target body: " & targetBody.Name
    toolBodyRegions = swIndentFeatureData.toolBodyRegion
    Debug.Print "  Number of tool body regions: " & UBound(toolBodyRegions) + 1
    For i = 0 To nbrBodies - 1
        swModel.ClearSelection2 True
        Set swSelectionMgr = swModel.SelectionManager
        status = swSelectionMgr.AddSelectionListObject(toolBodyRegions(i), Nothing)
        toolBodyRegionType = swSelectionMgr.GetSelectedObjectType3(1, -1)
        Debug.Print "  Type of object selected for tool body region (2 = face; 3 = vertex): " & toolBodyRegionType
        'If object selected for tool body region is a face,
        'then get the name of its body
        If toolBodyRegionType = 2 Then
            Set swFace = toolBodyRegions(i)
            Set toolRegionBody = swFace.GetBody
            Debug.Print "  Name of body of tool body region: " & toolRegionBody.Name
        End If
    Next i
    Debug.Print "  Original thickness: " & swIndentFeatureData.Thickness
    'Change thickness
    swIndentFeatureData.Thickness = 0.011
    Debug.Print "  Modified thickness: " & swIndentFeatureData.Thickness
    status = swFeature.ModifyDefinition(swIndentFeatureData, swModel, Nothing)
```

```
End Sub
```
