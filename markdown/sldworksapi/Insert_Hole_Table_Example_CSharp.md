---
title: "Insert Hole Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Hole_Table_Example_CSharp.htm"
---

# Insert Hole Table Example (C#)

This example shows how to insert a hole table in a drawing.

```
//---------------------------------------------------------------------------
// Preconditions: Ensure that the specified part to open, drawing template,
// and hole table template exist.
//
// Postconditions:
// 1. Opens the part and creates a drawing of it.
// 2. Inserts a hole table of the part in the drawing.
// 3. Examine the hole table in the drawing.
//
// NOTE: Because the part is used elsewhere, do not save changes.
// ---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {

        ModelDoc2 Part;
        DrawingDoc Drawing;
        bool boolstatus;

        public void Main()
        {
            DocumentSpecification spec = (DocumentSpecification)swApp.GetOpenDocSpec("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\cover_datum.sldprt");
            Part = (ModelDoc2)swApp.OpenDoc7(spec);
            Drawing = (DrawingDoc)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2019\\templates\\Drawing.drwdot", 2, 0.2794, 0.4318);
            Part = (ModelDoc2)Drawing;
            boolstatus = Part.Extension.SelectByID2("Sheet1", "SHEET", 0.39237, 0.5218942019544, 0, false, 0, null, 0);
            boolstatus = Drawing.Create3rdAngleViews2("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\cover_datum.sldprt");
            Part.ClearSelection2(true);

            boolstatus = Drawing.ActivateView("Drawing View1");

            //Select a vertex in the drawing view to be the origin of all datums in the table
            //All XLOC and YLOC table column values will be relative to this datum origin
            boolstatus = Part.Extension.SelectByID2("", "VERTEX", 0.117324728174898, 0.108554228680764, -500.0075, true, 1, null, 0);
            //Select a face that contains the holes that will be annotated in the table
            boolstatus = Part.Extension.SelectByID2("", "FACE", 0.090728339186173, 0.119052803281577, -500.0075, true, 2, null, 0);

            View myView = null;
            SelectionMgr selMgr = null;
            selMgr = (SelectionMgr)Part.SelectionManager;
            myView = selMgr.GetSelectedObjectsDrawingView2(1, -1);
            HoleTableAnnotation myHoleTable = null;
            //Insert a hole table
            //anchored with its top left corner at x-coordinate = 0.07m and y-coordinate = 0.175m,
            //with starting datum tag "A",
            //using hole table template: standard hole table--letters.sldholtbt
            myHoleTable = (HoleTableAnnotation)myView.InsertHoleTable3(false, 0.153019881817662, -3.77259107537343E-02, (int)swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft, "A", "C:\\Program Files\\SolidWorks Corp\\SOLIDWORKS\\lang\\english\\standard hole table--letters.sldholtbt", 1, 1, null);

            Part.ClearSelection2(true);

            boolstatus = Drawing.ActivateSheet("Sheet1");
        }

        public SldWorks swApp;

    }
}
```
