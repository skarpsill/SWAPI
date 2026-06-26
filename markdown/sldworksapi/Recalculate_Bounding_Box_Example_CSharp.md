---
title: "Recalculate Bounding Box Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Recalculate_Bounding_Box_Example_CSharp.htm"
---

# Recalculate Bounding Box Example (C#)

This example shows how to recalculate the bounding box of an assembly.

```
//-----------------------------------------
// Preconditions:
// 1. Specified assembly document exists.
// 2. Open the Immediate window.
// 3. Run the macro.
//
// Postconditions:
// 1. Opens assembly document.
// 2. Gets the bounding box for the assembly.
// 3. Prints the lower- and upper-diagonal corner points
//    of the bounding box to the Immediate window.
// 4. Modifies a dimension in a component in the assembly.
// 5. Updates the bounding box.
// 6. Prints the lower- and upper-diagonal corner points
//    of the bounding box to the Immediate window.
// 7. Examine the values printed to the Immediate window
//    to verify that the bounding box was updated.
//
// NOTE: Because this assembly is used elsewhere,
// do not save any changes when closing it.
//-------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace UpdateBoxCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void ProcessAssyBox(SldWorks swApp, AssemblyDoc swAssy)
        {
            object box = null;
            double[] boxArray = new double[6];
            box = (object)swAssy.GetBox((int)swBoundingBoxOptions_e.swBoundingBoxIncludeRefPlanes);
            boxArray = (double[])box;
            Debug.Print("  Min = (" + boxArray[0] * 1000.0 + ", " + boxArray[1] * 1000.0 + ", " + boxArray[2] * 1000.0 + ") mm");
            Debug.Print("  Max = (" + boxArray[3] * 1000.0 + ", " + boxArray[4] * 1000.0 + ", " + boxArray[5] * 1000.0 + ") mm");
        }

        public void Main()
        {

            ModelDoc2 swModel;
            AssemblyDoc swAssy;
            ModelDocExtension swModelDocExt;
            Dimension swDimension;
            string fileName;
            int errors = 0;
            int warnings = 0;
            bool status;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\key pad_1.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swAssy = (AssemblyDoc)swModel;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Print the two diagonal corner points
            // of the bounding box before modifying the
            // assembly
            Debug.Print("Before:");
            ProcessAssyBox(swApp, swAssy);

            // Change a dimension of one of the assembly components
            status = swModelDocExt.SelectByID2("Sketch1@Pad_1-1@key pad_1", "SKETCH", 0, 0, 0, false, 0, null, 0);
            swModel.EditSketch();
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("D1@Sketch1@Pad_1-1@key pad_1", "DIMENSION", 0.00306153201295202, 0.0373842545521677, -0.0323079625553351, false, 0, null, 0);
            swModel.ClearSelection2(true);
            swDimension = (Dimension)swModel.Parameter("D1@Sketch1@pad_1.Part");
            errors = (int)swDimension.SetSystemValue3(0.04, (int)swSetValueInConfiguration_e.swSetValue_InThisConfiguration, null);
            swModel.ClearSelection2(true);

            // Update the bounding box
            swAssy.UpdateBox();

            // Print the two diagonal corner points of the
            // bounding box after modifying the assembly
            Debug.Print("After:");
            ProcessAssyBox(swApp, swAssy);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
