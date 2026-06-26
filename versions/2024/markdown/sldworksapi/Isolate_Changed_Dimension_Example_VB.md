---
title: "Isolate Changed Dimension Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Isolate_Changed_Dimension_Example_VB.htm"
---

# Isolate Changed Dimension Example (VBA)

This example shows how to isolate a changed dimension.

```
'------------------------------------------------------
' Preconditions: Verify that the specified drawing and part
' documents exist.
'
' Postconditions:
' 1. Opens the drawing document.
' 2. Sets the system option to display
'    changed dimensions in the color selected
'    for Tools > Options > System Options >
'    Colors > Color scheme settings >
'    Drawings, Changed dimensions.
' 3. Saves and closes the drawing document.
' 4. Opens the part document of the drawing document.
' 5. Changes a dimension.
' 6. Saves and closes the part document.
' 7. Opens the previously saved drawing document.
' 8. Examine the drawing document to verify that
'    the changed dimension is displayed in the
'    changed-dimension colors. Place your cursor over
'    the dimension to see its previous value.
'-------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDrawing As SldWorks.DrawingDoc
Dim fileName As String
Dim saveFileName As String
Dim errors As Long
Dim warnings As Long
Dim status As Boolean
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
```

```
' Open drawing document
fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.slddrw"
Set swModel = swApp.OpenDoc6(fileName, swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings)
```

```
' Isolate changed dimensions
' Equivalent to selecting Tools > Options > System Options > Colors >
' Use specified color for changed drawing dimensions on open
swApp.SetUserPreferenceToggle swUserPreferenceToggle_e.swUseChangedDimensions, True
Set swDrawing = swModel
swDrawing.IsolateChangedDimensions
```

```
' Save drawing document to another name
saveFileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box_changed.slddrw"
Set swModelDocExt = swModel.Extension
status = swModelDocExt.SaveAs(saveFileName, swSaveAsCurrentVersion, swSaveAsOptions_Silent, Nothing, errors, warnings)
swApp.CloseDoc (saveFileName)
```

```
' Open the part document referenced by the drawing document,
' change a dimension, and save the document
fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt"
Set swModel = swApp.OpenDoc6(fileName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
Set swModelDocExt = swModel.Extension
status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
status = swModelDocExt.SelectByID2("D2@Sketch1@box.SLDPRT", "DIMENSION", -0.03613329319351, -0.02215939491444, 0.02938582119709, True, 0, Nothing, 0)
Dim swDimension As SldWorks.Dimension
Set swDimension = swModel.Parameter("D2@Sketch1")
swDimension.SystemValue = 0.185
swModel.ClearSelection2 True
status = swModel.EditRebuild3()
status = swModel.Save3(swSaveAsOptions_Silent, errors, warnings)
swApp.CloseDoc (fileName)
```

```
' Open the previously saved drawing document
' and place your cursor on the changed dimension,
' which displays in the color specified for
' changed dimensions, to see its previous value
Set swModel = swApp.OpenDoc6(saveFileName, swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings)
```

```
End Sub
```
