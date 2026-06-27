---
title: "Insert Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Table_Example_VB.htm"
---

# Insert Table Example (VBA)

This example shows how to insert a table into a drawing.

```
'-------------------------------------------
' Preconditions:
' 1. Open a drawing.
' 2. Select a drawing view.
'
' Postconditions: Inserts the table.
'-------------------------------------------
```

```
Option Explicit
```

```
Public Enum swBOMConfigurationAnchorType_e
    swBOMConfigurationAnchor_TopLeft = 1
    swBOMConfigurationAnchor_TopRight = 2
    swBOMConfigurationAnchor_BottomLeft = 3
    swBOMConfigurationAnchor_BottomRight = 4
End Enum
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swDraw As SldWorks.DrawingDoc
    Dim swTable As SldWorks.TableAnnotation
    Dim vPickPt As Variant
    Dim nNumCol As Long
    Dim nNumRow As Long
    Dim sRowStr As String
    Dim i As Long
    Dim j As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swSelMgr = swModel.SelectionManager
    vPickPt = swSelMgr.GetSelectionPoint(1)
    Set swTable = swDraw.InsertTableAnnotation(vPickPt(0), vPickPt(1), swBOMConfigurationAnchor_TopLeft, 6, 5)
    nNumCol = swTable.ColumnCount
    nNumRow = swTable.RowCount
    For i = 0 To nNumRow
        For j = 0 To nNumCol
            swTable.Text(i, j) = "[" & i & ", " & j & "]"
        Next j
    Next i
```

```
End Sub
```
