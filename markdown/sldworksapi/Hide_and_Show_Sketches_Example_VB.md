---
title: "Hide and Show Sketches Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_and_Show_Sketches_Example_VB.htm"
---

# Hide and Show Sketches Example (VBA)

This example shows how to hide and show sketches in a model.

```
'---------------------------------------
' Preconditions:
' 1. Open a new part document.
' 2. Create multiple sketches.
' 3. Select the sketches in the FeatureManager
'    design tree or graphics area that you want
'    to hide.
' 4. Run the macro.
'
' Postconditions:
' 1. Examine the graphics area.
'    The selected sketches are hidden.
' 2. Select the same sketches in the FeatureManager
'    design tree, and press F5.
' 3. Examine the graphics area to verify that
'    the sketches are visible.
'--------------------------------------
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
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
```

```
    ' Hide the selected sketches
    swModel.BlankSketch
```

```
    Stop
    ' Press F5
```

```
    ' Select the just hidden sketches in the
    ' FeatureManager design tree and show them
    swModel.UnblankSketch
```

```
End Sub
```
