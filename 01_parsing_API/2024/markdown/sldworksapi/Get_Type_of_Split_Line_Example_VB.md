---
title: "Get Type of Split Line Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Type_of_Split_Line_Example_VB.htm"
---

# Get Type of Split Line Example (VBA)

This example shows how to get the type of split line.

```
'----------------------------------------------------------
' Preconditions:
' 1. Open a part document with a split line feature.
' 2. Select the split line feature.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the type of split line.
' 2. Examine the Immediate window.
'-----------------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swFeat As SldWorks.Feature
 Dim swSplitLineFeat As SldWorks.SplitLineFeatureData
 Dim splittype As Long
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swSplitLineFeat = swFeat.GetDefinition

    splittype = swSplitLineFeat.GetType
     Debug.Print "Split line type (swSplitLineFeatureType_e): " & splittype
End Sub
```
