---
title: "Get Transform of Plane Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Transform_of_Plane_Example_VB.htm"
---

# Get Transform of Plane Example (VBA)

This example shows how to get the transform of a plane.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open a part that has a reference plane.
' 2. Select the reference plane.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the transform of the selected reference plane.
' 2. Examine the Immediate window.
'
' NOTE: Transform is from model origin to reference plane origin.
'------------------------------------------------------------------
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
    Dim swRefPlane As SldWorks.RefPlane
    Dim swXform As SldWorks.MathTransform
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Set swRefPlane = swFeat.GetSpecificFeature2
    Set swXform = swRefPlane.Transform
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Plane = " & swFeat.Name
    Debug.Print "    Origin = (" & -1# * swXform.ArrayData(9) * 1000# & ", " & -1# * swXform.ArrayData(10) * 1000# & ", " & -1# * swXform.ArrayData(11) * 1000# & ") mm"
    Debug.Print "    Rot1   = (" & swXform.ArrayData(0) & ", " & swXform.ArrayData(1) & ", " & swXform.ArrayData(2) & ")"
    Debug.Print "    Rot2   = (" & swXform.ArrayData(3) & ", " & swXform.ArrayData(4) & ", " & swXform.ArrayData(5) & ")"
    Debug.Print "    Rot3   = (" & swXform.ArrayData(6) & ", " & swXform.ArrayData(7) & ", " & swXform.ArrayData(8) & ")"
    Debug.Print "    Trans  = (" & swXform.ArrayData(9) * 1000# & ", " & swXform.ArrayData(10) * 1000# & ", " & swXform.ArrayData(11) * 1000# & ") mm"
    Debug.Print "    Scale  = " & swXform.ArrayData(12)
```

```
End Sub
```
