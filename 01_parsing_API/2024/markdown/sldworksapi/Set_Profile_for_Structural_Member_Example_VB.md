---
title: "Set Profile for Structural Member Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Profile_for_Structural_Member_Example_VB.htm"
---

# Set Profile for Structural Member Example (VBA)

This example shows how to set the profile for a structural member.

```
'-------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
' 2. Verify that the path specified for the weldment profile
'    exists.
' 3. Right-click Structural Member1, select Edit Feature,
'    examine Selections, and click OK.
'
' Postconditions:
' 1. Changes the weldment profile to the specified weldment
'    profile.
' 2. To verify step 1, right-click StructuralMember1, select
'    Edit Feature, examine Selections, and click OK.
'
' NOTE: Because the part is used elsewhere, do  not save
' changes.
'--------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swWeldFeat As SldWorks.Feature
Dim swWeldFeatData As SldWorks.StructuralMemberFeatureData
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
    boolstatus = swModelDocExt.SelectByID2("Structural Member1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swWeldFeat = swSelMgr.GetSelectedObject6(1, 0)
    Set swWeldFeatData = swWeldFeat.GetDefinition
    swWeldFeatData.AccessSelections swModel, Nothing
    swWeldFeatData.WeldmentProfilePath = "C:\Program Files\SolidWorks Corp\SolidWorks\lang\english\weldment profiles\iso\pipe\26.9 x 3.2.sldlfp"
    boolstatus = swWeldFeat.ModifyDefinition(swWeldFeatData, swModel, Nothing)
```

```
End Sub
```
