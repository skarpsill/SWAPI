---
title: "Get Forces for Selected Beams (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Forces_for_Selected_Beams_Example_CSharp.htm"
---

# Get Forces for Selected Beams (C#)

## Get Forces for Selected Beams Example (C#)

This example shows how to get the force load values for structural members.

```vb
//--------------------------------------------------------------------------
// Preconditions:
// 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
//    Tools > Add-ins > SOLIDWORKS Simulation > OK).

// 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference

//    (in the IDE, click Project > Add Reference > .NET >
//    SolidWorks.Interop.cosworks > OK).
// 3. Open the Immediate window.
// 4. Open a SOLIDWORKS model that has structural members and a
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Simulation static study with structural force loads on the
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}beams.
// 5. Select the Simulation study tab.
// 6. Click the Run button on the Simulation CommandManager to
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}refresh the study results.
// 7. In the Simulation Study tree, select the beams for which
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}you want to know their force loads.
// 8. Run the macro.
//
// Postconditions: The selected beams' forces are printed to the
// the Immediate window.
//-------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.cosworks;
using System;
using System.Diagnostics;
namespace ListBeamForcesCSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectionMgr swSelMgr = default(SelectionMgr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CosmosWorks COSMOSWORKS = default(CosmosWorks);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CwAddincallback COSMOSObject = default(CwAddincallback);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWModelDoc ActDoc = default(CWModelDoc);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWStudyManager StudyMngr = default(CWStudyManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWStudy Study = default(CWStudy);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWBeamManager BeamMgr = default(CWBeamManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWResults Results = default(CWResults);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int actStudy = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int beamForce = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int nbrSteps = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int unit = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int errCode = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] selBeams = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int nbrSelectedBeams = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int i = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int k = 0;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Connect to SOLIDWORKS
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = (SelectionMgr)swModel.SelectionManager;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get the SOLIDWORKS Simulation object
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}COSMOSObject = (CwAddincallback)swApp.GetAddInObject("Sldworks.Simulation");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (COSMOSObject == null) ErrorMsg("COSMOSObject object not found");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (COSMOSWORKS == null) ErrorMsg("COSMOSWORKS object not found");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get the active document
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (ActDoc == null) ErrorMsg("No active document");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get the active study
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}StudyMngr = (CWStudyManager)ActDoc.StudyManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (StudyMngr == null) ErrorMsg("No CWStudyManager object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}actStudy = StudyMngr.ActiveStudy;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Study = (CWStudy)StudyMngr.GetStudy(actStudy);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (Study == null) ErrorMsg("Study not created");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get the results
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Results = (CWResults)Study.Results;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get the selected beams' forces
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BeamMgr = (CWBeamManager)Study.BeamManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}beamForce = (int)swsBeamForceType_e.swsBeamForceMomentDirection1;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}nbrSteps = 1;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}unit = (int)swsUnit_e.swsUnitSI;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}nbrSelectedBeams = swSelMgr.GetSelectedObjectCount2(-1);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}selBeams = new object[nbrSelectedBeams];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (k = 1; k <= nbrSelectedBeams; k++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}selBeams[k-1] = (object)swSelMgr.GetSelectedObject6(k, -1);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Object arrBeamForces = Results.GetBeamForcesForEntities(beamForce, nbrSteps, (selBeams), unit, out errCode);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Array BeamForces = (Array)arrBeamForces;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (i = 0; i <= BeamForces.GetUpperBound(0); i++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}string beamForceElement = "";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}beamForceElement = Convert.ToString(BeamForces.GetValue(i));
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print (beamForceElement);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Error routine
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}private void ErrorMsg(string Message)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.SendMsgToUser2(Message, 0, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.RecordLine("'*** WARNING - General");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.RecordLine("'*** " + Message);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.RecordLine("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}

}
```
