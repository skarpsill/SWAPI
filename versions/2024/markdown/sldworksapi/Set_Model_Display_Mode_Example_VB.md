---
title: "Set Model Display Mode Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Model_Display_Mode_Example_VB.htm"
---

# Set Model Display Mode Example (VBA)

This example shows how to set the display mode of a model view.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open a part or assembly document.
' 2. Start up a ray-trace rendering engine.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Sets the model view display to integrated preview.
' 2. Examine the graphics area and Immediate window.
'---------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Const nNewDispMode As Long = swViewDisplayMode_e.swViewDisplayMode_IntegratedPreview
```

```
    Dim swApp As SldWorks.SldWorks
   Dim swModel As SldWorks.ModelDoc2
   Dim swModVie As SldWorks.ModelView
```

```
    Set swApp = Application.SldWorks
   Set swModel = swApp.ActiveDoc
   Set swModView = swModel.ActiveView
```

```
    swModView.DisplayMode = nNewDispMode
```

```
    Debug.Print "File = " & swModel.GetPathName
   Debug.Print "  Display mode (swViewDisplayMode_e.swViewDisplayMode_IntegratedPreview = 13): " & swModView.DisplayMode
```

```
End Sub
```
