---
title: "Create Standard Mates Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Standard_Mates_Example_CSharp.htm"
---

# Create Standard Mates Example (C#)

This example shows how to create a variety of standard mates.

```vb
  //----------------------------------------------------------------------------
  // Preconditions: Ensure the specified file paths exist.
 //
 // Postconditions: Inspect the Mates folder in the FeatureManager design tree.
 //
  // NOTE: Because the models are used elsewhere, do not save changes.
  //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace StandardMates_CSharp
 {
     partial class SolidWorksMacro
     {

         private AssemblyDoc swAssembly;
         private string AssemblyTitle;
         private ModelDoc2 tmpObj;
         private Component2 swInsertedComponent;
         private int errors;
         private ModelDoc2 Part;
         private double[] TransformData = new double[16];
         private object TransformDataVariant;
         private dynamic swMathUtil;
         private MathTransform swTransform;
         private TangentMateFeatureData MateData;
         private object[] EntitiesToMate = new object[2];
         private object EntitiesToMateVar;
         private Feature MateFeature;
         private PerpendicularMateFeatureData PerpMateData;
         private CoincidentMateFeatureData CoincMateData;
         private ParallelMateFeatureData ParMateData;
         private ConcentricMateFeatureData ConcMateData;
         private LockMateFeatureData LMateData;
         private bool boolstatus;
         private int longstatus;
         private int longwarnings;
         public void Main()
         {

             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\assem20.sldasm", 2, 0, "", ref longstatus, ref longwarnings);

             swAssembly = (AssemblyDoc)Part;
             swApp.ActivateDoc2("assem20.sldasm", false, longstatus);
             Part = (ModelDoc2)swApp.ActiveDoc;

             AssemblyTitle = Part.GetTitle();

             tmpObj = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\shaft.sldprt", 1, 32, "", ref errors, ref longwarnings);
             Part = (ModelDoc2)swApp.ActivateDoc3(AssemblyTitle, true, 0, ref errors);

             swInsertedComponent = swAssembly.AddComponent5("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\shaft.sldprt", 0, "", false, "", 0.29642267129384, 0.0920506109250709, -0.187506963149644);
             swApp.CloseDoc("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\shaft.sldprt");

             TransformData[0] = 1;
             TransformData[1] = 0;
             TransformData[2] = 0;
             TransformData[3] = 0;
             TransformData[4] = 1;
             TransformData[5] = 0;
             TransformData[6] = 0;
             TransformData[7] = 0;
             TransformData[8] = 1;
             TransformData[9] = 0.29642267129384;
             TransformData[10] = 0.0420506109250709;
             TransformData[11] = -0.187506963149644;
             TransformData[12] = 1;
             TransformData[13] = 0;
             TransformData[14] = 0;
             TransformData[15] = 0;

             TransformDataVariant = TransformData;

             swMathUtil = swApp.GetMathUtility();

             swTransform = swMathUtil.CreateTransform((TransformDataVariant));
             boolstatus = swInsertedComponent.SetTransformAndSolve2(swTransform);

             boolstatus = Part.Extension.SelectByRay(0.0443527596829085, 0.0297941775455115, 0.00219712535516692, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00299151229353486, 2, true, 1, 0);
             boolstatus = Part.Extension.SelectByRay(0.130082347379926, 0.0512737883206569, -0.0238688162796734, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00299151229353486, 2, true, 1, 0);

             // Create TangentMateFeatureData
             MateData = (TangentMateFeatureData)swAssembly.CreateMateData(4);

             // Set the Entities To Mate
             EntitiesToMate[0] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             EntitiesToMate[1] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(2, -1);

             EntitiesToMateVar = EntitiesToMate;
             MateData.EntitiesToMate = (EntitiesToMateVar);

             // Set the Mate Alignment
             MateData.MateAlignment = 1;

             // Create the mate
             MateFeature = (Feature)swAssembly.CreateMate(MateData);
             Part.ClearSelection2(true);
             Part.EditRebuild3();

             boolstatus = Part.Extension.SelectByRay(-0.00247922125254263, 0.028363044378807, 0.043532545142341, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00299151229353486, 2, true, 1, 0);
             boolstatus = Part.Extension.SelectByRay(0.114306836013213, 0.0719973430751679, -0.0518791456821077, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00299151229353486, 2, true, 1, 0);

             // Create PerpendicularMateFeatureData
             PerpMateData = (PerpendicularMateFeatureData)swAssembly.CreateMateData(2);

             // Set the Entities To Mate
             EntitiesToMate[0] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             EntitiesToMate[1] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(2, -1);
             EntitiesToMateVar = EntitiesToMate;
             PerpMateData.EntitiesToMate = (EntitiesToMateVar);

             // Create the mate
             MateFeature = (Feature)swAssembly.CreateMate(PerpMateData);
             Part.ClearSelection2(true);
             Part.EditRebuild3();

             boolstatus = Part.Extension.SelectByRay(-0.0130850967460105, 0.0540093074191645, 0.000810230676393076, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00299151229353486, 2, true, 1, 0);
             boolstatus = Part.Extension.SelectByRay(0.107909556750883, 0.0719973430752248, -0.0658876969148992, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00299151229353486, 2, true, 1, 0);

             // Create CoincidentMateFeatureData
             CoincMateData = (CoincidentMateFeatureData)swAssembly.CreateMateData(0);

             // Set the Entities To Mate
             EntitiesToMate[0] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             EntitiesToMate[1] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(2, -1);
             EntitiesToMateVar = EntitiesToMate;
             CoincMateData.EntitiesToMate = (EntitiesToMateVar);

             // Set the Mate Alignment
             CoincMateData.MateAlignment = 0;

             // Create the mate
             MateFeature = (Feature)swAssembly.CreateMate(CoincMateData);
             Part.ClearSelection2(true);
             Part.EditRebuild3();

             boolstatus = Part.Extension.SelectByRay(-0.0265813760897231, 0.0540093074191077, -0.0191102240282248, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00299151229353486, 2, true, 1, 0);
             boolstatus = Part.Extension.SelectByRay(0.104493667114582, 0.0540093074190509, -0.053508121263917, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00299151229353486, 2, true, 1, 0);

             // Create ParallelMateFeatureData
             ParMateData = (ParallelMateFeatureData)swAssembly.CreateMateData(3);

             // Set the Entities To Mate
             EntitiesToMate[0] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             EntitiesToMate[1] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(2, -1);
             EntitiesToMateVar = EntitiesToMate;
             ParMateData.EntitiesToMate = (EntitiesToMateVar);

             // Set the Mate Alignment
             ParMateData.MateAlignment = 0;

             // Create the mate
             MateFeature = (Feature)swAssembly.CreateMate(ParMateData);
             Part.ClearSelection2(true);
             Part.EditRebuild3();

             boolstatus = Part.Extension.SelectByRay(0.153629139956536, 0.0267016961580566, -0.0207225117635517, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00299151229353486, 2, true, 1, 0);
             boolstatus = Part.Extension.SelectByRay(0.31258643852118, 0.0771807121026882, -0.175728481540773, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00299151229353486, 2, true, 1, 0);

             // Create ConcentricMateFeatureData
             ConcMateData = (ConcentricMateFeatureData)swAssembly.CreateMateData(1);

             // Set the Entities To Mate
             EntitiesToMate[0] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             EntitiesToMate[1] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(2, -1);
             EntitiesToMateVar = EntitiesToMate;
             ConcMateData.EntitiesToMate = (EntitiesToMateVar);

             // Set the Mate Alignment
             ConcMateData.MateAlignment = 1;

             // Set the Lock Rotation
             ConcMateData.LockRotation = false;

             // Create the mate
             MateFeature = (Feature)swAssembly.CreateMate(ConcMateData);
             Part.ClearSelection2(true);
             Part.EditRebuild3();

             boolstatus = Part.Extension.SelectByID2("cylinder20-1@assem20", "COMPONENT", 0.136504049029156, 0.042017793613752, -0.00604340129007142, true, 1, null, 0);
             boolstatus = Part.Extension.SelectByID2("shaft-1@assem20", "COMPONENT", 0.116970722742224, 0.072421443211681, -0.0524867796554531, true, 1, null, 0);

             // Create LockMateFeatureData
             LMateData = (LockMateFeatureData)swAssembly.CreateMateData(16);

             // Set the Entities To Mate
             EntitiesToMate[0] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             EntitiesToMate[1] = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(2, -1);
             EntitiesToMateVar = EntitiesToMate;
             LMateData.EntitiesToMate = (EntitiesToMateVar);

             // Create the mate
             MateFeature = (Feature)swAssembly.CreateMate(LMateData);
             Part.ClearSelection2(true);
             Part.EditRebuild3();
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }

 }
```
