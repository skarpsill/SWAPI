---
title: "Create Frequency Study with Mixed Mesh Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Frequency_Study_with_Mixed_Mesh_Example_CSharp.htm"
---

# Create Frequency Study with Mixed Mesh Example (C#)

This example shows how to create a frequency study using a mixed mesh.

NOTE:To get persistent reference
identifiers (PIDs) for model selections, you can use[pidcollector.exe](GettingStarted-swsimulationapi.html)or IModelDocExtension::GetPersistReference3.

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure that the specified material library exists.
 // 4. Ensure that the specified model document exists.
 // 5. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the model.
 // 2. Creates a frequency mixed-mesh study.
 // 3. Applies material.
 // 4. Adds a fixed restraint.
 // 5. Adds a bonded contact set.
 // 6. Creates a mesh.
 // 7. Runs an analysis.
 // 8. Inspect the Immediate window.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 //---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.cosworks;
using System;
using System.Diagnostics;

namespace Macro1.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CosmosWorks COSMOSWORKS = default(CosmosWorks);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CwAddincallback COSMOSObject = default(CwAddincallback);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWModelDoc ActDoc = default(CWModelDoc);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWStudyManager StudyMngr = default(CWStudyManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWStudy Study = default(CWStudy);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWSolidManager SolidMgr = default(CWSolidManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWSolidComponent SolidComponent = default(CWSolidComponent);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWSolidBody SolidBody = default(CWSolidBody);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWShell Shell = default(CWShell);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWMesh CwMesh = default(CWMesh);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWResults CWResult = default(CWResults);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 Part = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWShellManager ShellMgr = default(CWShellManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWLoadsAndRestraintsManager LBCMgr = default(CWLoadsAndRestraintsManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWContactManager ContactMgr = default(CWContactManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWContactSet CWContactSet = default(CWContactSet);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWRestraint CWRes1 = default(CWRestraint);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object pDisp1 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object pDisp2 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object oselect1 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object oselect2 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object oselect3 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object oselect4 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object oselect5 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object oselect6 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}byte[] var1 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}byte[] var2 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}byte[] var3 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}byte[] var4 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}byte[] var5 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}byte[] var6 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}byte[] var8 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}byte[] var9 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] Freq = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string str1 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string str2 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string selection1 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string selection2 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string selection3 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string selection4 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string selection5 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string selection6 = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int status = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int warnings = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int errCode = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double el = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double tl = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int j = 0;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Open document
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\mixedmesh-1.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref status, ref warnings);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Part = (ModelDoc2)swApp.ActiveDoc;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get the SOLIDWORKS Simulation object
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (COSMOSObject == null) ErrorMsg("COSMOSObject object not found");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (COSMOSWORKS == null) ErrorMsg("COSMOSWORKS object not found");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Open and get active document
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (ActDoc == null) ErrorMsg("No active document", true);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Create new frequency study
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}StudyMngr = (CWStudyManager)ActDoc.StudyManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (StudyMngr == null) ErrorMsg("No CWStudyManager object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Study = (CWStudy)StudyMngr.CreateNewStudy3("Frequency_Mixed", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeFrequency, 0, out errCode);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (Study == null) ErrorMsg("Frequency study not created");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get selections for restraint
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Faces of the six holes in the solid
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}selection1 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}selection1 = selection1 + "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,16,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}StringtoArray(selection1, ref var1);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}oselect1 = Part.Extension.GetObjectByPersistReference3((var1), out status);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}selection2 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}selection2 = selection2 + "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,15,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}StringtoArray(selection2, ref var2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}oselect2 = Part.Extension.GetObjectByPersistReference3((var2), out status);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}selection3 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}selection3 = selection3 + "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,14,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}StringtoArray(selection3, ref var3);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}oselect3 = Part.Extension.GetObjectByPersistReference3((var3), out status);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}selection4 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}selection4 = selection4 + "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,11,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,6,0,0,0,0,0,0,0,0,0,0,0,0,0";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}StringtoArray(selection4, ref var4);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}oselect4 = Part.Extension.GetObjectByPersistReference3((var4), out status);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}selection5 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}selection5 = selection5 + "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,12,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,6,0,0,0,0,0,0,0,0,0,0,0,0,0";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}StringtoArray(selection5, ref var5);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}oselect5 = Part.Extension.GetObjectByPersistReference3((var5), out status);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}selection6 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}selection6 = selection6 + "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,13,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,6,0,0,0,0,0,0,0,0,0,0,0,0,0";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}StringtoArray(selection6, ref var6);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}oselect6 = Part.Extension.GetObjectByPersistReference3((var6), out status);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get selections for contact set
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Shell edge
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}str1 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,69,100,103,101,82,101,102,95,99,1,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}str1 = str1 + ",0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,24,0,0,0,26,50,104,66,9,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,10,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,1,0,0,0,0,0,0,0,14,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,0,0,0,0,0,0,0,0,0,0,0,0";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}StringtoArray(str1, ref var8);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pDisp1 = (object)Part.Extension.GetObjectByPersistReference3((var8), out status);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Solid face
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}str2 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}str2 = str2 + ",112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,24,0,0,0,26,50,104,66,11,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,0,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,10,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,1,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}StringtoArray(str2, ref var9);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pDisp2 = (object)Part.Extension.GetObjectByPersistReference3((var9), out status);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Create arrays
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] varArray2 = { oselect1, oselect2, oselect3, oselect4, oselect5, oselect6 };
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] varArray3 = { pDisp1 };
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] varArray4 = { pDisp2 };

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Add bonded contact set
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ContactMgr = (CWContactManager)Study.ContactManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("No CWContactManager object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWContactSet = (CWContactSet)ContactMgr.CreateContactSet2((int)swsContactType_e.swsContactTypeBonded, 0, (varArray3), (varArray4), out errCode);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("No CWContactSet object");
             Debug.Print(CWContactSet.ContactName + " is suppressed? (1=yes, 0=no) " + CWContactSet.State);

             // If contact set is suppressed, unsuppress it
             if (CWContactSet.State == 1)
                 errCode = ContactMgr.SuppressUnsuppressContactPair(CWContactSet.ContactName, 0);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Apply material to shell
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ShellMgr = Study.ShellManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (ShellMgr == null) ErrorMsg("No CWShellManager object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Shell = (CWShell)ShellMgr.GetShellAt(0, out errCode);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}status = Shell.SetLibraryMaterial("c:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Ductile Iron");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (status == 0) ErrorMsg("No material applied");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Define shell properties
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Shell.ShellBeginEdit();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Shell.Formulation = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Shell.ShellUnit = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Shell.ShellThickness = 5.0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}errCode = Shell.ShellEndEdit();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("Shell not created");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Apply material to solid
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidMgr = (CWSolidManager)Study.SolidManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (SolidMgr == null) ErrorMsg("No CWSolidManager object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidComponent = (CWSolidComponent)SolidMgr.GetComponentAt(1, out errCode);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("No solid component");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidBody = (CWSolidBody)SolidComponent.GetSolidBodyAt(0, out errCode);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("No solid body");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}status = SolidBody.SetLibraryMaterial2("c:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Ductile Iron");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (status == 0) ErrorMsg("No material applied");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Add fixed restraint
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}LBCMgr = (CWLoadsAndRestraintsManager)Study.LoadsAndRestraintsManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWRes1 = (CWRestraint)LBCMgr.AddRestraint((int)swsRestraintType_e.swsRestraintTypeFixed, (varArray2), null, out errCode);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("No fixed restraint created");

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Set meshing
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CwMesh = (CWMesh)Study.Mesh;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (CwMesh == null) ErrorMsg("No CWMesh object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CwMesh.Quality = 1;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CwMesh.GetDefaultElementSizeAndTolerance((int)swsLinearUnit_e.swsLinearUnitMillimeters, out el, out tl);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}errCode = Study.CreateMesh((int)swsLinearUnit_e.swsLinearUnitMillimeters, el, tl);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("Mesh failed");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Run analysis
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}errCode = Study.RunAnalysis();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("Analysis failed with error code as defined in swsRunAnalysisError_e: " + errCode);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get results
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWResult = (CWResults)Study.Results;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (CWResult == null) ErrorMsg("No CWResults object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Freq = CWResult.GetResonantFrequencies(out errCode);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("No frequency result");
             Debug.Print("Resonant frequencies:");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (j = 0; j < Freq.Length; j++)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print (Freq[j].ToString());
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}private void ErrorMsg(string Message)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.SendMsgToUser2(Message, 0, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.RecordLine("'*** WARNING - General");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.RecordLine("'*** " + Message);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.RecordLine("");
kadov_tag{{<spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}private void StringtoArray(string inputSTR, ref byte[] varEntity)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string[] PIDArray = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}byte[] PID = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int i;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Parse string into an array
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}PIDArray = inputSTR.Split(new char[] { ',' });
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Convert string array to byte array
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int sizeArray = PIDArray.Length;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}PID = new byte[sizeArray];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (i = 0; i < PIDArray.Length; i++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}PID[i] = Convert.ToByte(PIDArray[i]);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}varEntity = PID;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
