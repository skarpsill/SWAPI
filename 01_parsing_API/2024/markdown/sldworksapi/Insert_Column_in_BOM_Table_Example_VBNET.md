---
title: "Insert Column in BOM Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Column_in_BOM_Table_Example_VBNET.htm"
---

# Insert Column in BOM Table Example (VB.NET)

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
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim SelMgr As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim theTableAnnotation As TableAnnotation
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim SelObjType As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim TableAnnotationType As Long

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SelMgr = swModel.SelectionManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SelObjType = SelMgr.GetSelectedObjectType3(1, -1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If SelObjType <> swSelectType_e.swSelANNOTATIONTABLES Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MsgBox("Select a BOM table in the drawing before running this example.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}theTableAnnotation = SelMgr.GetSelectedObject6(1, -1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}TableAnnotationType = theTableAnnotation.Type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If TableAnnotationType <> swTableAnnotationType_e.swTableAnnotation_BillOfMaterials Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MsgBox("Select a BOM table in the drawing before running this example.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Table before inserting a column...")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Display table before inserting a column
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DisplayTableColumnProps(theTableAnnotation)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Insert new column
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = theTableAnnotation.InsertColumn2(swTableItemInsertPosition_e.swTableItemInsertPosition_Last, 0, "New Column", swInsertTableColumnWidthStyle_e.swInsertColumn_DefaultWidth)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = theTableAnnotation.SetColumnType2(theTableAnnotation.ColumnCount - 1, swTableColumnTypes_e.swBomTableColumnType_PartNumber, True)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" ")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Table after inserting a column...")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Display table after inserting a column
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DisplayTableColumnProps(theTableAnnotation)
```

```vb
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub DisplayTableColumnProps(ByVal theTableAnnotation As Object)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim ColCount As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim iString As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim ColType As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim ColTypeString As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim ColTitle As String

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Col# kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}" + "Type kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}" + "Title")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ColCount = theTableAnnotation.ColumnCount
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 0 To ColCount - 1
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ColType = theTableAnnotation.GetColumnType2(i, True)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ColTypeString = CType(ColType, String)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ColTitle = theTableAnnotation.GetColumnTitle2(i, True)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iString = CType(i, String)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(iString + " kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}" + ColTypeString + " kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}" + ColTitle)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next i
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
