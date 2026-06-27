---
title: "Edit Mate Reference Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Edit_Mate_Reference_Example_VB.htm"
---

# Edit Mate Reference Example (VBA)

This example shows how to insert and edit a mate reference.

```
'----------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Adds a mate reference.
' 3. Edits the mate reference.
' 4. Expand MateReferences in the FeatureManager design tree
'    and click MyDefault<1>.
' 5. Examine the graphics area and Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeature As SldWorks.Feature
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swPlane As SldWorks.Entity
Dim swFace As SldWorks.Face2
Dim swMateReference As SldWorks.MateReference
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
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\fillets\knob.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    'Insert mate reference
    status = swModelDocExt.SelectByID2("Front", "PLANE", 0, 0, 0, True, 1, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swPlane = swSelectionMgr.GetSelectedObject6(1, -1)
    status = swModelDocExt.SelectByID2("", "FACE", 8.35786916030656E-03, 4.29540237419701E-03, 0, True, 2, Nothing, 0)
    Set swFeatureMgr = swModel.FeatureManager
    Set swFeature = swFeatureMgr.InsertMateReference2("Default", Nothing, 0, 1, False, Nothing, 0, 2, False, Nothing, 0, 0)
    swModel.ClearSelection2 True
```

```
    'Edit mate reference
    status = swModelDocExt.SelectByID2("", "FACE", 1.17890806857872E-02, 4.19179196288511E-03, 9.99999999999091E-03, False, 0, Nothing, 0)
    Set swFace = swSelectionMgr.GetSelectedObject6(1, -1)
    status = swModelDocExt.SelectByID2("Default-<1>", "POSGROUP", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swMateReference = swFeature.GetSpecificFeature2
    swModel.ClearSelection2 True
    status = swMateReference.Edit("MyDefault", swPlane, swMateReferenceType_default, swMateReferenceAlignment_Any, swFace, swMateReferenceType_default, swMateReferenceAlignment_Any, Nothing, swMateReferenceType_default, swMateReferenceAlignment_Any)
    Debug.Print "Mate reference modified and replaced? " & status
```

```
    swModel.EditRebuild3
```

```
End Sub
```
