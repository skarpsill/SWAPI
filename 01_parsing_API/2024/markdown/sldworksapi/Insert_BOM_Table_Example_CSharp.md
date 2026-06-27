---
title: "Insert BOM Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_BOM_Table_Example_CSharp.htm"
---

# Insert BOM Table Example (C#)

This example shows how to insert a BOM table using IView::InsertBomTable2.

```
//-----------------------------------------------------
// Preconditions: Open a drawing document and select
// a drawing view.
//
// Postconditions:
// 1. Inserts a BOM at the anchor point, if the
//    drawing view does not already contain a BOM.
// 2. Examine the drawing and FeatureManager design tree.
//-----------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace SetConfigurationsCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            FeatureManager swFeatMgr = default(FeatureManager);
            View swView = default(View);
            BomTableAnnotation swBomAnn = default(BomTableAnnotation);
            BomFeature swBomFeat = default(BomFeature);
            int AnchorType = 0;
            int BomType = 0;
            string Configuration = null;
            string TableTemplate = null;
            object Names = null;
            object Visible = null;
            bool boolstatus = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swFeatMgr = (FeatureManager)swModel.FeatureManager;

            // Get selected drawing view
            swView = (View)swSelMgr.GetSelectedObject6(1, 0);
            AnchorType = (int)swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_BottomLeft;
            BomType = (int)swBomType_e.swBomType_TopLevelOnly;
            Configuration = "";
            TableTemplate = "";

            // Insert BOM table
            swBomAnn = (BomTableAnnotation)swView.InsertBomTable2(true, 0.4, 0.3, AnchorType, BomType, Configuration, TableTemplate);

            swModel.ClearSelection2(true);

            // Because BOM type is swBomType_TopLevelOnly,
            // then work with BomFeature to get and set configurations
            swBomFeat = (BomFeature)swBomAnn.BomFeature;
            Names = swBomFeat.GetConfigurations(false, ref Visible);
            Visible = true;
            boolstatus = swBomFeat.SetConfigurations(true, Visible, Names);

            // Update FeatureManager design tree
            swFeatMgr.UpdateFeatureTree();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
