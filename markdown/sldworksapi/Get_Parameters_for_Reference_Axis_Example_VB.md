---
title: "Get Parameters for Reference Axis Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Parameters_for_Reference_Axis_Example_VB.htm"
---

# Get Parameters for Reference Axis Example (VBA)

## Get Parameters of Reference Axis Example (VBA)

This example shows how to get the parameters of a reference axis.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a part, assembly, or drawing that
'    contains a reference axis feature.
' 2. Select the reference axis feature.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the parameters of the selected
'    reference axis feature.
' 2. Examine the Immediate window.
'-----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swRefAxis As SldWorks.RefAxis
    Dim vAxisParam As Variant
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Set swRefAxis = swFeat.GetSpecificFeature2
```

```
    vAxisParam = swRefAxis.GetRefAxisParams
```

```
    Debug.Print "Name = " & swFeat.Name
    Debug.Print "  Start    = (" & vAxisParam(0) * 1000 & ", " & vAxisParam(1) * 1000 & ", " & vAxisParam(2) * 1000 & ") mm"
    Debug.Print "  End      = (" & vAxisParam(3) * 1000 & ", " & vAxisParam(4) * 1000 & ", " & vAxisParam(5) * 1000 & ") mm"

End Sub
```
