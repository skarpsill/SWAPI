---
title: "Manage Collision Detection Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Manage_Collision_Detection_Example_CSharp.htm"
---

# Manage Collision Detection Example (C#)

This example shows how to manage collision detection.

```vb
  //---------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\Spindleassem.sldasm.
 // 2. Open the Immediate window.
 //
 // Postconditions: Inspect the Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save changes to it.
  //----------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace ManageCollisionDetection
 {
     partial class SolidWorksMacro
     {

         private ModelDoc2 Part;
         private AssemblyDoc swDoc;
         private CollisionDetectionManager cdm;
         private CollisionDetectionGroup cdg;
         private CollisionDetectionGroup cdg2;
         private CollisionDetectionGroup cdg3;
         private Collision aCollision;
         private double[] TransformData = new double[16];
         private object TransformDataVariant;
         private double[] TransformData1 = new double[16];
         private object TransformDataVariant1;
         private Component2[] comp = new Component2[1];
         private Component2[] comp1 = new Component2[1];
         private Component2[] comp2 = new Component2[1];
         private MathTransform[] transform = new MathTransform[1];
         private MathTransform[] transform1 = new MathTransform[1];
         private MathUtility swMathUtil;
         private object var1;
         private bool boolstatus;
         private int longstatus;
         private int numCollisions;
         private int i;
         private int j;
         private object[] comps;

         public void Main()
         {

             Part = (ModelDoc2)swApp.ActiveDoc;
             swDoc = (AssemblyDoc)Part;
             cdm = (CollisionDetectionManager)swApp.GetCollisionDetectionManager();
             longstatus = cdm.SetAssembly(swDoc);

             cdm.GraphicsRedrawEnabled = true;

             cdg = (CollisionDetectionGroup)cdm.CreateGroup();
             cdg2 = (CollisionDetectionGroup)cdm.CreateGroup();
             cdg3 = (CollisionDetectionGroup)cdm.CreateGroup();

             //Holder
             boolstatus = Part.Extension.SelectByID2("Holder-1@Spindleassem", "COMPONENT", 0, 0, 0, true, 0, null, 0);

             TransformData[0] = 0.561729092855705;
             TransformData[1] = -0.827321235216108;
             TransformData[2] = 0;
             TransformData[3] = 0.827321235216108;
             TransformData[4] = 0.561729092855705;
             TransformData[5] = 0;
             TransformData[6] = 0;
             TransformData[7] = 0;
             TransformData[8] = 1.0D;
             TransformData[9] = 0.0202097529022064;
             TransformData[10] = 0.025899850979138;
             TransformData[11] = 0.1;
             TransformData[12] = 1;
             TransformData[13] = 0;
             TransformData[14] = 0;
             TransformData[15] = 0;

             TransformDataVariant = TransformData;
             swMathUtil = (MathUtility)swApp.GetMathUtility();

             //Cutting tool
             boolstatus = Part.Extension.SelectByID2("CuttingTool-1@Spindleassem", "COMPONENT", 0, 0, 0, true, 0, null, 0);

             TransformData1[0] = 1;
             TransformData1[1] = 0;
             TransformData1[2] = 0;
             TransformData1[3] = 0;
             TransformData1[4] = 1;
             TransformData1[5] = 0;
             TransformData1[6] = 0;
             TransformData1[7] = 0;
             TransformData1[8] = 1;
             TransformData1[9] = -0.01;
             TransformData1[10] = -0.03;
             TransformData1[11] = 0.1;
             TransformData1[12] = 1;
             TransformData1[13] = 0;
             TransformData1[14] = 0;
             TransformData1[15] = 0;

             TransformDataVariant1 = TransformData1;

             //Work piece
             boolstatus = Part.Extension.SelectByID2("workpiece-1@Spindleassem", "COMPONENT", 0, 0, 0, true, 0, null, 0);

             comp[0] = (Component2)((SelectionMgr)(Part.SelectionManager)).GetSelectedObjectsComponent4(1, -1);
             comp1[0] = (Component2)((SelectionMgr)(Part.SelectionManager)).GetSelectedObjectsComponent4(2, -1);
             comp2[0] = (Component2)((SelectionMgr)(Part.SelectionManager)).GetSelectedObjectsComponent4(3, -1);

             transform[0] = (MathTransform)swMathUtil.CreateTransform((TransformDataVariant));
             transform1[0] = (MathTransform)swMathUtil.CreateTransform((TransformDataVariant1));

             longstatus = cdg.SetComponents(comp); //Holder
             longstatus = cdg2.SetComponents(comp1); //Cutting tool
             longstatus = cdg3.SetComponents(comp2); //Work piece

             longstatus = cdg.ApplyTransforms(transform);
             longstatus = cdg2.ApplyTransforms(transform1);

             longstatus = cdm.IsCollisionPresent(true);
             numCollisions = cdm.GetCollisions(true, out var1);

             object[] collisions;
             collisions = (object[])var1;

             if (numCollisions > 0)
             {

                 int tempVar = numCollisions - 1;
                 for (i = 0; i <= tempVar; i++)
                 {
                     Debug.Print("Collision " + (i + 1));
                     aCollision = (Collision)collisions[i];
                     Debug.Print("  Is penetrating? " + aCollision.IsPenetrating());
                     comps = (object[])aCollision.GetComponents();
                     for (j = 0; j<=comps.GetUpperBound(0); j++)
                     {
                         Debug.Print("   " + ((Component2)comps[j]).Name);
                     }
                 }
             }
             else
             {
                 Debug.Print("No collisions present");
             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }

 }
```
