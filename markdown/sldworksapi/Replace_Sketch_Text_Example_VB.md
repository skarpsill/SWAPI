---
title: "Replace Sketch Text Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Replace_Sketch_Text_Example_VB.htm"
---

# Replace Sketch Text Example (VBA)

This example shows how to replace sketch text in a part.

```
'----------------------------------------------------
' Preconditions:
' 1. Open a part that contains sketch text.
' 2. Select the sketch that contains the sketch text.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Replaces the original sketch text with
'    new sketch text, "New text".
' 2. Examine the Immediate window and graphics area.
'----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As Object
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As SldWorks.Feature
Dim swSketch As SldWorks.Sketch
Dim swSketchText As SldWorks.SketchText
Dim params As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
```

```
    ' Get the selected feature of the sketch text
    Set swFeat = swSelMgr.GetSelectedObject6(1, 0)
    Set swSketch = swFeat.GetSpecificFeature2
```

```
    ' Edit the sketch of the sketch text
    swModel.EditSketch
```

```
    ' Get the sketch text
    params = swSketch.GetSketchTextSegments
```

```
    ' Only one instance of sketch text so
    ' set SketchText to that instance
    Set swSketchText = params(0)
```

```
    ' Print the current sketched text
    Debug.Print swSketchText.Text
```

```
    'Change the sketched text
    swSketchText.Text = "New text"
```

```
    ' Print the changed text
    Debug.Print swSketchText.Text
```

```
    ' Insert the new text in the sketch,
    ' rebuild the part with any changes
    ' made to the sketch, and
    ' exit sketch mode
    swModel.InsertSketch2 True
```

```
End Sub
```
