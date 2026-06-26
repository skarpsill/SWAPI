---
title: "Toggle Display of Surface Curvatures Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Toggle_Display_of_Surface_Curvatures_Example_VB.htm"
---

# Toggle Display of Surface Curvatures Example (VBA)

This example shows how to toggle the display of surface curvatures.

```
'------------------------------------
' Preconditions: Open a part.
'
' Postconditions:
' 1. Turns the display of the surface
'    curvatures on if off or off if on.
' 2. Examine the graphics area.
'-------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    swModel.ViewDisplayCurvature
```

```
End Sub
```
