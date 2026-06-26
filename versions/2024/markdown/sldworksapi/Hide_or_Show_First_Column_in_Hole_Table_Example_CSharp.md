---
title: "Hide or Show First Column in Hole Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_or_Show_First_Column_in_Hole_Table_Example_CSharp.htm"
---

# Hide or Show First Column in Hole Table Example (C#)

This example shows how to hide the first column in a hole table.

```vb
//-------------------------------------------------------------------
 // Preconditions:
 // kadov_tag{{<spaces>}}1. Open public_documents\samples\tutorial\api\simplehole.slddrw.
 // kadov_tag{{<spaces>}}2. Select the hole table feature in the FeatureManager
 // kadov_tag{{<spaces>}}   design tree.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Hides the first column.
 // kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2. Examine the hole table and Immediate window.
 //
 // NOTE: Because the drawing is used elsewhere, do not save changes.
 //------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace ColumnHiddenTableAnnotation_CSharp.csproj
 {
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectionMgr swSelMgr = default(SelectionMgr);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] swHoleTableAnnotation = new object[1];
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}TableAnnotation swTableAnnotation = default(TableAnnotation);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Annotation swAnnotation = default(Annotation);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}HoleTable swHoleTable = default(HoleTable);

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = (SelectionMgr)swModel.SelectionManager;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if ((swSelMgr.GetSelectedObjectCount() == 0 | !(swSelMgr.GetSelectedObjectType(1) == (int)swSelectType_e.swSelHOLETABLEFEATS)))
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}System.Windows.Forms.MessageBox.Show("Please select a hole table feature in the FeatureManager design tree.");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swHoleTable = (HoleTable)swSelMgr.GetSelectedObject6(1, -1);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swHoleTableAnnotation = (object[])swHoleTable.GetTableAnnotations();
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swTableAnnotation = (TableAnnotation)swHoleTableAnnotation[0];
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAnnotation = (Annotation)swTableAnnotation.GetAnnotation();
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// If column hidden, then show it
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if ((swTableAnnotation.get_ColumnHidden(0)))
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" First column hidden before API call: " + swTableAnnotation.get_ColumnHidden(0));
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swTableAnnotation.set_ColumnHidden(0, false);
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" First column hidden after API call: " + swTableAnnotation.get_ColumnHidden(0));
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// If column shown, then hide it
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" First column hidden before API call: " + swTableAnnotation.get_ColumnHidden(0));
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swTableAnnotation.set_ColumnHidden(0, true);
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" First column hidden after API call: " + swTableAnnotation.get_ColumnHidden(0));
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
 }
```
