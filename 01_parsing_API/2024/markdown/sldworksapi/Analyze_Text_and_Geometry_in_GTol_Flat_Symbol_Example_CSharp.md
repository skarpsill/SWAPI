---
title: "Analyze Text and Geometry in GTol Flat Symbol Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Analyze_Text_and_Geometry_in_GTol_Flat_Symbol_Example_CSharp.htm"
---

# Analyze Text and Geometry in GTol Flat Symbol Example (C#)

## Analyze Text and Geometry in GTol Symbol Example (C#)

This example shows how to analyze the text and geometry in a GTol symbol.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified part document exists.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the specified part document.
 // 2. Gets whether <"GTOL-SPROF"> is bound.
  // 3. Gets the number of lines, arcs, circles, text strings,
 //    and triangles in <"GTOL-SPROF">.
  // 4. Gets the number of point coordinates in the
 //    lines in <"GTOL-SPROF">.
 // 5. Gets the x,y,z coordinates for the first and
 //    second points  of each line in <"GTOL-SPROF">.
 // 6. Gets the arc information for <"GTOL-SPROF">.
 // 7. Examine the Immediate window.
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
 namespace GetGTolSymbolInfo_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         SolidWorks.Interop.sldworks.Environment swEnvironment;
         string fileName;
         int errors;
         int warnings;
         short[] nbrSymbols;
         double[] lineSymbols;
         double[] arcInfo;
         int nbrLineCoordinates;
         int i;

         public void Main()
         {

             fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\tolanalyst\\minimum_clearance\\top_plate.sldprt";
             swModel = swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             swEnvironment = (SolidWorks.Interop.sldworks.Environment)swApp.GetEnvironment();

             Debug.Print("GTOL library - Surface Profile symbol name:");

             //Get whether <"GTOL-SPROF"> is bound
             bool bound;
             swEnvironment.GetIsBound("<GTOL-SPROF>", out bound);
             Debug.Print(" Bound? " + bound);
             Debug.Print("");

             //Get the number of lines, arcs, circles, text strings,
             //and triangles in <"GTOL-SPROF">
             nbrSymbols = (short[])swEnvironment.GetSymEdgeCounts("<GTOL-SPROF>");
             Debug.Print(" Line count:     " + nbrSymbols[0]);
             Debug.Print(" Arc count:      " + nbrSymbols[1]);
             Debug.Print(" Circle count:   " + nbrSymbols[2]);
             Debug.Print(" Text count:     " + nbrSymbols[3]);
             Debug.Print(" Triangle count: " + nbrSymbols[4]);
             Debug.Print("");
             Debug.Print("Number of lines: " + nbrSymbols[0]);

             //Get the x,y,z coordinates for the first
             //and second points of each line
             lineSymbols = (double[])swEnvironment.GetSymLines("<GTOL-SPROF>");
             nbrLineCoordinates = lineSymbols.GetUpperBound(0);
             Debug.Print("  Number of point coordinates: " + (nbrLineCoordinates + 1));
             Debug.Print("     Point coordinates:");
             Debug.Print("       (Line 1's x,y,z coordinates for first and second points,");
             Debug.Print("        Line 2's x,y,z coordinates for first and second points,");
             Debug.Print("        ...)");
             for (i = 0; i <= nbrLineCoordinates; i++)
             {
                 Debug.Print("        " + lineSymbols[i]);
             }
             Debug.Print("");
             Debug.Print("Number of arcs: " + nbrSymbols[1]);

             //Get the x,y,z coordinates of the center, start,
             //and end points of each arc, whether the arc is filled, and
             //whether a chord joining the start and end points of
             //the arc is drawn
             Debug.Print("  x,y,z coordinates of the center, start, and end points of each arc,");
             Debug.Print("  whether the arc is filled (1 = true, 0 = false),");
             Debug.Print("  and whether a chord is displayed for each arc (1 = true, 0 = false):");
             arcInfo = (double[])swEnvironment.GetSymArcs2("<GTOL-SPROF>");
             for (i = 0; i <= arcInfo.GetUpperBound(0); i++)
             {
                 Debug.Print("        " + arcInfo[i]);
             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
