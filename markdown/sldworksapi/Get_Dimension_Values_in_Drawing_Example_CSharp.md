---
title: "Get Dimension Values in Drawing Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Dimension_Values_in_Drawing_Example_CSharp.htm"
---

# Get Dimension Values in Drawing Example (C#)

This example shows how to get the values of the dimensions in a drawing.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a drawing document.
 // 2. Open the Immediate window.
 //
 // Postconditions: Inspect the Immediate window.
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
 namespace GetDimensionValues_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             DrawingDoc swDraw = default(DrawingDoc);
             View swView = default(View);
             DisplayDimension swDispDim = default(DisplayDimension);
             Dimension swDim = default(Dimension);
             Annotation swAnn = default(Annotation);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swDraw = (DrawingDoc)swModel;

             Debug.Print("File = " + swModel.GetPathName());

             swView = (View)swDraw.GetFirstView();

             while ((swView != null))
             {
                 Debug.Print("  View = " + swView.Name);

                 swDispDim = swView.GetFirstDisplayDimension5();

                 while ((swDispDim != null))
                 {
                     swAnn = (Annotation)swDispDim.GetAnnotation();
                     swDim = (Dimension)swDispDim.GetDimension();

                     Debug.Print("    ------------------------------------");
                     Debug.Print("    AnnName = " + swAnn.GetName());
                     Debug.Print("      DimFullName                  = " + swDim.FullName);
                     Debug.Print("      DimName                      = " + swDim.Name);
                     Debug.Print("      swDimensionParamType_e type  = " + swDim.GetType());
                     Debug.Print("      DrivenState                  = " + swDim.DrivenState);
                     Debug.Print("      ReadOnly                     = " + swDim.ReadOnly);
                     Debug.Print("      Value                        = " + swDim.GetSystemValue2(""));
                     Debug.Print("");
                     Debug.Print("      Arrowside                    = " + swDispDim.ArrowSide);
                     Debug.Print("      TextAll                      = " + swDispDim.GetText((int)swDimensionTextParts_e.swDimensionTextAll));
                     Debug.Print("      TextPrefix                   = " + swDispDim.GetText((int)swDimensionTextParts_e.swDimensionTextPrefix));
                     Debug.Print("      TextSuffix                   = " + swDispDim.GetText((int)swDimensionTextParts_e.swDimensionTextSuffix));
                     Debug.Print("      CalloutAbove                 = " + swDispDim.GetText((int)swDimensionTextParts_e.swDimensionTextCalloutAbove));
                     Debug.Print("      CalloutBelow                 = " + swDispDim.GetText((int)swDimensionTextParts_e.swDimensionTextCalloutBelow));

                     swDispDim = (DisplayDimension)swDispDim.GetNext3();

                 }

                 swView = (View)swView.GetNextView();

             }

         }

         public SldWorks swApp;

     }

 }
```
