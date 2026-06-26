---
title: "Add Decal Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Decal_Example_CSharp.htm"
---

# Add Decal Example (C#)

This example shows how to add a decal to a selected face on a part.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document to open exists.
// 2. Verify that the specified decal files exist.
// 3. Verify that a ray-trace rendering engine is active.
// 4. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Selects the face where to apply a decal.
// 3. Applies a decal to the selected face.
// 4. Gets the properties of the decal and prints them
//    to the Immediate window.
// 5. Examine the graphics area and the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//----------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace FaceDecalPropertiesCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Face2 swFace = default(Face2);
            Decal swDecal = default(Decal);
            RenderMaterial swMaterial = default(RenderMaterial);
            object[] swFaceDecalPropertiesArray = null;
            FaceDecalProperties swFaceDecalProperties = default(FaceDecalProperties);
            bool status = false;
            string strname = null;
            int nDecalID = 0;
            int i = 0;
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            int nbrDecals = 0;

            //Open part document and select face where to
            //apply a decal
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\tolanalyst\\minimum_clearance\\top_plate.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("", "FACE", -0.00374778769440809, 0.0609129688728558, 0.0160000000000196, false, 0, null, 0);
            swFace = (Face2)swSelMgr.GetSelectedObject6(1, -1);
            swModel.ClearSelection2(true);

            //Create the decal
            swDecal = (Decal)swModelDocExt.CreateDecal();
            swMaterial = (RenderMaterial)swDecal;
            status = swMaterial.AddEntity(swFace);
            strname = "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\data\\graphics\\Decals\\Logos\\sw.p2d";
            swMaterial.FileName = strname;
            strname = "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\data\\graphics\\Decals\\Logos\\sw.bmp";
            swMaterial.TextureFilename = strname;
            swMaterial.MappingType = 0;
            swMaterial.FixedAspectRatio = false;
            swMaterial.FitHeight = true;
            swMaterial.FitWidth = true;
            status = swModelDocExt.AddDecal(swDecal, out nDecalID);

            //Rebuild the model
            swModelDocExt.Rebuild((int)swRebuildOptions_e.swRebuildAll);

            //Get decal properties
            status = swModelDocExt.SelectByID2("", "FACE", -0.00374778769440809, 0.0609129688728558, 0.0160000000000196, false, 0, null, 0);
            swFace = (Face2)swSelMgr.GetSelectedObject6(1, -1);
            nbrDecals = swFace.GetDecalsCount();
            Debug.Print("Number of decals applied to this face: " + nbrDecals);
            if (nbrDecals > 0)
            {
                swFaceDecalPropertiesArray = (object[])swFace.GetAllDecalProperties();
                for (i = 0; i < swFaceDecalPropertiesArray.Length; i++)
                {
                    swFaceDecalProperties = (FaceDecalProperties)swFaceDecalPropertiesArray[i];
                    Debug.Print("Decal " + (i + 1) + "'s texture:");
                    Debug.Print("  Angle: " + swFaceDecalProperties.TextureAngle);
                    Debug.Print("  Angle UV: " + swFaceDecalProperties.TextureAngleUV);
                    Debug.Print("  File: ");
                    Debug.Print("     Name: " + swFaceDecalProperties.TextureFilename);
                    Debug.Print("     ID: " + swFaceDecalProperties.TextureFilenameID);
                    Debug.Print("  ID: " + swFaceDecalProperties.TextureID);
                    Debug.Print("  Map ID: " + swFaceDecalProperties.TextureMapID);
                    Debug.Print("  Mirrored? " + swFaceDecalProperties.TextureMirrored);
                    Debug.Print("  Render mode (0 = Image; 1 = Luminance):  " + swFaceDecalProperties.TextureRenderMode);
                    Debug.Print("  Translation: ");
                    Debug.Print("      U: " + swFaceDecalProperties.TextureTranslationU);
                    Debug.Print("      V: " + swFaceDecalProperties.TextureTranslationV);
                    Debug.Print("      X: " + swFaceDecalProperties.TextureTranslationX);
                    Debug.Print("      Y: " + swFaceDecalProperties.TextureTranslationY);
                    Debug.Print("  UV scale: ");
                    Debug.Print("      U: " + swFaceDecalProperties.TextureUScale);
                    Debug.Print("      V: " + swFaceDecalProperties.TextureVScale);
                }
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
