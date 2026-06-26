---
title: "Move Copy Sketch Entities Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Copy_Sketch_Entities_Example_CSharp.htm"
---

# Move Copy Sketch Entities Example (C#)

This example shows how to move, copy, and move and copy sketch entities.

```
//--------------------------------------------------------------------
// Preconditions: Verify that the specified part template exists.
//
// Postconditions:
// 1. Insert a breakpoint at the following lines of code:
//
//    swFeature = swPart.FeatureByName("Sketch1")
//
//    swModel.EditUndo2(1)
//
// 2. Run the macro.
// 3. Examine the sketch at each breakpoint, then press F5.
//     1.  Opens a new part document.
//     2.  Opens a sketch and sketches a line and a circle.
//     3.  Selects the line and circle.
//     4.  Moves the line and circle.
//     5.  Moves and copies the line and circle once.
//     6.  Moves and copies the line and circle twice.
// 4. Close the part document without saving it.
//--------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace MoveOrCopyCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            PartDoc swPart = default(PartDoc);
            Feature swFeature = default(Feature);
            SketchManager swSketchMgr = default(SketchManager);
            SketchSegment swSketchSegment = default(SketchSegment);
            long lIdx = 0;
            bool bCopy = false;
            int lNumCopies = 0;
            double[] aBasePoint = new double[3];
            double[] aMoveVector = new double[3];
            int errors = 0;
            bool status = false;

            // Open a new part document and sketch a line and a circle
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
            swApp.ActivateDoc3("Part1", true, 0, ref errors);
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swPart = (PartDoc)swModel;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSketchMgr = (SketchManager)swModel.SketchManager;
            swSketchMgr.InsertSketch(true);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(-0.096389, 0.032667, 0.0, -0.062943, 0.019437, 0.0);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateCircle(-0.084504, 0.013823, 0.0, -0.087932, 0.006083, 0.0);
            swFeature = (Feature)swPart.FeatureByName("Sketch1");
            status = swFeature.Select2(false, 0);
            swModel.EditSketch();
            aBasePoint[0] = 0.0;
            aBasePoint[1] = 0.0;
            aBasePoint[2] = 0.0;
            aMoveVector[0] = 0.1;
            aMoveVector[1] = 0.0;
            aMoveVector[2] = 0.0;

            for (lIdx = 0; lIdx <= 2; lIdx++)
            {
                swModel.ClearSelection2(true);
                status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", -0.0752087432116777, 0.0368667656031986, 0.0146398923143701, true, 0, null, 0);
                status = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", -0.0802420935887737, 0.0333695230163339, 0.019671897706856, true, 0, null, 0);
                switch ((lIdx))
                {
                    case 0:
                        // Move
                        bCopy = false;
                        lNumCopies = 0;
                        break;
                    case 1:
                        // Move and copy once
                        bCopy = true;
                        lNumCopies = 1;
                        break;
                    case 2:
                        // Move and copy twice
                        bCopy = true;
                        lNumCopies = 2;
                        break;
                }
                if ((!bCopy))
                {
                    lNumCopies = 0;
                }
                swModelDocExt.MoveOrCopy(bCopy, lNumCopies, true, aBasePoint[0], aBasePoint[1], 0.0, aBasePoint[0] + aMoveVector[0], aBasePoint[1] + aMoveVector[1], aBasePoint[2] + aMoveVector[2]);
                swModel.ClearSelection2(true);
                // Undo so that you can do it again, but differently
                swModel.EditUndo2(1);
            }
            swSketchMgr.InsertSketch(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
