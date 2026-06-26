---
title: "Delete Design Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Design_Table_Example_VB.htm"
---

# Delete Design Table Example (VBA)

This example shows how to delete a design table.

```
'--------------------------------------------------------
' Preconditions:
' 1. Part or assembly document is open that contains a
'    design table.
' 2. Verify that a design table exists by expanding
'    Tables in the ConfigurationManager.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Deletes the design table.
' 2. Examine the Immediate window and ConfigurationManager.
'-------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel  As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim status As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.HasDesignTable
    If status Then
        swModel.DeleteDesignTable
        Debug.Print "Design table deleted."
    Else
        Debug.Print "Model document does not contain design table."
    End If
End Sub
```
