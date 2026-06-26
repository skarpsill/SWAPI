---
title: "Insert Column in BOM Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Column_in_BOM_Table_Example_CSharp.htm"
---

# Insert Column in BOM Table Example (C#)

This example shows how to insert a part number column in a BOM table.

```
//---------------------------------------------------
// Preconditions:
// 1. Open a drawing that contains a BOM table.
// 2. Right-click the BOM table, select Select,
//    and select Table.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Inserts a part number column at the end of the
//    the BOM table.
// 2. Examine the BOM table and Immediate window.
//---------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Windows.Forms;
```

```vb
namespace InsertColumn2TableAnnotationCSharp.csproj
{
partial class SolidWorksMacro
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SelectionMgr SelMgr = default(SelectionMgr);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}TableAnnotation theTableAnnotation = default(TableAnnotation);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int SelObjType = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int TableAnnotationType = 0;

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SelMgr = (SelectionMgr)swModel.SelectionManager;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SelObjType = SelMgr.GetSelectedObjectType3(1, -1);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (SelObjType != (int)swSelectType_e.swSelANNOTATIONTABLES)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("Select a BOM table in the drawing before running this example.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}theTableAnnotation = (TableAnnotation)SelMgr.GetSelectedObject6(1, -1);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}TableAnnotationType = theTableAnnotation.Type;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}if (TableAnnotationType != (int)swTableAnnotationType_e.swTableAnnotation_BillOfMaterials)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("Select a BOM table in the drawing before running this example.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Table before inserting a column...");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Display table before inserting a column
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DisplayTableColumnProps(theTableAnnotation);

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Insert new column
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = theTableAnnotation.InsertColumn2((int)swTableItemInsertPosition_e.swTableItemInsertPosition_Last, 0, "New Column", (int)swInsertTableColumnWidthStyle_e.swInsertColumn_DefaultWidth);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = theTableAnnotation.SetColumnType2(theTableAnnotation.ColumnCount - 1, (int)swTableColumnTypes_e.swBomTableColumnType_PartNumber, true);

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" ");

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Table after inserting a column...");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Display table after inserting a column
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DisplayTableColumnProps(theTableAnnotation);
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public void DisplayTableColumnProps(TableAnnotation theTableAnnotation)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int ColCount = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int i = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string iString = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int ColType = 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string ColTypeString = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string ColTitle = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Col# " + "Type kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}" + "Title");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ColCount = theTableAnnotation.ColumnCount;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}for (i = 0; i <= ColCount - 1; i++)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ColType = theTableAnnotation.GetColumnType2(i, true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ColTypeString = System.Convert.ToString(ColType);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ColTitle = theTableAnnotation.GetColumnTitle2(i, true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iString = System.Convert.ToString(i);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(iString + " kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}" + ColTypeString + " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}" + ColTitle);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public SldWorks swApp;
}
}
```
