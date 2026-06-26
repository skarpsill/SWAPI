---
title: "Get Sketch Regions Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Regions_Example_CSharp.htm"
---

# Get Sketch Regions Example (C#)

This example shows how to get the sketch regions in a sketch.

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a model document that contains a Sketch1 feature with
 //   one or more sketch regions.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Gets each sketch region.
 // 2. Press F5 at each System.Diagnostics.Debugger.Break statement.
 // 3. Examine the Immediate window.
 //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace SelectSketchRegion_CSharp.csproj
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
             int regionCount = 0;
             object[] vSkRegions = null;
             SketchRegion skRegion = default(SketchRegion);
             Loop2 myLoop = default(Loop2);
             int edgeCount = 0;
             int vertexCount = 0;
             object[] vEdges = null;
             Edge myEdge = default(Edge);
             object[] vVertices = null;
             Vertex myVertex = default(Vertex);
             double[] vPoint = null;
             double X = 0;
             double Y = 0;
             double Z = 0;
             bool outer = false;
             string strOuter = null;
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
                 regionCount = mySketch.GetSketchRegionCount();
                 Debug.Print("");
                 Debug.Print(regionCount + " regions in sketch " + myFeature.Name);

                 vSkRegions = (object[])mySketch.GetSketchRegions();

                 for (i = vSkRegions.GetLowerBound(0); i <= vSkRegions.GetUpperBound(0); i++)
                 {
                     skRegion = (SketchRegion)vSkRegions[i];

                     if ((skRegion != null))
                     {
                         Debug.Print("  Region " + i +  ":");
                         j = 0;
                         myLoop = skRegion.GetFirstLoop();
                         while ((myLoop != null))
                         {
                             edgeCount = myLoop.GetEdgeCount();
                             vertexCount = myLoop.GetVertexCount();
                             outer = myLoop.IsOuter();

                             if (outer == false)
                             {
                                 strOuter =  "Inner loop";
                             }
                             else
                             {
                                 strOuter =  "Outer loop";
                             }

                             Debug.Print("    Loop " + j +  ": " + edgeCount +  " edges, " + vertexCount + " vertices, " + strOuter);

                             vEdges = (object[])myLoop.GetEdges();

                             for (k = vEdges.GetLowerBound(0); k <= vEdges.GetUpperBound(0); k++)
                             {
                                 myEdge = (Edge)vEdges[k];
                                 if ((myEdge != null))
                                 {
                                     Debug.Print("      Edge " + k +  ": ");
                                 }

                             }

                             vVertices = (object[])myLoop.GetVertices();

                             for (k = vVertices.GetLowerBound(0); k <= vVertices.GetUpperBound(0); k++)
                             {
                                 myVertex = (Vertex)vVertices[k];
                                 if ((myVertex != null))
                                 {
                                     vPoint = (double[])myVertex.GetPoint();
                                     X = vPoint[0];
                                     Y = vPoint[1];
                                     Z = vPoint[2];

                                     Debug.Print("      Vertex " + k +  ": " +  "(" + X +  ", " + Y + ", " + Z + ")");
                                 }
                             }

                             myLoop = (Loop2)myLoop.GetNext();
                             j = j + 1;
                         }

                         boolstatus = skRegion.Select2(false, mySelectData);
                         if (boolstatus == false)
                         {
                             Debug.Print("    Selection of region failed.");
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
