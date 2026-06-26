---
title: "Insert Part Number Column in BOM Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Part_Number_Column_in_BOM_Table_Example_CSharp.htm"
---

# Insert Part Number Column in BOM Table Example (C#)

This example shows how to insert a part number column in a BOM table.

```
//----------------------------------------------------
// Preconditions:
// 1. Open a drawing with a BOM table.
// 2. Right-click the BOM table, select Select,
//    and select Table.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Inserts a  part number column at the end of the
//    the BOM table.
// 2. Examine the BOM table and the Immediate window.
//----------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
using System.Windows.Forms;

namespace GetColumnTitleCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            bool boolstatus = false;
            SelectionMgr SelMgr = null;
            TableAnnotation theTableAnnotation = default(TableAnnotation);
            int SelObjType = 0;
            int TableAnnotationType = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            SelMgr = (SelectionMgr)swModel.SelectionManager;
            SelObjType = (int)SelMgr.GetSelectedObjectType2(1);
            if (SelObjType != (int)swSelectType_e.swSelANNOTATIONTABLES)
            {
                MessageBox.Show("Select a BOM table in the drawing before running this macro.");
                return;
            }
            theTableAnnotation = (TableAnnotation)SelMgr.GetSelectedObject6(1, -1);
            TableAnnotationType = theTableAnnotation.Type;
            if (TableAnnotationType != (int)swTableAnnotationType_e.swTableAnnotation_BillOfMaterials)
            {
                MessageBox.Show("Select a BOM table in the drawing before running this example.");
                return;
            }
            DisplayTableColumnProps(theTableAnnotation);
            boolstatus = theTableAnnotation.InsertColumn((int)swTableItemInsertPosition_e.swTableItemInsertPosition_Last, 0, "New Column");
            boolstatus = theTableAnnotation.SetColumnType(theTableAnnotation.ColumnCount - 1, (int)swTableColumnTypes_e.swBomTableColumnType_PartNumber);
            DisplayTableColumnProps(theTableAnnotation);

        }

        public void DisplayTableColumnProps(TableAnnotation theTableAnnotation)
        {
            int ColCount = 0;
            int i = 0;
            int ColType = 0;
            string ColTitle = null;

            Debug.Print("Index" + "\t" + "Type" + "\t" + "Title");
            ColCount = theTableAnnotation.ColumnCount;
            for (i = 0; i <= ColCount - 1; i++)
            {
                ColType = theTableAnnotation.GetColumnType(i);
                ColTitle = theTableAnnotation.GetColumnTitle(i);
                Debug.Print("\t" + i + "\t" + ColType + "\t\t" + ColTitle);
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
