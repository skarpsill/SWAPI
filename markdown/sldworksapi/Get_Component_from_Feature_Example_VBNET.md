---
title: "Get Component from Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_from_Feature_Example_VBNET.htm"
---

# Get Component from Feature Example (VB.NET)

This example shows how to get a component from an assembly feature.

```vb
 '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly document with at least one component.
 ' 2. Select a feature in a component in the FeatureManager design tree.
'
 ' Postconditions: Inspect the Immediate window.
 '----------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub Main()

         Dim swModel As ModelDoc2
         Dim swFeature As Feature
         Dim swEntity As Entity
         Dim bValue As Boolean
         Dim swComponent As Component2

         ' Get active document
         swModel = swApp.ActiveDoc

         ' Check the document is an assembly
         If (swModel.GetType <> swDocumentTypes_e.swDocASSEMBLY)  Then
             Exit Sub
         End If

         ' Get the feature
         swFeature = swModel.SelectionManager.GetSelectedObject6(1, -1)

         ' Cast the feature to an entity
         swEntity = swFeature

         ' Get type through entity interface
         Debug.Print("Entity type as defined in swSelectType_e: " & swEntity.GetType)
         Debug.Assert(swEntity.GetType = swSelectType_e.swSelBODYFEATURES)

         ' Get type through feature interface
         ' Feature inherits from Entity, this will actually call Entity::GetType
         Debug.Print("Entity type as defined in swSelectType_e: " & swFeature.GetType)
         Debug.Assert(swFeature.GetType = swSelectType_e.swSelBODYFEATURES)

         ' Get the component for the entity
         swComponent = swEntity.GetComponent

         ' Print component details
         Debug.Print(swComponent.Name2)
         Debug.Print("  " & swComponent.GetPathName)

         ' Clear the selection lists
         swModel.ClearSelection2(True)

         ' Select the feature through the Entity interface
         bValue = swEntity.Select4(False, Nothing)

         ' Print the type of the selected object
         Debug.Print("Selected object type as defined in swSelectType_e: " & swModel.SelectionManager.GetSelectedObjectType3(1, -1))
         Debug.Assert(swModel.SelectionManager.GetSelectedObjectType3(1, -1) = swSelectType_e.swSelBODYFEATURES)

         ' Clear the selection lists
         swModel.ClearSelection2(True)

         ' Select the feature through the Feature interface
         bValue = swFeature.Select2(False, 0)

         ' Print the type of the selected object
         Debug.Print("Selected object type as defined in swSelectType_e: " & swModel.SelectionManager.GetSelectedObjectType3(1, -1))
         Debug.Assert(swModel.SelectionManager.GetSelectedObjectType3(1, -1) = swSelectType_e.swSelBODYFEATURES)

     End Sub

     Public swApp As SldWorks

 End  Class
```
