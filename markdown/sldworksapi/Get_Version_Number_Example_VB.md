---
title: "Get Version Number Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Version_Number_Example_VB.htm"
---

# Get Version Number Example (VBA)

This example shows how to get the version number of the SOLIDWORKS
executable.

```
'-----------------------------------
' Preconditions: Open the Immediate window.
'
' Postconditions: Examine the Immediate
' window.
'------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim BaseVersion As String
Dim CurrentVersion As String
Dim HotFixes As String
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
Debug.Print "SOLIDWORKS Version = " & swApp.RevisionNumber
swApp.GetBuildNumbers2 BaseVersion, CurrentVersion, HotFixes
Debug.Print "SOLIDWORKS major revision number: " & BaseVersion
Debug.Print "SOLIDWORKS build number: " & CurrentVersion
Debug.Print "SOLIDWORKS hot fix numbers: " & HotFixes
```

```
End Sub
```
