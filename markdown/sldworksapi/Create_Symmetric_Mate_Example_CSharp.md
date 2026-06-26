---
title: "Create and Edit Symmetric Mate Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Symmetric_Mate_Example_CSharp.htm"
---

# Create and Edit Symmetric Mate Example (C#)

This example shows how to create and edit a symmetric mate.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open:
 //    public_documents\samples\tutorial\api\AdvancedMates\AdvancedMateDemo3.sldasm
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates a symmetric mate.
 // 2. Press F5 to continue.
  // 3. Changes the symmetry plane and the entities to mate.
 // 4. Inspect the Immediate window and graphics area.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace CreateSymmetricMate_CSharp
 {
     partial class SolidWorksMacro
     {

         private ModelDoc2 swModel;
         private bool boolstatus;
         private AssemblyDoc AsmDoc;
         private MateFeatureData MateData;
         private SymmetricMateFeatureData SymmMateData;
         private SelectionMgr selman;
         private object FaceVar;
         private Feature Feat;
         private object Plane;
         private Face2[] FaceArr = new Face2[2];
         public void Main()
         {

             swModel = (ModelDoc2)swApp.ActiveDoc;
             AsmDoc = (AssemblyDoc)swModel;

             MateData = (MateFeatureData)AsmDoc.CreateMateData(8); //Symmetric mate
             selman = (SelectionMgr)swModel.SelectionManager;

             SymmMateData = (SymmetricMateFeatureData)MateData;

             // Set the symmetry plane
             Plane = AsmDoc.FeatureByName("Front Plane");
             SymmMateData.SymmetryPlane = Plane;

             // Select the faces
             boolstatus = swModel.Extension.SelectByRay(-0.119833719900839, 0.14832954277739, -0.0138999787131979, -0.638789958006775, -0.241329918931549, -0.730552708418903, 0.00194730543661126, 2, false, 0, 0);
             boolstatus = swModel.Extension.SelectByRay(0.00598755999561718, 0.0437101841503704, -0.0138999787133685, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000954271027477843, 2, true, 0, 0);

             // Set the entities to mate
             FaceArr[0] = (Face2)selman.GetSelectedObject6(1, -1);
             FaceArr[1] = (Face2)selman.GetSelectedObject6(2, -1);
             FaceVar = FaceArr;
             SymmMateData.EntitiesToMate = FaceVar;
             SymmMateData.MateAlignment = 1;

             Feat = (Feature)AsmDoc.CreateMate(MateData);

             swModel.GraphicsRedraw2();

             System.Diagnostics.Debugger.Break();

             Feat = swModel.Extension.GetLastFeatureAdded();
             Debug.Print("Feature type of mate created is " + Feat.GetTypeName2());

             MateData = (MateFeatureData)Feat.GetDefinition();

             swModel.ClearSelection2(true);

             SymmMateData = (SymmetricMateFeatureData)MateData;

             Plane = AsmDoc.FeatureByName("Top Plane");
             SymmMateData.SymmetryPlane = Plane;

             boolstatus = swModel.Extension.SelectByRay(-0.122740690662738, 0.149346213190292, -0.0800800212867898, -0.640294734796254, 0.0558893693642409, 0.766093356572332, 0.00243053632782351, 2, false, 0, 0);
             boolstatus = swModel.Extension.SelectByRay(0.00598755999561718, 0.0437101841503704, -0.0138999787133685, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000954271027477843, 2, true, 0, 0);
             FaceArr[0] = (Face2)selman.GetSelectedObject6(1, -1);
             FaceArr[1] = (Face2)selman.GetSelectedObject6(2, -1);

             FaceVar = FaceArr;

             SymmMateData.EntitiesToMate = FaceVar;

             Debug.Print("Symmetric mate alignment is " + SymmMateData.MateAlignment);

             Feat.ModifyDefinition(SymmMateData, swModel, null);
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }

 }
```
