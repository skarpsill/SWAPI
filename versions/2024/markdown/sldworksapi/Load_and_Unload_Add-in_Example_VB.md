---
title: "Load and Unload Add-in Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Load_and_Unload_Add-in_Example_VB.htm"
---

# Load and Unload Add-in Example (VBA)

This example shows how to prompt the user to load or unload an add-in.

```
'---------------------------------------------
' Preconditions:
' 1. Create a VB.NET add-in in Microsoft Visual Studio
'    2010, or later, in C:\test, following the instructions in
'    Add Shortcut Menu to Add-ins Example (VB.NET).
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Click Yes to load SwVBAddin1 or click No to unload
'    swVBAddin1.
' 2. Examine the Immediate window.
'----------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    'Path to add-in
    Const sAddinName As String = "C:\test\SwVBAddin1\SwVBAddin1\bin\SwVBAddin1.dll"
```

```
    Dim swApp As SldWorks.SldWorks
    Dim response As Long
    Dim status As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
```

```
    response = MsgBox("Load add-in?", vbYesNo)
```

```
    If response = vbYes Then
        Debug.Print "Loading: " + sAddinName
        status = swApp.LoadAddIn(sAddinName)
    Else
        Debug.Print "Unloading: " + sAddinName
        status = swApp.UnloadAddIn(sAddinName)
    End If
```

```
    Debug.Print "  Status = " & status
```

```
End Sub
```
