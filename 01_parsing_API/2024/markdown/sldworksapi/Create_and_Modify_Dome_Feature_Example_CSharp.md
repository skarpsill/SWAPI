---
title: "Create and Modify Dome Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Modify_Dome_Feature_Example_CSharp.htm"
---

# Create and Modify Dome Feature Example (C#)

This example shows how to create and modify a dome feature.

```
//---------------------------------------------------------
// Preconditions:
// 1. Verify that the part document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Edits Sketch1, sketches an ellipse, and creates a boss feature.
// 3. Selects a face on the boss feature and
//    inserts a dome feature.
// 4. Prints to the Immediate window some
//    dome feature data.
// 5. Reverses the direction of the dome feature.
// 6. Examine the Immediate window, graphics area,
//    and FeatureManager design tree.
//
// NOTE: Because the part is used elsewhere, do not
// save changes.
//----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace DomeFeatureData2CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchManager swSketchMgr = default(SketchManager);
            SketchSegment swSketchSegment = default(SketchSegment);
            Feature swFeature = default(Feature);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            DomeFeatureData2 swDomeFeatureData = default(DomeFeatureData2);
            object[] faces = null;
            Face2 swFace = default(Face2);
            Body2 oneBody = default(Body2);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            //Open model document to which to add a dome feature
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\box.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Open sketch to which to add a sketch of an ellipse
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
            swModel.EditSketch();
            swModel.ClearSelection2(true);

            //Sketch an ellipse
            swModel.ShowNamedView2("*Top", 5);
            swSketchMgr = (SketchManager)swModel.SketchManager;
            swSketchSegment = (SketchSegment)swSketchMgr.CreateEllipse(-0.0761501034873036, 0.0490523248480422, 0, -0.0513492425103863, 0.0490523248480422, 0, -0.0761501034873036, 0.0545451329838695, 0);
            swModel.ClearSelection2(true);
            swSketchMgr.InsertSketch(true);
            swModel.ViewZoomtofit2();
            swModel.ShowNamedView2("*Dimetric", 9);

            //Insert dome feature
            status = swModelDocExt.SelectByID2("", "FACE", -0.0930732824141103, 0.0299999999999727, -0.0482299571224303, true, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("", "FACE", -0.0930732824141103, 0.0299999999999727, -0.0482299571224303, false, 1, null, 0);
            swModel.InsertDome(0.01, false, true);

            //Get and modify dome feature data
            status = swModelDocExt.SelectByID2("Dome1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swDomeFeatureData = (DomeFeatureData2)swFeature.GetDefinition();
            status = swDomeFeatureData.AccessSelections(swModel, null);
            Debug.Print("Is dome feature elliptical? " + swDomeFeatureData.Elliptical);
            Debug.Print("Height of dome: " + swDomeFeatureData.Height);
            Debug.Print("Number of faces on dome feature: " + swDomeFeatureData.GetFaceCount());
            faces = (object[])swDomeFeatureData.Faces;
            foreach (object aFace in faces)
            {
                swFace = (Face2)aFace;
                oneBody = (Body2)swFace.GetBody();
                Debug.Print("Name of body for this dome feature face: " + oneBody.Name);
            }
            //Change direction of dome feature to concave
            swDomeFeatureData.ReverseDir = true;
            status = swFeature.ModifyDefinition(swDomeFeatureData, swModel, null);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
