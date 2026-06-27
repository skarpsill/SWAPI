---
title: "Redraw Graphics Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Redraw_Graphics_Example_VB.htm"
---

# Redraw Graphics Example (VBA)

This example shows how to redraw the graphics area.

```
'-----------------------------------------------
' Preconditions: Open a model document.
'
' Postconditions: Redraws the graphics area.
'------------------------------------------------
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
    swModel.GraphicsRedraw2
```

```
End Sub
```
