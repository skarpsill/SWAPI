---
title: "Create Wrap Feature on Multiple Faces Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Wrap_Feature_on_Multiple_Faces_Example_CSharp.htm"
---

# Create Wrap Feature on Multiple Faces Example (C#)

This example shows how to create a wrap feature on multiple faces.

```
//---------------------------------------------------------------------------
// Preconditions: Verify that the part to open exists.
//
// Postconditions:
// 1. Opens the part.
// 2. Selects the plane on which to sketch a circle.
// 3. Sketches the circle.
// 4. Selects the sketch of the circle and the faces on which to
//    wrap it.
// 5. Creates the wrap feature.
// 6. Examine the FeatureManager design tree and part.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//----------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SketchManager swSketchManager = default(SketchManager);
            SketchSegment swSketchSegment = default(SketchSegment);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatureManager = default(FeatureManager);
            Feature swFeature = default(Feature);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\molds\\telephone.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Select the plane on which to sketch the circle for the wrap feature
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Plane8", "PLANE", 0, 0, 0, false, 0, null, 0);

            //Sketch the circle
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);
            swSketchSegment = (SketchSegment)swSketchManager.CreateCircle(-0.035, 0.011624, 0.0, -0.031081, 0.018171, 0.0);
            swModel.ClearSelection2(true);
            swSketchManager.InsertSketch(true);

            //Select the sketch of the circle and the faces on which to wrap it
            //Because the type of wrap feature to create Scribe, no pull direction entity is selected
            status = swModelDocExt.SelectByID2("Sketch30", "SKETCH", 0, 0, 0, false, 4, null, 0);
            status = swModelDocExt.SelectByRay(-0.103709743982563, 0.00466186411857746, 0.0465727951450701, 1, 0, 0, 0.000421383417784414, 2, true, 1, 0);
            status = swModelDocExt.SelectByRay(-0.105251033879711, 0.0013155840361718, 0.0360382097004597, 1, 0, 0, 0.000421383417784414, 2, true, 1, 0);
            status = swModelDocExt.SelectByRay(-0.104507668954227, 0.00255494702965538, 0.0257514968545461, 1, 0, 0, 0.000421383417784414, 2, true, 1, 0);
            status = swModelDocExt.SelectByRay(-0.101403318635789, 0.0181709207475484, 0.0255036242558494, 1, 0, 0, 0.000421383417784414, 2, true, 1, 0);
            status = swModelDocExt.SelectByRay(-0.100395783628869, 0.0205257104351672, 0.0356664008024147, 1, 0, 0, 0.000421383417784414, 2, true, 1, 0);
            status = swModelDocExt.SelectByRay(-0.0997494761213602, 0.0190384748429869, 0.0484318396352955, 1, 0, 0, 0.000421383417784414, 2, true, 1, 0);

            //Create the wrap feature
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureManager.InsertWrapFeature2((int)swWrapSketchType_e.swWrapSketchType_Scribe, 0.00254, false, (int)swWrapMethods_e.swWrapMethods_SplineSurface, 5);

            swModel.ClearSelection2(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
