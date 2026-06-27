---
title: "Create Detail Circle and Detail View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Detail_Circle_and_Detail_View_Example_CSharp.htm"
---

# Create Detail Circle and Detail View Example (C#)

This example shows how to create a detail circle and a detail view.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the drawing to open exists.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the specified drawing.
 // 2. Activates Drawing View4.
 // 3. Creates a detail circle and a detail view using the visible
 //    corner of Drawing View4.
 // 4. Activates the detail view.
 // 5. Gets and sets some properties of the detail circle and detail view.
 // 6. Examine the drawing document and Immediate window.
 //
 // NOTE: Because the drawing is used elsewhere, do not save changes.
 //------------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace Macro1CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             DrawingDoc swDrawing = default(DrawingDoc);
             SketchManager swSketchManager = default(SketchManager);
             SketchSegment swSketchSegment = default(SketchSegment);
             View swView = default(View);
             DetailCircle swDetailCircle = default(DetailCircle);
             SelectionMgr swSelMgr = default(SelectionMgr);
             SelectData swSelData = default(SelectData);
             string fileName = null;
             bool status = false;
             int errors = 0;
             int warnings = 0;

             // Open drawing
             fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\replaceview.slddrw";
             swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             swDrawing = (DrawingDoc)swModel;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swSelData = (SelectData)swSelMgr.CreateSelectData();
             swApp.ActivateDoc3("replaceview - Sheet1", false, (int)swRebuildOnActivation_e.swDontRebuildActiveDoc, ref errors);

             // Activate Drawing View4 and create detail circle and detail view
             status = swDrawing.ActivateView("Drawing View4");
             swSketchManager = (SketchManager)swModel.SketchManager;
             swSketchSegment = (SketchSegment)swSketchManager.CreateCircle(0.007581, 0.053509, 0.0, 0.013533, 0.016475, 0.0);
             swView = (View)swDrawing.CreateDetailViewAt4(0.22305342706156, 0.0762140266484527, 0, (int)swDetViewStyle_e.swDetViewSTANDARD, 1, 1, "A", (int)swDetCircleShowType_e.swDetCircleCIRCLE, true, true, false, 5);

             swModel.ClearSelection2(true);

             // Activate detail view
             status = swDrawing.ActivateView("Drawing View5");

             // Get and set some properties of detail circle and detail view
             swDetailCircle = (DetailCircle)swView.GetDetail();
             Debug.Print("Detail circle:");
             Debug.Print("  Selected: " + swDetailCircle.Select(true, null));
             Debug.Print("  Label: " + swDetailCircle.GetLabel());
              Double xpos;
             Double ypos;
             swDetailCircle.GetLabelPosition(out xpos, out ypos);
              Debug.Print("  Label X position: " + xpos);
             Debug.Print("  Label Y position: " + ypos);
             Debug.Print("  Type of circle: " + swDetailCircle.GetDisplay());
             Debug.Print("  Name: " + swDetailCircle.GetName());
             Debug.Print("  Style: " + swDetailCircle.GetStyle());
             Debug.Print("  Default document text formatting? " + swDetailCircle.GetUseDocTextFormat());
             if (swDetailCircle.NoOutline == false)
             {
                 Debug.Print("  No outline? False");
                 if (swDetailCircle.JaggedOutline == true)
                 {
                     swDetailCircle.ShapeIntensity = 2;
                     Debug.Print("  Jagged outline and shape intensity? True and 2");
                 }
             }
 }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
