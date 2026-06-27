---
title: "Create Frequency Study with Solid Mesh Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Frequency_Study_with_Solid_Mesh_Example_CSharp.htm"
---

# Create Frequency Study with Solid Mesh Example (C#)

This example shows how to create a frequency study with solid mesh.

```vb
//--------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in  (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure that the specified model exists.
 // 4. Ensure that the specified material library exists.
 // 5. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the assembly.
 // 2. Specifies the default frequency study results plots.
 // 3. Creates a frequency study.
 // 4. Applies the same material to all bodies.
 // 5. Creates a mesh with default global size and tolerance parameters.
 // 6. Sets the number of frequencies.
 // 7. Runs the analysis.
 // 8. Gets the result frequencies and mass participation factors.
 // 9. Inspect the results plots and the Immediate window.
 //
 // NOTE: Because the model is used elsewhere, do not save any changes.
 // -----------------------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.cosworks;
using System;
namespace CreateFrequencyStudySolidMeshCSharp.csproj
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
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWMesh CwMesh = default(CWMesh);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWResults CWResult = default(CWResults);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWFrequencyStudyOptions FrequencyOptions = default(CWFrequencyStudyOptions);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int status = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int warnings = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int errCode = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int errorCode = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int CompCount = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int BodyCount = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int j = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int i = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int returnValue = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object Freq = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object MassPart = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double el = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double tl = 0;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get SOLIDWORKS Simulation object
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (COSMOSObject == null) ErrorMsg("COSMOSObject object not found");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}COSMOSWORKS = (CosmosWorks)COSMOSObject.CosmosWorks;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (COSMOSWORKS == null) ErrorMsg("COSMOSWORKS object not found");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get active document
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\shaft.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref status, ref warnings);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (ActDoc == null) ErrorMsg("No active document");
```

```vb
            // Add default frequency study result plot of resultant amplitude
             errCode = ActDoc.AddDefaultFrequencyOrBucklingStudyPlot(true, 0, true, (int)swsFrequencyBucklingResultDisplacementComponentTypes_e.swsFrequencyBucklingDisplacement_URES);
```

```vb
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Create new frequency study
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}StudyMngr = (CWStudyManager)ActDoc.StudyManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (StudyMngr == null) ErrorMsg("No CWStudyManager object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Study = (CWStudy)StudyMngr.CreateNewStudy3("Frequency", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeFrequency, (int)swsMeshType_e.swsMeshTypeSolid, out errCode);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (Study == null) ErrorMsg("Study not created");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get number of solid components
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidMgr = (CWSolidManager)Study.SolidManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (SolidMgr == null) ErrorMsg("No CWSolidManager object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CompCount = SolidMgr.ComponentCount;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Apply SOLIDWORKS material to rest of components
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidBody = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidComponent = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (j = 0; j <= (CompCount - 1); j++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}SolidComponent = (CWSolidComponent)SolidMgr.GetComponentAt(j, out errorCode);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}BodyCount = SolidComponent.SolidBodyCount;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}for (i = 0; i <= (BodyCount - 1); i++)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}SolidBody = (CWSolidBody)SolidComponent.GetSolidBodyAt(i, out errCode);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("No solid body");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}returnValue = SolidBody.SetLibraryMaterial("c:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Ductile Iron (SN)");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}if (returnValue != 1) ErrorMsg("No material applied");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}SolidBody = null;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Set meshing
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CwMesh = (CWMesh)Study.Mesh;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (CwMesh == null) ErrorMsg("No mesh object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CwMesh.Quality = 1;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CwMesh.GetDefaultElementSizeAndTolerance(0, out el, out tl);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}errCode = Study.CreateMesh(0, el, tl);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("Mesh failed");

             // Set frequency study options
             FrequencyOptions = Study.FrequencyStudyOptions;
             if (FrequencyOptions == null)
                     ErrorMsg("No CWFrequencyStudyOptions object");

             FrequencyOptions.Options = (int)swsFrequencyStudyOption_e.swsFrequencyStudyOptionNumberFrequencies;
             FrequencyOptions.NoOfFrequencies = 8;

             Debug.Print("Study: " + Study.Name);
             Debug.Print("  Option as defined in swsFrequencyStudyOption_e: " + FrequencyOptions.Options);
             if (FrequencyOptions.Options == 1)
             {
                     Debug.Print("  Upper-bound frequency: " + FrequencyOptions.UpperBoundFrequency);
             }
             else if (FrequencyOptions.Options == 0)
             {
                     Debug.Print("  Number of frequencies: " + FrequencyOptions.NoOfFrequencies);
                     Debug.Print("  Calculate frequencies around a specified frequency? (true=yes, false=no): " + FrequencyOptions.UseLowerBoundFrequency2);
                     if (FrequencyOptions.UseLowerBoundFrequency2)
                     {
                         Debug.Print("    Lower bound frequency: " + FrequencyOptions.LowerBoundFrequency);
                     }
             }

             Debug.Print("  Result folder: " + FrequencyOptions.ResultFolder);
             Debug.Print("  Solver type as defined in swsSolverType_e: " + FrequencyOptions.SolverType);
             Debug.Print("  Use soft spring to stabilize the model? (true=yes, false=no): " + FrequencyOptions.UseSoftSpring2);
             double zeroStrainTemp = 0;
             int tempUnit = 0;
             FrequencyOptions.GetZeroStrainTemperature(out zeroStrainTemp, out tempUnit);
             Debug.Print("  Flow/Thermal Effects:");
             Debug.Print("    Temperature source as defined in swsThermalOption_e: " + FrequencyOptions.ThermalResults);
             Debug.Print("    Temperature source:");
             if (FrequencyOptions.ThermalResults == 1)
             {
                     Debug.Print("        Thermal study: " + FrequencyOptions.ThermalStudyName);
                     Debug.Print("        Time step of transient thermal study: " + FrequencyOptions.TimeStep);
             }
             else if (FrequencyOptions.ThermalResults == 2)
             {
                     Debug.Print("        SOLIDWORKS Flow Simulation results file: " + FrequencyOptions.FlowTemperatureFile);
             }
             else
             {
                     Debug.Print("        Model");
             }
             Debug.Print("    Reference temperature at zero strain: " + zeroStrainTemp);
             Debug.Print("    Import fluid pressure loads from SOLIDWORKS Flow Simulation? (true=yes, false=no): " + FrequencyOptions.CheckFlowPressure2);
             if (FrequencyOptions.CheckFlowPressure2)
             {
                     Debug.Print("        SOLIDWORKS Flow Simulation results file: " + FrequencyOptions.FlowPressureFile);
                     Debug.Print("        Use reference pressure offset from Flow Simulation? (1=yes, 0=no): " + FrequencyOptions.ReferencePressureOption);
                     if (FrequencyOptions.ReferencePressureOption == 1)
                     {
                         Debug.Print("          Reference pressure offset: " + FrequencyOptions.DefinedReferencePressure);
                     }
                     Debug.Print("        Run as legacy study and import only the normal component of the pressure load? (true=yes, false=no): " + FrequencyOptions.CheckRunAsLegacy2);
             }

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Run analysis
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}errCode = Study.RunAnalysis();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("Analysis failed");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get results: frequencies and mass participation factors
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWResult = (CWResults)Study.Results;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (CWResult == null) ErrorMsg("No result object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Freq = CWResult.GetResonantFrequencies(out errCode);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MassPart = CWResult.GetMassParticipation(out errCode);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}private void ErrorMsg(string Message)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.SendMsgToUser2(Message, 0, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.RecordLine("'*** WARNING - General");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.RecordLine("'*** " + Message);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.RecordLine("");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
