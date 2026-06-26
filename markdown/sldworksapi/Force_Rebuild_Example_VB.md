---
title: "Force Rebuild Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Force_Rebuild_Example_VB.htm"
---

# Force Rebuild Example (VBA)

This example shows how to force a rebuild of a model.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Rebuilds the model.
' 2. Examine the Immediate window.
'
' NOTE: This macro turns off saving the model automatically. Before
' running this macro, click Tools > Options >
' System Options > Backup/Recover > Save auto-recover information
' every. If saving the model automatically before running this
' macro, then change this option back to its original values
' after running the macro.
'--------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
   Dim swModel As SldWorks.ModelDoc2
   Dim nStart As Single
   Dim i As Long
   Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
   Set swModel = swApp.ActiveDoc
```

```
    ' Turn off saving model automatically
    swApp.SetUserPreferenceIntegerValue swAutoSaveInterval, False
```

```
    ' Use VBA Timer function to calculate time to rebuild model
    nStart = Timer
```

```
    bRet = swModel.ForceRebuild3(False)
```

```
    Debug.Print "File = " + swModel.GetPathName
   Debug.Print "  Time to rebuild model = " & Timer - nStart & " sec"
```

```
End Sub
```
