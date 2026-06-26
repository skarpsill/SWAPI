---
title: "Get Mirror Pattern Feature Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mirror_Pattern_Feature_Data_Example_CSharp.htm"
---

# Get Mirror Pattern Feature Data Example (C#)

This example shows how to get data for a mirror pattern feature.

```
//--------------------------------------------------------------------
// Postconditions:
// 1. Verify that the specified part document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Creates Boss-Extrude2.
// 3. Mirrors Boss-Extrude2 to create LPattern1.
// 4. Mirrors Boss-Extrude1 and LPattern1 to create Mirror1.
// 5. Gets the patterned features of Mirror1.
// 6. Examine the FeatureManager design tree, the graphics area, and
//    the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//--------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace MirrorPatternFeatureDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchSegment swSketchSegment = default(SketchSegment);
            SketchManager swSketchManager = default(SketchManager);
            Feature swFeature = default(Feature);
            FeatureManager swFeatureManager = default(FeatureManager);
            MirrorPatternFeatureData swMirrorPatternFeatureData = default(MirrorPatternFeatureData);
            Entity swEntity = default(Entity);
            Face2 swFace = default(Face2);
            SelectData swSelData = null;
            bool status = false;
            string fileName = null;
            int errors = 0;
            int warnings = 0;
            object[] faceArray = null;
            object[] patternArray = null;
            int i = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\beam with holes.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Create Boss-Extrude2
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("", "FACE", 0.0919322519657158, -0.0190749842767559, 0.0399999999999068, false, 0, null, 0);
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchSegment = (SketchSegment)swSketchManager.CreateCircle(0.092035, -0.020145, 0.0, 0.093952, -0.029594, 0.0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureManager.FeatureExtrusion3(true, false, false, 0, 0, 0.01, 0.01, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
            0, 0, false);

            //Create LPattern1
            status = swModelDocExt.SelectByID2("Boss-Extrude2", "BODYFEATURE", 0, 0, 0, false, 4, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.0441545689173921, -0.0398591118729428, 0.0402307394506352, true, 1, null, 0);
            swFeature = (Feature)swFeatureManager.FeatureLinearPattern4(3, 0.04, 1, 0.01, false, false, "NULL", "NULL", false, false,
            false, false, false, false, true, true, false, false, 0, 0);

            //Create Mirror1
            status = swModelDocExt.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", 0.232539736404746, -0.0399999999999068, 0.0224388980993808, true, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("LPattern1", "BODYFEATURE", 0, 0, 0, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", 0.232539736404746, -0.0399999999999068, 0.0224388980993808, true, 2, null, 0);
            swFeature = (Feature)swFeatureManager.InsertMirrorFeature2(false, false, false, false, (int)swFeatureScope_e.swFeatureScope_AllBodies);

            //Get Mirror1 properties
            swMirrorPatternFeatureData = (MirrorPatternFeatureData)swFeature.GetDefinition();
            Debug.Print("  " + swFeature.Name);
            Debug.Print("    Geometry pattern                                     = " + swMirrorPatternFeatureData.GeometryPattern);
            Debug.Print("    Number of mirrored faces                             = " + swMirrorPatternFeatureData.GetMirrorFaceCount());
            Debug.Print("    Type of mirrored plane (0 = face; 1 = plane)         = " + swMirrorPatternFeatureData.GetMirrorPlaneType());
            Debug.Print("    Number of patterned features                         = " + swMirrorPatternFeatureData.GetPatternFeatureCount());

            //Roll back to get to the faces and features
            status = swMirrorPatternFeatureData.AccessSelections(swModel, null);
            swModel.ClearSelection2(true);

            if (1 == swMirrorPatternFeatureData.GetMirrorPlaneType())
            {
                swFeature = (Feature)swMirrorPatternFeatureData.Plane;
                //Cannot select a reference plane through Entity, so
                //use Feature
                Debug.Print("    Plane                  = " + swFeature.Name);
                status = swFeature.Select2(true, 0);
            }
            else
            {
                //Select face through Entity
                swEntity = (Entity)swMirrorPatternFeatureData.Plane;
                status = swEntity.Select4(true, swSelData);
            }

            faceArray = (object[])swMirrorPatternFeatureData.MirrorFaceArray;
            if ((faceArray != null))
            {
                swModel.ClearSelection2(true);
                status = false;
                for (i = 0; i < faceArray.Length; i++)
                {
                    swFace = (Face2)faceArray[i];
                    swEntity = (Entity)swFace;
                    status = swEntity.Select4(true, swSelData);
                }
            }

            patternArray = (object[])swMirrorPatternFeatureData.PatternFeatureArray;
            if ((patternArray != null))
            {
                swModel.ClearSelection2(true);
                status = false;
                for (i = 0; i < patternArray.Length; i++)
                {
                    swFeature = (Feature)patternArray[i];
                    Debug.Print("    Feature (" + i + ")                                          = " + swFeature.Name);
                    status = swFeature.Select2(true, 0);
                }
            }
            //Cancel changes
            swMirrorPatternFeatureData.ReleaseSelectionAccess();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
