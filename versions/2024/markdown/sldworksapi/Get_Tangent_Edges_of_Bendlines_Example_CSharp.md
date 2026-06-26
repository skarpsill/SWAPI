---
title: "Get Tangent Edges of Bendlines Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Tangent_Edges_of_Bendlines_Example_CSharp.htm"
---

# Get Tangent Edges of Bendlines Example (C#)

This example shows how to get each bendline's visible tangent edges
in a flat-pattern view in a drawing of a sheet metal part.

```
//---------------------------------------------------
// Preconditions:
// 1. Open a SOLIDWORKS drawing of a sheet metal part
//    that has a flat-pattern view with
//    bend lines with tangent edges.
// 2. Open the Immediate window.
//
// Preconditions: Examine the Immediate window.
//---------------------------------------------------
using SolidWorks.Interop.sldworks;
```

```vb
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace GetBendlinesTangentEdges_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DrawingDoc swDrawing = default(DrawingDoc);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Sheet swSheet = default(Sheet);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}View swView = default(View);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}long nbrBendlines = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] BendlinesArr = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}long nbrRelatedTangentEdges = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object RelatedTangentEdgesArr = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}long i = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SketchSegment swSketchSegment = default(SketchSegment);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDrawing = (DrawingDoc)swModel;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get drawing sheet
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSheet = (Sheet)swDrawing.GetCurrentSheet();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get name of drawing sheet
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Name of drawing sheet: " + swSheet.GetName());

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get number of views on drawing sheet
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" Number of drawing views on drawing sheet: " + swDrawing.GetViewCount());

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// First view is the current drawing sheet
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swView = (View)swDrawing.GetFirstView();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" First drawing view is the current drawing sheet, so...");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get first drawing view on drawing sheet
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swView = (View)swView.GetNextView();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}while ((swView != null))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Get next drawing view on drawing sheet...");

kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Get first true drawing view on current drawing sheet
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Is this drawing view a flat-pattern view? " + swView.IsFlatPatternView());

kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// If this drawing view is a flat pattern view, then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// get its bendlines and their related tangent edges
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (swView.IsFlatPatternView())
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}// Get number of bendlines in the drawing view
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}nbrBendlines = swView.GetBendLineCount();
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}BendlinesArr = new Object[nbrBendlines];
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Number of bendlines in this drawing view: " + nbrBendlines);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}if ((nbrBendlines > 0))
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}BendlinesArr = (Object[])swView.GetBendLines();
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}for (i = 0; i <= BendlinesArr.GetUpperBound(0); i++)
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}swSketchSegment = (SketchSegment)BendlinesArr[i];
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Debug.Print(" Is bend line " + i + " really a bend line? " + swSketchSegment.IsBendLine());
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}// Get the number of tangent lines related to
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}// the bendline
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}nbrRelatedTangentEdges = swView.GetRelatedTangentEdgeCount(BendlinesArr[i]);
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}Debug.Print(" Number of tangent edges for Bendline " + i + ": " + nbrRelatedTangentEdges);
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}// Get the tangent lines related to the bendline
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}if ((nbrRelatedTangentEdges > 0))
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}RelatedTangentEdgesArr = swView.GetRelatedTangentEdges(BendlinesArr[i]);
kadov_tag{{<spaces>}}                                kadov_tag{{</spaces>}}nbrRelatedTangentEdges = nbrRelatedTangentEdges - 1;
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Get next drawing view
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swView = (View)swView.GetNextView();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
