---
title: "Get Document Referenced by Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Document_Referenced_by_Drawing_View_Example_VB.htm"
---

# Get Document Referenced by Drawing View Example (VBA)

This example shows how to get the name of the document referenced by a drawing view.

```
'------------------------------------------------------
' Preconditions:
' 1. Open a drawing document.
' 2. Select a drawing view.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the name of the document referenced in the
'    selected drawing view.
' 2. Examine the Immediate window.
'------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swView As SldWorks.View
    Dim swDrawModel As SldWorks.ModelDoc2
    Dim sModelName  As String
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swView = swSelMgr.GetSelectedObject6(1, -1)
    Set swDrawModel = swView.ReferencedDocument
    sModelName = swView.GetReferencedModelName
    Debug.Print "File                      = " & swModel.GetPathName
    Debug.Print "  View                    = " & swView.Name
    Debug.Print "    Referenced model name = " & sModelName
    Debug.Print "    Model path            = " & swDrawModel.GetPathName
```

```
End Sub
```
