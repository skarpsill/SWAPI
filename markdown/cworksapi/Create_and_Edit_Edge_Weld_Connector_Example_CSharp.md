---
title: "Create and Edit Edge Weld Connector Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_and_Edit_Edge_Weld_Connector_Example_CSharp.htm"
---

# Create and Edit Edge Weld Connector Example (C#)

This example shows how to create and edit an edge weld connector.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Open public_documents\samples\tutorial\api\tjoint.sldprt.
 //
 // Postconditions: Creates and modifies Edge Weld Connector-3.
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
 namespace EdgeWeldConnector_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 Part = default(ModelDoc2);
             int errCode = 0;
             CosmosWorks COSMOSWORKS = default(CosmosWorks);
             CwAddincallback CWAddinCallBack = default(CwAddincallback);
             CWModelDoc ActDoc = default(CWModelDoc);
             CWStudyManager StudyMngr = default(CWStudyManager);
             CWStudy Study = default(CWStudy);
             CWLoadsAndRestraintsManager LoadAndRestraintMngr = default(CWLoadsAndRestraintsManager);
             CWEdgeWeldConnector theCurrentLoad = default(CWEdgeWeldConnector);
             CWEdgeWeldConnector theNewLoad = default(CWEdgeWeldConnector);
             byte[] var1 = null;
             byte[] var2 = null;
             byte[] var4 = null;
             object pDisp1 = null;
             object pDisp2 = null;
             object pDisp4 = null;
             object FirstFace = null;
             object SecondFace = null;
             int NWeakMaterial = 0;
             double DUltimateTensileStrength = 0;
             int NTensileStrengthUnit = 0;
             double DCorrelationFactor = 0;
             double DPartialSafetyFactor = 0;
             bool BIsEstimatedWeldSize = false;
             int nElectrodeMaterial = 0;
             double dWeldStrength = 0;
             int nWeldStrengthUnit = 0;
             int nFOSOption = 0;
             double dFOS = 0;
             bool bEstimatedWeldSize = false;
             double dEstimatedWeldSize = 0;
             int nEstimatedWeldSizeUnit = 0;
             int EdgeWeldType = 0;
             bool WeldOrientation = false;
             bool InducedBendingMomentIncluded = false;
             int CodeType = 0;
             ArrayList PIDCollection = new ArrayList();

             CWAddinCallBack = (CwAddincallback)swApp.GetAddInObject("CosmosWorks.CosmosWorks");
             COSMOSWORKS = CWAddinCallBack.CosmosWorks;
             ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
             StudyMngr = (CWStudyManager)ActDoc.StudyManager;
             StudyMngr.ActiveStudy = 0;
             Study = StudyMngr.GetStudy(StudyMngr.ActiveStudy);
             LoadAndRestraintMngr = Study.LoadsAndRestraintsManager;

             PIDCollection = PIDInitializer();

             Part = (ModelDoc2)swApp.ActiveDoc;

             SelectByPID("selection1", PIDCollection, ref var1);
             SelectByPID("selection2", PIDCollection, ref var2);
             SelectByPID("selection4", PIDCollection, ref var4);

             pDisp1 = (object)Part.Extension.GetObjectByPersistReference((var1)); //face
             pDisp2 = (object)Part.Extension.GetObjectByPersistReference((var2)); //face
             pDisp4 = (object)Part.Extension.GetObjectByPersistReference((var4)); //edge

             theCurrentLoad = LoadAndRestraintMngr.GetEdgeWeldConnector(5, errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get edge weld connector");

             object[] varArray9 = { pDisp4 };
             theNewLoad = LoadAndRestraintMngr.AddEdgeWeldConnector(pDisp1, pDisp2, varArray9, 0, 0, out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to add edge weld connector");

             errCode = theNewLoad.SetEdgeWeldType(3);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to set edge weld type");

             EdgeWeldType = theNewLoad.GetEdgeWeldType(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get edge weld type");

             FirstFace = theNewLoad.GetFirstFace(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get Face Set1");

             SecondFace = theNewLoad.GetSecondFace(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get Face Set2");

             errCode = theNewLoad.ReplaceFacesThenAutoGenerateTouchingEdges(0, pDisp1, pDisp2);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to replace faces and find touching edges");

             object[] var = (object[])theNewLoad.GetEdgeList(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get edge list");

             object[] varArray = { var[0] };
             errCode = theNewLoad.ReplaceFacesAndEdges(0, pDisp1, pDisp2, varArray);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to replace faces and edges");

             object[] varArray2 = { var[1] };
             errCode = theNewLoad.AddEdges(0, varArray2);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to add edges");

             errCode = theNewLoad.RemoveEdges(0, varArray);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to remove edges");

             errCode = theNewLoad.SetEdgeWeldType(3);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to set edge weld type");

             errCode = theNewLoad.SetWeldOrientation(true);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to set whether to show weld orientation");

             WeldOrientation = theNewLoad.IsWeldOrientation(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get whether to show weld orientation");

             errCode = theNewLoad.SetInducedBendingMomentIncluded(true);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to set whether induced bending moment is included");

             InducedBendingMomentIncluded = theNewLoad.IsInducedBendingMomentIncluded(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get whether induced bending moment is included");

             CodeType = theNewLoad.GetCodeType(out errCode);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get weld code");

             //American Standard weld sizing
             errCode = theNewLoad.SetCodeType(0);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to set American Standard weld code");

             errCode = theNewLoad.SetWeldSizingSettingUS(4, 100.1, 4, 1, 1, true, 98, 0);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to set American Standard weld sizing");

             errCode = theNewLoad.GetWeldSizingSettingUS(out nElectrodeMaterial, out dWeldStrength, out nWeldStrengthUnit, out nFOSOption, out dFOS, out bEstimatedWeldSize, out dEstimatedWeldSize, out nEstimatedWeldSizeUnit);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get American Standard weld sizing");

             //European weld sizing
             errCode = theNewLoad.SetCodeType(1);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to set european weld code");

             errCode = theNewLoad.SetWeldSizingSettingEuro(1, 155.2, 4, 1, 1, true, 98, 0);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to set european weld sizing");

             errCode = theNewLoad.GetWeldSizingSettingEuro(out NWeakMaterial, out DUltimateTensileStrength, out NTensileStrengthUnit, out DCorrelationFactor, out DPartialSafetyFactor, out BIsEstimatedWeldSize, out dEstimatedWeldSize, out nEstimatedWeldSizeUnit);
             if (errCode != 0)
                 ErrorMsg(swApp, "Failed to get european weld sizing");

         }

         private void SelectByPID(string PIDName, ArrayList PIDCollection, ref byte[] varEntity)
         {
             // Select by PID
             byte[] PID = null;
             string[] PIDVariant = null;
             string PIDString = null;
             int i = 0;

             // Get string from array
             PIDString = "";
             switch (PIDName)
             {
                 case "selection1":
                     PIDString = (string)PIDCollection[0];
                     break;
                 case "selection2":
                     PIDString = (string)PIDCollection[1];
                     break;
                 case "selection3":
                     PIDString = (string)PIDCollection[2];
                     break;
                 default:
                     break;
             }

             // Parse the string into an array
             PIDVariant = PIDString.Split(new char[] { ',' });

             // Convert string array to byte array
             int sizeArray = PIDVariant.Length;
             PID = new byte[sizeArray];
             for (i = 0; i < PIDVariant.Length - 1; i++)
             {
                 PID[i] = Convert.ToByte(PIDVariant[i]);
             }
             varEntity = PID;
         }

         public ArrayList PIDInitializer()
         {

             ArrayList PIDCollection = new ArrayList();

             string selection1 = null;
             string selection2 = null;
             string selection4 = null;

             //Faces

            selection1 = "233,35,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,4,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,78,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,115,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,116,0,117,0,116,0,111,0,114,0,105,0,97,0,108,0,92,0,97,0,112,0,105,0,92,0,116,0,106,0,111,0,105,0,110,0,116,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,6,116,0,106,0,111,0,105,0,110,0,116,0,2,0,";
             selection1 = selection1 + "0,239,130,43,72,255,254,255,0,255,254,255,0,0,176,178,110,16,0,0,0,0,0,0,0,0,0,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,176,178,110,16,45,0,0,0,80,132,43,72,1,0,0,0,255,255,1,0,16,0,109,111,84,111,112,69,100,103,101,73,100,82,101,112,95,99,0,0,5,128,8,0,45,0,0,0,80,132,43,72,1,0,0,0,12,128,0,0,5,128,8,0,45,0,0,0,80,132,43,72,1,0,0,0,0,0,255,255,1,0,19,0,109,111,66,111,116,116,111,109,69,100,103,101,73,100,82,101,112,95,99,0,0,5,128,8,0,45,0,0,0,80,132,43,72,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0";
             selection1 = selection1 + ",Type=1;
            selection2 = "233,35,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,4,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,78,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,115,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,116,0,117,0,116,0,111,0,114,0,105,0,97,0,108,0,92,0,97,0,112,0,105,0,92,0,116,0,106,0,111,0,105,0,110,0,116,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,6,116,0,106,0,111,0,105,0,110,0,116,0,2,";
             selection2 = selection2 + "0,0,239,130,43,72,255,254,255,0,255,254,255,0,0,176,178,110,16,0,0,0,0,0,0,0,0,0,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,176,178,110,16,26,0,0,0,36,131,43,72,1,0,0,0,255,255,1,0,16,0,109,111,84,111,112,69,100,103,101,73,100,82,101,112,95,99,0,0,5,128,8,0,26,0,0,0,36,131,43,72,1,0,0,0,0,0,255,255,1,0,19,0,109,111,66,111,116,116,111,109,69,100,103,101,73,100,82,101,112,95,99,0,0,5,128,8,0,26,0,0,0,36,131,43,72,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0";
             selection2 = selection2 + ",Type=1";

             //Edge

            selection4 = "233,35,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,69,100,103,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,4,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,78,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,115,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,116,0,117,0,116,0,111,0,114,0,105,0,97,0,108,0,92,0,97,0,112,0,105,0,92,0,116,0,106,0,111,0,105,0,110,0,116,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,6,116,0,106,0,111,0,105,0,110,0,116,0,2,";
             selection4 = selection4 + "0,0,239,130,43,72,255,254,255,0,255,254,255,0,0,176,178,110,16,0,0,0,0,0,0,0,0,0,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,176,178,110,16,26,0,0,0,36,131,43,72,1,0,0,0,0,0,255,255,1,0,21,0,109,111,76,101,102,116,84,114,105,109,69,100,103,101,73,100,82,101,112,95,99,0,0,5,128,8,0,46,0,0,0,139,132,43,72,3,128,0,0,5,128,8,0,45,0,0,0,80,132,43,72,1,0,0,0,1,0,0,0,12,128,0,0,5,128,8,0,46,0,0,0,139,132,43,72,3,128,0,0,5,128,8,0,45,0,0,0,80,132,43,72,1,0,0,0,1,0,0,0,12,128,0,0,5,128,8,0,46,0,0,0,139,132,43,72,3,128,0,0,5,128,8,0,45,0,0,0,80,132,43,72,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0";
             selection4 = selection4 + ",Type=1";

             //Store constants in a collection
             PIDCollection.Add(selection1);
             PIDCollection.Add(selection2);
             PIDCollection.Add(selection4);

             return PIDCollection;
         }

         private void ErrorMsg(SldWorks SwApp, string Message)
         {
             SwApp.SendMsgToUser2(Message, 0, 0);
             SwApp.RecordLine("'*** WARNING - General");
             SwApp.RecordLine("'*** " + Message);
             SwApp.RecordLine("");
         }

         public SldWorks swApp;

     }
 }
```
