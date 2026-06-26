---
title: "Create Sketch Path Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Sketch_Path_Example_CSharp.htm"
---

# Create Sketch Path Example (C#)

This example shows how to create a sketch path.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified document template exists.
 // 2. Open an Immediate window.
 //
// Postconditions:
 // 1. Creates a new model document with Sketch1.
 // 2. Selects the Sketch1 segments.
 // 3. Creates a sketch path.
 // 4. Creates a sketch circle.
 // 5. Adds a tangent relation between the sketch path and sketch circle.
 // 6. Inspect the Immediate window.
 //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace CreateSketchPath_CSharp.csproj
{

    partial class SolidWorksMacro
    {

        ModelDoc2 swModel;
        SelectionMgr swSelMgr;
        Feature swFeat;
        Sketch swSketch;
        int i;
        bool bRet;
        object[] vSketchPath;
        SketchPath swSketchPath;
        double nLength;
        object[] vConstraint;
        SketchRelation swSkRel;
        object[] vRelation;
        object vSkRel;
        object[] vSketchSeg;
        SketchSegment swSketchSeg;
        SketchManager swSketchMgr;
        bool boolstatus;

        public void Main()
        {
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2015\\templates\\Part.prtdot", 0, 0, 0);
            swModel = (ModelDoc2)swApp.ActiveDoc;

            swModel.SketchManager.InsertSketch(true);
            boolstatus = swModel.Extension.SelectByID2("Front Plane", "PLANE", -0.0416217612836357, 0.0270960165695038, 0.00355460240358513, false, 0, null, 0);

            object skSegment = null;
            skSegment = swModel.SketchManager.CreateLine(-0.055655, 0.037535, 0.0, 0.011848, 0.039924, 0.0);
            skSegment = swModel.SketchManager.CreateLine(0.011848, 0.039924, 0.0, 0.018817, 0.009658, 0.0);
            skSegment = swModel.SketchManager.CreateLine(0.018817, 0.009658, 0.0, 0.05227, 0.008264, 0.0);
            skSegment = swModel.SketchManager.CreateLine(0.05227, 0.008264, 0.0, 0.065809, 0.036414, 0.0);

            swModel.SketchManager.InsertSketch(true);

            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swSketchMgr = swModel.SketchManager;

            // Select the sketch
            bRet = swModel.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);

            swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swSketch = (Sketch)swFeat.GetSpecificFeature2();

            // Put the sketch in edit mode
            swModel.EditSketch();

            // Get the sketch segments
            vSketchSeg = (object[])swSketch.GetSketchSegments();

            for (i = 0; i <= vSketchSeg.GetUpperBound(0); i++) {
                swSketchSeg = (SketchSegment)vSketchSeg[i];
                swSketchSeg.Select4(true, null);
            }

            // Create a chain using the selected sketch segments
            bRet = swSketchMgr.MakeSketchChain();
            swModel.ClearSelection2(true);

            // Get the sketch path
            vSketchPath = (object[])swSketch.GetSketchPaths();
            swModel.ClearSelection2(true);

            // Create a circle
            swSketchMgr.CreateCircle(-0.07515069296375, 0.04810565031983, 0, -0.055655, 0.037535, 0);

            // Add a tangent relation between sketch path and sketch circle
            boolstatus = swModel.Extension.SelectByID2("Arc1", "SKETCHSEGMENT", -5.44261072733269E-02, 4.71088420855688E-02, -3.28513702299429E-03, false, 0, null, 0);
            boolstatus = swModel.Extension.SelectByID2("Line1", "SKETCHSEGMENT", -4.22450565500339E-02, 3.67651345154678E-02, -2.68554920844266E-03, true, 0, null, 0);
            swModel.SketchAddConstraints("sgTANGENT");

            // Print the number of constraints, number of relations,
            // path length, number of sketch segments, whether the path was selected,
            // type of constraints, and type of relations
            for (i = 0; i <= vSketchPath.GetUpperBound(0); i++) {
                swSketchPath = (SketchPath)vSketchPath[i];
                Debug.Print(" Number of constraints: " + swSketchPath.GetConstraintsCount());
                Debug.Print(" Number of relations: " + swSketchPath.GetRelationsCount());
                Debug.Print(" Path length: " + swSketchPath.GetLength());
                Debug.Print(" Number of segments: " + swSketchPath.GetSketchSegmentCount());
                Debug.Print(" Selection result: " + swSketchPath.Select(false, null));

                vConstraint = (object[])swSketchPath.GetConstraints();

                 int j = 0;
                j = 0;

                if (((vConstraint != null))) {
                     for (j = 0; j <= vConstraint.GetUpperBound(0); j++) {
                        Debug.Print("  SketchSegConstraint[" + i + "]: " + vConstraint[j]);
                    }
                }

                vRelation = (object[])swSketchPath.GetRelations();

                 int k = 0;
                    for (k = 0; k <= vRelation.GetUpperBound(0); k++ ){
                        vSkRel = vRelation[k];
                        swSkRel = (SketchRelation)vSkRel;
                        Debug.Print("    Relation(" + k + ")");
                        Debug.Print("      Type: " + swSkRel.GetRelationType());

                    }

                // Get the sketch segments in the sketch path and
                 // their lengths
                vSketchSeg = (object[])swSketchPath.GetSketchSegments();

                 int l = 0;

                 for (l = 0; l <= vSketchSeg.GetUpperBound(0); l++) {
                    swSketchSeg = (SketchSegment)vSketchSeg[l];

                     // Ignore construction lines
                     if (swSketchSeg.ConstructionGeometry == false) {
                         // Ignore text
                         if ((int)swSketchSegments_e.swSketchTEXT != swSketchSeg.GetType()) {
                            nLength = nLength + swSketchSeg.GetLength();
                        }
                    }

                }

                Debug.Print(" Total path length calculated by segment: " + nLength);

            }

            swModel.SketchManager.InsertSketch(true);
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
