---
title: "Save File as PDF Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_File_as_PDF_Example_CSharp.htm"
---

# Save File as PDF Example (C#)

This example shows how to save multiple drawing sheets to a PDF file.

```vb
 //--------------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified drawing document to open exists.
 // 2. Verify that c:\test, the folder where to save
 //    the PDF file, exists. If it does not exist,
 //    create it or change the path to a folder that
 //    exists on your system.
 //
 // Postconditions:
 // 1. Opens the specified drawing document.
 // 2. Saves all but the last drawing sheet to an array.
 // 3. Saves the array of drawing sheets ato a PDF file
 //    called foodprocessor.pdf.
 // 4. Opens foodprocessor.pdf.
 //---------------------------------------------------------------------------

 using System.Runtime.InteropServices;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;

 namespace ViewPDF_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             ExportPdfData swExportPDFData = default(ExportPdfData);
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModExt = default(ModelDocExtension);
             DrawingDoc swDrawDoc = default(DrawingDoc);
             Sheet swSheet = default(Sheet);
             bool boolstatus = false;
             string filename = null;
             int errors = 0;
             int warnings = 0;
             string[] obj = null;

             // Save PDF file to this folder and filename
             filename =  "c:\\test\\foodprocessor.pdf";

             // Open drawing document
             swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw", (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             swModExt = (ModelDocExtension)swModel.Extension;
             swExportPDFData = (ExportPdfData)swApp.GetExportFileData((int)swExportDataFileType_e.swExportPdfData);

             // Get the names of the drawing sheets in the drawing
             // to get the size of the array of drawing sheets
             swDrawDoc = (DrawingDoc)swModel;

             obj = (string[])swDrawDoc.GetSheetNames();
             int count = 0;
             count = obj.Length;
             int i = 0;
             object[] objs = new object[count - 1];
              DispatchWrapper[] arrObjIn = new DispatchWrapper[count - 1];

             // Activate each drawing sheet, except the last drawing sheet, for
             // demonstration purposes only and add each sheet to an array
             // of drawing sheets
             for (i = 0; i < count - 1; i++)
             {
                 boolstatus = swDrawDoc.ActivateSheet((obj[i]));
                 swSheet = (Sheet)swDrawDoc.GetCurrentSheet();
                 objs[i] = swSheet;
                 arrObjIn[i] = new DispatchWrapper(objs[i]);

             }

             // Save the drawings sheets to a PDF file
             boolstatus = swExportPDFData.SetSheets((int)swExportDataSheetsToExport_e.swExportData_ExportSpecifiedSheets, (arrObjIn));
             swExportPDFData.ViewPdfAfterSaving =  true;
             boolstatus = swModExt.SaveAs(filename, (int)swSaveAsVersion_e.swSaveAsCurrentVersion, (int)swSaveAsOptions_e.swSaveAsOptions_Silent, swExportPDFData, ref errors, ref warnings);
         }

         public SldWorks swApp;

     }

 }
```
