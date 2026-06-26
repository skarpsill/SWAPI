---
title: "Insert Cosmetic Weld Bead Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Cosmetic_Weld_Bead_Example_CSharp.htm"
---

# Insert Cosmetic Weld Bead Example (C#)

This example shows how to insert a cosmetic weld bead feature and access an existing weld bead feature's properties.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\Insert_weld.sldprt.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Inserts a fillet weld, Weld Bead2, and adds it to the Weld Folder in
//    the FeatureManager design tree.
// 2. Inspect the Immediate window for Weld Bead1 settings and properties.
// 3. Expand the Weld Folder and 20.08in Fillet Weld(1) folders in the
//    FeatureManager design tree to verify step 1.
//
// NOTE: Because the model is used elsewhere, do not save changes.
//---------------------------------------------------------------------------

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
            CosmeticWeldBeadFeatureData swCosmeticWeldBeadFeatureData = default(CosmeticWeldBeadFeatureData);
            CosmeticWeldBeadFolder swWeldFolder = default(CosmeticWeldBeadFolder);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            object[] edges = null;
            bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Insert Weld Bead2
            status = swModelDocExt.SelectByID2("", "FACE", -0.0344320907599354, 0.0170180000000641, -0.00227566098720899, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", -0.0161637176506133, 0.0503122973344716, -0.0013752238241409, true, 0, null, 0);
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureManager.InsertCosmeticWeldBead(0.51);

            swModel.ClearSelection2(true);

            //Get Weld Bead1 and get and set some properties
            status = swModelDocExt.SelectByID2("Weld Bead1", "COSMETIC_WELD", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, 0);
            swCosmeticWeldBeadFeatureData = (CosmeticWeldBeadFeatureData)swFeature.GetDefinition();
            swCosmeticWeldBeadFeatureData.AccessSelections(swModel, null);
            Debug.Print("Weld Bead1 settings: ");
            Debug.Print("   Weld bead size: " + swCosmeticWeldBeadFeatureData.BeadSize * 39.37 + " in");
            Debug.Print("   Tangent propagation? " + swCosmeticWeldBeadFeatureData.TangentPropagation);
            Debug.Print("   Weld sides as defined in swCosmeticWeldBeadSide_e (1 = swCosmeticWeldBeadSide_selection): " + swCosmeticWeldBeadFeatureData.Side);
            Debug.Print("   From/to length properties enabled? " + swCosmeticWeldBeadFeatureData.FromToLength);
            if (swCosmeticWeldBeadFeatureData.FromToLength == false)
            {
                swCosmeticWeldBeadFeatureData.FromToLength = true;
            }
            if (swCosmeticWeldBeadFeatureData.FromToLength == true)
            {
                Debug.Print("   Start weld at: " + swCosmeticWeldBeadFeatureData.FromToStartPoint);
                Debug.Print("   Weld length: " + swCosmeticWeldBeadFeatureData.FromToWeldLength);
                Debug.Print("   Reverse weld? " + swCosmeticWeldBeadFeatureData.FromToReverse);
            }
            Debug.Print("   Intermittent weld properties enabled? " + swCosmeticWeldBeadFeatureData.IntermittentWeld);
            if (swCosmeticWeldBeadFeatureData.IntermittentWeld == false)
            {
                swCosmeticWeldBeadFeatureData.IntermittentWeld = true;
            }
            if (swCosmeticWeldBeadFeatureData.IntermittentWeld == true)
            {
                if (swCosmeticWeldBeadFeatureData.GapOrPitch == true)
                {
                    Debug.Print("   Intermittent gap: " + swCosmeticWeldBeadFeatureData.Gap);
                    Debug.Print("   Intermittent weld length: " + swCosmeticWeldBeadFeatureData.IntermittentWeldLength);
                }
                else
                {
                    Debug.Print("   Intermittent pitch: " + swCosmeticWeldBeadFeatureData.Pitch);
                    Debug.Print("   Intermittent weld length: " + swCosmeticWeldBeadFeatureData.IntermittentWeldLength);
                    Debug.Print("   Stagger welds if welding on both sides? " + swCosmeticWeldBeadFeatureData.Staggered);
                }
            }
            edges = (object[])swCosmeticWeldBeadFeatureData.GetReferenceEdges();
            Debug.Print("   Number of reference edges: " + edges.GetUpperBound(0));

            swWeldFolder = (CosmeticWeldBeadFolder)swCosmeticWeldBeadFeatureData.GetWeldBeadFolder();

            Debug.Print("Weld Bead1 properties:");
            Debug.Print("   Weld material was: " + swWeldFolder.Material);
            swWeldFolder.Material = "Steel";
            Debug.Print("   Weld material is now: " + swWeldFolder.Material);
            Debug.Print("   Welding cost per unit mass: " + swWeldFolder.CostPerUnitMass);
            Debug.Print("   Weld mass per unit length: " + swWeldFolder.MassPerUnitLength);
            Debug.Print("   Number of weld passes: " + swWeldFolder.NumberOfWeldPasses);
            Debug.Print("   Weld process: " + swWeldFolder.Process);
            Debug.Print("   Welding time per unit length: " + swWeldFolder.TimePerUnitLength);
            Debug.Print("   Total welding cost: $" + swWeldFolder.TotalCost);
            Debug.Print("   Total weld length: " + swWeldFolder.TotalLength);
            Debug.Print("   Total weld mass: " + swWeldFolder.TotalMass + " lb");
            Debug.Print("   Total number of welds: " + swWeldFolder.TotalNumber);
            Debug.Print("   Total welding time: " + swWeldFolder.TotalTime + " sec");

            status = swFeature.ModifyDefinition(swCosmeticWeldBeadFeatureData, swModel, null);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
