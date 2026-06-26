---
title: "Get Drawing Sheets Properties (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Drawing_Sheets_Properties_Example_CSharp.htm"
---

# Get Drawing Sheets Properties (C#)

## Get Drawing Sheets' Properties Example (C#)

This example shows how to get the properties of a drawing's sheets.

```vb
 //--------------------------------------------------------------------------
 // Preconditions:
 // 1. Read the SOLIDWORKS Document Manager API Getting Started topic
 //    and ensure that the required DLLs are registered.
 // 2. Copy and paste this code into a C# console application
 //    in Microsoft Visual Studio.
 // 3. Add the SolidWorks.Interop.swdocumentmgr.dll reference
 //    to the project:
 //    a. Right-click the solution in Solution Explorer.
 //    b. Click Add Reference.
 //    c. Click Browse.
 //    d. Click:
 //       install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll
 // 4. Ensure that the specified drawing document exists.
 // 5. Open the Immediate window.
 // 6. Substitute your_license_key with your SOLIDWORKS Document
 //    Manager license key.
 // 7. Run the macro.
 //
 // Postconditions: Examine the Immediate window.
 //---------------------------------------------------------------------------
```

```vb
 using System;
 using System.Diagnostics;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using SolidWorks.Interop.swdocumentmgr;

     class Program
     {
         static void Main(string[] args) {
             SwDMClassFactory swClassFact;
             SwDMApplication docMgrApp;
             SwDMDocument13 docDrw;
             SwDmDocumentOpenError res;

             swClassFact = new SwDMClassFactory();
             docMgrApp = (SwDMApplication)swClassFact.GetApplication("your_license_key");
             string sDocFileName;
             sDocFileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw";
             docDrw = (SwDMDocument13)docMgrApp.GetDocument(sDocFileName, SwDmDocumentType.swDmDocumentDrawing, true, out res);
             string[] sheetNameVar;
             int sheetCount;

             sheetCount = docDrw.GetSheetCount();
             sheetNameVar = (string[])docDrw.GetSheetNames();

             string sheetName;
             int sheetNameCount;
             for (sheetNameCount = 0; sheetNameCount <= sheetNameVar.Length - 1; sheetNameCount++)
             {
                 string formatName;
                 swSheetFormatPathResult status1;
                 sheetName = sheetNameVar[sheetNameCount];
                 status1 = (swSheetFormatPathResult)docDrw.GetSheetFormatPath(sheetName, out formatName);

                 Debug.Print(sheetName + " ---- " + formatName + "\n");

                 swSheetPropertiesResult status2;
                 object formatPropObj;

                 status2 = (swSheetPropertiesResult)docDrw.GetSheetProperties(sheetName, out formatPropObj);

                 double[] formatProp = (double[])formatPropObj;

                 double para;
                 para = System.Math.Round(formatProp[0]);

                 string paperSize;

                 GetPaperSize(para, out paperSize);

                 Debug.Print("Paper Size = " + paperSize);
                 Debug.Print("Size = " + formatProp[1] + " x " + formatProp[2]);
                 Debug.Print("Scale = " + formatProp[3] + " : " + formatProp[4]);

                 bool boolData;

                 boolData = false;

                 if ((formatProp[5] == 1))
                 {
                     boolData = true;
                 }

                 Debug.Print("First angle = " + boolData);
                 string templateSize;
                 para = System.Math.Round(formatProp[6]);
                 GetTemplateSize(para, out templateSize);
                 Debug.Print("Template size = " + templateSize);
                 boolData = false;

                 if ((formatProp[7] == 1))
                 {
                     boolData = true;
                 }

                 Debug.Print("Template visible = " + boolData);
                 Debug.Print("===========================================");
             }
             docDrw.CloseDoc();
         }

         static void GetPaperSize(double inpNum, out string outPaperType)
         {
             if ((inpNum == 0))
             {
                 outPaperType = "swDwgPaperAsize";
             }
             else if ((inpNum == 1))
             {
                 outPaperType = "swDwgPaperAsizeVertical";
             }
             else if ((inpNum == 2))
             {
                 outPaperType = "swDwgPaperBsize";
             }
             else if ((inpNum == 3))
             {
                 outPaperType = "swDwgPaperCsize";
             }
             else if ((inpNum == 4))
             {
                 outPaperType = "swDwgPaperDsize";
             }
             else if ((inpNum == 5))
             {
                 outPaperType = "swDwgPaperEsize";
             }
             else if ((inpNum == 6))
             {
                 outPaperType = "swDwgPaperA4size";
             }
             else if ((inpNum == 7))
             {
                 outPaperType = "swDwgPaperA4sizeVertical";
             }
             else if ((inpNum == 8))
             {
                 outPaperType = "swDwgPaperA3size";
             }
             else if ((inpNum == 9))
             {
                 outPaperType = "swDwgPaperA2size";
             }
             else if ((inpNum == 10))
             {
                 outPaperType = "swDwgPaperA1size";
             }
             else if ((inpNum == 11))
             {
                 outPaperType = "swDwgPaperA0size";
             }
             else
             {
                 outPaperType = "swDwgPapersUserDefined";
             }
         }

         static void GetTemplateSize(double inpNum, out string outTemplateType)
         {
             if ((inpNum == 0))
             {
                 outTemplateType = "swDwgTemplateAsize";
             }
             else if ((inpNum == 1))
             {
                 outTemplateType = "swDwgTemplateAsizeVertical";
             }
             else if ((inpNum == 2))
             {
                 outTemplateType = "swDwgTemplateBsize";
             }
             else if ((inpNum == 3))
             {
                 outTemplateType = "swDwgTemplateCsize";
             }
             else if ((inpNum == 4))
             {
                 outTemplateType = "swDwgTemplateDsize";
             }
             else if ((inpNum == 5))
             {
                 outTemplateType = "swDwgTemplateEsize";
             }
             else if ((inpNum == 6))
             {
                 outTemplateType = "swDwgTemplateA4size";
             }
             else if ((inpNum == 7))
             {
                 outTemplateType = "swDwgTemplateA4sizeVertical";
             }
             else if ((inpNum == 8))
             {
                 outTemplateType = "swDwgTemplateA3size";
             }
             else if ((inpNum == 9))
             {
                 outTemplateType = "swDwgTemplateA2size";
             }
             else if ((inpNum == 10))
             {
                 outTemplateType = "swDwgTemplateA1size";
             }
             else if ((inpNum == 11))
             {
                 outTemplateType = "swDwgTemplateA0size";
             }
             else if ((inpNum == 12))
             {
                 outTemplateType = "swDwgTemplateCustom";
             }
             else
             {
                 outTemplateType = "swDwgTemplateNone";
             }
         }

     }
```
