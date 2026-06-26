---
title: "Insert Explode Line Sketch and Route Line Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Exploded_Line_Sketch_and_Route_Line_Example_CSharp.htm"
---

# Insert Explode Line Sketch and Route Line Example (C#)

This example shows how to insert a route line in an explode line sketch.

```
//---------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\floxpress\ball valve\ball_valve.sldasm.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates an exploded view of the assembly.
// 2. Adds a route line, which is a type of explode line.
// 3. Examine the Immediate window and graphics area.
// 4. Locate and click 3DExplode1, the explode line sketch, on the
//    ConfigurationManager tab (click the ConfigurationManager
//    tab and expand default and ExplView1).
//
// NOTE: Because this assembly is used elsewhere, do not save changes.
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
            AssemblyDoc swAssembly = default(AssemblyDoc);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Sketch swSketch = default(Sketch);
            SketchManager swSketchMgr = default(SketchManager);
            Face2 swFace = default(Face2);
            object[] itemsToConnect = new object[2];
            object[] itemsReverse = new object[2];
            object[] itemsPath = new object[2];
            object[] alongXYZ = new object[2];
            bool boolstatus = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssembly = (AssemblyDoc)swModel;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSketchMgr = (SketchManager)swModel.SketchManager;

            // Explode the assembly
            swAssembly.AutoExplode();
            swModel.EditRebuild3();
            swModel.ViewZoomtofit2();

            // Insert an explode line sketch
            swSketchMgr.InsertExplodeLineSketch();

            // Select two faces for the route line
            boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.00555234504082591, 0.0271707519863185, 0.00337956573349629, false, 0, null, 0);
            swFace = (Face2)swSelMgr.GetSelectedObject6(1, -1);
            itemsToConnect[0] = (object)swFace;
            boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.00581777224675761, 0.0211322449790146, 0.127676153954326, true, 0, null, 0);
            swFace = (Face2)swSelMgr.GetSelectedObject6(1, -1);
            itemsToConnect[1] = (object)swFace;

            itemsReverse[0] = false;
            itemsReverse[1] = false;
            itemsPath[0] = false;
            itemsPath[1] = false;
            alongXYZ[0] = false;
            alongXYZ[1] = false;

            // Insert the route line in the explode line sketch
            swSketch = (Sketch)swModel.GetActiveSketch2();
            boolstatus = swSketch.InsertRouteLine((itemsToConnect), itemsReverse, itemsPath, alongXYZ);
            Debug.Print("Route line inserted in explode line sketch? " + boolstatus);

            // Close the explode line sketch
            swSketchMgr.InsertExplodeLineSketch();
        }
        public SldWorks swApp;
    }
}
```
