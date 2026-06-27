---
title: "Get Design Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Design_Table_Example_VB.htm"
---

# Get Design Table Example (VBA)

This example shows how to get a design table and its contents.

```
'---------------------------------------
' Preconditions:
' 1. Open a part or assembly document that
'    contains a design table.
' 2. Verify that a design table exists by
'    expanding Tables in the ConfigurationManager.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Prints the design table contents to the
'    Immediate window.
' 2. Examine the Immediate window.
'----------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swDesTable              As SldWorks.DesignTable
    Dim nTotRow                 As Long
    Dim nTotCol                 As Long
    Dim sRowStr                 As String
    Dim i                       As Long
    Dim j                       As Long
    Dim bRet                    As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc

    Set swDesTable = swModel.GetDesignTable
    bRet = swDesTable.Attach

    Debug.Assert bRet
```

```
    nTotRow = swDesTable.GetTotalRowCount
    nTotCol = swDesTable.GetTotalColumnCount
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Title        = " & swDesTable.GetTitle
    Debug.Print "  Row          = " & swDesTable.GetRowCount
    Debug.Print "  Col          = " & swDesTable.GetColumnCount
    Debug.Print "  TotRow       = " & nTotRow
    Debug.Print "  TotCol       = " & nTotCol
    Debug.Print "  VisRow       = " & swDesTable.GetVisibleRowCount
    Debug.Print "  VisCol       = " & swDesTable.GetVisibleColumnCount
    Debug.Print ""
```

```
    For i = 0 To nTotRow
        sRowStr = "  |"
```

```
        For j = 0 To nTotCol
            sRowStr = sRowStr + swDesTable.GetEntryText(i, j) + "|"
        Next j
```

```
        Debug.Print sRowStr
```

```
    Next i
```

```
    swDesTable.Detach
```

```
End Sub
```
