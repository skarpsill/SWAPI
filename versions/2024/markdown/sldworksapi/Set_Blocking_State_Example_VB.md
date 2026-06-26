---
title: "Set Blocking State Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Blocking_State_Example_VB.htm"
---

# Set Blocking State Example (VBA)

This example shows how to set and reset the blocking state for a model document.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open a model document
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Displays a message box asking whether
'    to reset the blocking state to the previous
'    blocking state.
' 2. Click Yes to reset the blocking state to allow changes
'    to the document.
' 3. Examine the Immediate window and click the Sketch tab to verify
'    that you can make changes to the document.
' 4. Run the macro again and click No to set the blocking state
'    to disallow changes to document.
' 5. Examine the Immediate window and the Sketch toolbar to verify
'    that you cannot make changes to the document.
' 6  Run the macro again and click Yes.
' 7. Examine the Immediate window and the Sketch toolbar to verify
'    that you can make changes to the document.
'------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim nResponse As Integer
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    ' Get current blocking state
    Debug.Print "Starting blocking state = " & swModel.GetBlockingState
```

```
    ' Ask user if blocking state should be reset to previous state
    nResponse = MsgBox("Reset blocking state?", vbYesNo)
```

```
    ' If user responds yes, then reset blocking state
    If nResponse = vbYes Then
        swModel.ResetBlockingState
    Else
    ' If use responds no, then set blocking state to
    ' disallow changes to document
        swModel.SetBlockingState swPartialModifyBlock
    End If
```

```
    Debug.Print "Ending blocking state = " & swModel.GetBlockingState
    Debug.Print ""
```

```
End Sub
```
