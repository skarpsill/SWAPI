---
title: "Get Mates and Mate Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mates_and_Mate_Entities_Example_CSharp.htm"
---

# Get Mates and Mate Entities Example (C#)

This example shows how to iterate through a FeatureManager design tree and get all of an assembly's mates and mate entities.

```
//------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified assembly document.
// 2. Iterates through the FeatureManager design tree to find
//    and print Mates to the Immediate window.
// 3. Iterates through the subfeatures of Mates and prints each mate
//    entity's information to the Immediate window.
// 4. Examine the Immediate window.
//------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
using System.Collections;

namespace Mate2CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            Feature swFeat = default(Feature);
            Feature swMateFeat = null;
            Feature swSubFeat = default(Feature);
            Mate2 swMate = default(Mate2);
            Component2 swComp = default(Component2);
            MateEntity2[] swMateEnt = new MateEntity2[3];
            string fileName = null;
            int errors = 0;
            int warnings = 0;
            int i = 0;
            double[] entityParameters = new double[8];

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\simple-block.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Get the first feature in the assembly
            swFeat = (Feature)swModel.FirstFeature();
            //Iterate over features in FeatureManager design tree
            while ((swFeat != null))
            {
                if ("MateGroup" == swFeat.GetTypeName())
                {
                    swMateFeat = (Feature)swFeat;
                    break;
                }
                swFeat = (Feature)swFeat.GetNextFeature();
            }
            Debug.Print("  " + swMateFeat.Name);
            Debug.Print("");

            //Get first mate, which is a subfeature
            swSubFeat = (Feature)swMateFeat.GetFirstSubFeature();
            while ((swSubFeat != null))
            {
                swMate = (Mate2)swSubFeat.GetSpecificFeature2();
                if ((swMate != null))
                {
                    for (i = 0; i <= 1; i++)
                    {
                        swMateEnt[i] = swMate.MateEntity(i);
                        Debug.Print("    " + swSubFeat.Name);
                        Debug.Print("      Type              = " + swMate.Type);
                        Debug.Print("      Alignment         = " + swMate.Alignment);
                        Debug.Print("      Can be flipped    = " + swMate.CanBeFlipped);
                        Debug.Print("");
                        swComp = (Component2)swMateEnt[i].ReferenceComponent;
                        Debug.Print("      Component         = " + swComp.Name2);
                        Debug.Print("      Mate enity type   = " + swMateEnt[i].ReferenceType);
                        entityParameters = (double[])swMateEnt[i].EntityParams;
                        Debug.Print("      (x,y,z)           = (" + (double)entityParameters[0] + ", " + (double)entityParameters[1] + ", " + (double)entityParameters[2] + ")");
                        Debug.Print("      (i,j,k)           = (" + (double)entityParameters[3] + ", " + (double)entityParameters[4] + ", " + (double)entityParameters[5] + ")");
                        Debug.Print("      Radius 1          = " + (double)entityParameters[6]);
                        Debug.Print("      Radius 2          = " + (double)entityParameters[7]);
                        Debug.Print("");
                    }
                    Debug.Print(" ");
                }
                // Get the next mate in MateGroup
                swSubFeat = (Feature)swSubFeat.GetNextSubFeature();
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
