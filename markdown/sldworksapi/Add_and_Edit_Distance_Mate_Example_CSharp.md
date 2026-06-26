---
title: "Add and Edit Distance Mate Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Edit_Distance_Mate_Example_CSharp.htm"
---

# Add and Edit Distance Mate Example (C#)

This example shows how to add and edit a cylindrical distance mate.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Ensure the specified template exists.
 // 2. Open public_documents\samples\tutorial\api\cylinder20.sldprt.
 // 3. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates and saves a new cylindrical part.
  // 2. Adds two cylindrical entities to a new assembly.
  // 3. Creates a distance mate between the cylindrical entities.
  // 4. Edits the distance mate to change the distance from 0.2 to 0.3.
  // 5. Inspect the Immediate window, the graphics area, and the Mates folder
 //    of the FeatureManager design tree.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //----------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using System.Diagnostics;

 namespace AddDistanceMate_CSharp
 {
     public partial class SolidWorksMacro
     {
         public void Main()
         {
             AssemblyDoc swAssembly = default(AssemblyDoc);
             ModelDoc2 Part = default(ModelDoc2);
             string AssemblyTitle = null;
             Component2 swInsertedComponent = default(Component2);
             Feature swFeat = default(Feature);
             bool boolstatus = false;
             int longstatus = 0;
             int longwarnings = 0;
             double swSheetWidth = 0;
             double swSheetHeight = 0;
             Mate2 swMate = default(Mate2);
             ModelDoc2 tmpObj = default(ModelDoc2);
             int errors = 0;
             Entity swEnt1 = default(Entity);
             Entity swEnt2 = default(Entity);

             Part = (ModelDoc2)swApp.ActiveDoc;

             // Shell the active part
             boolstatus = Part.Extension.SelectByRay(-0.0108900020093756, 0.0655319999998483, -0.00515652172191494, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00167637314537445, 2, false, 1,
             0);
             Part.InsertFeatureShell(0.00254, false);

             // Save the shelled part
             longstatus = Part.SaveAs3("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\cylinder20_shell.sldprt", 0, 2);

             // Create a new assembly
             swSheetWidth = 0;
             swSheetHeight = 0;
             Part = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2018\\templates\\Assembly.asmdot", 0, swSheetWidth, swSheetHeight);

             // Insert a cylinder20_shell component
             AssemblyTitle = Part.GetTitle();
             tmpObj = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\cylinder20_shell.sldprt", 1, 32, "", longstatus, longwarnings);
             swAssembly = (AssemblyDoc)swApp.ActivateDoc3(AssemblyTitle, true, 0, longstatus);
             swInsertedComponent = swAssembly.AddComponent5("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\cylinder20_shell.sldprt", 0, "", false, "", 0.119562469422817, -0.0102308109635487, -0.0474663286004215);
             swApp.CloseDoc("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\cylinder20_shell.sldprt");

             // Insert another cylinder20_shell component
             tmpObj = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\cylinder20_shell.sldprt", 1, 32, "", errors, longwarnings);
             swAssembly = (AssemblyDoc)swApp.ActivateDoc3(AssemblyTitle, true, 0, errors);
             swInsertedComponent = swAssembly.AddComponent5("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\cylinder20_shell.sldprt", 0, "", false, "", -0.130620346986689, -0.0101738580269739, 0.084551733918488);
             swApp.CloseDoc("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\cylinder20_shell.sldprt");

             // Select two cylindrical entities
             boolstatus = Part.Extension.SelectByRay(-0.140174514310559, 0.00237221117538411, 0.0264513806530431, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.00086563679245283, 2, false, 1,
             0);
             swEnt1 = (Entity)((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             boolstatus = Part.Extension.SelectByRay(0.0679787981690652, -0.00725673614920197, -0.0758574895979791, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000636203082166533, 2, true, 1,
             0);
             swEnt2 = (Entity)((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);

             swEnt1.Select4(true, null);
             swEnt2.Select4(true, null);

             // Add a center-to-center distance mate between the selected cylindrical entities
             swMate = swAssembly.AddDistanceMate(2, false, 0.2, 0, 0, 1, 1, out errors);
             Debug.Print("First arc condition as defined in swDistanceMateArcConditions_e: " + swMate.DistanceFirstArcCondition);
             Debug.Print("Second arc condition as defined in swDistanceMateArcConditions_e: " + swMate.DistanceSecondArcCondition);
             swFeat = (Feature)swMate;

             Part.EditRebuild3();

             // Edit the distance mate to change the distance from 0.2 to 0.3
             boolstatus = Part.Extension.SelectByRay(-0.0936626010895907, 0.000678476678046991, -0.000454698905400619, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000808436123348018, 2, true, 1,
             0);
             swEnt1 = (Entity)((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             boolstatus = Part.Extension.SelectByRay(0.0803986691953469, -0.00107796570199525, -0.0914337018962783, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000808436123348018, 2, true, 2,
             0);
             swEnt2 = (Entity)((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(2, -1);

             swEnt1.Select4(true, null);
             swEnt2.Select4(true, null);
             swFeat.Select2(true, 0);

             swAssembly.EditDistanceMate(2, false, 0.3, 0, 0, 1, 1, out errors);

             Part.EditRebuild3();
         }

         // The SldWorks swApp variable is pre-assigned for you.
         public SldWorks swApp;

     }
 }
```
