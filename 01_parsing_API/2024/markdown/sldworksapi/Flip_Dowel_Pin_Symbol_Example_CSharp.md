---
title: "Flip Dowel Pin Symbol Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Flip_Dowel_Pin_Symbol_Example_CSharp.htm"
---

# Flip Dowel Pin Symbol Example (C#)

This example shows how to insert and flip a dowel pin symbol in a drawing.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified drawing document
//    to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified drawing document.
// 2. Selects a circular edge in a drawing view.
// 3. Inserts a dowel pin symbol.
// 4. Selects the dowel pin symbol and flips it.
// 5. Examine the drawing and the Immediate window.
//
// NOTE: Because the drawing is used elsewhere, do not save changes.
//--------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace DowelSymbolCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            DrawingDoc swDrawingDoc = default(DrawingDoc);
            DowelSymbol swDowelSymbol = default(DowelSymbol);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Annotation swAnnotation = default(Annotation);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            //Open drawing document and insert a dowel pin symbol
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\assem20.slddrw";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("", "EDGE", 0.128048002364532, 0.165546371003625, -1499.96487716824, false, 0, null, 0);
            swDrawingDoc = (DrawingDoc)swModel;
            swDowelSymbol = (DowelSymbol)swDrawingDoc.InsertDowelSymbol();
            swModel.ClearSelection2(true);

            //Flip the dowel pin symbol
            status = swModelDocExt.SelectByID2("DetailItem354@Drawing View1", "DOWELSYM", 0.121630029714286, 0.180965058285714, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swDowelSymbol = (DowelSymbol)swSelectionMgr.GetSelectedObject6(1, -1);
            swDowelSymbol.Flipped = true;
            swModel.EditRebuild3();
            Debug.Print("Dowel pin symbol flipped? " + swDowelSymbol.Flipped);
            swAnnotation = (Annotation)swDowelSymbol.GetAnnotation();
            Debug.Print("Name of dowel pin symbol annotation: " + swAnnotation.GetName());

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
