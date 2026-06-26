---
title: "Add Comment to Assembly Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Comment_to_Assembly_Component_Example_VB.htm"
---

# Add Comment to Assembly Component Example (VBA)

This example shows how to add a comment to an assembly component.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly document.
 ' 2. Select a component in the FeatureManager design tree.
 ' 3. Open an Immediate window.
 '
 ' Postconditions: A comment about the selected component is added to the
 ' document's Comments folder.
 ' ---------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swModelDocExt As SldWorks.ModelDocExtension

 Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swModelDocExt = swModel.Extension

    Dim selComp As SldWorks.Component2
     Dim selCompName As String
     Set selComp = swSelMgr.GetSelectedObjectsComponent4(1, -1)

    selCompName = selComp.Name2

    Dim newComment As SldWorks.Comment
     Set newComment = swModelDocExt.AddComment("This component's name is " & selCompName)
End Sub
```
