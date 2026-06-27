---
title: "Get Surface-finish Image Path and File Name Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Surface-finish_Image_Path_and_Filename_Example_CSharp.htm"
---

# Get Surface-finish Image Path and File Name Example (C#)

This example shows how to set and get the path and file name of the image used for an appearance's surface finish.

```
//----------------------------------------------------------------
// Preconditions:
// 1. Verify that:
//    * specified model document exists.
//    * specified materials and surface-finish image files exist.
//    * a ray-trace rendering engine is loaded.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified model document.
// 2. Applies the specified appearance and surface finish to the model.
// 3. Gets the file name of the first appearance and surface finish
//    applied to the model.
// 4. If prompted to use perspective views in rendering, click
//    Continue without Camera or Perspective.
// 5. Renders the model.
// 6. Examine the Final Render and Immediate windows.
//
// NOTES:
// * Rendering can take several minutes to complete.
// * Because the model is used elsewhere, do not save changes.
//----------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace FileNameCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Component2 swComponent = default(Component2);
            Configuration swConfiguration = default(Configuration);
            RenderMaterial swRenderMaterial = default(RenderMaterial);
            RayTraceRenderer swRayTraceRenderer = default(RayTraceRenderer);
            int nbrRenderMaterials = 0;
            string fileName = null;
            int warnings = 0;
            int errors = 0;
            bool status = false;
            string materialName = null;
            string[] displayStateNames = null;
            int materialID1 = 0;
            int materialID2 = 0;

            //Open part document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\tolanalyst\\offset\\bushing.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Access the ray-trace rendering engine
            //swRayTraceRenderer = (RayTraceRenderer)swApp.GetRayTraceRenderer();

            //Create material for the appearance
            materialName = "C:\\Program Files\\SolidWorks Corp\\SolidWorks\\data\\graphics\\Materials\\metal\\bronze\\cast bronze.p2m";
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swRenderMaterial = (RenderMaterial)swModelDocExt.CreateRenderMaterial(materialName);

            //Verify that RealView Graphics is set
            Debug.Print("RealView Graphics set? " + swModelDocExt.ViewDisplayRealView);

            //Add an appearance
            status = swModelDocExt.SelectByID2("bushing.SLDPRT", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swComponent = (Component2)swSelectionMgr.GetSelectedObject6(1, -1);
            status = swRenderMaterial.AddEntity(swComponent);
            Debug.Print("Appearance added to model? " + status);

            //Add surface finish
            fileName = "C:\\Program Files\\SolidWorks Corp\\SolidWorks\\data\\Images\\textures\\metal\\cast\\cast_bump.jpg";
            swRenderMaterial.BumpTextureFilename = fileName;

            swModel.ClearSelection2(true);

            //Get the names of display states
            //Add the appearance to all of the display states
            swConfiguration = (Configuration)swModel.GetActiveConfiguration();
            displayStateNames = (string[])swConfiguration.GetDisplayStates();
            status = swModelDocExt.AddDisplayStateSpecificRenderMaterial(swRenderMaterial, (int)swDisplayStateOpts_e.swAllDisplayState, displayStateNames, out materialID1, out materialID2);

            //Get the number of appearances
            nbrRenderMaterials = swModelDocExt.GetRenderMaterialsCount2((int)swDisplayStateOpts_e.swAllDisplayState, displayStateNames);

            //If one or more appearances are applied to the model,
            //then get the file names of the first appearance and surface finish applied
            if (nbrRenderMaterials > 0)
            {
                Debug.Print("First appearance's file name: " + swRenderMaterial.FileName);
                Debug.Print("  Surface finish's file name: " + swRenderMaterial.BumpTextureFilename);
                Debug.Print("Fixed aspect ratio? " + swRenderMaterial.FixedAspectRatio);
                Debug.Print("  Width: " + swRenderMaterial.Width * 1000 + "mm");
                Debug.Print("  Height: " + swRenderMaterial.Height * 1000 + "mm");
                if (swRenderMaterial.DoubleSided == false)
                {
                    swRenderMaterial.DoubleSided = true;
                }
                Debug.Print("Doubled-sided? " + swRenderMaterial.DoubleSided);
                swRenderMaterial.RoundSharpEdges = 0.005;
                Debug.Print("Round sharp edges value: " + swRenderMaterial.RoundSharpEdges * 1000 + "mm");

                //Display final render window
                status = swRayTraceRenderer.InvokeFinalRender();

            }
            else
            {
                Debug.Print("No appearances applied to this model.");
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
