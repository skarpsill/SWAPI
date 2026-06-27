---
title: "Get Table Cell Text Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Table_Cell_Text_Example_CSharp.htm"
---

# Get Table Cell Text Example (C#)

This example shows how to get all of the cell text
from a BOM table using the SOLIDWORKS Document Manager API.

```vb
// -------------------------------------------------------------------------
// Preconditions:
// 1. Read the SOLIDWORKS Document Manager API Help
//    Getting Started topic and ensure that the
//    required DLLs are registered.
// 2. Open SOLIDWORKS and copy the code below to a C# macro.
// 3. Ensure that the latest SolidWorks.Interop.swdocumentmgr.dll
//    interop assembly is loaded in the project.
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}(Right-click on the project in Project Explorer, click
//    Add Reference, kadov_tag{{</spaces>}} click the interop assembly in the .NET
//    tab, or browse for the DLL in install_dir\api\redist.)
// 4. In SOLIDWORKS, create a part document with a BOM table.
// 5. Save the part and close it.
// 6. Substitute your license key for your_license_key in the code.
// 7. Substitute the new file name for sFile in the code.
// 8. Uncomment the appropriate swDoc line.
//
// Postconditions: The Immediate Window displays the BOM
// table row and column count and all of the table's cell
// text in row order.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swdocumentmgr;
using System;
using System.Diagnostics;

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SwDMClassFactory classfac;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SwDMApplication tapp;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SwDMDocument13 swDoc;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SwDMTable3 swTable;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SwDmDocumentOpenError e;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string sFile;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}String[] vTables;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}String[] vTabArr;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SwDmTableError err;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int row;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int col;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int j;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}classfac = new SwDMClassFactory();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}tapp = classfac.GetApplication("your_license_key");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}sFile = "C:\\temp\\Part1.SLDPRT";

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//get the SW document file
swDoc = (SwDMDocument13)tapp.GetDocument(sFile, SwDmDocumentType.swDmDocumentPart, false, out e);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//swDoc = (SwDMDocument13)tapp.GetDocument(sFile, SwDmDocumentType.swDmDocumentAssembly, false, out e)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//swDoc = (SwDMDocument13)tapp.GetDocument(sFile, SwDmDocumentType.swDmDocumentDrawing, false, out e)

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Doc Version is " + swDoc.GetVersion());
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Doc name is " + swDoc.FullName);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}vTables = (String[])swDoc.GetTableNames(SwDmTableType.swDmTableTypeBOM);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if ((vTables != null))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swTable = (SwDMTable3)swDoc.GetTable((String)vTables[0]);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if ((swTable != null))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Table retrieved is " + vTables[0]);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}vTabArr = (String[])swTable.GetTableCellText(out err, out row, out col);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Row count is " + row);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Column count is " + col);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print("Table cell text:");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}for (j = 0; j <= vTabArr.GetUpperBound(0); j++)
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" " + vTabArr[j]);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDoc.CloseDoc();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
```
