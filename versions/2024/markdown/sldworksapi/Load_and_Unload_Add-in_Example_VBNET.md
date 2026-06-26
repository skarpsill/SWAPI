---
title: "Load and Unload Add-in Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Load_and_Unload_Add-in_Example_VBNET.htm"
---

# Load and Unload Add-in Example (VB.NET)

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
'---------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        'Path to add-in
        Const sAddinName As String = "C:\test\SwVBAddin1\SwVBAddin1\bin\SwVBAddin1.dll"
        Dim response As Integer
        Dim status As Integer

        swApp = CreateObject("SldWorks.Application")
        response = MsgBox("Load add-in?", vbYesNo)
        If response = vbYes Then
            Debug.Print("Loading: " + sAddinName)
            status = swApp.LoadAddIn(sAddinName)
        Else
            Debug.Print("Unloading: " + sAddinName)
            status = swApp.UnloadAddIn(sAddinName)
        End If

        Debug.Print("  Status = " & status)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
