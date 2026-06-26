---
title: "Get Component from Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_from_Feature_Example_CSharp.htm"
---

# Get Component from Feature Example (C#)

This example shows how to get a component from an assembly feature.

```vb
 //-----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open an assembly document with at least one component.
 // 2. Select a feature in a component in the FeatureManager design tree.
 //
 // Postconditions: Inspect the Immediate window.
 //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace GetComponentFromFeature_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             Feature swFeature = default(Feature);
             Entity swEntity = default(Entity);
             bool bValue = false;
             Component2 swComponent = default(Component2);

             // Get active document
             swModel = (ModelDoc2)swApp.ActiveDoc;

             // Check the document is an assembly
             if ((swModel.GetType() != (int)swDocumentTypes_e.swDocASSEMBLY))
             {
                 return;
             }

             // Get the feature
             swFeature = (Feature)((SelectionMgr)(swModel.SelectionManager)).GetSelectedObject6(1, -1);

             // Cast the feature to an entity
             swEntity = (Entity)swFeature;

             // Get type through entity interface
             Debug.Print("Entity type as defined in swSelectType_e: " + swEntity.GetType());
             Debug.Assert(swEntity.GetType() == (int)swSelectType_e.swSelBODYFEATURES);

             // Get type through feature interface
             // Feature inherits from Entity, so will actually call Entity::GetType
             Debug.Print("Entity type: " + swFeature.GetType());

             // Get the component for the entity
             swComponent = (Component2)swEntity.GetComponent();

             // Print component details
             Debug.Print(swComponent.Name2);
             Debug.Print("  " + swComponent.GetPathName());

             // Clear the selection lists
             swModel.ClearSelection2(true);

             // Select the feature through the Entity interface
             bValue = swEntity.Select4(false, null);

             // Print the type of the selected object
             Debug.Print("Selected object type as defined in swSelectType_e: " + ((SelectionMgr)(swModel.SelectionManager)).GetSelectedObjectType3(1, -1));
             Debug.Assert(((SelectionMgr)(swModel.SelectionManager)).GetSelectedObjectType3(1, -1) == (int)swSelectType_e.swSelBODYFEATURES);

             // Clear the selection lists
             swModel.ClearSelection2(true);

             // Select the feature through the Feature interface
             bValue = swFeature.Select2(false, 0);

             // Print the type of the selected object
             Debug.Print("Selected object type as defined in swSelectType_e: " + ((SelectionMgr)(swModel.SelectionManager)).GetSelectedObjectType3(1, -1));
             Debug.Assert(((SelectionMgr)(swModel.SelectionManager)).GetSelectedObjectType3(1, -1) == (int)swSelectType_e.swSelBODYFEATURES);

         }

         public SldWorks swApp;

     }
 }
```
