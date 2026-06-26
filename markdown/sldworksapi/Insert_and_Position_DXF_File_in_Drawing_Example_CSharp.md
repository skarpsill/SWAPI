---
title: "Insert and Position DXF/DWG File in Drawing Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Position_DXF_File_in_Drawing_Example_CSharp.htm"
---

# Insert and Position DXF/DWG File in Drawing Example (C#)

This example shows how to insert and position a DXF/DWG file in a drawing.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a drawing.
 // 2. Replace DXF_file_path with the pathname of an existing DXF/DWG file.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Inserts the DXF/DWG file as per the specified import data.
 // 2. Inspect the Immediate window.
 //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 namespace InsertDXFDrawing_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             const string sDwgFileName = "DXF_file_path";

             ModelDoc2 swModel = default(ModelDoc2);
             ModelView swModelView = default(ModelView);
             DrawingDoc swDraw = default(DrawingDoc);
             FeatureManager swFeatMgr = default(FeatureManager);
             Feature swFeat = default(Feature);
             Sketch swSketch = default(Sketch);
             View swView = default(View);
             double[] vPos = null;
             bool bRet = false;
             ImportDxfDwgData importData = default(ImportDxfDwgData);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelView = (ModelView)swModel.ActiveView;

             bRet = swModel.Extension.SelectByID2("Sheet1", "SHEET", 0.0, 0.0, 0, false, 0, null, 0);

             swDraw = (DrawingDoc)swModel;
             swFeatMgr = swModel.FeatureManager;
             importData = (ImportDxfDwgData)swApp.GetImportFileData(sDwgFileName);

             // Unit
             importData.set_LengthUnit("", (int)swLengthUnit_e.swINCHES);

             // Position
             bRet = importData.SetPosition("", (int)swDwgImportEntitiesPositioning_e.swDwgEntitiesCentered, 0, 0);

             // Sheet scale
             bRet = importData.SetSheetScale("", 1.0, 2.0);

             // Paper size
             bRet = importData.SetPaperSize("", (int)swDwgPaperSizes_e.swDwgPaperAsize, 0.0, 0.0);

             //Import method
             importData.set_ImportMethod("", (int)swImportDxfDwg_ImportMethod_e.swImportDxfDwg_ImportToExistingDrawing);

             // Import file with importData
             swFeat = swFeatMgr.InsertDwgOrDxfFile2(sDwgFileName, importData);
             swSketch = (Sketch)swFeat.GetSpecificFeature2();

             swView = (View)swDraw.GetFirstView();

             while ((swView != null))
             {
                 if (object.ReferenceEquals(swSketch, swView.GetSketch()))
                 {
                     break;
                 }
                 swView = (View)swView.GetNextView();
             }

             vPos = (double[])swView.Position;

             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("  Sketch       = " + swFeat.Name);
             Debug.Print("  View         = " + swView.Name);
             Debug.Print("    Old Pos    = (" + vPos[0] * 1000.0 +  ", " + vPos[1] * 1000.0 + ") mm");

             // Move to right
             vPos[0] = vPos[0] + 0.01;
             swView.Position = vPos;

             vPos = (double[])swView.Position;
             Debug.Print("    New Pos    = (" + vPos[0] * 1000.0 +  ", " + vPos[1] * 1000.0 + ") mm");

             // Redraw
             double[] rect = null;
             rect = null;
             swModelView.GraphicsRedraw(rect);

         }

         public SldWorks swApp;

     }
 }
```
