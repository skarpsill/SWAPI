---
title: "Apply Material to Bodies Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Apply_Material_to_Bodies_Example_CSharp.htm"
---

# Apply Material to Bodies Example (C#)

This example shows how to apply user-defined and SOLIDWORKS-defined
materials to different bodies.

```vb
//---------------------------------------------------------------------------
// Preconditions:
// 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
//    Tools > Add-ins > SOLIDWORKS Simulation > OK).

// 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference

//    (in the IDE, click Project > Add Reference > .NET >
//    SolidWorks.Interop.cosworks > OK).
// 3. Verify that the specified material library exists.
// 4. Verify that the specified assembly exists.
//
// Postconditions:
// 1. Opens the assembly.
// 2. Creates a nonlinear study.
// 3. Gets the number of components.
// 4. Applies materials to all components.
// 5. Expand the Parts folder in the Simulation Study tree
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}to verify step 4.
//
// NOTE: Because this assembly is used elsewhere, do not save changes.
//-------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.cosworks;
using System;
using System.Diagnostics;
namespace SimulationApplyMaterialsBodiesCSharp.csproj
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
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int errorCode = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int status = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int warnings = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int errCode = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int CompCount = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int j = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWMaterial CWMat = default(CWMaterial);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int returnValue = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string SName = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int materialProperty = 0;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get SOLIDWORKS Simulation object>
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (COSMOSObject == null) ErrorMsg("No CwAddincallback object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (COSMOSWORKS == null) ErrorMsg("No COSMOSWORKS object");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Open and get document
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\basketball_hoop.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref status, ref warnings);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (ActDoc == null) ErrorMsg("No active document");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Create new nonlinear study
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}StudyMngr = (CWStudyManager)ActDoc.StudyManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (StudyMngr == null) ErrorMsg("No CWStudyManager object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Study = (CWStudy)StudyMngr.CreateNewStudy("Nonlinear", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeNonlinear, (int)swsMeshType_e.swsMeshTypeSolid, out errCode);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (Study == null) ErrorMsg("No CWStudy object");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get number of solid components
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidMgr = (CWSolidManager)Study.SolidManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (SolidMgr == null) ErrorMsg("No CWSolidManager object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CompCount = SolidMgr.ComponentCount;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidComponent = (CWSolidComponent)SolidMgr.GetComponentAt(0, out errorCode);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (SolidComponent == null) ErrorMsg("No CWSolidComponent object");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get name of solid component
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SName = SolidComponent.ComponentName;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Apply user-defined material for the first component in the tree
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidBody =(CWSolidBody) SolidComponent.GetSolidBodyAt(0, out errCode);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("No solid body");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (SolidBody == null) ErrorMsg("No CWSolidBody object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWMat = (CWMaterial)SolidBody.GetDefaultMaterial();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWMat.MaterialUnits = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (CWMat == null) ErrorMsg("No CWMaterial object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWMat.MaterialName = "Alloy Steel";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWMat.SetPropertyByName("EX", 210000000000.0, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Property EX: " + CWMat.GetPropertyByName((int)swsUnitSystem_e.swsUnitSystemSI, "EX", out materialProperty));
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWMat.SetPropertyByName("NUXY", 0.28, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWMat.SetPropertyByName("GXY", 79000000000.0, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWMat.SetPropertyByName("DENS", 7700, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWMat.SetPropertyByName("SIGXT", 723825600, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWMat.SetPropertyByName("SIGYLD", 620422000, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWMat.SetPropertyByName("ALPX", 1.3E-05, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWMat.SetPropertyByName("KX", 50, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWMat.SetPropertyByName("C", 460, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}errCode = SolidBody.SetSolidBodyMaterial(CWMat);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("Failed to apply material");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Apply a different SOLIDWORKS Simulation library material to rest of components
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidBody = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidComponent = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (j = 1; j <= (CompCount - 1); j++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}SolidComponent = (CWSolidComponent)SolidMgr.GetComponentAt(j, out errorCode);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}SName = SolidComponent.ComponentName;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}SolidBody = (CWSolidBody)SolidComponent.GetSolidBodyAt(0, out errCode);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("No CWSolidBody object");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}returnValue = SolidBody.SetLibraryMaterial("c:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "2024 Alloy (SN)");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (returnValue == 0) ErrorMsg("No material applied");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}SolidBody = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Error function
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
