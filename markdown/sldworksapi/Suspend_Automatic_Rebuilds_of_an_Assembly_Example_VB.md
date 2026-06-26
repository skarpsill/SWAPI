---
title: "Suspend Automatic Rebuilds of an Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Suspend_Automatic_Rebuilds_of_an_Assembly_Example_VB.htm"
---

# Suspend Automatic Rebuilds of an Assembly Example (VBA)

This example shows how to suspend automatic rebuilds of an assembly.

```
'-------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Disables automatic rebuilds of the assembly.
' 3. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not
' save changes.
'------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swAssemblyDoc As SldWorks.AssemblyDoc
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
    Dim status As Boolean
```

```
    Set swApp = Application.SldWorks
```

```
   ' Open assembly
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\smartcomponents\pillow_block.sldasm"
    Set swAssemblyDoc = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    Debug.Print "State (False = rebuilds enabled; True = rebuilds suspended)"
```

```
    ' Get current state
    status = swAssemblyDoc.EnableAssemblyRebuild
    Debug.Print "   Before running macro = " + CStr(swAssemblyDoc.EnableAssemblyRebuild)
```

```
    ' Suspend automatic rebuilds of the assembly
    swAssemblyDoc.EnableAssemblyRebuild = Not status
    Debug.Print "   After running macro  = " + CStr(swAssemblyDoc.EnableAssemblyRebuild)
```

```
End Sub
```
