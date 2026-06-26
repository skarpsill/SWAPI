---
title: "Add Gravity Load Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Gravity_Load_Example_CSharp.htm"
---

# Add Gravity Load Example (C#)

This example shows how to add a gravity load to a static study.

```vb
  //------------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in  (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
  // 3. Verify that the specified model document exists.
 // 4. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the document.
 // 2. Activates Ready - 8 plies.
 // 3. Deletes two pressure loads from Ready - 8 plies.
 // 4. Adds the Gravity-1 load to Ready - 8 plies.
 // 5. Prints the Gravity-1 properties to the Immediate window.
 // 6. Meshes the part.
 // 7. Sets the solver type.
 // 8. Analyzes Ready - 8 plies.
  // 9. Inspect the Immediate window, the Simulation study tree,
 //    and the graphics area.
 //
  // NOTE: Because this part document is used elsewhere, do not save any changes.
  //-----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.cosworks;
 using System.Runtime.InteropServices;

 namespace AddGravityLoad_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 Part = default(ModelDoc2);
             string fileName = null;
             int errors = 0;
             int warnings = 0;
             int errCode = 0;
             int longstatus = 0;
             CosmosWorks COSMOSWORKS = default(CosmosWorks);
             CwAddincallback CWAddinCallBack = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWMesh mesh = default(CWMesh);
             CWStaticStudyOptions StaticOptions = default(CWStaticStudyOptions);
             CWLoadsAndRestraintsManager lrMgr = default(CWLoadsAndRestraintsManager);
             CWGravity Gravity = default(CWGravity);
             object dispEntity = null;
             string str1 = null;
             object var1 = null;
             double xval = 0;
             double yval = 0;
             double zval = 0;

             const double MeshEleSize = 1.4769;
             const double MeshTol = 0.073847;

             fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\tjoint.sldprt";
             Part = swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, 1, "", ref errors, ref warnings);

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;

             ActDoc = COSMOSWORKS.ActiveDoc;

             StudyMngr = ActDoc.StudyManager;
             StudyMngr.ActiveStudy = 1;
             Study = StudyMngr.GetStudy(StudyMngr.ActiveStudy);

             //Select top plane for gravity's direction reference
             str1 = "64,31,0,0,1,0,0,0,255,254,255,0,0,0,0,0,3,0,0,0";
             StringtoArray(str1, ref var1);
             dispEntity = Part.Extension.GetObjectByPersistReference3((var1), out longstatus);

             lrMgr = Study.LoadsAndRestraintsManager;

             //Delete pressure loads
             lrMgr.DeleteLoadsAndRestraints("Pressure-1");
             lrMgr.DeleteLoadsAndRestraints("Pressure-2");

             //Add gravity load
             Gravity = lrMgr.AddGravity(dispEntity, out errCode);
             Gravity.GetGravitationalAcclerationValues(out xval, out yval, out zval);
             Debug.Print("Gravity acceleration:");
             Debug.Print("  Direction 1: " + xval);
             Debug.Print("     Reverse? (true=yes, false=no) " + Gravity.ReverseDirectionAlongPlaneDir1_2);
             Debug.Print("  Direction 2: " + yval);
             Debug.Print("     Reverse? (true=yes, false=no) " + Gravity.ReverseDirectionAlongPlaneDir2_2);
             Debug.Print("  Normal direction: " + zval);
             Debug.Print("     Reverse? (true=yes, false=no) " + Gravity.ReverseDirectionNormalToPlane2);
             Debug.Print("  Units as defined in swsUnitSystem_e: " + Gravity.Unit);

             //Mesh
             mesh = Study.Mesh;
             mesh.MesherType = 0;
             mesh.Quality = 0;
             errCode = Study.CreateMesh(0, MeshEleSize, MeshTol);

             StaticOptions = Study.StaticStudyOptions;
             StaticOptions.SolverType = 2;

             //Run analysis
             errCode = Study.RunAnalysis();

         }

         public void StringtoArray(string inputSTR, ref object varEntity)
         {
             string[] PIDArray = null;
             byte[] PID = null;
             int i;

             // Parse string into an array
             PIDArray = inputSTR.Split(new char[] { ',' });

             //Convert string array to byte array
             int sizeArray = PIDArray.Length;
             PID = new byte[sizeArray];
             for (i = 0; i < PIDArray.Length; i++)
             {

                 PID[i] = Convert.ToByte(PIDArray[i]);
             }
             varEntity = PID;
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
