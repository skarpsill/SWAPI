---
title: "Get Weld Bead Symbol Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Weld_Bead_End_Treatment_Symbol_Data_Example_CSharp.htm"
---

# Get Weld Bead Symbol Data Example (C#)

This example shows how to get weld bead symbol data in a drawing.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
  // 1. Open a drawing that contains at least one view with a weld bead
 //    annotation.
 // 2. Open an Immediate window.
 //
 // Postconditions: Inspect the Immediate window.
  //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace WeldBead_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             DrawingDoc swDraw = default(DrawingDoc);
             Sheet swSheet = default(Sheet);
             View swView = default(View);
             WeldBead swWBead = default(WeldBead);
             DisplayData swDispData = default(DisplayData);
             string strFilled = null;
             int lineCount = 0;
             double[] vLine = null;
             int lineColor = 0;
             int lineLineType = 0;
             int lineStyle = 0;
             int lineWeight = 0;
             double lineX = 0;
             double lineY = 0;
             double lineZ = 0;
             int polygonCount = 0;
             double[] vPolygon = null;
             int polyColor = 0;
             int polyLineType = 0;
             int polyNumPts = 0;
             double polyX = 0;
             double polyY = 0;
             double polyZ = 0;
             int index = 0;
             int index2 = 0;
             int arrayIndex = 0;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swDraw = (DrawingDoc)swModel;
             swSheet = (Sheet)swDraw.GetCurrentSheet();
             swView = (View)swDraw.GetFirstView();

             while ((swView != null))
             {
                 Debug.Print(swView.Name);
                 swWBead = swView.GetFirstWeldBead();

                 while ((swWBead != null))
                 {
                     Debug.Print("  Weld Bead...");
                     if ((swWBead.SolidFill == false))
                     {
                         strFilled = "open";
                     }
                     else
                     {
                         strFilled = "solid filled";
                     }

                     swDispData = (DisplayData)swWBead.GetAnnotation().GetDisplayData();
                     lineCount = swDispData.GetLineCount();
                     Debug.Print("    Line count = " + lineCount);

                     for (index = 0; index <= lineCount - 1; index++)
                     {
                         vLine = (double[])swDispData.GetLineAtIndex3(index);
                         if ((vLine != null))
                         {
                             lineColor = (int)vLine[0];
                             lineLineType = (int)vLine[1];
                             lineStyle = (int)vLine[2];
                             lineWeight = (int)vLine[3];
                             Debug.Print("      Color = " + lineColor + ", line type = " + lineLineType + ", line style = " + lineStyle + ", line weight = " + lineWeight);

                             arrayIndex = 4;
                             for (index2 = 0; index2 <= 1; index2++)
                             {
                                 lineX = (double)vLine[arrayIndex];
                                 lineY = (double)vLine[arrayIndex + 1];
                                 lineZ = (double)vLine[arrayIndex + 2];
                                 Debug.Print("       " + index2 + " (" + lineX + ", " + lineY + ", " + lineZ + ")");
                                 arrayIndex = arrayIndex + 3;
                             }
                         }
                     }

                     Debug.Print("    Polyline count = " + swDispData.GetPolyLineCount());
                     Debug.Print("    Arc count = " + swDispData.GetArcCount());
                     polygonCount = swDispData.GetPolygonCount();
                     Debug.Print("    Polygon count = " + polygonCount);

                     for (index = 0; index <= polygonCount - 1; index++)
                     {
                         vPolygon = (double[])swDispData.GetPolygonAtIndex(index);
                         if ((vPolygon != null))
                         {
                             polyColor = (int)vPolygon[0];
                             polyLineType = (int)vPolygon[1];
                             polyNumPts = (int)vPolygon[4];
                             Debug.Print("      Color = " + polyColor + ", line type = " + polyLineType + ", point count = " + polyNumPts + ", " + strFilled);
                             arrayIndex = 5;

                             for (index2 = 0; index2 <= polyNumPts - 1; index2++)
                             {
                                 polyX = (double)vPolygon[arrayIndex];
                                 polyY = (double)vPolygon[arrayIndex + 1];
                                 polyZ = (double)vPolygon[arrayIndex + 2];
                                 Debug.Print("       " + index2 + " (" + polyX + ", " + polyY + ", " + polyZ + ")");
                                 arrayIndex = arrayIndex + 3;
                             }
                         }
                     }
                     swWBead = swWBead.GetNext();
                 }
                 swView = (View)swView.GetNextView();
             }

         }

         public SldWorks swApp;

     }

 }
```
