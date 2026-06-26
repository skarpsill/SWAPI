---
title: "Insert and Access Fold Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Access_Fold_Feature_Example_VB.htm"
---

# Insert and Access Fold Feature Example (VBA)

This example shows how to insert and access a fold feature.

```
'---------------------------------------------------------------
' Postconditions:
' 1. Verify that the specified sheet metal part document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified sheet metal part document.
' 2. Creates an unfold feature.
' 3. Creates a fold feature.
' 4. Prints to the Immediate window some fold feature data.
' 5. Examine the FeatureManager design tree and the Immediate window.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'---------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeature As SldWorks.Feature
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFoldsFeatureData As SldWorks.FoldsFeatureData
Dim swFace As SldWorks.Face2
Dim swBody As SldWorks.Body2
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim i As Long
Dim bendsArray As Variant
```

```
Sub main()

    Set swApp = Application.SldWorks
```

```
    'Open sheet metal part
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\2012-sm.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Insert unfold feature
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("", "FACE", 1.35437392197275E-02, 0.013831948116092, 1.80159642212061E-02, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("EdgeBend3", "BODYFEATURE", 1.39765211971223E-02, 0.045779599797811, -0.018375967305019, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("EdgeBend4", "BODYFEATURE", 1.45403568253926E-02, 4.61305825900808E-02, -8.49880301666417E-03, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("EdgeBend5", "BODYFEATURE", 0.013808065447904, 4.55785871991452E-02, 1.09703538056465E-02, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("EdgeBend6", "BODYFEATURE", 1.39037479688966E-02, 4.57015473971296E-02, 2.75647689667267E-02, True, 0, Nothing, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("", "FACE", 1.35437392197275E-02, 0.013831948116092, 1.80159642212061E-02, False, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("EdgeBend3", "BODYFEATURE", 1.39765211971223E-02, 0.045779599797811, -0.018375967305019, True, 4, Nothing, 0)
    status = swModelDocExt.SelectByID2("EdgeBend4", "BODYFEATURE", 1.45403568253926E-02, 4.61305825900808E-02, -8.49880301666417E-03, True, 4, Nothing, 0)
    status = swModelDocExt.SelectByID2("EdgeBend5", "BODYFEATURE", 0.013808065447904, 4.55785871991452E-02, 1.09703538056465E-02, True, 4, Nothing, 0)
    status = swModelDocExt.SelectByID2("EdgeBend6", "BODYFEATURE", 1.39037479688966E-02, 4.57015473971296E-02, 2.75647689667267E-02, True, 4, Nothing, 0)
    swModel.InsertSheetMetalUnfold
```

```
    'Insert fold feature
    status = swModelDocExt.SelectByID2("", "FACE", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("EdgeBend3", "BODYFEATURE", 1.35437392197559E-02, 4.60611937937756E-02, -0.019419982567797, True, 0, Nothing, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Unfold1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", 0, 0, 0, True, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("EdgeBend3", "BODYFEATURE", 1.35437392197559E-02, 4.60611937937756E-02, -0.019419982567797, True, 4, Nothing, 0)
    swModel.InsertSheetMetalFold
```

```
    'Access the fold feature
    status = swModelDocExt.SelectByID2("Fold1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swFoldsFeatureData = swFeature.GetDefinition
    status = swFoldsFeatureData.AccessSelections(swModel, Nothing)
    'Get name of fixed face body in the fold feature
    Set swFace = swFoldsFeatureData.FixedFace
    Set swBody = swFace.GetBody
    Debug.Print "Name of the body of the fixed face of the fold feature: " & swBody.Name
    'Get the names bend features in the fold feature
    bendsArray = swFoldsFeatureData.Bends
    For i = 0 To UBound(bendsArray)
        Set swFeature = bendsArray(i)
        Debug.Print "Name of bend feature" & i + 1 & " of the fold feature: " & swFeature.Name
    Next i
    'Release selection access
    swFoldsFeatureData.ReleaseSelectionAccess
```

```
End Sub
```
