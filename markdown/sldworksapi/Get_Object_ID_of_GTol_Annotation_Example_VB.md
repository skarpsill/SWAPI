---
title: "Get Object ID of GTol Annotation Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Object_ID_of_GTol_Annotation_Example_VB.htm"
---

# Get Object ID of GTol Annotation Example (VBA)

This example shows how to get the object ID of a GTol annotation.

```
'---------------------------------------------
' Preconditions:
' 1. Verify that the drawing to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing.
' 2. Selects the GTol annotation.
' 3. Gets the type of annotation selected.
' 4. Gets the selected GTol annotation's object ID.
' 5. Examine the Immediate window.
'--------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawing As SldWorks.DrawingDoc
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swGTol As SldWorks.Gtol
Dim swGTolAnnotation As SldWorks.Annotation
Dim status As Boolean
Dim errors As Long, warnings As Long
Dim id As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open the drawing
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\gtolwitnessline.slddrw", 3, 0, "", errors, warnings)
    Set swDrawing = swModel
```

```
    'Select GTol
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("DetailItem40@Drawing View3", "GTOL", 0.44609485235144, 0.381203477032446, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swGTol = swSelectionMgr.GetSelectedObject6(1, -1)
```

```
    'Print type of annotation and its object ID
    Set swGTolAnnotation = swGTol.GetAnnotation
    Debug.Print "Annotation type: " & swGTolAnnotation.GetType
    id = swModelDocExt.GetObjectId(swGTolAnnotation)
    Debug.Print "ID = " & id
```

```
End Sub
```
