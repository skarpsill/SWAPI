---
title: "Suppress Rebuild Error Dialogs Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Suppress_Rebuild_Error_Dialogs_Example_VB.htm"
---

# Suppress Rebuild Error Dialogs Example (VBA)

This example shows how to suppress dialogs when rebuild errors occur.

```
'--------------------------------------------------------------
' Preconditions: Open the Immediate window.
'
' Postconditions:
' 1. Examine the Immediate window.
' 2. Change False to True.
' 3. Rerun the macro.
'--------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Set swApp = Application.SldWorks
    Debug.Print "ShowErrorsEveryRebuild = " & swApp.GetUserPreferenceToggle(swShowErrorsEveryRebuild)
```

```
    swApp.SetUserPreferenceToggle swShowErrorsEveryRebuild, False
    Debug.Print "ShowErrorsEveryRebuild = " & swApp.GetUserPreferenceToggle(swShowErrorsEveryRebuild)
```

```
End Sub
```
