---
title: "Get Depth of Extrusion Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Depth_of_Extrusion_Example_VB.htm"
---

# Get Depth of Extrusion Example (VBA)

This example shows how to get the depth of an extrusion.

```
'------------------------------------------------------------
' Preconditions:
' 1. Open a part containing a Boss-Extrude1 feature.
' 2. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'------------------------------------------------------------
Option Explicit
```

```vb
Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim swModel As SldWorks.ModelDoc2
     Dim swDim As SldWorks.Dimension
     Dim vConfigNames As Variant
     Dim vValue As Variant
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swDim = swModel.Parameter("D1@Boss-Extrude1")
    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "  Full name = " & swDim.FullName
     Debug.Print "  Name = " & swDim.Name
    vConfigNames = swModel.GetConfigurationNames
     vValue = swDim.GetSystemValue3(swThisConfiguration, (vConfigNames))
    Debug.Print "  System value = " & vValue(0) * 1000#; "" & " mm"
End Sub
```
