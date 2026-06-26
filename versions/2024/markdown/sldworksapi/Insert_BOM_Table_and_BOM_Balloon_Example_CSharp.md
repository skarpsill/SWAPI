---
title: "Insert BOM Table and BOM Balloon Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_BOM_Table_and_BOM_Balloon_Example_CSharp.htm"
---

# Insert BOM Table and BOM Balloon Example (C#)

This example shows how to insert a BOM table and a BOM balloon in a
drawing document.

```
//------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Inserts a parts-only BOM table.
// 2. Inserts a split-circle BOM balloon, which uses the BOM
//    table item number for its upper text,
//    to the selected edge.
// 3. Zoom to area and examine both the BOM table and BOM
//    balloon to verify.
//
// NOTE: Because this drawing document is used elsewhere,
// do not save any changes.
//-------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace InsertBOMBalloonModelDocExtension_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DrawingDoc swDrawing = default(DrawingDoc);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}View swView = default(View);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BomTableAnnotation swBOMAnnotation = default(BomTableAnnotation);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BomFeature swBOMFeature = default(BomFeature);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Note swNote = default(Note);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int AnchorType = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int BomType = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string Configuration = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string TableTemplate = null;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDrawing = (DrawingDoc)swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swDrawing.ActivateView("Drawing View1");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swView = (View)swDrawing.ActiveDrawingView;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Insert parts-only BOM table
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AnchorType = (int)swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BomType = (int)swBomType_e.swBomType_PartsOnly;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Configuration = "";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}TableTemplate = "";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swBOMAnnotation = swView.InsertBomTable2(false, 0.4, 0.3, (int)AnchorType, (int)BomType, Configuration, TableTemplate);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swBOMFeature = swBOMAnnotation.BomFeature;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Print the name of the configuration used for the BOM table
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Name of configuration used for BOM table: " + swBOMFeature.Configuration);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Insert BOM balloon for the selected edge
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.1205506330468, 0.261655309417, -0.0004000000000133, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swNote = (Note)swModelDocExt.InsertBOMBalloon((int)swBalloonStyle_e.swBS_SplitCirc, (int)swBalloonFit_e.swBF_Tightest, (int)swBalloonTextContent_e.swBalloonTextItemNumber, "", (int)swBalloonTextContent_e.swBalloonTextCustom, "Lower text", (int)swBalloonFit_e.swBF_UserDef, true, 2, "Denotation Text"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}});
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get whether balloon is a BOM balloon;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// if so, print the name of the BOM balloon
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (swNote.IsBomBalloon())
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Name of BOM balloon: " + swNote.GetName());
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
