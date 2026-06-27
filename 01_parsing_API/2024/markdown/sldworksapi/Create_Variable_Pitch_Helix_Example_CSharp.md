---
title: "Create Variable-pitch Helix Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Variable_Pitch_Helix_Example_CSharp.htm"
---

# Create Variable-pitch Helix Example (C#)

This example shows how to create a variable-pitch helix.

```vb
//---------------------------------------------------------
 // Preconditions: Verify that the specified part document
 // template exists.
 //
 // Postconditions:
 // 1. Creates a variable-pitch helix.
 // 2. Examine the graphics area and FeatureManager design
 //    tree.
 //---------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;

 namespace AddVariablePitchHelixCSharp.csproj
 {
     partial  class  SolidWorksMacro
     {

         public  void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SketchManager swSketchManager = default(SketchManager);
             SketchSegment swSketchSegment = default(SketchSegment);
             FeatureManager swFeatureManager = default(FeatureManager);
             Feature swFeature = default(Feature);
             int errors = 0;
             bool status = false;

             // Create part document
             swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSketchManager = (SketchManager)swModel.SketchManager;
             swFeatureManager = (FeatureManager)swModel.FeatureManager;

             // Sketch a circle
             swSketchSegment = (SketchSegment)swSketchManager.CreateCircle(0.0, 0.0, 0.0, 0.045549, 0.013926, 0.0);

             // Create a variable-pitch helix using the sketched circle
             status = swFeatureManager.InsertVariablePitchHelix(false, true, 1, 4.712388980385);
             status = swFeatureManager.AddVariablePitchHelixFirstPitchAndDiameter(0.053, 0.05382625271268);
             status = swFeatureManager.AddVariablePitchHelixSegment(0.0265, 0.05382625271268, 0.5);
             status = swFeatureManager.AddVariablePitchHelixSegment(0.03975, 0.05382625271268, 0.75);
             status = swFeatureManager.AddVariablePitchHelixSegment(0.046375, 0.05382625271268, 0.875);
             status = swFeatureManager.AddVariablePitchHelixSegment(0.053, 0.05382625271268, 1);
             swFeature = (Feature)swFeatureManager.EndVariablePitchHelix();

         }

         ///  <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
