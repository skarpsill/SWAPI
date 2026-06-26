---
title: "Add Spring Connector Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Spring_Connector_Example_CSharp.htm"
---

# Add Spring Connector Example (C#)

This example shows how to add a spring connector to a frequency study.

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
 // 2. Activates the Sample study.
 // 3. Deletes Connectors-2.
 // 4. Adds Spring Connector-4 to the Connectors folder in the Simulation study
 //    tree.
 // 5. Prints the properties of Spring Connector-4 to the Immediate window.
 // 6. Meshes the model.
 // 7. Analyzes Sample.
  // 8. Inspect the Immediate window, the Simulation Study tree, and the
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

 namespace AddSpringConnector_CSharp.csproj
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
         CWSpringConnector springConnector;
         CWMesh CwMesh;
         string str3;
         string str4;
         object[] varArray1 = new object[1];
         object[] varArray2 = new object[1];
         object pDisp3;
         object pDisp4;
         byte[] var20;
         byte[] var21;
         int errCode;
         double el;
         double tl;
         int longstatus;
         int longwarnings;

         public void Main()
         {
             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\Verification\\frequency_8.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref longstatus, ref longwarnings);
             Part = (ModelDoc2)swApp.ActiveDoc;

             COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             if (COSMOSObject == null)
                 ErrorMsg(swApp, "Failed to get the Simulation add-in");

             COSMOSWORKS = COSMOSObject.CosmosWorks;
             if (COSMOSWORKS == null)
                 ErrorMsg(swApp, "Failed to get COSMOSWORKS");

             ActDoc = COSMOSWORKS.ActiveDoc;
             if (ActDoc == null)
                 ErrorMsg(swApp, "Failed to get the active document");

             StudyMngr = ActDoc.StudyManager;
             if (StudyMngr == null)
                 ErrorMsg(swApp, "Failed to get the CWStudyManager object");

             Study = StudyMngr.GetStudy(0);
             if (Study == null)
                 ErrorMsg(swApp, "Failed to get the frequency study");

             StudyMngr.ActiveStudy = 0;

             str3 = "64,31,0,0,3,0,0,0,255,254,255,16,80,0,51,0,45,0,49,0,64,0,102,0,114,0,101,0,113,0,117,0,101,0,110,0,99,0,121,0,95,0,56,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,18,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,32,69,0,58,0,92,0,65,0,115,0,104,0,105,0,115,0,104,0,92,0,118,0,101,0,114,0,105,0,102,0,105,0,99,0,97,0,116,0,105,0,111,0,110,0,92,0,80,0,51,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,2,80,0,51,0,2,0,0,217,166,36,65,0,105,167,36,65,0,0,0,0,0,0,0,0,1,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,105,167,36,65,24,0,0,0,162,167,3";
             str3 = str3 + "6,65,4,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,162,167,36,65,0,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,162,167,36,65,1,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,162,167,36,65,1,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,162,167,36,65,3,0,0,0,0,0,0,0,0,0,0,0,0,0";

             str4 = "64,31,0,0,3,0,0,0,255,254,255,16,80,0,52,0,45,0,50,0,64,0,102,0,114,0,101,0,113,0,117,0,101,0,110,0,99,0,121,0,95,0,56,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,21,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,32,69,0,58,0,92,0,65,0,115,0,104,0,105,0,115,0,104,0,92,0,118,0,101,0,114,0,105,0,102,0,105,0,99,0,97,0,116,0,105,0,111,0,110,0,92,0,80,0,52,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,2,80,0,52,0,2,0,0,217,166,36,65,0,105,167,36,65,0,0,0,0,0,0,0,0,0,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,105,167,36,65,18,0,0,0,105,167";
             str4 = str4 + ",36,65,2,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,18,0,0,0,105,167,36,65,0,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,18,0,0,0,105,167,36,65,1,0,0,0,12,128,0,0,5,128,8,0,18,0,0,0,105,167,36,65,1,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,18,0,0,0,105,167,36,65,3,0,0,0,0,0,0,0,0,0,0,0,0,0";

             StringtoArray(str3, ref var20);
             pDisp3 = Part.Extension.GetObjectByPersistReference3((var20), out longstatus);

             StringtoArray(str4, ref var21);
             pDisp4 = Part.Extension.GetObjectByPersistReference3((var21), out longstatus);

             varArray1[0] = pDisp3;
             varArray2[0] = pDisp4;

             lrMngr = Study.LoadsAndRestraintsManager;
             lrMngr.DeleteLoadsAndRestraints("Connectors-2");

             // Add spring connector
             springConnector = lrMngr.AddSpringConnector((int)swsSpringConnectorType_e.swsSpringConnectoryTypeFlatParallelFaces, (varArray1), (varArray2), ref errCode);

             springConnector.SpringConnectorBeginEdit();
             springConnector.Unit = (int)swsUnit_e.swsUnitEnglish;
             springConnector.NormalRadialStiffnessValue = 800.0;
             springConnector.TangentialOrShearStiffnessValue = 100000.0;
             Debug.Print("Spring Connector-4");
             int sType = 0;
             int sSubType = 0;
             springConnector.GetSpringType(out sType, out sSubType);
             Debug.Print("  Type as defined in swsSpringType_e: " + sType);
             Debug.Print("  Sub-type as defined in swsSpringSubType_e: " + sSubType);
             Debug.Print("  Source entity count: " + springConnector.GetSourceEntityCount());
             Debug.Print("  Target entity count: " + springConnector.GetTargetEntityCount());
             springConnector.SpringConnectorEndEdit();
             Debug.Print("  Normal radial stiffness: " + springConnector.NormalRadialStiffnessValue);
             Debug.Print("  Preload force type as defined in swsPreloadForceType_e: " + springConnector.PreLoadForceType);
             Debug.Print("  Preload force: " + springConnector.PreLoadForceValue);
             Debug.Print("  Rotational stiffness: " + springConnector.RotationalStiffnessValue);
             Debug.Print("  Stiffness type as defined in swsStiffnessType_e: " + springConnector.StiffnessType);
             Debug.Print("  Tangential or shear stiffness: " + springConnector.TangentialOrShearStiffnessValue);
             Debug.Print("  Units of stiffness as defined in swsUnit_e: " + springConnector.Unit);

             // Mesh model
             CwMesh = Study.Mesh;
             if (CwMesh == null)
                 ErrorMsg(swApp, "Failed to get CWMesh object");

             CwMesh.Quality = 1;
             CwMesh.GetDefaultElementSizeAndTolerance((int)swsLinearUnit_e.swsLinearUnitMillimeters, out el, out tl);

             errCode = Study.CreateMesh((int)swsLinearUnit_e.swsLinearUnitMillimeters, el, tl);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to create mesh");

             // Run analysis
             errCode = Study.RunAnalysis();
             if (errCode != 0)
                 ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " + errCode);

         }

         public void StringtoArray(string inputSTR, ref byte[] varEntity)
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
