---
title: "Get Process ID of SOLIDWORKS Session Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Process_ID_of_SOLIDWORKS_Session_Example_VB.htm"
---

# Get Process ID of SOLIDWORKS Session Example (VBA)

This example shows how to get and verify the process ID of the current
SOLIDWORKS session.

```
'--------------------------------------------------------
' Preconditions:
' 1. Verify that only one SOLIDWORKS session is running.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the process ID of the SOLIDWORKS session.
' 2. Examine the Immediate window.
' 3. To verify the process ID, open a Command Prompt window,
'    type TASKLIST, and locate sldworks.exe in the Image Name
'    column and its process ID in the corresponding PID column.
' 4. Exit the Command Prompt window.
'----------------------------------------------------------
```

```
Dim swApp As SldWorks.SldWorks
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
' Print the current SOLIDWORKS session's PID to the
' Immediate window
Debug.Print "SOLIDWORKS process ID: " & swApp.GetProcessID
```

```
End Sub
```
