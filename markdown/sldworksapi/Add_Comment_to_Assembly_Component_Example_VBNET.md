---
title: "Add Comment to Assembly Component Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Comment_to_Assembly_Component_Example_VBNET.htm"
---

# Add Comment to Assembly Component Example (VB.NET)

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

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swModelDocExt As ModelDocExtension
         Dim selComp As Component2
         Dim selCompName As String
         Dim newComment As Comment

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swModelDocExt = swModel.Extension

         selComp = swSelMgr.GetSelectedObjectsComponent4(1, -1)
         selCompName = selComp.Name2

         newComment = swModelDocExt.AddComment("This component's name is " & selCompName)

     End Sub

     Public swApp As SldWorks

 End  Class
```
