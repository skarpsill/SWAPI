---
title: "Copy and Paste Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_and_Paste_Feature_Example_VB.htm"
---

# Copy and Paste Feature Example (VBA)

This example shows how to copy and paste a feature in a part document.

```
'----------------------------------------------------------------
' Preconditions: Verify that the specified part document to
' open exists.
'
' Postconditions:
' 1. Displays the Copy Confirmation dialog after calling
'    IModelDoc2::Paste.
' 2. Click Delete.
' 3. Pastes the copied feature on the selected face.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim fileName As String
Dim status As Boolean
Dim errors As Long, warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\testpart1.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
```

```
    ' Select the feature to copy
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    swModel.EditCopy

    swModel.ClearSelection2 True
```

```
    ' Select the face where to paste the copied feature
    status = swModelDocExt.SelectByID2("", "FACE", 2.97472797980731E-02, 5.64587562103043E-02, 6.76585125080464E-03, False, 0, Nothing, 0)
```

```
    ' Paste the copied feature on the selected face
    swModel.Paste
```

```
    ' Displays the Copy Confirmation dialog
    ' Click Delete
    ' Pastes the copied feature on the selected face
```

```
    ' Zoom to selection, then zoom to fit
    swModel.ViewZoomToSelection
    swModel.ViewZoomtofit2
```

```
End Sub
```
