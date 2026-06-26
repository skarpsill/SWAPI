---
title: "Get DimXpert Tolerance3 Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Tolerance3_Example_CSharp.htm"
---

# Get DimXpert Tolerance3 Example (C#)

This example builds a part to demonstrate usage of the
SOLIDWORKS Document Manager API for the following DimXpert annotations:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Position
geometric tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Orientation
(Perpendicularity) geometric tolerance

```vb
 //-----------------------------------------------------------------------------
// kadov_tag{{<spaces>}}1. Open public_documents\samples\tutorial\api\cover_position.sldprt.
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2. Click Geometric Tolerance on the DimXpert toolbar.
// kadov_tag{{<spaces>}}   In the Geometric Tolerance Properties dialog:
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}a. Select Position from the Symbol dropdown
//       list in the first row.
// kadov_tag{{<spaces>}}   b. Type A in Primary, B in Secondary, and C in Tertiary.
// kadov_tag{{<spaces>}}   c. In second row (lower tier), select Position from the
//       Symbol dropdown list.
// kadov_tag{{<spaces>}}   d. Type 0.25 in Tolerance1.
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}e. Type A in Primary.
// kadov_tag{{<spaces>}}   f. Select the Composite frame check box.
// kadov_tag{{<spaces>}}   g. Click the circular face of the boss.
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}h. Click outside the part to place the annotation.
// kadov_tag{{<spaces>}}   i. Click OK to close the Geometric Tolerance
//       Properties dialog.
// kadov_tag{{<spaces>}}3. Observe the following DimXpert annotations: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
//    Position1 and Perpendicularity1.
// kadov_tag{{<spaces>}}4. Close the part, saving it to another name.
// kadov_tag{{<spaces>}}   NOTE: Because this part is used in a SOLIDWORKS online
//          tutorial, do not save any changes to the original file name.
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}5. Read how to load and run Code_Example_CSharp with this part.
 //------------------------------------------------------------------------------
```
