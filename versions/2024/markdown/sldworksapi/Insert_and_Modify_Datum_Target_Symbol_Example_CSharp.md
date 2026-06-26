---
title: "Insert and Modify Datum Target Symbol Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Modify_Datum_Target_Symbol_Example_CSharp.htm"
---

# Insert and Modify Datum Target Symbol Example (C#)

This example shows how to insert and modify a datum target symbol.

```
//------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Inserts a datum target symbol on the selected
//    face.
// 3. Gets and modifies the datum target symbol's reference label.
// 4. Examine the Immediate window and graphics area.
//
// NOTE: Because the part document is used elsewhere,
// do not save any changes.
//------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace DatumTargetSymCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            DatumTargetSym swDatumTargetSym = default(DatumTargetSym);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            //Open part document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\holecube.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Select face for datum target symbol
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("", "FACE", -0.00723565448987529, -0.0259480787517532, 0, false, 0, null, 0);

            //Insert datum target symbol
            swDatumTargetSym = (DatumTargetSym)swModelDocExt.InsertDatumTargetSymbol3("a", "", "", 0, false, 0.003, 0.03, "3", "", true,
            12, 0, true, false, true, (int)swMoveableDatumStyle_e.swMoveableDatumStyle_Horizontal);

            //Get and set datum reference label
            Debug.Print("Current reference label: " + swDatumTargetSym.GetDatumReferenceLabel(0));
            status = swDatumTargetSym.SetDatumReferenceLabel(0, "b");
            Debug.Print("Modified reference label: " + swDatumTargetSym.GetDatumReferenceLabel(0));

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
