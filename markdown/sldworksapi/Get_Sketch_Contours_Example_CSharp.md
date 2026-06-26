---
title: "Get Sketch Contours Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Contours_Example_CSharp.htm"
---

# Get Sketch Contours Example (C#)

This example shows how to get the sketch contours in a model document.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open a part that contains a Sketch1 feature.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets the number of sketch contours in Sketch1 and whether
//    they are open or closed.
// 2. Gets the number of sketch segments in Sketch1 and their type.
// 3. Gets the number of edges Sketch1.
// 4. Examine the Immediate window.
//----------------------------------------------------------------------------

	using SolidWorks.Interop.sldworks;

	using SolidWorks.Interop.swconst;

	using System.Runtime.InteropServices;

	using System;

	using System.Diagnostics;

	namespace SelectSketchContour_CSharp.csproj

	{

	    partial class SolidWorksMacro

	    {

	        public void Main()

	        {

	            ModelDoc2 myModel = default(ModelDoc2);

	            PartDoc myPart = default(PartDoc);

	            SelectionMgr SelMgr = default(SelectionMgr);

	            SelectData mySelectData = default(SelectData);

	            Feature myFeature = default(Feature);

	            Sketch mySketch = default(Sketch);

	            int contourCount = 0;

	            object[] vSkContours = null;

	            SketchContour skContour = default(SketchContour);

	            object[] vEdges = null;

	            Edge myEdge = default(Edge);

	            int skSegCount = 0;

	            object[] vSkSegments = null;

	            SketchSegment skSegment = default(SketchSegment);

	            int skSegType = 0;

	            string skSegTypesString = null;

	            bool closed = false;

	            string closedString = null;

	            int i = 0;

	            int j = 0;

	            int k = 0;

	            bool boolstatus = false;

	            myModel = (ModelDoc2)swApp.ActiveDoc;

	            SelMgr = (SelectionMgr)myModel.SelectionManager;

	            mySelectData = (SelectData)SelMgr.CreateSelectData();

	            myPart = (PartDoc)myModel;

	            myFeature = (Feature)myPart.FeatureByName("Sketch1");

	            mySketch = (Sketch)myFeature.GetSpecificFeature2();

	            //             or

	            //    Set mySketch = myModel.GetActiveSketch2()

	            //    Set myFeature = mySketch

	            if ((mySketch != null))

	            {

	                vSkContours = (object[])mySketch.GetSketchContours();

	                contourCount = vSkContours.GetUpperBound(0) -
	vSkContours.GetLowerBound(0) + 1;

	                Debug.Print("");

	                Debug.Print(contourCount + " Contours in sketch " + myFeature.Name);

	                for (i = vSkContours.GetLowerBound(0); i <= vSkContours.GetUpperBound(0); i++)

	                {

	                    skContour = (SketchContour)vSkContours[i];

	                    if ((skContour != null))

	                    {

	                        closed = skContour.IsClosed();

	                        if ((closed == false))

	                        {

	                            closedString = "Open";

	                        }

	                        else

	                        {

	                            closedString = "Closed";

	                        }

	                        Debug.Print("  Contour
	" + i + ": " + closedString);

	                        vSkSegments = (object[])skContour.GetSketchSegments();

	                        skSegCount = vSkSegments.GetUpperBound(0) -
	vSkSegments.GetLowerBound(0) + 1;

	                        for (j = vSkSegments.GetLowerBound(0); j <= vSkSegments.GetUpperBound(0); j++)

	                        {

	                            if (j == vSkSegments.GetLowerBound(0))

	                            {

	                                skSegTypesString = "(";

	                            }

	                            skSegment = (SketchSegment)vSkSegments[j];

	                            if ((skSegment != null))

	                            {

	                                skSegType = skSegment.GetType();

	                                switch (skSegType)

	                                {

	                                    case (int)swSketchSegments_e.swSketchLINE:

	                                        skSegTypesString = skSegTypesString + "line";

	                                        break;

	                                    case (int)swSketchSegments_e.swSketchARC:

	                                        skSegTypesString = skSegTypesString + "arc";

	                                        break;

	                                    case (int)swSketchSegments_e.swSketchELLIPSE:

	                                        skSegTypesString = skSegTypesString + "ellipse";

	                                        break;

	                                    case (int)swSketchSegments_e.swSketchPARABOLA:

	                                        skSegTypesString = skSegTypesString + "parabola";

	                                        break;

	                                    case (int)swSketchSegments_e.swSketchSPLINE:

	                                        skSegTypesString = skSegTypesString + "spline";

	                                        break;

	                                    case (int)swSketchSegments_e.swSketchTEXT:

	                                        skSegTypesString = skSegTypesString + "text";

	                                        break;

	                                    case -1:

	                                        skSegTypesString = skSegTypesString + "unknown";

	                                        break;

	                                }

	                            }

	                            if (j == vSkSegments.GetUpperBound(0))

	                            {

	                                skSegTypesString = skSegTypesString + ")";

	                            }

	                            else

	                            {

	                                skSegTypesString = skSegTypesString + ",";

	                            }

	                        }

	                        Debug.Print("    Sketch
	segment count = " + skSegCount + " " + skSegTypesString);

	                        vEdges = (object[])skContour.GetEdges();

	                        if ((vEdges == null))

	                        {

	                            Debug.Print("    No
	edges.");

	                        }

	                        else

	                        {

	                            for (k = vEdges.GetLowerBound(0); k <= vEdges.GetUpperBound(0); k++)

	                            {

	                                myEdge = (Edge)vEdges[k];

	                                if ((myEdge != null))

	                                {

	                                    Debug.Print("    Edge
	" + k + ": ");

	                                }

	                            }

	                        }

	                        boolstatus = skContour.Select2(false, mySelectData);

	                        if (boolstatus == false)

	                        {

	                            Debug.Print("    Selection
	of contour failed.");

	                        }

	                        System.Diagnostics.Debugger.Break();

	                    }

	                }

	            }

	        }

	        public SldWorks swApp;

	    }

	}
```
