---
title: "Offset Edges to Create 3D Sketch Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Offset_Edges_to_Create_3D_Sketch_on_Surface_Example_CSharp.htm"
---

# Offset Edges to Create 3D Sketch Example (C#)

This example shows how to offset edges to create a 3D sketch on a face.

```
//--------------------------------------------------------------
// Preconditions: Verify that the part to open exists.
//
// Postconditions:
// 1. Opens the part.
// 2. Selects the edges to offset.
// 3. Creates a 3D sketch on the face whose edges were selected.
// 4. Examine the graphics area.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//---------------------------------------------------------------
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
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchManager swSketchManager = default(SketchManager);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\lesson1\\tutor1a.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Select the edges
            status = swModelDocExt.SelectByID2("", "EDGE", 0.06, 0.12, 0.03, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0, 0.12, 0.015, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.06, 0.12, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.12, 0.12, 0.015, true, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.06, 0.12, 0.03, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0, 0.12, 0.015, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.06, 0.12, 0, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.12, 0.12, 0.015, true, 1, null, 0);

            //Create a 3D sketch
            status = swModelDocExt.SketchOffsetOnSurface(0.01, false, true, false);

            swModel.ClearSelection2(true);

            //Close the sketch
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchManager.InsertSketch(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
