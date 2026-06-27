---
title: "Change Wrap Feature Face Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Wrap_Feature_Face_Example_CSharp.htm"
---

# Change Wrap Feature Face Example (C#)

This example shows how to insert a wrap feature and change the face on which to apply a wrap feature.

```
//-----------------------------------------------------------------------------
// Preconditions: Verify that the part to open exists.
//
// Postconditions:
// 1. Opens the part document.
// 2. Sketches a rectangle on the top plane.
// 3. Selects the sketch of the rectangle and the
//    face where to scribe the sketch as a wrap feature.
// 4. Inserts the wrap feature.
// 5. Rotates the part about its center.
// 6. Selects another face on the part.
// 7. Edits the wrap feature and wraps the rectangular
//    sketch on the second face.
//
// NOTE: Because the part document is used elsewhere, do not save changes.
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

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchManager swSketchManager = default(SketchManager);
            Feature swFeature = default(Feature);
            FeatureManager swFeatureManager = default(FeatureManager);
            ModelView swModelView = default(ModelView);
            Feature swWrapFeature = default(Feature);
            WrapSketchFeatureData swWrapFeatureData = default(WrapSketchFeatureData);
            SelectionMgr swSelectionManager = default(SelectionMgr);
            PartDoc swPart = default(PartDoc);
            Face2 swFace = default(Face2);
            object[] sketchLines = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            // Open part document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\clamp1.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Sketch a rectangle on the top plane
            swModel.ShowNamedView2("*Top", 5);
            status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);
            swModel.ViewZoomtofit2();
            sketchLines = (object[])swSketchManager.CreateCornerRectangle(-0.00169758295694522, 0.000948506512727088, 0, 0.0013668226995581, -0.000984987532447629, 0);
            swModel.ClearSelection2(true);
            swSketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);

            // Select the sketch of the rectangle and the
            // face where to scribe the sketch as a wrap feature
            status = swModelDocExt.SelectByID2("Sketch11", "SKETCH", 0, 0, 0, false, 4, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", 3.03698880696047E-03, 0.036653462145523, -1.43855543627342E-03, true, 1, null, 0);

            // Insert the wrap feature
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureManager.InsertWrapFeature(2, 0.001, false);
            swModel.ClearSelection2(true);

            // Rotate the part about its center to select another face
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0282662578086486, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0282662578086486, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0282662578086486, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0339195093703783, 0);
            swModelView.RotateAboutCenter(0.039572760932108, 0);
            swModelView.RotateAboutCenter(0.0282662578086486, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0339195093703783, 0);
            swModelView.RotateAboutCenter(0.0508792640555675, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, -0.00845813406735716);
            swModelView.RotateAboutCenter(0.0339195093703783, 0);
            swModelView.RotateAboutCenter(0.0508792640555675, -0.00845813406735716);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.039572760932108, -0.00845813406735716);
            swModelView.RotateAboutCenter(0.0508792640555675, -0.00845813406735716);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0339195093703783, 0);
            swModelView.RotateAboutCenter(0.039572760932108, 0);
            swModelView.RotateAboutCenter(0.0282662578086486, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0282662578086486, 0);
            swModelView.RotateAboutCenter(0.0339195093703783, 0);
            swModelView.RotateAboutCenter(0.0339195093703783, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0339195093703783, 0);
            swModelView.RotateAboutCenter(0.0339195093703783, 0);
            swModelView.RotateAboutCenter(0.0508792640555675, -0.0169162681347143);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0508792640555675, 0);
            swModelView.RotateAboutCenter(0.0339195093703783, 0);
            swModelView.RotateAboutCenter(0.0961052765494052, -0.00845813406735716);
            swModelView.RotateAboutCenter(0.039572760932108, 0);
            swModelView.RotateAboutCenter(0.0678390187407566, 0);
            swModelView.RotateAboutCenter(0.0621857671790269, 0);
            swModelView.RotateAboutCenter(0.0282662578086486, 0);
            swModelView.RotateAboutCenter(0.0508792640555675, -0.00845813406735716);
            swModelView.RotateAboutCenter(0.0226130062469189, -0.00845813406735716);
            swModelView.RotateAboutCenter(0.0339195093703783, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, -0.00845813406735716);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, -0.00845813406735716);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, -0.00845813406735716);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, -0.00845813406735716);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0282662578086486, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0226130062469189, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0169597546851892, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, -0.00845813406735716);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, -0.00845813406735716);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.0113065031234594, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);
            swModelView.RotateAboutCenter(0.00565325156172972, 0);

            // Select another face where to apply the wrap feature
            status = swModelDocExt.SelectByID2("", "FACE", 0.00239269080197957, 0.0263524999999731, -0.000479719888705432, true, 0, null, 0);
            swSelectionManager = (SelectionMgr)swModel.SelectionManager;
            swFace = (Face2)swSelectionManager.GetSelectedObject6(1, -1);

            // Edit the wrap feature to wrap the rectangular
            // sketch on the second face
            swPart = (PartDoc)swModel;
            swWrapFeature = (Feature)swPart.FeatureByName("Wrap1");
            swWrapFeatureData = (WrapSketchFeatureData)swWrapFeature.GetDefinition();
            status = swWrapFeatureData.AccessSelections(swModel, null);
            swWrapFeatureData.Face = swFace;
            Debug.Print("Wrap type: " + swWrapFeatureData.Type.ToString());
            Debug.Print("Wrap thickness: " + swWrapFeatureData.Thickness.ToString());
            Debug.Print("Reverse direction? " + swWrapFeatureData.ReverseDirection);
            status = swWrapFeature.ModifyDefinition(swWrapFeatureData, swModel, null);

            swModel.ClearSelection2(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
