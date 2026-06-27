---
title: "Get Areas of MidSurface Faces Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Areas_of_MidSurface_Faces_Example_CSharp.htm"
---

# Get Areas of MidSurface Faces Example (C#)

This example shows how to get the areas of mid-surface faces.

```
//-----------------------------------------------------------
// Postconditions:
// 1. Verify that the part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the part.
// 2. Selects two faces and inserts a midsurface feature.
// 3. Gets the number of faces in the midsurface feature.
// 4. Gets the areas of the faces in the midsurface feature.
// 5. Examine the Immediate window, FeatureManager design
//    tree, and graphics area.
//
// NOTE: Because the part used elsewhere, do not save changes.
//------------------------------------------------------------

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
            FeatureManager swFeatureManager = default(FeatureManager);
            MidSurface3 swMidSurfaceFeature = default(MidSurface3);
            Feature swFeature = default(Feature);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Face2 swFace = default(Face2);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            int count = 0;
            object[] faces = null;
            int i = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\box.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("", "FACE", -0.0533080255641494, 0.0299999999999727, 0.0131069871973182, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", -0.0370905424398416, 0, 0.0289438729892595, true, 0, null, 0);
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeatureManager.InsertMidSurface(null, null, 0.0, false);
            status = swModelDocExt.SelectByID2("Surface-MidSurface1", "REFSURFACE", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swMidSurfaceFeature = (MidSurface3)swFeature.GetSpecificFeature2();
            count = swMidSurfaceFeature.GetFaceCount();
            Debug.Print("Number of faces for midsurface feature: " + count);
            faces = (object[])swMidSurfaceFeature.GetFaces();
            for (i = faces.GetLowerBound(0); i <= faces.GetUpperBound(0); i++)
            {
                swFace = (Face2)faces[i];
                Debug.Print("Area of face " + i + " of midsurface feature: " + swFace.GetArea());
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
