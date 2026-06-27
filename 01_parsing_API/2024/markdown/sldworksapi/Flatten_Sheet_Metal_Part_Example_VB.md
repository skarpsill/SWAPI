---
title: "Flatten Sheet Metal Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Flatten_Sheet_Metal_Part_Example_VB.htm"
---

# Flatten Sheet Metal Part Example (VBA)

This example shows how to flatten a sheet metal part.

```
'---------------------------------------
' Preconditions:
' 1. Open a sheet metal part.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Flattens the sheet metal part.
' 2. Examine the graphics area and Immediate window.
'---------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim nBendState As Long
    Dim nRetVal As Long
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    nBendState = swModel.GetBendState
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Original bend state = " & nBendState
```

```
    If nBendState <> swSMBendStateFlattened Then
        nRetVal = swModel.SetBendState(swSMBendStateFlattened)
        Debug.Print "  Modified bend state = " & nRetVal
```

```
        ' Rebuild to see changes
        bRet = swModel.EditRebuild3: Debug.Assert bRet
```

```
    End If
```

```
End Sub
```
