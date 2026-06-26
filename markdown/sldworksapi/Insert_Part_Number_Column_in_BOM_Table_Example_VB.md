---
title: "Insert Part Number Column in BOM Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Part_Number_Column_in_BOM_Table_Example_VB.htm"
---

# Insert Part Number Column in BOM Table Example (VBA)

This example shows how to insert a part number column in a BOM table.

```
'----------------------------------------------------
' Preconditions:
' 1. Open a drawing with a BOM table.
' 2. Right-click the BOM table, select Select,
'    and select Table.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Inserts a  part number column at the end of the
'    the BOM table.
' 2. Examine the BOM table and the Immediate window.
'----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim boolstatus As Boolean
Dim SelMgr As Object
Dim theTableAnnotation As SldWorks.TableAnnotation
Dim SelObjType As Long
Dim TableAnnotationType As Long
```

```
Sub DisplayTableColumnProps(theTableAnnotation As Object)
    Dim ColCount As Long
    Dim i As Long
    Dim ColType As swTableColumnTypes_e
    Dim ColTitle As String
```

```
    Debug.Print "Index" & vbTab & "Type" & vbTab & "Title"
    ColCount = theTableAnnotation.ColumnCount
```

```
    For i = 0 To ColCount - 1
        ColType = theTableAnnotation.GetColumnType(i)
        ColTitle = theTableAnnotation.GetColumnTitle(i)
        Debug.Print i & vbTab & ColType & vbTab & ColTitle
    Next i
```

```
End Sub
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set SelMgr = swModel.SelectionManager
```

```
    SelObjType = SelMgr.GetSelectedObjectType2(1)
```

```
    If SelObjType <> swSelectType_e.swSelANNOTATIONTABLES Then
        MsgBox "Select a BOM table in the drawing before running this macro."
        End
    End If
```

```
    Set theTableAnnotation = SelMgr.GetSelectedObject6(1, -1)
    TableAnnotationType = theTableAnnotation.Type
    If TableAnnotationType <> swTableAnnotationType_e.swTableAnnotation_BillOfMaterials Then
        MsgBox "Select a BOM table in the drawing before running this example."
        End
    End If
```

```
    DisplayTableColumnProps theTableAnnotation
```

```
    boolstatus = theTableAnnotation.InsertColumn(swTableItemInsertPosition_e.swTableItemInsertPosition_Last, 0, "New Column")
    boolstatus = theTableAnnotation.SetColumnType(theTableAnnotation.ColumnCount - 1, swTableColumnTypes_e.swBomTableColumnType_PartNumber)
```

```
    DisplayTableColumnProps theTableAnnotation
```

```
End Sub
```
