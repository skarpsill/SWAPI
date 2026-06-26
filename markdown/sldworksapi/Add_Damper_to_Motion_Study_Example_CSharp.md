---
title: "Add Damper to Motion Study Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Damper_to_Motion_Study_Example_CSharp.htm"
---

# Add Damper to Motion Study Example (C#)

This example shows how to add a damper to a motion study.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\wrench.sldasm.
 // 2. Click View > MotionManager if the MotionStudy tabs are not visible.
 // 3. Click Tools > Add-ins > SOLIDWORKS Motion to enable motion analysis.
 // 4. Reference the SOLIDWORKS MotionStudy type library.
 //
 // Postconditions:
 // 1. Adds a damper feature, LinearDamper1, between the grips of the wrench.
 // 2. Examine the Motion Analysis to verify.
 //
 // NOTE: Because the assembly is used elsewhere, do not save changes.
 //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using System.Windows.Forms;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.swmotionstudy;
 using System.Runtime.InteropServices;
 namespace SimulationDamperFeatureData_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             MotionStudyManager swMotionMgr = default(MotionStudyManager);
             MotionStudy swMotionStudy1 = default(MotionStudy);
             SimulationDamperFeatureData swDamperFeat = default(SimulationDamperFeatureData);
             bool boolstatus = false;
             Feature swFeat = default(Feature);
             SelectionMgr swSelMgr = default(SelectionMgr);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             // Get the MotionManager
             swMotionMgr = (MotionStudyManager)swModelDocExt.GetMotionStudyManager();

             if ((swMotionMgr == null))
             {
                 return;
             }

             // Get and activate "MotionStudy1_Distance=0.5in"
             swMotionStudy1 = swMotionMgr.GetMotionStudy("MotionStudy1_Distance=0.5in");

             if ((swMotionStudy1 == null))
             {
                 MessageBox.Show("MotionStudy1_Distance=0.5in is not available.");
                 return;
             }

             // Activate swMotionStudy1
             swMotionStudy1.Activate();

             // Define Damper feature
             swDamperFeat = (SimulationDamperFeatureData)swMotionStudy1.CreateDefinition((int)swFeatureNameID_e.swFmAEMLinearDamper);

             if (swDamperFeat == null)
             {
                 Debug.Print("ERROR: Creation of Damper feature data object failed.");
                 return;
             }

             // Select the faces for the Damper's endpoints
             Face2 swFace1 = default(Face2);
             Face2 swFace2 = default(Face2);

             swModel.ShowNamedView2("*Left", 3);
             swModel.ViewZoomtofit2();
             boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.03344586330968, 0.0525345575174, 0, true, 0, null, 0);
             swFace1 = (Face2)swSelMgr.GetSelectedObject6(1, -1);
             boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.02244533711473, 0.0131288302002, 0.0002238961779386,  true, 0,  null, 0);
             swFace2 = (Face2)swSelMgr.GetSelectedObject6(2, -1);

             // Set Damper's characteristics
             swDamperFeat.SetEndPoints(swFace1, swFace2);

             // Create Damper feature
             swFeat = (Feature)swMotionStudy1.CreateFeature(swDamperFeat);

             if (swFeat == null)
             {
                 Debug.Print(" ERROR: Creation of the Damper feature failed.");
             }
             else
             {
                 Debug.Print("Type of Damper as defined in swSimulationDamperType_e: " + swDamperFeat.Type);
             }

         }

         public SldWorks swApp;

     }
 }
```
