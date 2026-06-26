---
title: "Roll Model View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Roll_Model_View_Example_VB.htm"
---

# Roll Model View Example (VBA)

This example shows how to roll a model view by a specified angle.

```
'---------------------------------
' Preconditions: Open a part or assembly.
'
' Postconditions:
' 1. Rolls the model view 90 degrees.
' 2. Examine the graphics area.
'---------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelView As SldWorks.ModelView
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelView = swModel.ActiveView
```

```
    ' Roll the model view by 90 degrees
    swModelView.RollBy (90#)
```

```
End Sub
```
