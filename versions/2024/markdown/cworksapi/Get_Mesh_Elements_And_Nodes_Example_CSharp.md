---
title: "Get Mesh Elements and Nodes Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Mesh_Elements_And_Nodes_Example_CSharp.htm"
---

# Get Mesh Elements and Nodes Example (C#)

This example shows how to get the elements and nodes of a solid mesh.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
  //    (in the IDE, click Project > Add Reference > .NET >
  //    SolidWorks.Interop.cosworks > OK).
 // 3. Open public_documents\Simulation Examples\tutor1.sldprt.
 // 4. Open the Immediate window.
 //
 // Postconditions:
 // 1. Activates the Ready study.
 // 2. Creates a solid mesh.
 // 3. Gets the elements and nodes of the solid mesh.
  // 4. Gets the elements and nodes at a depth of 0.001m in the solid mesh.
 // 5. Runs the study.
 // 6. Inspect the Immediate window.
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
 namespace GetMeshElementsAndNodes_CSharp.csproj
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

             int errCode = 0;
             double el = 0;
             double tl = 0;
             int num = 0;
             object idList = null;
             object normalNum = null;
             object normalVec = null;

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

             //Get the elements of this solid mesh
             num = CWMesh.GetElementList(0, out idList);
             Debug.Print("Number of elements in the mesh: " + num);

             //Get the nodes of this solid mesh
             num = CWMesh.GetNodeList(0, out idList);
             Debug.Print("Number of nodes in the mesh: " + num);

             //Get the elements at a depth of 0.001m in this solid mesh
             num = CWMesh.GetSolidElementList(0.001, 2, out idList);
             Debug.Print("Number of elements at a depth of 0.001m: " + num);

             //Get the nodes at a depth of 0.001m in this solid mesh
             num = CWMesh.GetSolidNodeList(0.001, 2, out idList);
             Debug.Print("Number of nodes at a depth of 0.001m: " + num);

             //Get the nodes and normal vectors at the surface of this solid mesh
             num = CWMesh.GetSurfaceNodesAndNormals(out idList, out normalNum, out normalVec);
             Debug.Print("Number of surface nodes: " + num);

             //Run analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: "  + errCode);

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
