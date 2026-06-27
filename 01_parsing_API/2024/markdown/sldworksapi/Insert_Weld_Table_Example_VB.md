---
title: "Insert Weld Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weld_Table_Example_VB.htm"
---

# Insert Weld Table Example (VBA)

This example shows how to insert a weld table into a drawing view.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open the drawing of a part that contains a weld bead.
' 2. Verify that install_dir\lang\english\weldtable-standard.sldwldtbt exists.
'
' Postconditions:
' 1. Inserts a weld table.
' 2. Examine the drawing and the FeatureManager design tree.
' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
Dim Draw As SldWorks.DrawingDoc
Dim swActiveView As SldWorks.View
Dim boolstatus As Boolean
```

```
Option Explicit
Const WeldTableTemplate As String = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\weldtable-standard.sldwldtbt"
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set Draw = swApp.ActiveDoc
    boolstatus = Draw.Extension.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
    boolstatus = Draw.ActivateView("Drawing View1")
```

```
    Set swActiveView = Draw.ActiveDrawingView
    Dim boolResult As Boolean
    boolResult = swActiveView.InsertWeldTable(False, True, False, 0#, 0#, swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_BottomLeft, "Default", WeldTableTemplate)
```

```
End Sub
```
