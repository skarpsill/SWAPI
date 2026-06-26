---
title: "Get Gusset Feature Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Gusset_Feature_Data_Example_VB.htm"
---

# Get Gusset Feature Data Example (VBA)

This example shows how to get some data for a gusset feature.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Selects and gets the Gusset1 feature.
' 3. Gets to some Gusset1 feature data.
' 4. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swGussetFeatureData As SldWorks.GussetFeatureData
Dim status As Boolean
Dim fileName As String
Dim errors As Long
Dim warnings As Long
Dim oneFace As SldWorks.face2
Dim twoFace As SldWorks.face2

Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open part document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\weldment_box3.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Select and get Gusset1
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Gusset1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swGussetFeatureData = swFeature.GetDefinition
```

```
    'Access Gusset1 and get some feature data
    swGussetFeatureData.AccessSelections swModel, Nothing
    Debug.Print "Profile type: " & swGussetFeatureData.ProfileType
    Debug.Print "Thickness type: " & swGussetFeatureData.ThicknessType
    Debug.Print "Thickness: " & swGussetFeatureData.Thickness
    If swGussetFeatureData.OffsetUsed = True Then
        Debug.Print "Profile offset distance: " & swGussetFeatureData.ProfileOffsetDistance
    Else
        Debug.Print "No profile offset used."
    End If
    status = swGussetFeatureData.GetSupportingFaces(oneFace, twoFace)
    status = oneFace.IsSame(twoFace)
    Debug.Print "Is the first supporting face the same as the second supporting: " & status
    swGussetFeatureData.ReleaseSelectionAccess
```

```
End Sub
```
