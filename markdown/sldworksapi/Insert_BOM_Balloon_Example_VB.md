---
title: "Insert BOM Balloon Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_BOM_Balloon_Example_VB.htm"
---

# Insert BOM Balloon Example (VBA)

This example shows how to insert a BOM balloon.

```
'------------------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Select an edge, silhouette, face, or vertex.
'
' Postconditions:
' 1. Inserts a split-circle BOM balloon at
'    the selected object.
' 2. Examine the graphics area.
'-------------------------------------------------
Option Explicit
```

```
Sub main()
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelComp As SldWorks.Component2
    Dim sCompName As String
    Dim swNote As SldWorks.Note
    Dim swAnn As SldWorks.Annotation
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swNote = swModel.InsertBOMBalloon2(swBS_SplitCirc, swBF_Tightest, swBalloonTextCustom, "Upper text", swBalloonTextCustom, "Lower text")
```

```
End Sub
```
