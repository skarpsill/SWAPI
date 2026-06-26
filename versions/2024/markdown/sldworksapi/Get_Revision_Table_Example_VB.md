---
title: "Get Revision Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Revision_Table_Example_VB.htm"
---

# Get Revision Table Example (VBA)

This example shows how to get information from a revision table annotation.

```
'--------------------------------------
' Preconditions:
' 1. Open a drawing whose current sheet
'    contains a revision table annotation.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the number of columns and rows
'    in the revision table annotation and
'    the text in each row.
' 2. Examine the Immediate window.
'--------------------------------------
Option Explicit
```

```
Sub ProcessTableAnn(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swTable As SldWorks.TableAnnotation)
```

```
    Dim sRowStr As String
   Dim i As Long
   Dim j As Long
```

```
    Debug.Print "Number of columns: " & swTable.ColumnCount
   Debug.Print "Number of rows: " & swTable.RowCount
   For i = 0 To swTable.RowCount - 1
        sRowStr = "  "
        For j = 0 To swTable.ColumnCount - 1
             sRowStr = sRowStr & "|" & swTable.Text2(i, j, True)
        Next j
        Debug.Print "  " & sRowStr & "|"
   Next i
```

```
End Sub
```

```
Sub main()
```

```
     Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swSheet As SldWorks.Sheet
    Dim swRevTable As SldWorks.RevisionTableAnnotation
    Dim swTable As SldWorks.TableAnnotation
    Dim bRet As Boolean
```

```
     Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swSheet = swDraw.GetCurrentSheet
    Set swRevTable = swSheet.RevisionTable
    Set swTable = swRevTable
    Debug.Print "File = " & swModel.GetPathName
    ProcessTableAnn swApp, swModel, swTable
```

```
End Sub
```
