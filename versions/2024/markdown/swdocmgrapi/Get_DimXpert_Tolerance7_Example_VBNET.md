---
title: "Get DimXpert Tolerance7 Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Tolerance7_Example_VBNET.htm"
---

# Get DimXpert Tolerance7 Example (VB.NET)

This example builds a part to demonstrate usage of the SOLIDWORKS Document
Manager API for a DimXpert line profile geometric tolerance annotation.

```vb
 '--------------------------------------------------------------------------
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1. Open public_documents\samples\tutorial\api\plate_tolstatus.sldprt.
' kadov_tag{{<spaces>}}2. Open the DimXpert toolbar from View > Toolbars
'    (select the first instance of Toolbars on the View menu).
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}3. Click Datum on the DimXpert toolbar and create
'    Datum A somewhere on the part.
' kadov_tag{{<spaces>}}4. Create the line profile geometric tolerance:
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}a. Click Geometric Tolerance on the DimXpert toolbar.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}   In the Geometric Tolerance Properties dialog:
' kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}i.    Select Line Profile from the Symbol dropdown in
'                the first row.
' kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}} ii.   Type A in Primary of the first row.
' kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}  iii.  In the second row, select Line Profile from the Symbol
'                dropdown list.
' kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}iv.   In the second row, type a tolerance in Tolerance 1.
' kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}v.    In the second row, type A in Primary.
' kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}} vi.   Select Composite frame.
' kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}  vii.  Click the inner face of the hole.
' kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}   viii. Click outside the part to place the annotation.
' kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}} ix.   Click OK to close the Geometric Tolerance
'                Properties dialog.
' kadov_tag{{<spaces>}}   b. Observe LineProfile1 and LineProfile2 under SimpleHole1
'       in the DimXpert tree.
' kadov_tag{{<spaces>}}5. Close the part, saving it to another name.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}NOTE: Because these parts are used in a SOLIDWORKS online
'          tutorial, do not save any changes to the original
'          file name.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}6. Read how to load and run Code_Example_VBNET with this part.
 '-----------------------------------------------------------------------------
```
