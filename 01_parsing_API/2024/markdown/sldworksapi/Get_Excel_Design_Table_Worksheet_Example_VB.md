---
title: "Get Excel Design Table Worksheet Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Excel_Design_Table_Worksheet_Example_VB.htm"
---

# Get Excel Design Table Worksheet Example (VBA)

This example shows how to get the Excel worksheet of a design table.

```
'-------------------------------------
' Preconditions:
' 1. Open a drawing document that contains an
'    Excel-based design table.
' 2. Add a reference to Microsoft Excel release Object Library.
' 3. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'-------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim myModelDoc As SldWorks.ModelDoc2
    Dim myDrawingDoc As SldWorks.DrawingDoc
    Dim myView As SldWorks.View
    Dim myDesignTable As SldWorks.DesignTable
    Dim designTableDoc As SldWorks.ModelDoc2
    Dim hasDT As Boolean
    Dim viewModelName As String
    Dim longstatus As Long
    Dim myWorksheet As Excel.Worksheet
    Dim tableRowCount As Long, tableColCount As Long
    Dim tableFirstRow As Long, tableFirstCol As Long
```

```
    Set swApp = Application.SldWorks
    Set myModelDoc = swApp.ActiveDoc
    Set myDrawingDoc = myModelDoc
    Set myView = myDrawingDoc.GetFirstView
    While Not myView Is Nothing
        hasDT = myView.HasDesignTable()
        If Not (hasDT = 0) Then
            viewModelName = myView.GetReferencedModelName()
            Set designTableDoc = swApp.ActivateDoc2(viewModelName, True, longstatus)
            Set myDesignTable = designTableDoc.GetDesignTable()
            If Not myDesignTable Is Nothing Then
                myDesignTable.Attach
            ' These methods deal with the actual design table data,
            ' not necessarily all of the information
            ' that is in the Excel worksheet
                Debug.Print "Total Row Count = " & myDesignTable.GetTotalRowCount
                Debug.Print "      Col Count = " & myDesignTable.GetTotalColumnCount
                Debug.Print "Start Row = " & myDesignTable.GetStartRowNumber
                Debug.Print "      Col = " & myDesignTable.GetStartColumnNumber
            ' These methods and properties deal with the information in
            ' the Excel worksheet
                tableRowCount = myDesignTable.GetVisibleRowCount
                Debug.Print "Table row count = " & tableRowCount
                tableColCount = myDesignTable.GetVisibleColumnCount
                Debug.Print "Table column count = " & tableColCount
                tableFirstRow = myDesignTable.GetVisibleTopRowNumber
                tableFirstCol = myDesignTable.GetVisibleLeftColumnNumber
                Debug.Print "Visible Row Count = " & tableRowCount
                Debug.Print "        Col Count = " & tableColCount
                Debug.Print "Visible Top Row  = " & tableFirstRow
                Debug.Print "        Left Col = " & tableFirstCol
            ' Exposing the Excel interface provides you with more information
            ' than currently available from the SOLIDWORKS API; for example,
            ' DXF/DWG translation can now reproduce a table that looks like
            ' the design table
                Set myWorksheet = myDesignTable.Worksheet
                If Not myWorksheet Is Nothing Then
                    Debug.Print ""
                    Debug.Print "The name of the worksheet is " & myWorksheet.Name
                    Dim i As Integer, rowIndex As Integer
                    Dim j As Integer, colIndex As Integer
                    Dim cellRange As Excel.Range
                    Dim rowRange As Excel.Range
                    Dim colRange As Excel.Range
                    Dim rowHeight As Double, colWidth As Double
                    Dim rowHidden As Boolean, colHidden As Boolean
                    Dim cellValue As String, cellText As String
                    Dim horzalign As Integer, vertalign As Integer, ismerged As Boolean
                    Dim halignStr As String, valignStr As String
                    For i = 1 To tableRowCount
                        rowIndex = tableFirstRow + i - 1
                        Set rowRange = myWorksheet.Rows(rowIndex)
                        rowHeight = rowRange.rowHeight
                        rowHidden = rowRange.Hidden
                        Debug.Print "Row[" & rowIndex & "] Height = " & rowHeight & ", Hidden = " & rowHidden
                    Next i
                    For j = 1 To tableColCount
                        colIndex = tableFirstCol + j - 1
                        Set colRange = myWorksheet.Columns(colIndex)
                        colWidth = colRange.ColumnWidth
                        colHidden = colRange.Hidden
                        Debug.Print "Col[" & colIndex & "] Width = " & colWidth & ", Hidden = " & colHidden
                    Next j
```

```
                    For i = 1 To tableRowCount
                        rowIndex = tableFirstRow + i - 1
                        For j = 1 To tableColCount
                            colIndex = tableFirstCol + j - 1
                            Set cellRange = myWorksheet.Cells(rowIndex, colIndex)
                            cellValue = cellRange.Value2
                            cellText = cellRange.Text
                            horzalign = cellRange.HorizontalAlignment
                            Select Case horzalign
                            Case XlHAlign.xlHAlignLeft
                                halignStr = "Left"
                            Case XlHAlign.xlHAlignCenter
                                halignStr = "Center"
                            Case XlHAlign.xlHAlignRight
                                halignStr = "Right"
                            Case XlHAlign.xlHAlignCenterAcrossSelection
                                halignStr = "Center Across"
                            Case XlHAlign.xlHAlignDistributed
                                halignStr = "Distributed"
                            Case Else
                                halignStr = "unknown"
                            End Select
                            vertalign = cellRange.VerticalAlignment
                            Select Case vertalign
                            Case XlVAlign.xlVAlignBottom
                                valignStr = "Bottom"
                            Case XlVAlign.xlVAlignCenter
                                valignStr = "Middle"
                            Case XlVAlign.xlVAlignTop
                                valignStr = "Top"
                            Case XlVAlign.xlVAlignDistributed
                                valignStr = "Distributed"
                            Case Else
                                valignStr = "unknown"
                            End Select
                            ismerged = cellRange.MergeCells
                            Debug.Print "Cell[" & rowIndex & "," & colIndex & "] = " & cellText & " " & cellValue & " " & halignStr & " " & valignStr & " " & ismerged
                        Next j
                    Next i
                End If
                Set myWorksheet = Nothing
                myDesignTable.Detach
            End If
            swApp.CloseDoc viewModelName
        End If
        Set myView = myView.GetNextView()
    Wend
```

```
End Sub
```
