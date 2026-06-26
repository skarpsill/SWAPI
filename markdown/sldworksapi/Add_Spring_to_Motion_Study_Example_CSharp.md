---
title: "Add Spring to Motion Study Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Spring_to_Motion_Study_Example_CSharp.htm"
---

# Add Spring to Motion Study Example (C#)

This example shows how to add a spring to a motion study.

```vb
 //---------------------------------------------------------------------------
 // Preconditions: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
 // 1. Open public_documents\samples\tutorial\api\wrench.sldasm.
 // kadov_tag{{<spaces>}}2. Verify that the MotionManager tab is visible. If it is not visible,
 // kadov_tag{{<spaces>}}   click View > MotionManager.
 // kadov_tag{{<spaces>}}3. Right-click the project, select Add Reference, click Browse, and
 //    select install_dir\api\redist\SolidWorks.Interop.swmotionstudy.dll.
 // 4. Open the Immediate window.
 //
 // Postconditions:
 // 1. Adds a spring feature between the grips of the wrench.
 // 2. Examine the Immediate window.
 //
 // kadov_tag{{<spaces>}}NOTE: Because the assembly is used elsewhere, do not save changes.
 //--------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SwMotionStudy;
using System;
using System.Diagnostics;
namespace ExampleCS.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MotionStudyManager swMotionMgr;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MotionStudy swMotionStudy1;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SimulationSpringFeatureData swSpringFeat;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Feature swFeat;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectionMgr swSelMgr;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc as ModelDoc2;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager as SelectionMgr;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get the MotionManager
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swMotionMgr = swModelDocExt.GetMotionStudyManager() as MotionStudyManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if ((swMotionMgr == null))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get "MotionStudy1_Distance=0.5in"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swMotionStudy1 = swMotionMgr.GetMotionStudy("MotionStudy1_Distance=0.5in");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if ((swMotionStudy1 == null))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swApp.SendMsgToUser("MotionStudy1_Distance=0.5in is not available.");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Activate swMotionStudy1
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swMotionStudy1.Activate();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Define spring feature
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSpringFeat = swMotionStudy1.CreateDefinition((int)swFeatureNameID_e.swFmAEMLinearMotionSpring) as SimulationSpringFeatureData;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (swSpringFeat == null)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("ERROR: Creation of Spring feature data object failed.");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Select spring's endpoints
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Face2 swFace1;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Face2 swFace2;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ShowNamedView2("*Left", 3);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.03344586330968, 0.0525345575174, 0, true, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFace1 = swSelMgr.GetSelectedObject6(1, -1) as Face2;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.02244533711473, 0.0131288302002, 2.238961779386E-04, true, 0, null,
0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFace2 = swSelMgr.GetSelectedObject6(2, -1) as Face2;

kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}// Set spring's characteristics
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSpringFeat.SetEndPoints(swFace1, swFace2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSpringFeat.CoilDiameter = 0.0102;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSpringFeat.NumberOfCoils = 3;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSpringFeat.WireDiameter = 0.00152;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSpringFeat.FreeLength = 0.02;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Create Spring feature
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeat = swMotionStudy1.CreateFeature(swSpringFeat) as Feature; kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (swFeat == null)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" ERROR: Creation of the Spring feature failed.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Type of the feature added: " + swFeat.GetTypeName2());
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}

             Debug.Print("Type of spring as defined in swSpringType_e: " + swSpringFeat.Type.ToString());
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
