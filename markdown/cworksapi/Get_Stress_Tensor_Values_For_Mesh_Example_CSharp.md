---
title: "Get Stress Tensor Values For Mesh Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Stress_Tensor_Values_For_Mesh_Example_CSharp.htm"
---

# Get Stress Tensor Values For Mesh Example (C#)

This example shows how to get the stress tensor values for a mesh in a static study.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Open public_documents\samples\Simulation Examples\tutor1.sldprt.
 // 4. Open an Immediate window.
 //
 // Postconditions:
 // 1. Activates the Ready static study.
 // 2. Meshes and runs the study.
  // 3. Gets the stress tensor values for all nodes of element 10 of the mesh.
 // 4. Inspect the Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  // ---------------------------------------------------------------------------
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

 namespace GetStressTensorValues_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             CosmosWorks COSMOSWORKS = default(CosmosWorks);
             CwAddincallback CWAddinCallBack = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWMesh CWMesh = default(CWMesh);
             CWResults CWResult = default(CWResults);
             int errCode = 0;
             double el = 0;
             double tl = 0;
             object[] Stress = null;
             object[] elem = null;
             int i = 0;

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("CosmosWorks.CosmosWorks");
             if (CWAddinCallBack == null)
                 ErrorMsg(swApp, "No CWAddinCallBack object");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "No CosmosWorks object");

             //Get active document
             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "No active document");

             //Get Ready study
             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No study manager object");
             StudyMngr.ActiveStudy = 0;
             Study = StudyMngr.GetStudy(0);
             if (Study == null)
                 ErrorMsg(swApp, "No study object");

             //Mesh
             CWMesh = Study.Mesh;
             if (CWMesh == null)
                 ErrorMsg(swApp, "No mesh object");
             CWMesh.Quality = 1;
             CWMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);
             errCode = Study.CreateMesh(0, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed");

             //Run analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed");

             //Get results
             CWResult = Study.Results;
             if (CWResult == null)
                 ErrorMsg(swApp, "No result object");

             //Get two-dimensional array of stress tensor values at all nodes of element 10 of the mesh
             Stress = (object[])CWResult.GetStressTensorValuesForAllNodesOfElement(10, (int)swsStrengthUnit_e.swsStrengthUnitPascal, 1, out errCode);
             if (errCode != 0)
             {
                 ErrorMsg(swApp, "Error getting stress tensor values as defined in swsNodalResultsOfElementError_e: " + errCode);
             }
             else
             {
                 for (i = Stress.GetLowerBound(0); i <= Stress.GetUpperBound(0); i++)
                 {
                     elem = (object[])Stress[i];
                     if (i == 0)
                     {
                         Debug.Print("Stress tensor values for all nodes of element 10 of the mesh:");
                         Debug.Print("");
                     }
                     else
                     {
                         Debug.Print("===================================================");
                     }
                     Debug.Print("Element index: " + elem[0]);
                     Debug.Print("Shell face (0=top, 1=bottom, -1=none): " + elem[1]);
                     Debug.Print("Node index: " + elem[2]);
                     Debug.Print("Stress tensor 1 (N/m**2): " + elem[3]);
                     Debug.Print("Stress tensor 2 (N/m**2): " + elem[4]);
                     Debug.Print("Stress tensor 3 (N/m**2): " + elem[5]);
                     Debug.Print("Stress tensor 4 (N/m**2): " + elem[6]);
                     Debug.Print("Stress tensor 5 (N/m**2): " + elem[7]);
                     Debug.Print("Stress tensor 6 (N/m**2): " + elem[8]);
                 }
             }

         }

         public void ErrorMsg(SldWorks SwApp, string Message)
         {
             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```
