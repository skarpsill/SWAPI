---
title: "Get Table Anchor Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Table_Anchor_Example_VB.htm"
---

# Get Table Anchor Example (VBA)

This example shows how to get the anchor for a selected bill of materials table.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing document that has a bill of materials.
 ' 2. Expand the Sheet Format node in the FeatureManager design tree and
 '    select the bill of materials anchor feature.
 '
 ' Postconditions: Inspect the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swFeat As SldWorks.Feature
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swTableAnchor As SldWorks.TableAnchor
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, 0)
     Set swTableAnchor = swFeat.GetSpecificFeature2

    ' Type of table anchor as defined in swTableAnnotationType_e
     Debug.Print "Type of table anchor = " & swTableAnchor.Type

End Sub
```
