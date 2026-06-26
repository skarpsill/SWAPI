---
title: "Insert Column in BOM Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Column_in_BOM_Table_Example_VB.htm"
---

# Insert Column in BOM Table Example (VBA)

This example shows how to insert a part number column in a BOM table.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a drawing that contains a BOM table.
' 2. Right-click the BOM table, select Select,
'    and select Table.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Inserts a part number column at the end of the
'    the BOM table.
' 2. Examine the BOM table and Immediate window.
'---------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim boolstatus As Boolean
Dim SelMgr As Object
Dim theTableAnnotation As SldWorks.TableAnnotation
Dim SelObjType As Long
Dim TableAnnotationType As Long

Sub DisplayTableColumnProps(theTableAnnotation As Object)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim ColCount As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim i As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim ColType As swTableColumnTypes_e
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim ColTitle As String

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Col#"; vbTab; "Type"; vbTab; "Title"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ColCount = theTableAnnotation.ColumnCount
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}For i = 0 To ColCount - 1
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ColType = theTableAnnotation.GetColumnType2(i, True)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ColTitle = theTableAnnotation.GetColumnTitle2(i, True)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print i; vbTab; ColType; vbTab; ColTitle
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Next i

End Sub

Sub main()

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swApp = Application.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set SelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SelObjType = SelMgr.GetSelectedObjectType3(1, -1)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If SelObjType <> swSelANNOTATIONTABLES Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox "Select a BOM table in the drawing before running this example."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set theTableAnnotation = SelMgr.GetSelectedObject6(1, -1)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}TableAnnotationType = theTableAnnotation.Type
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If TableAnnotationType <> swTableAnnotation_BillOfMaterials Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox "Select a BOM table in the drawing before running this example."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Table before inserting a column..."
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Display table before inserting a column
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}DisplayTableColumnProps theTableAnnotation
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Insert new column
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = theTableAnnotation.InsertColumn2(swTableItemInsertPosition_Last, 0, "New Column", swInsertColumn_DefaultWidth)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = theTableAnnotation.SetColumnType2(theTableAnnotation.ColumnCount - 1, swBomTableColumnType_PartNumber, True)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print " "
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Table after inserting a column..."
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Display table after inserting a column
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}DisplayTableColumnProps theTableAnnotation

End Sub
```
