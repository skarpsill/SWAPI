---
title: "Get BOM Tables Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_BOM_Tables_Example_CSharp.htm"
---

# Get BOM Tables Example (C#)

This example shows how to get the BOM tables in a drawing document.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Create a console application using Visual C#.
 // 2. Verify that all output is redirected to the Immediate window. (In
 //    Visual Studio 2015, click Tools > Options > Debugging > General >
 //    Redirect all Output Window text to the Immediate Window).
 // 3. Click Project > Add Reference > install_dir/api/redist/
 //     SolidWorks.Interop.swdocumentmgr.dll > OK.
 // 4. Substitute your license key for your_license_key in the code.
 // 5. Copy the specified drawing document to another file name.
 // 6. Open the specified drawing document in SOLIDWORKS.
 // 7. Ensure that both Bills of Materials are not hidden.
 // 8. Save and rebuild the drawing.
 // 9. Close SOLIDWORKS.
 //
 // Postconditions: Prints to the Immediate window:
 // * Document:
 //   * Path and filename
 //   * Last saved date
 // * For each BOM table that is not hidden in the document:
 //   * Name
 //   * Whether hidden
 //   * Whether to display components with multiple configurations as one item
 //   * Part configuration grouping setting
 //   * Sheet name
 //   * Number of views on the sheet
 //   * Name of the custom property view for the sheet
 //
 // NOTE: Restore the original drawing document, as it is used elsewhere.
 //---------------------------------------------------------------------------

 using SolidWorks.Interop.swdocumentmgr;
 using System;
 using System.Diagnostics;

 namespace ConsoleApplication2
 {
     class Module1
     {
         static void Main()
         {
             SwDMClassFactory dmClassFact = default(SwDMClassFactory);
             SwDMApplication3 dmDocMgr = default(SwDMApplication3);
             ISwDMDocument15 dmDoc = default(ISwDMDocument15);
             ISwDMTable5 dmTable = default(ISwDMTable5);
             ISwDMSheet4 dmSheet = default(ISwDMSheet4);
             ISwDMView custPropView = default(ISwDMView);
             SwDmDocumentOpenError dmError = default(SwDmDocumentOpenError);
             Array arrViews = null;
             string nameDrawing = "";

             dmClassFact = new SwDMClassFactory();
             dmDocMgr = (SwDMApplication3)dmClassFact.GetApplication("your_license_key"); //Do not distribute
             nameDrawing = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\introsw\\cabinet_bath.slddrw";

             //Get the SOLIDWORKS drawing document
             dmDoc = (ISwDMDocument15)dmDocMgr.GetDocument(nameDrawing, SwDmDocumentType.swDmDocumentDrawing, false, out dmError);
             Debug.Print("Document's full name: " + dmDoc.FullName);
             Debug.Print("Date document last saved: " + dmDoc.LastSavedDate);

             // Get the names of the BOM tables that are not hidden in the SOLIDWORKS drawing document
             string[] tableNames = null;
             tableNames = (string[])dmDoc.GetTableNames(SwDmTableType.swDmTableTypeBOM);
             int i = 0;
             if ((tableNames != null))
             {
                 for (i = 0; i <= tableNames.Length - 1; i++)
                 {
                     dmTable = (SwDMTable5)dmDoc.GetTable(tableNames[i]);
                     Debug.Print(" BOM table name: " + dmTable.Name);
                     Debug.Print("   Is BOM table hidden? " + dmTable.Hidden);
                     Debug.Print("   If BOM table contains components with multiple configurations, display as one item? " + dmTable.DisplayAsOneItem);
                     Debug.Print("   Part configuration grouping as defined in swDMPartConfigurationGrouping:  " + dmTable.PartConfigurationGrouping);
                     dmSheet = (SwDMSheet4)dmTable.Sheet;
                     if (dmSheet != null)
                     {
                         custPropView = dmSheet.CustomPropertyView;
                         arrViews = dmSheet.GetViews();
                         Debug.Print("   On sheet: " + dmSheet.Name);
                         Debug.Print("   Number of views on sheet: " + arrViews.Length);
                         Debug.Print("   Custom property view: " + custPropView.Name);
                     }

                 }
             }
         }
     }
 }
```
