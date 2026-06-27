---
title: "Get Component from Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_from_Feature_Example_VB.htm"
---

# Get Component from Feature Example (VBA)

This example shows how to get a component from an assembly feature.

```vb
 '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly document with at least one component.
 ' 2. When the macro stops, select a feature in a component.
 ' 3. Press F5 to continue.
 '
 ' Postconditions: Inspect the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
Sub Main()
    Dim swModel      As SldWorks.ModelDoc2
     Dim swFeature    As SldWorks.Feature
     Dim swEntity     As SldWorks.Entity
     Dim bValue       As Boolean
     Dim swComponent  As SldWorks.Component2
    ' Connect to SOLIDWORKS
     Set swApp = Application.SldWorks
    ' Get active document
     Set swModel = swApp.ActiveDoc
    ' Check the document is an assembly
     If (swModel.GetType <> swDocASSEMBLY) Then
         Exit Sub
     End If
    ' Clear the selection
     swModel.ClearSelection2 True
    ' Select a feature in a part document
     Stop
    ' Get the feature
     Set swFeature = swModel.SelectionManager.GetSelectedObject6(1, -1)
    ' Cast the feature to an entity
     Set swEntity = swFeature

    ' Get type through entity interface
     Debug.Print "Entity type as defined in swSelectType_e: " & swEntity.GetType
     Debug.Assert (swEntity.GetType = swSelectType_e.swSelBODYFEATURES)
    ' Get type through feature interface
     ' Feature inherits from Entity, so will actually call Entity::GetType
     Debug.Print "Entity type as defined in swSelectType_e: " & swFeature.GetType
     Debug.Assert (swFeature.GetType = swSelectType_e.swSelBODYFEATURES)
    ' Get the component for the entity
     Set swComponent = swEntity.GetComponent
    ' Print component details
     Debug.Print swComponent.Name2
     Debug.Print "  " & swComponent.GetPathName
    ' Clear the selection
     swModel.ClearSelection2 True
    ' Select the feature through the Entity interface
     bValue = swEntity.Select4(False, Nothing)
    ' Print the type of the selected object
     Debug.Print "Selected object type as defined in swSelectType_e: " & swModel.SelectionManager.GetSelectedObjectType3(1, -1)
     Debug.Assert (swModel.SelectionManager.GetSelectedObjectType3(1, -1) = swSelectType_e.swSelBODYFEATURES)
    ' Clear the selection
     swModel.ClearSelection2 True
    ' Select the feature through the Feature interface
     bValue = swFeature.Select2(False, 0)
    ' Print the type of the selected object
     Debug.Print "Selected object type as defined in swSelectType_e: " & swModel.SelectionManager.GetSelectedObjectType3(1, -1)
     Debug.Assert (swModel.SelectionManager.GetSelectedObjectType3(1, -1) = swSelectType_e.swSelBODYFEATURES)
End Sub
```
