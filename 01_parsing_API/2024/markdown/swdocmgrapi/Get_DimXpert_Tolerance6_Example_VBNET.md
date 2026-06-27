---
title: "Get DimXpert Tolerance6 Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Tolerance6_Example_VBNET.htm"
---

# Get DimXpert Tolerance6 Example (VB.NET)

This example builds a part to demonstrate usage of the
SOLIDWORKS Document Manager API for the following DimXpert annotations:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Surface profile geometric tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Tangency
geometric tolerance

```vb
 '-------------------------------------------------------------------------
' kadov_tag{{<spaces>}}1. Open public_documents\samples\tutorial\cosmosxpress\aw_anchor_plate.sldprt.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2. Open the DimXpert toolbar from View > Toolbars
'    (select the first instance of Toolbars on the View menu).
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}3. Create a surface profile tolerance:
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}a. Click Datum on the DimXpert toolbar.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}b. Click a top face of the part.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}c. Click outside the part to place Datum A.
' kadov_tag{{<spaces>}}   d. Click a back face of the part.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}e. Click outside the part to place Datum B.
' kadov_tag{{<spaces>}}   f. Click a side face of the part.
' kadov_tag{{<spaces>}}   g. Click outside the part to place Datum C.
' kadov_tag{{<spaces>}}   h. Click Geometric Tolerance on the DimXpert toolbar.
' kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}In the Geometric Tolerance Properties dialog:
' kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}i.    Select Profile of Surface from the Symbol dropdown list.
' kadov_tag{{<spaces>}}      ii.   Type 50 in Tolerance 1.
'       iii.  Type A in the Primary box and C in the
'             Secondary box.
' kadov_tag{{<spaces>}}      iv.   In the second row, select Profile of Surface from
'             the Symbol dropdown list.
'       v.    In the second row, type 50 in Tolerance 1.
' kadov_tag{{<spaces>}}      vi.   In the second row, type A in the Primary box.
' kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}vii.  Select the Composite frame check box.
' kadov_tag{{<spaces>}}      viii. Click the front curve of the hook.
' kadov_tag{{<spaces>}}      ix.   Click outside the part to place the annotation.
' kadov_tag{{<spaces>}}      x.    Click OK to close the Geometric Tolerance
'             Properties dialog.
' kadov_tag{{<spaces>}}   i. In the DimXpertManager tab of the Management Panel,
'       expand Cylinder1.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}j. Observe the following DimXpert annotations: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
'       Surface Profile1 and Surface Profile2
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}4. Create tangency tolerances:
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}a. Click Auto Dimension Scheme on the DimXpert toolbar.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}b. Select all feature filters.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}c. Click the green check mark to accept the settings.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}d. Observe several tangency tolerance annotations.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}5. Close the part, saving it to another name.
' kadov_tag{{<spaces>}}   NOTE: Because this part is used in a SOLIDWORKS online
'          tutorial, do not save any changes to the original
'          file name.
' kadov_tag{{<spaces>}}6. Read how to load and run Code_Example_VBNET with this part.
 ' --------------------------------------------------------------------------
```
