---
title: "Get Title Block Tables Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Title_Block_Tables_Example_CSharp.htm"
---

# Get Title Block Tables Example (C#)

This example shows how to get title block tables.

```
//-------------------------------------------------
// Preconditions:
// 1. Open a part that does not contain any annotations.
// 2. Verify that the specified table template exists.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Inspect the output in the Immediate window.
// 2. Observe the new title block table feature under Tables
//    in the FeatureManager design tree (if necessary, right-click the
//    part in the FeatureManager design tree, click Hidden Tree
//    Items > Hide/Show Tree Items > Show in the Tables drop-down list).
// 3. Observe the corresponding title block table annotation
//    in the graphics area.
//--------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        ModelDoc2 Part;
        TitleBlockTableAnnotation tbtAnno;
        TitleBlockTableAnnotation anno;
        TitleBlockTableAnnotation tabannoObject;
        TitleBlockTableFeature feat;
        TitleBlockTableFeature tabfeatObject;
        object[] annos;
        int I;
        SelectionMgr selMgr;
        bool boolstatus;

        public void Main()
        {

            Part = (ModelDoc2)swApp.ActiveDoc;
            Debug.Print("Inserting a title block table into the model using a general table template (*.sldtbt)");
            Debug.Print("");
            tbtAnno = Part.Extension.InsertTitleBlockTable("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\connector-table.sldtbt", 500, 500);
            feat = tbtAnno.TitleBlockTableFeature;
            Debug.Print("Title block table feature: " + feat.GetFeature().Name);
            string count = null;
            count = feat.GetTableAnnotationCount().ToString();
            Debug.Print("Title block table annotation count: " + count);
            Debug.Print("Title block table annotations");
            annos = (Object[])feat.GetTableAnnotations();
            for (I = 0; I <= annos.GetUpperBound(0); I++)
            {
                anno = (TitleBlockTableAnnotation)annos[I];
                Debug.Print(" Title block table feature: " + anno.TitleBlockTableFeature.GetFeature().Name);
            }
            Debug.Print("");

            Debug.Print("Selecting title block table feature through SelectByID2 type, TITLEBLOCKTABLEFEAT");
            boolstatus = Part.Extension.SelectByID2(feat.GetFeature().Name, "TITLEBLOCKTABLEFEAT", 0, 0, 0, false, 0, null, 0);
            Debug.Print("  Casting selected object to ITitleBlockTableFeature");
            selMgr = (SelectionMgr)Part.SelectionManager;
            tabfeatObject = (TitleBlockTableFeature)selMgr.GetSelectedObject6(1, -1);
            Debug.Print("   Title block table feature: " + tabfeatObject.GetFeature().Name);
            Debug.Print("");

            Debug.Print("Selecting title block table annotation through SelectByID2 type, ANNOTATIONTABLES");
            boolstatus = Part.Extension.SelectByID2("DetailItem1@Annotations", "ANNOTATIONTABLES", -0.1205280774849, -0.01199819470702, 0.04087038255709, false, 0, null, 0);
            Debug.Print("  Casting selected object to ITitleBlockTableAnnotation type...");
            tabannoObject = (TitleBlockTableAnnotation)selMgr.GetSelectedObject6(1, -1);
            Debug.Print("    Getting title block table feature from the title block table annotation");
            Debug.Print("       Title block table feature: " + tabannoObject.TitleBlockTableFeature.GetFeature().Name);
            Debug.Print("");

            Debug.Print("  Casting selected object to ITableAnnotation type");
            TableAnnotation annoObject = default(TableAnnotation);
            annoObject = (TableAnnotation)selMgr.GetSelectedObject6(1, -1);
            swTableAnnotationType_e annoType;
            annoType = (swTableAnnotationType_e)annoObject.Type;
            if (annoType == swTableAnnotationType_e.swTableAnnotation_TitleBlock)
            {
                Debug.Print("     The selected table annotation is defined in swTableAnnotationType_e as TitleBlock");
            }
            else
            {
                Debug.Print("     The selected table annotation is defined in swTableAnnotationType_e with value: " + annoType);
            }
        }
        public SldWorks swApp;
    }
}
```
