---
title: "Get Ruled-Surface Feature Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Ruled_Surface_Feature_Data_Example_VB.htm"
---

# Get Ruled-Surface Feature Data Example (VBA)

This example shows how to get ruled-surface feature data.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open a part document that contains a ruled-surface feature.
' 2. Select the ruled-surface feature.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the type of ruled-surface feature.
' 2. Examine the Immediate window.
'------------------------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swFeat As SldWorks.Feature
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swRuledSurfFeat As SldWorks.RuledSurfaceFeatureData
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc

    Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swRuledSurfFeat = swFeat.GetDefinition
    ' Ruled-surface feature type as defined in swRuledSurfaceType_e
     Debug.Print "Ruled-surface feature type: " & swRuledSurfFeat.Type
End Sub
```
