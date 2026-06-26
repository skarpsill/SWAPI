---
title: "Get Surface Trim Feature Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Surface_Trim_Feature_Data_Example_VB.htm"
---

# Get Surface Trim Feature Data Example (VBA)

This example shows how to get surface trim feature data.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open a part document with a surface trim feature.
' 2. Select the surface trim feature.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the type of surface trim feature.
' 2. Examine the Immediate window.
'---------------------------------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swFeat As SldWorks.Feature
 Dim swSurfTrimFeat As SldWorks.SurfaceTrimFeatureData
 Dim surftrimtype As Long
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swSurfTrimFeat = swFeat.GetDefinition

    surftrimtype = swSurfTrimFeat.GetType
     Debug.Print "Surface trim type (swSurfaceTrimType_e): " & surftrimtype
End Sub
```
