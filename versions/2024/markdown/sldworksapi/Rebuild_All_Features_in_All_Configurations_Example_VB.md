---
title: "Rebuild All Features in All Configurations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rebuild_All_Features_in_All_Configurations_Example_VB.htm"
---

# Rebuild All Features in All Configurations Example (VBA)

This example shows how to rebuild all features in all configurations without activating each configuration.

```
'------------------------------------------------------------
' Preconditions:
' 1. Copy public_documents\samples\tutorial\PDMWorks to c:\temp.
' 2. Open c:\temp\membrane.sldprt.
'    a. Expand Revolve-Thin1, click Sketch1 > Edit Sketch.
'    b. Click R30 and change 30 to 60.
'    c. Click File > Save All > Rebuild and save document
'       (recommended).
'    d. Click File > Close.
' 3. Open c:\temp\speaker.sldasm.
' 4. Click Don't rebuild.
' 5. Open the Immediate window.
'
' Postconditions:
' 1. Rebuilds all features in all configurations without
'    activating each configuration.
' 2. Examine the Immediate window.
'------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim bRebuild As Boolean
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    bRet = swModelDocExt.NeedsRebuild2
    Debug.Print "Features need to be rebuilt? " & bRet
```

```
    If bRet Then
        bRebuild = swModelDocExt.ForceRebuildAll
        Debug.Print "    All features rebuilt in all configurations without activating each configuration? " & bRebuild
    End If
```

```
End Sub
```
