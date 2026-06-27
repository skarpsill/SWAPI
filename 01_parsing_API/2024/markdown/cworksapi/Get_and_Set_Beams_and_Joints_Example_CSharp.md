---
title: "Get and Set Beams and Joints Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_and_Set_Beams_and_Joints_Example_CSharp.htm"
---

# Get and Set Beams and Joints Example (C#)

This example shows how to get and set beams and joints.

```vb
//--------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure that the specified part exists.
 // 4. Ensure that the specified material library exists.
 // 5. Open the Immediate window.
 //
 // Postconditions:
 // 1. Creates static study, frame.
 // 2. Prints beam information to the Immediate window.
 // 3. Applies Plain Carbon Steel material to all beams.
 // 4. Calculates joints for all beams and displays a neutral axis for
 //    each beam.
 // 5. Prints the pinball tolerance value and unit to the Immediate window.
 // 6. Creates a mixed mesh and prints its type and state to the
 //    Immediate window.
 //
 // NOTES:
 // *  Creates beam elements by default for parts with structural members.
 // *  Because the part document is used elsewhere, do not save any changes.
 //----------------------------------------------------------------------------
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
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWBeamManager BeamMgr = default(CWBeamManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWBeamBody BeamBody = default(CWBeamBody);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWJoints Joints = default(CWJoints);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CWMesh Mesh = default(CWMesh);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int nbrBeamBodies = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int beamBodyType = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double ElementSize = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double Tolerance = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int errors = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int warnings = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int errCode = 0;
            bool boolCode = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int j = 0;
             bool keepJointUpdates = true;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Get the SOLIDWORKS Simulation object
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}COSMOSObject = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (COSMOSObject == null) ErrorMsg("COSMOSObject object not found");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}COSMOSWORKS = COSMOSObject.CosmosWorks;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (COSMOSWORKS == null) ErrorMsg("COSMOSWORKS object not found");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Open and get the active document
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\weldments\\weldment_box2.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ActDoc = (CWModelDoc)COSMOSWORKS.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (ActDoc == null) ErrorMsg("No active document");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Create new static study named frame
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}StudyMngr = (CWStudyManager)ActDoc.StudyManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (StudyMngr == null) ErrorMsg("StudyMngr object not there");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Study = (CWStudy)StudyMngr.CreateNewStudy3("frame", (int)swsAnalysisStudyType_e.swsAnalysisStudyTypeStatic, 0, out errCode);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (Study == null) ErrorMsg("Study not created");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Get and set beam info
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BeamMgr = (CWBeamManager)Study.BeamManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}nbrBeamBodies = BeamMgr.BeamCount;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Beams...");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" Number of beams: " + nbrBeamBodies);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BeamBody = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (j = 0; j <= (nbrBeamBodies - 1); j++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}BeamBody = (CWBeamBody)BeamMgr.GetBeamBodyAt(j, out errCode);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("No beam body");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Name of beam body: " + BeamBody.BeamBodyName);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}beamBodyType = BeamBody.BeamType;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (beamBodyType == 0)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Type of beam body: beam");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Type of beam body: truss");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
                 Debug.Print("      Beam cross-section properties:");

                 Debug.Print("         Maximum distance from the shear center to the furthest point: " + BeamBody.BeamDistForMaxShearStress);

                 Debug.Print("         Beam shear:");

                 Debug.Print("           Direction 1: " + BeamBody.BeamShearY);

                 Debug.Print("           Direction 2: " + BeamBody.BeamShearZ);

                 Debug.Print("         Beam torsional stiffness constant: " + BeamBody.BeamTorsionalConstant);

                 Debug.Print("           Units of length as defined in swsLinearUnit_e: " + BeamBody.BeamTorsionalConstantUnit);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}boolCode = BeamBody.SetLibraryMaterial2("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\sldmaterials\\solidworks materials.sldmat", "Plain Carbon Steel");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (boolCode == false) ErrorMsg("No material applied");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}BeamBody = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Calculate joints
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Joints = (CWJoints)BeamMgr.GetJointGroup(out errCode);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" ");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Joints...");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("No joint group");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Joints.JointsBeginEdit();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Joints.IncludeAllSelectedBeam = true;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Joints.IncludeDisplayNeutralAxis = true;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Joints.CalculateJoints();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Joints.JointsEndEdit();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" Pinball radius: " + Joints.PinBallRadius * 0.001);
```

```vb
            keepJointUpdates = Joints.IncludeKeepModifiedJointOnUpdate;
            if (keepJointUpdates == true)
            {
               Debug.Print(" Keep joint updates: yes");
            }
               else
            Debug.Print(" Keep joint udpates: no");
            Debug.Print(" Overwrite pinball value: " + Joints.IncludeTreatAsJointForClearanceLessThan);
```

```vb
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}switch (Joints.PinBallRadiusUnit)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 0:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Pinball radius unit: mm");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 1:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Pinball radius unit: cm");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 2:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Pinball radius unit: m");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 3:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Pinball radius unit: in");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 4:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Pinball radius unit: ft");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 5:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Pinball radius unit: ft-in");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 6:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Pinball radius unit: am");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 7:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Pinball radius unit: nm");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 8:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Pinball radius unit: micron");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 9:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Pinball radius unit: mil");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 10:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Pinball radius unit: MicroIn");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Mesh the part
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Mesh = Study.Mesh;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (Mesh == null) ErrorMsg("No mesh object");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Mesh.Quality = (int)swsMeshQuality_e.swsMeshQualityHigh;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Mesh.GetDefaultElementSizeAndTolerance((int)swsLinearUnit_e.swsLinearUnitMillimeters, out ElementSize, out Tolerance);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}errCode = Study.CreateMesh((int)swsLinearUnit_e.swsLinearUnitMillimeters, ElementSize, Tolerance);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (errCode != 0) ErrorMsg("Mesh failed");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" ");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Mesh...");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" Time to create mesh (hh:mm:ss): " + Mesh.TimeToCompleteMesh);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}switch (Mesh.MeshType)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 0:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Mesh type: solid");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 1:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Mesh type: midsurface");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 2:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Mesh type: surface");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 3:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Mesh type: mixed");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 4:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Mesh type: beam");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" Number of mesh controls: " + Mesh.MeshControlCount);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}switch (Mesh.MeshState)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 0:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Mesh state: no mesh");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 1:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Mesh state: exists and is current");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 2:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Mesh state: exists and is not current");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 3:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Mesh state: failed");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 4:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Mesh state: interrupted");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
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
