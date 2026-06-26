---
title: "Create and Modify Variable-pitch Helix Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Modify_Variable-pitch_Helix_Example_CSharp.htm"
---

# Create and Modify Variable-pitch Helix Example (C#)

This example shows how to create and modify a variable-pitch helix.

```
//--------------------------------------------
// Preconditions:
// 1. Specified part template exits.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens a new part document.
// 2. Selects Front Plane, creates a circle, and
//    and uses the circle to create a variable-pitch
//    helix feature named Helix/Spiral1.
// 3. Gets whether the Helix/Spiral1 feature is a
//    variable-pitch helix. If so:
//    a. Prints to the Immediate window the number
//       of regions.
//    b. Prints to the Immediate window
//       each region's diameter, pitch, height,
//       and revolution.
//    c. If second region of variable-pitch helix
//       is defined by height and revolution:
//       1. Modifies region's diameter, height, and
//          revolution values.
//       2. Prints to the Immediate window the status
//          of modifications made in previous step.
//    d. Deletes the last region in the Helix/Spiral1 feature and
//       prints the status of the deletion to the Immediate window.
//    e. Adds a new last region to the Helix/Spiral1 feature and
//       prints the status of the addition to the Immediate window.
//    - or -
//    Prints to the Immediate window that the Helix/Spiral1
//    feature is not a variable-pitch helix.
// 4. Examine the Immediate window.
//--------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace HelixCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            PartDoc swPart = default(PartDoc);
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchManager swSketchMgr = default(SketchManager);
            FeatureManager swFeatureMgr = default(FeatureManager);
            Feature swFeat = default(Feature);
            HelixFeatureData swHelixFeatData = default(HelixFeatureData);
            bool status = false;
            int i = 0;
            int helixType = 0;
            int helixStatus = 0;
            int[] helixRegionArray = new int[1];

            swPart = (PartDoc)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2015\\templates\\Part.prtdot", 0, 0, 0);
            swModel = (ModelDoc2)swPart;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Select plane on which to create circle
            //for variable-pitch helix
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", -0.0571253507530972, 0.0536428819342089, 0.00349118658744337, false, 0, null, 0);
            swSketchMgr = (SketchManager)swModel.SketchManager;
            swSketchMgr.InsertSketch(true);
            //Create circle for variable-pitch helix
            swSketchMgr.CreateCircle(0.007581, 0.053509, 0.0, 0.013533, 0.016475, 0.0);
            // Create a variable-pitch helix using the just-sketched circle
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            status = swFeatureMgr.InsertVariablePitchHelix(false, true, (int)swHelixDefinedBy_e.swHelixDefinedByHeightAndRevolution, 4.712388980385);
            status = swFeatureMgr.AddVariablePitchHelixFirstPitchAndDiameter(0.053, 0.05382625271268);
            status = swFeatureMgr.AddVariablePitchHelixSegment(0.0265, 0.05382625271268, 0.5);
            status = swFeatureMgr.AddVariablePitchHelixSegment(0.03975, 0.05382625271268, 0.75);
            status = swFeatureMgr.AddVariablePitchHelixSegment(0.046375, 0.05382625271268, 0.875);
            status = swFeatureMgr.AddVariablePitchHelixSegment(0.053, 0.05382625271268, 1);
            swFeat = swFeatureMgr.EndVariablePitchHelix();
            //Get variable-pitch helix
            swHelixFeatData = (HelixFeatureData)swFeat.GetDefinition();
            if (swHelixFeatData.VariablePitch)
            {
                Debug.Print("  Number of regions: " + swHelixFeatData.PitchCount);
                for (i = 1; i <= swHelixFeatData.PitchCount; i++)
                {
                    Debug.Print("   Region " + i + ":");
                    Debug.Print("      Diameter: " + swHelixFeatData.GetRegionParameterAtIndex(i, (int)swVariablePitchHelixRegionParameter_e.swVariablePitchHelixRegionParameter_Diameter));
                    Debug.Print("      Pitch: " + swHelixFeatData.GetRegionParameterAtIndex(i, (int)swVariablePitchHelixRegionParameter_e.swVariablePitchHelixRegionParameter_Pitch));
                    Debug.Print("      Height: " + swHelixFeatData.GetRegionParameterAtIndex(i, (int)swVariablePitchHelixRegionParameter_e.swVariablePitchHelixRegionParameter_Height));
                    Debug.Print("      Revolutions: " + swHelixFeatData.GetRegionParameterAtIndex(i, (int)swVariablePitchHelixRegionParameter_e.swVariablePitchHelixRegionParameter_Revolution));
                }
                //Modify region 2 of variable-pitch helix
                //defined by height and revolution
                helixType = swHelixFeatData.DefinedBy;

                switch (helixType)
                {
                    case (int)swHelixDefinedBy_e.swHelixDefinedByHeightAndRevolution:
                        if (i >= 2)
                        {
                            //Cannot change pitch
                            //Can change diameter, height, and revolution
                            //Revolution must be smaller than previous region's
                            //revolution and less than next region's revolution
                            Debug.Print("");
                            Debug.Print("Helix defined by height and revolution:");
                            Debug.Print("   Region modified: 2");
                            helixStatus = swHelixFeatData.SetRegionParameterAtIndex(2, (int)swVariablePitchHelixRegionParameter_e.swVariablePitchHelixRegionParameter_Diameter, 0.052);
                            Debug.Print("      Diameter modified (0 = success): " + helixStatus);
                            helixStatus = swHelixFeatData.SetRegionParameterAtIndex(2, (int)swVariablePitchHelixRegionParameter_e.swVariablePitchHelixRegionParameter_Height, 0.025);
                            Debug.Print("      Height modified (0 = success): " + helixStatus);
                            helixStatus = swHelixFeatData.SetRegionParameterAtIndex(2, (int)swVariablePitchHelixRegionParameter_e.swVariablePitchHelixRegionParameter_Revolution, 0.45);
                            Debug.Print("      Revolution modified (0 = success): " + helixStatus);
                        }
                        else
                        {
                            Debug.Print("Less than three regions in Helix/Spiral1 feature.)");
                        }
                        break;

                    case (int)swHelixDefinedBy_e.swHelixDefinedByHeightAndPitch:
                        //Cannot change revolution
                        //TODO: Add code for variable-pitch helix defined by height and pitch
                        break;

                    case (int)swHelixDefinedBy_e.swHelixDefinedByPitchAndRevolution:
                        //Cannot change height
                        //TODO: Add code for variable-pitch helix defined by pitch and revolution
                        break;
                }

                //Delete last region in the Helix/Spiral1 feature
                i = i - 1;
                helixRegionArray[0] = (int)i;
                Debug.Print("");
                status = swHelixFeatData.DeleteRecord(helixRegionArray);
                Debug.Print("Last region in Helix/Spiral1 deleted; i.e., region " + i + " was deleted: " + status);

                //Add new region to end of Region parameters table
                double[] record = new double[4];
                //Height
                record[0] = 0.055;
                //Number of revolutions
                record[1] = 1;
                //0 indicates that this value cannot be specified
                //for this type of variable-pitch helix (Height and Revolution)
                //Instead, SOLIDWORKS calculates it
                record[2] = 0;
                //Diameter
                record[3] = 0.05382625271268;
                status = swHelixFeatData.AddLastRecord(record);
                Debug.Print("New region 5 added as last record to Helix/Spiral1: " + status);

                status = swFeat.ModifyDefinition(swHelixFeatData, swModel, null);
            }
            else
            {
                Debug.Print("Helix is not variable pitch.");
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
