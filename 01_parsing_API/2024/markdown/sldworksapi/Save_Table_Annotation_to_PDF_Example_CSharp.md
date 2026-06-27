---
title: "Save Table to PDF Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Table_Annotation_to_PDF_Example_CSharp.htm"
---

# Save Table to PDF Example (C#)

This example shows how to save a table as a PDF file.

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Open a part document that contains a table annotation.
// 2. Select the table annotation.
//
// Postconditions:
// 1. Saves the selected table as c:\test\table.pdf.
// 2. Examine c:\test\table.pdf.
//-----------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace SaveAsPDFCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            TableAnnotation swTableAnnotation = default(TableAnnotation);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;

            //Get the selected table and save it as a PDF file
            swTableAnnotation = (TableAnnotation)swSelectionMgr.GetSelectedObject6(1, 0);
            swTableAnnotation.SaveAsPDF("c:\\test\\table.pdf");

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;
    }

}
```
