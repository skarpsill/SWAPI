---
title: "Get Whether Feature is Frozen Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Whether_Feature_is_Locked_Example_VB.htm"
---

# Get Whether Feature is Frozen Example (VBA)

This example shows how to get whether a feature is frozen.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part or assembly.
 ' 2. Select a frozen feature in the FeatureManager design tree.
 '
 ' Postconditions: Inspect the Immediate Window.
 '------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swFeat                  As SldWorks.Feature
     Dim bRet                    As Boolean
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    bRet = swFeat.IsFrozen
     Debug.Print "Feature is frozen? " & bRet
End Sub
```
