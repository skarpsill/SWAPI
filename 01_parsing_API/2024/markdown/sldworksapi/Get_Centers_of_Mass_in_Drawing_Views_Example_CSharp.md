---
title: "Get Centers of Mass in Drawing Views Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Centers_of_Mass_in_Drawing_Views_Example_CSharp.htm"
---

# Get Centers of Mass in Drawing Views Example (C#)

This example shows how to get the centers of mass in drawing views.

```vb
 //----------------------------------------------------------------------
 // Preconditions: Open a drawing that has one or more centers of mass.
 //
 // Postconditions: Inspect the Immediate window for the coordinates of
 // all of the centers of mass in all of the views of the
 // drawing.
 //----------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace CenterOfMass_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         DrawingDoc swDrawDoc;
         View swView;
         CenterOfMass swCenterOfMass;
         Annotation swAnnotation;
         int sheetCount;
         int viewCount;
         object[] ss;
         object[] vv;
         double[] coord;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swDrawDoc = (DrawingDoc)swModel;

             viewCount = swDrawDoc.GetViewCount();
             ss = (object[])swDrawDoc.GetViews();

             for (sheetCount = ss.GetLowerBound(0); sheetCount <= ss.GetUpperBound(0); sheetCount++)
             {
                 vv = (object[])ss[sheetCount];
                 for (viewCount = 1; viewCount <= vv.GetUpperBound(0); viewCount++)
                 {
                     Debug.Print(((View)vv[viewCount]).GetName2());
                     swView = (View)vv[viewCount];
                     swCenterOfMass = (CenterOfMass)swView.GetFirstCenterOfMass();
                     if ((swCenterOfMass != null))
                     {
                         swAnnotation = (Annotation)swCenterOfMass.GetAnnotation();
                         if ((swAnnotation != null))
                         {
                             Debug.Print("  Annotation name: " + swAnnotation.GetName());
                         }
                         coord = (double[])swCenterOfMass.GetCoordinates();
                         Debug.Print("  Center of mass coordinates: X: " + coord[0] + ", Y: " + coord[1] + ", and Z: " + coord[2]);

                         while ((swCenterOfMass.GetNext() != null))
                         {
                             swCenterOfMass = (CenterOfMass)swCenterOfMass.GetNext();
                             if ((swCenterOfMass != null))
                             {
                                 swAnnotation = (Annotation)swCenterOfMass.GetAnnotation();
                                 if ((swAnnotation != null))
                                 {
                                     Debug.Print("  Annotation name: " + swAnnotation.GetName());
                                 }
                                 coord = (double[])swCenterOfMass.GetCoordinates();
                                 Debug.Print("  Center of mass coordinates: X: " + coord[0] + ", Y: " + coord[1] + ", and Z: " + coord[2]);
                             }
                         }
                     }
                 }

             }

         }

         public SldWorks swApp;

     }
 }
```
