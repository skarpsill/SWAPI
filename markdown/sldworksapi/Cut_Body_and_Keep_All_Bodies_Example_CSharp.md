---
title: "Cut Body and Keep All Bodies Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Cut_Body_and_Keep_All_Bodies_Example_CSharp.htm"
---

# Cut Body and Keep All Bodies Example (C#)

This example shows how to cut a body and keep all bodies.

```
//----------------------------------------------------------------------------
// Preconditions:
//  1. Verify that the specified part document template exists.
//  2. Open the Immediate window.
//
// Postconditions:
// 1. Opens a new part document.
// 2. Creates a body.
// 3. Splits the body into two bodies.
// 4. Examine the graphics area and Immediate window.
//-----------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public PartDoc swPart;
        ModelDoc2 Part;
        bool boolstatus;
        Feature Feature;

        public void Main()
        {
            //Open new part document
            Part = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2015\\templates\\part.prtdot", 0, 0, 0);

            //Set up event
            swPart = (PartDoc)Part;
            AttachEventHandlers();

            //Create body
            CreateBodiesAndSketch();
            boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, false, 0, null, 0);
            Feature = (Feature)Part.FeatureManager.FeatureCut3(true, false, false, (int)swEndConditions_e.swEndCondThroughAll, (int)swEndConditions_e.swEndCondBlind, 0.01, 0.01, false, false, false, false, 0.01745329251994, 0.01745329251994, false, false, false, false, false, true, true, false, false, false, (int)swStartConditions_e.swStartSketchPlane, 0, false);
             if ((Feature == null))
            {
                Debug.Print("No feature created.");
            }
        }

        public void CreateBodiesAndSketch()
        {
            //Create body
            boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -0.06869486923422, 0.06291203863612, -0.006492164309718, false, 0, null, 0);
            Part.ClearSelection2(true);
            Part.SketchRectangle(-0.0424567617866, 0.0388405707196, 0, 0.05638579404467, -0.03750124069479, 0, false);
            Part.ShowNamedView2("*Trimetric", 8);
            Part.ClearSelection2(true);
            boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            boolstatus = Part.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            Part.FeatureManager.FeatureExtrusion3(true, false, false, 0, 0, 0.12, 0.01, false, false, false,
            false, 0.01745329251994, 0.01745329251994, false, false, false, false, false, false, false,
            0, 0, false);
            Part.ClearSelection2(true);

            //Create sketch for cut feature
            boolstatus = Part.Extension.SelectByID2("", "FACE", -0.02909828822015, 0.03884057071963, 0.09843602253397, false, 0, null, 0);
            Part.SketchManager.InsertSketch(true);
            Part.ClearSelection2(true);
            object[] vSkLines = null;
            vSkLines = (object[])Part.SketchManager.CreateCornerRectangle(-0.0628943705795, -0.07743122635196, 0, 0.1160562766823, -0.04532565168643, 0);
            Part.ClearSelection2(true);
            boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            boolstatus = Part.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);

        }

        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }

        public void AttachSWEvents()
        {
            swPart.PromptBodiesToKeepNotify += this.swPart_PromptBodiesToKeepNotify;
        }

        private int swPart_PromptBodiesToKeepNotify(object swFeat, ref object bodies)
        {
            Debug.Print("PartDoc_PromptBodiesToKeepNotify fired.");
            Feature theFeature = default(Feature);
            object[] bodiesArr = null;
            bodiesArr = (object[])bodies;
            if ((swFeat != null))
            {
                theFeature = (Feature)swFeat;
                object[] bodiesToKeep = new object[1];
                //Change BodyOption to Body1 or Body2 to show other options
                string BodyOption = null;
                BodyOption = "AllBodies";
                switch (BodyOption)
                {
                    case "AllBodies":
                        theFeature.SetBodiesToKeep(true, bodiesToKeep, (int)swInConfigurationOpts_e.swThisConfiguration, null);
                        break;
                    case "Body1":
                        bodiesToKeep[0] = bodiesArr[0];
                        theFeature.SetBodiesToKeep(false, bodiesToKeep, (int)swInConfigurationOpts_e.swThisConfiguration, null);
                        break;
                    case "Body2":
                        bodiesToKeep[0] = bodiesArr[1];
                        theFeature.SetBodiesToKeep(false, bodiesToKeep, (int)swInConfigurationOpts_e.swThisConfiguration, null);
                        break;
                }
            }
            return 1;
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
