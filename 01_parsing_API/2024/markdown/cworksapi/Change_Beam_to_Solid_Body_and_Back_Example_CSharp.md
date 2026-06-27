---
title: "Change Beam to Solid Body and Back Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Change_Beam_to_Solid_Body_and_Back_Example_CSharp.htm"
---

# Change Beam to Solid Body and Back Example (C#)

This example shows how to change a beam to a solid body and then back
to a beam.

```vb
//---------------------------------------------------------------------------
// Preconditions:
// 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
//    Tools > Add-ins > SOLIDWORKS Simulation > OK).

// 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference

//    (in the IDE, click Project > Add Reference > .NET >
//    SolidWorks.Interop.cosworks > OK).
// 3. Open the Immediate window.

// 4. Ensure that the specified part exists.
//
// Postconditions: Examine the the Immediate window to verify
// kadov_tag{{</spaces>}}that beams were converted to solid bodies and then back to beams.
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}You can also expand and examine the Simulation Study tree to verify the
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}macro.
//
// NOTES: Because the part document is used elsewhere, do not save kadov_tag{{</spaces>}}changes.
//-------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.cosworks;
using System;
using System.Diagnostics;
namespace BeamToSolidSolidToBeamCSharp.csproj
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
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWBeamManager BeamMgr = default(CWBeamManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWBeamBody BeamBody = default(CWBeamBody);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWSolidManager SolidMgr = default(CWSolidManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWSolidComponent SolidComponent = default(CWSolidComponent);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWSolidBody SolidBody = default(CWSolidBody);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int nbrBeamBodies = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int beamBodyType = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int errors = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int warnings = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int errCode = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int j = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int nbrSolidComponents = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int nbrSolidBodies = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int k = 0;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Get the SOLIDWORKS Simulation object
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (COSMOSObject == null) ErrorMsg("No CwAddincallback object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (COSMOSWORKS == null) ErrorMsg("No COSMOSWORKS object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Open and get the active document
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\Beams\\Beam_Truss.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (ActDoc == null) ErrorMsg("No active document");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Get the study
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}StudyMngr = (CWStudyManager)ActDoc.StudyManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (StudyMngr == null) ErrorMsg("No CWStudyManager object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}StudyMngr.ActiveStudy = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Study = (CWStudy)StudyMngr.GetStudy(0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (Study == null) ErrorMsg("No study at that index");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Get and set beams to solids and solids to beams
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Beams...");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BeamMgr = (CWBeamManager)Study.BeamManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}nbrBeamBodies = BeamMgr.BeamCount;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" Number of beams: " + nbrBeamBodies);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BeamBody = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Convert beams to solid bodies
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (j = 0; j <= (nbrBeamBodies - 1); j++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}BeamBody = (CWBeamBody)BeamMgr.GetBeamBodyAt(0, out errCode);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("No beam body");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Name of beam body: " + BeamBody.BeamBodyName);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}beamBodyType = BeamBody.BeamType;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (beamBodyType == 0)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}BeamBody.ConvertToSolidBody();
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Beam converted to solid body");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}BeamBody = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" ");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Convert solid bodies to beams
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Solid components and bodies...");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get solid bodies and components
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidMgr = (CWSolidManager)Study.SolidManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (SolidMgr == null) ErrorMsg("No CWSolidManager object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}nbrSolidComponents = SolidMgr.ComponentCount;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" Number of solid components: " + nbrSolidComponents);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (j = 0; j <= (nbrSolidComponents - 1); j++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}SolidComponent = (CWSolidComponent)SolidMgr.GetComponentAt(j, out errCode);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (SolidComponent == null) ErrorMsg("No solid component");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Name of solid components: " + SolidComponent.ComponentName);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Get solid bodies
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}nbrSolidBodies = SolidComponent.SolidBodyCount;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Number of solid bodies: " + nbrSolidBodies);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}for (k = 0; k <= (nbrSolidBodies - 1); k++)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}SolidBody = (CWSolidBody)SolidComponent.GetSolidBodyAt(0, out errCode);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("No solid body");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}Name of solid body: " + SolidBody.SolidBodyName);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}SolidBody.ConvertToBeamBody();
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Solid body converted to beam");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}SolidBody = null;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}private void ErrorMsg(string Message)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.SendMsgToUser2(Message, 0, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.RecordLine("'*** WARNING - General");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.RecordLine("'*** " + Message);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.RecordLine("");
kadov_tag{{<spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
