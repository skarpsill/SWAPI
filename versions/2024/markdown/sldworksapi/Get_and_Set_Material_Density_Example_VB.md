---
title: "Get and Set Material Density Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Material_Density_Example_VB.htm"
---

# Get and Set Material Density Example (VBA)

This example shows how to get and set the material density for a part.

```
'------------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets and sets the part's density.
' 2. Examine the Immediate window.
'------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim nDensity As Double
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    Debug.Print "File   = " + swModel.GetPathName
```

```
    ' Density is returned in metric units, i.e., kg/m^3
    nDensity = swModel.GetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swMaterialPropertyDensity)
    Debug.Print "  Get current density = " & nDensity & " kg/m^3"
```

```
    swModel.SetUserPreferenceDoubleValue swMaterialPropertyDensity, nDensity / 2#
    nDensity = swModel.GetUserPreferenceDoubleValue(swUserPreferenceDoubleValue_e.swMaterialPropertyDensity)
    Debug.Print "  Set new density = " & nDensity & " kg/m^3"
```

```
End Sub
```
