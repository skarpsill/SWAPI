---
title: "Add Elastic Support Fixture Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Elastic_Support_Connector_Example_CSharp.htm"
---

# Add Elastic Support Fixture Example (C#)

This example shows how to add an elastic support fixture to a frequency study.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
  // 3. Ensure that the specified model document exists.
 // 4. Open an Immediate window.
 //
 // Postconditions:
 // 1. Opens the model.
 // 2. Gets the Ready frequency study.
 // 3. Deletes Fixture-1 from Ready.
 // 4. Adds an Elastic Support-1 fixture to Ready.
 // 5. Prints the properties of Elastic Support-1 to the Immediate window.
 // 6. Meshes the model.
 // 7. Analyzes Ready.
  // 8. Prints the resonant frequency of each mode to the Immediate window.
  // 9. Inspect the Immediate window, the Simulation Study tree, and the
 //    graphics area.
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
 namespace AddElasticSupport_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         CosmosWorks COSMOSWORKS;
         CwAddincallback COSMOSObject;
         CWModelDoc ActDoc;
         CWStudyManager StudyMngr;
         CWStudy Study;
         CWLoadsAndRestraintsManager lrMngr;
         CWLoadsAndRestraints lr;
         CWElasticConnector elasticSupport;
         CWMesh CwMesh;
         CWResults CWResult;
         string str3;
         string str4;
         object[] varArray1 = new object[2];
         object[] dir = new object[2];
         object[] Freq;
         object pDisp3;
         object pDisp4;
         byte[] var20;
         byte[] var21;
         int errCode;
         int i;
         double el;
         double tl;
         int longstatus;
         int longwarnings;

         public void Main()
         {
             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\shaft.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref longstatus, ref longwarnings);
             swApp.ActivateDoc2("shaft", false, ref longstatus);
             Part = (ModelDoc2)swApp.ActiveDoc;

             COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (COSMOSObject == null)
                 ErrorMsg(swApp, "Failed to get the Simulation add-in");

             COSMOSWORKS = COSMOSObject.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "Failed to get COSMOSWORKS");

             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "Failed to get active document");

             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "Failed to get the CWStudyManager object");

             Study = StudyMngr.GetStudy(0);
             if (Study == null)
                 ErrorMsg(swApp, "Failed to get the frequency study");

             str3 = "64,31,0,0,3,0,0,0,255,254,255,28,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,45,0,49,0,64,0,115,0,104,0,97,0,102,0,116,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,20,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,63,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,";
             str3 = str3 + "101,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,20,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,2,0,0,130,66,58,52,0,144,22,28,65,1,0,0,0,0,0,0,0,34,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,52,0,0,0,0,0,0,0,144,22,28,65,8,0,0,0,157,67,58,52,1,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,8,0,0,0,157,67,58,52,0,0,0,0,255,255,255,255,3,128,0,0,5,128,8,0,8,0,0,0,157,67,58,52,8,0,0,0,12,128,0,0,5,128,8,0,8,0,0,0,157,67,58,52,1,0,0,0,255,255,255,255,3,128,0,0,5,128,8,0,8,0,0,0,157,67,58,52,2,0,0,0,0,0,0,0,0,0,0,0,0,0";
             StringtoArray(str3, ref var20);
             pDisp3 = Part.Extension.GetObjectByPersistReference3((var20), out longstatus);

             str4 = "64,31,0,0,3,0,0,0,255,254,255,28,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,45,0,50,0,64,0,115,0,104,0,97,0,102,0,116,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,21,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,63,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,";
             str4 = str4 + "101,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,20,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,2,0,0,130,66,58,52,0,144,22,28,65,1,0,0,0,0,0,0,0,34,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,52,0,0,0,0,0,0,0,144,22,28,65,8,0,0,0,157,67,58,52,1,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,8,0,0,0,157,67,58,52,0,0,0,0,255,255,255,255,3,128,0,0,5,128,8,0,8,0,0,0,157,67,58,52,8,0,0,0,12,128,0,0,5,128,8,0,8,0,0,0,157,67,58,52,1,0,0,0,255,255,255,255,3,128,0,0,5,128,8,0,8,0,0,0,157,67,58,52,2,0,0,0,0,0,0,0,0,0,0,0,0,0";
             StringtoArray(str4, ref var21);
             pDisp4 = Part.Extension.GetObjectByPersistReference3((var21), out longstatus);

             varArray1[0] = new DispatchWrapper(pDisp3);
             varArray1[1] = new DispatchWrapper(pDisp4);

             lrMngr = Study.LoadsAndRestraintsManager;

             // Delete Fixture-1
             lrMngr.DeleteLoadsAndRestraints("Fixture-1");

             // Add elastic support fixture
             elasticSupport = lrMngr.AddElasticConnector((varArray1), ref errCode);

             lr = lrMngr.GetLoadsAndRestraints(0, out errCode);
             dir = (object[])lr.GetDirection();
             Debug.Print("Fixture " + lr.Name);
             Debug.Print("  Direction: " + dir[0] + ", " + dir[1] + ", " + dir[2]);
             Debug.Print("  Number of entities: " + lr.EntityCount);
             Debug.Print("  Suppression state as defined in swsSuppressionState_e: " + lr.State);
             Debug.Print("  Type of fixture as defined in swsLoadsAndRestraintsType_e: " + lr.Type);

             elasticSupport.ElasticConnectorBeginEdit();

             Debug.Print("  Stiffness");
             Debug.Print("    Normal: " + elasticSupport.NormalStiffnessValue);
             Debug.Print("    Shear: " + elasticSupport.ShearStiffnessValue);
             Debug.Print("  Units as defined in swsUnit_e: " + elasticSupport.Unit);

             elasticSupport.ElasticConnectorEndEdit();

             // Mesh model
             CwMesh = Study.Mesh;
             if (CwMesh == null)
                 ErrorMsg(swApp, "Failed to get the CWMesh object");

             CwMesh.Quality = 1;
             CwMesh.GetDefaultElementSizeAndTolerance((int)swsLinearUnit_e.swsLinearUnitMillimeters, out el, out tl);

             errCode = Study.CreateMesh((int)swsLinearUnit_e.swsLinearUnitMillimeters, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create mesh");

             // Run analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " + errCode);

             // Get resonant frequency of each mode
             CWResult = Study.Results;
             if (CWResult == null)
                 ErrorMsg(swApp, "Failed to get results object", true);

             Freq = (object[])CWResult.GetResonantFrequencies(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get resonant frequencies", true);

             Debug.Print("");
             Debug.Print("Study " + Study.Name);
             Debug.Print("  Resonant frequencies (mode number, radians/second, cycles/second, period in seconds):");
             for (i = 0; i <= Freq.GetUpperBound(0); i++)
             {
                 Debug.Print("    " + Freq[i]);
             }

         }

         private void StringtoArray(string inputSTR, ref byte[] varEntity)
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
