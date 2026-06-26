---
title: "Isolate Changed Dimension Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Isolate_Changed_Dimension_Example_CSharp.htm"
---

# Isolate Changed Dimension Example (C#)

This example shows how to isolate a changed dimension.

```vb
 //------------------------------------------------------
 // Preconditions: The specified drawing and part
 // documents exist.
 //
 // Postconditions:
 // 1. Opens the drawing document.
 // 2. Sets the system option to display
 //    changed dimensions in the color selected
 //    for Tools > Options > System Options >
 //    Colors > Color scheme settings >
 //    Drawings, Changed dimensions.
 // 3. Saves and closes the drawing document.
 // 4. Opens the part document of the drawing document.
 // 5. Changes a dimension.
 // 6. Saves and closes the part document.
 // 7. Opens the previously saved drawing document.
 // 8. Examine the drawing document to verify that
 //    the changed dimension is displayed in the
 //    changed-dimension color. Place your cursor over
 //    the dimension  to see its previous value.
 //-------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;

 namespace IsolateChangedDimensionsDrawingDocCSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt =  default(ModelDocExtension);
             DrawingDoc swDrawing = default(DrawingDoc);
             string fileName = null;
             string saveFileName = null;
             int errors = 0;
             int warnings = 0;
             bool status = false;

             // Open drawing document
             fileName =  "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\box.slddrw";
             swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

             // Isolate changed dimensions
             // Equivalent to selecting Tools > Options > System Options > Colors >
             // Use specified color for changed drawing dimensions on open
             swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swUseChangedDimensions, true);
             swDrawing = (DrawingDoc)swModel;
             swDrawing.IsolateChangedDimensions();

             // Save drawing document to another name
             saveFileName =  "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\box_changed.slddrw";
             swModelDocExt = (ModelDocExtension)swModel.Extension;
             status = swModelDocExt.SaveAs(saveFileName, (int)swSaveAsVersion_e.swSaveAsCurrentVersion, (int)swSaveAsOptions_e.swSaveAsOptions_Silent, null, ref errors, ref warnings);
             swApp.CloseDoc(saveFileName);

             // Open the part document referenced by the drawing document,
             // change a dimension, and save the document
             fileName =  "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\box.sldprt";
             swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             swModelDocExt = (ModelDocExtension)swModel.Extension;
             status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, true, 0, null, 0);
             status = swModelDocExt.SelectByID2("D2@Sketch1@box.SLDPRT", "DIMENSION", -0.03613329319351, -0.02215939491444, 0.02938582119709,  true, 0,  null, 0);
             Dimension swDimension = default(Dimension);
             swDimension = (Dimension)swModel.Parameter("D2@Sketch1");
             swDimension.SystemValue = 0.185;
             swModel.ClearSelection2(true);
             status = swModel.EditRebuild3();
             status = swModel.Save3((int)swSaveAsOptions_e.swSaveAsOptions_Silent, ref errors, ref warnings);
             swApp.CloseDoc(fileName);

             // Open the previously saved drawing document
             // and place your cursor on the changed dimension,
             // which displays in the color specified for
             // changed dimensions, to see its previous value
             swModel = (ModelDoc2)swApp.OpenDoc6(saveFileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
