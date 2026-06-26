---
title: "Display Hidden Lines Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Hidden_Lines_Example_VB.htm"
---

# Display Hidden Lines Example (VBA)

This example shows how to set the display mode of a model.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document.
 ' 2. Press F5 five times, inspecting the graphics area each time.
 '
 ' Postconditions: The display mode settings for the document are modified
 ' as specified.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                           As SldWorks.SldWorks
     Dim swModel                         As SldWorks.ModelDoc2
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc

    ' Make hidden lines visible
     swModel.ViewDisplayHiddengreyed
     Stop
     ' Display shaded
     swModel.ViewDisplayShaded
     Stop
     ' Remove hidden lines
     swModel.ViewDisplayHiddenremoved
     Stop
     ' Display as wireframe
     swModel.ViewDisplayWireframe
     Stop
     ' Toggle display of surface curvature
     swModel.ViewDisplayCurvature
     Stop
     ' Display the facets of the shaded model
     swModel.ViewDisplayFaceted
End Sub
```
