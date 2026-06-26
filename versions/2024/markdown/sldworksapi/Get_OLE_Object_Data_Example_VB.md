---
title: "Get OLE Object Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_OLE_Object_Data_Example_VB.htm"
---

# Get OLE Object Data Example (VBA)

This example shows how to get OLE object data from a model document.

```
'----------------------------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Click Insert > Object.
' 3. Click Paintbrush Picture > OK.
' 4. Click File > Close.
' 5. Open the Immediate window.
'
' Postconditions: Inspect the Immediate window.
'-----------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swModelDocExt As SldWorks.ModelDocExtension

Dim swSelMgr As SldWorks.SelectionMgr

Dim swOleObj As SldWorks.SwOLEObject

Dim boolstatus As Boolean
```

```vb
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension
     Set swSelMgr = swModel.SelectionManager
    Set swOleObj = swSelMgr.GetSelectedObject6(1, 0)
    Debug.Print "OLE Object"
     Debug.Print "  Class ID: " & swOleObj.Clsid
     Debug.Print "  Is linked? " & swOleObj.IsLinked
     Debug.Print "    Filename: " & swOleObj.FileName
     Debug.Print "  Buffer size: " & swOleObj.BufferSize
     Debug.Print "  Viewing aspect (1=Content, 2=Thumbnail, 4=Icon, 8=DocPrint): " & swOleObj.Aspect
End Sub
```
