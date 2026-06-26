---
title: "Get Text Items in GTol Frame Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Text_Items_in_GTol_Frame_VB.htm"
---

# Get Text Items in GTol Frame Example (VBA)

This example shows how to get text items, values, and symbols in a GTol frame.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Open a document with a GTol frame and select that GTol
'    frame.
' 2. Open an Immediate window.
'
' Postconditions:
' 1. Gets the text items, values, and symbols in the
'    selected GTol frame.
' 2. Examine the Immediate window.
'-------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim selGtol As SldWorks.Gtol
Dim idx As Long
Dim params As Variant
Dim arrSymbols As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    Set selGtol = swSelMgr.GetSelectedObject6(1, 0)
```

```
    Debug.Print "GetTextCount = " & CStr(selGtol.GetTextCount)
```

```
    For idx = 0 To selGtol.GetTextCount - 1
        Debug.Print "GetTextAtIndex(" & CStr(idx) & ") = " & selGtol.GetTextAtIndex(idx)
    Next idx
```

```
    Debug.Print "GetFrameCount = " & (CStr(selGtol.GetFrameCount) - 1)
```

```
    For idx = 1 To selGtol.GetFrameCount - 1
        params = selGtol.GetFrameValues(idx)
        Debug.Print "GetFrameValues(" & CStr(idx) & ") = " & params(0) & "," & params(1) & "," & params(2) & "," & params(3) & "," & params(4)
        arrSymbols = selGtol.GetFrameSymbols3(idx)
        Debug.Print "  GetFrameSymbols3(" & CStr(idx) & ") = " & arrSymbols(0) & ", " & arrSymbols(1) & ", " & arrSymbols(2) & ", " & arrSymbols(3) & ", " & arrSymbols(4) & ", " & arrSymbols(5) & ")"
   Next idx
```

```
End Sub
```
