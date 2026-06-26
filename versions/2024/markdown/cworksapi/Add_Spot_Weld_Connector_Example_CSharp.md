---
title: "Get Spot Weld Connector Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Spot_Weld_Connector_Example_CSharp.htm"
---

# Get Spot Weld Connector Example (C#)

This example shows how to get the properties of a spot weld connector.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure the specified part exists.
 // 4. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the specified part.
 // 2. Activates the Ready study.
  // 3. Prints properties of Spot Weld Connector-1 to the Immediate window.
 // 4. Meshes the model.
 // 5. Analyzes Ready.
  // 6. Inspect the Immediate window, the Simulation study tree, and the
 //    graphics area.
 //
  // NOTE: Because this part is used elsewhere, do not save any changes.
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
 namespace AddSpotWeldConnector_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             CosmosWorks COSMOSWORKS = null;
             CwAddincallback CWObject = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWMesh CwMesh = default(CWMesh);
             ModelDoc2 Part = default(ModelDoc2);
             CWLoadsAndRestraintsManager LBCMgr = default(CWLoadsAndRestraintsManager);
             CWSpotWeldConnector spotWeldConnector = default(CWSpotWeldConnector);
             int longstatus = 0;
             int longwarnings = 0;
             int errCode = 0;
             double el = 0;
             double tl = 0;

             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\car_model.sldasm", 2, 0, "", ref longstatus, ref longwarnings);
             if (Part == null)
                 ErrorMsg(swApp, "Failed to open C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\car_model.sldasm");

             // Get SOLIDWORKS Simulation add-in
             CWObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (CWObject == null)
                 ErrorMsg(swApp, "Failed to get the Simulation add-in");
             COSMOSWORKS = CWObject.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "Failed to get CosmosWorks");

             // Get active document
             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "No active document");

             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "No CWStudyManager object");
             Study = StudyMngr.GetStudy(0);
             if (Study == null)
                 ErrorMsg(swApp, "No CWStudy object");

             StudyMngr.ActiveStudy = 0;

             LBCMgr = Study.LoadsAndRestraintsManager;
             if (LBCMgr == null)
                 ErrorMsg(swApp, "No CWLoadsAndRestraintsManager object");

             spotWeldConnector = (CWSpotWeldConnector)LBCMgr.GetLoadsAndRestraints(2, out errCode);
             Debug.Print("Spot Weld Connector-1");
             spotWeldConnector.SpotWeldConnectorBeginEdit();
             Debug.Print("  Source entity count: " + spotWeldConnector.GetSourceEntityCount());
             Debug.Print("  Target entity count: " + spotWeldConnector.GetTargetEntityCount());
             Debug.Print("  Location count: " + spotWeldConnector.GetSpotWeldLocationCount());
             Debug.Print("  Diameter: " + spotWeldConnector.SpotWeldDiameterValue);
             Debug.Print("  Diameter units as defined in swsLinearUnit_e: " + spotWeldConnector.SpotWeldDiameterUnit);
             spotWeldConnector.SpotWeldConnectorEndEdit();

             // Mesh model
             CwMesh = Study.Mesh;
             if (CwMesh == null)
                 ErrorMsg(swApp, "No CWMesh object");
             CwMesh.Quality = 1;
             CwMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);
             errCode = Study.CreateMesh(0, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Mesh failed");

             // Run analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " + errCode);

         }

         private void ErrorMsg(SldWorks SwApp, string Message)
         {
             swApp.SendMsgToUser2(Message, 0, 0);
             swApp.RecordLine("'*** WARNING - General");
             swApp.RecordLine("'*** " + Message);
             swApp.RecordLine("");

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
