---
title: "Get Fixed Face of Flatten-Bends Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Fixed_Face_of_Flatten-Bends_Feature_Example_VB.htm"
---

# Get Fixed Face of Flatten-Bends Feature Example (VBA)

This example shows how to get the fixed face of a flatten-bends feature.

```vb
 '------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a sheet metal part.
 ' 2. Select a Process-Bends feature in the FeatureManager design
 '    tree.
 '
 ' Postconditions:
 ' 1. Rolls the FeatureManager design tree back to the feature
 '    that contains the fixed face of the Process-Bends feature.
 ' 2. Selects the fixed face of the Process-Bends feature.
 ' 3. Examine the FeatureManager design tree and graphics area,
 '    then press F5.
 ' 4. Rolls the FeatureManager design tree forward.
 '------------------------------------------------------------------
 Option Explicit
Sub main()

     Dim swApp As SldWorks.SldWorks
     Dim swModel As SldWorks.ModelDoc2
     Dim swSelMgr As SldWorks.SelectionMgr
     Dim swFeat As SldWorks.Feature
     Dim swBends As SldWorks.BendsFeatureData
     Dim swFace As SldWorks.Face2
     Dim swEntity As SldWorks.Entity
     Dim bRet As Boolean

    Set swApp = CreateObject("SldWorks.Application")
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swBends = swFeat.GetDefinition

   ' Roll back to access the Process-Bends feature data
     bRet = swBends.AccessSelections(swModel, Nothing)
    Set swFace = swBends.GetFixedFace
     Set swEntity = swFace
     bRet = swEntity.Select4(False, Nothing)
    Stop
     ' Press F5

    ' Cancel any changes made
     swBends.ReleaseSelectionAccess
End Sub
```
