---
title: "Get Simple Fillet Feature Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Simple_Fillet_Feature_Data_Example_VB.htm"
---

# Get Simple Fillet Feature Data Example (VBA)

This example shows how to get simple fillet feature data.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document that contains a simple fillet feature.
 ' 2. Select the simple fillet feature.
 '
 ' Postconditions: Inspect the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swFeat As SldWorks.Feature
 Dim swFeatData As SldWorks.SimpleFilletFeatureData2
 Dim boolstatus As Boolean
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension
     Set swSelMgr = swModel.SelectionManager
    boolstatus = swModelDocExt.SelectByID2("Fillet2", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)

    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swFeatData = swFeat.GetDefinition

    Debug.Print "Edge count: " & swFeatData.GetEdgeCount
End Sub
```
