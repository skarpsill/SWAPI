---
title: "Get DimXpert Tolerance5 Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Tolerance5_Example_VBNET.htm"
---

# Get DimXpert Tolerance5 Example (VB.NET)

This example builds a part to demonstrate usage of the SOLIDWORKS Document
Manager API for a DimXpert concentricity
geometric tolerance annotation.

```vb
 '-----------------------------------------------------------------------------
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1. Open public_documents\samples\tutorial\api\cover_with_dimensions.sldprt.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2. Open the DimXpert toolbar from View > Toolbars
'    (select the first instance of Toolbars on the View menu).
' kadov_tag{{<spaces>}}3. Create concentricity tolerance:
' kadov_tag{{<spaces>}}   a. Click Datum on the DimXpert toolbar.
' kadov_tag{{<spaces>}}   b. Click Boss1 (front extrusion).
' kadov_tag{{<spaces>}}   c. Click outside the part to place the annotation.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}d. Click the green check mark to accept Datum A.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}e. Click Geometric Tolerance on the DimXpert toolbar.
' kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}In the Geometric Tolerance Properties dialog:
' kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}i.   Select Concentricity from the Symbol dropdown list.
' kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}} ii.  Click inside the Tolerance 1 field.
' kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}} iii. Click Diameter on the toolbar
'                 at the top of the dialog.
' kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}} iv.  Type A in the Primary field.
' kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}v.   Click the inside face of Simple Hole2.
' kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}vi.  Click outside the part to place the annotation.
' kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}  vii. Click OK to close the Geometric Tolerance
'                 Properties dialog.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}f. In the DimXpertManager tab of the Management Panel,
'       expand Simple Hole2.
' kadov_tag{{<spaces>}}   g. Observe the following Dimxpert annotation: kadov_tag{{<spaces>}}kadov_tag{{</spaces>}} Concentricity1.
' kadov_tag{{<spaces>}}4. Close the part, saving it to another name.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}NOTE: Because this part is used in a SOLIDWORKS online
'          tutorial, do not save any changes to the original
'          file name.
' kadov_tag{{<spaces>}}5. Read how to load and run Code_Example_VBNET with this part.
 '-------------------------------------------------------------------------------
```
