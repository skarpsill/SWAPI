---
title: "Get DimXpert Tolerance8 Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Tolerance8_Example_CSharp.htm"
---

# Get DimXpert Tolerance8 Example (C#)

This example builds a part to demonstrate usage of the
SOLIDWORKS Document Manager API for the following DimXpert annotations:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Circular
runout geometric tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Total runout
geometric tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Angularity
geometric tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Parallelism
geometric tolerance

```vb
 //------------------------------------------------------------------------
// 1. Open public_documents\samples\tutorial\api\cover_datum.sldprt.
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2. Click Datum on the DimXpert toolbar and place
//    Datum A inside the hole.
// kadov_tag{{<spaces>}}3. Create the circular runout geometric tolerance:
// kadov_tag{{<spaces>}}   a. Click Geometric Tolerance on the DimXpert toolbar.
// kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}In the Geometric Tolerance Properties dialog:
// kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}i.   Select Circular Runout from the Symbol dropdown
//            list in the first row.
// kadov_tag{{<spaces>}}      ii.  In the Primary field, type A.
// kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}iii. Click the outer cylinder of the part and click
//            again outside the part to place
// kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}   the annotation.
// kadov_tag{{<spaces>}}      iv.  Click OK to close the Geometric Tolerance
//            Properties dialog.
// kadov_tag{{<spaces>}}   b. Observe CircularRunout1 under Cylinder1 in the
//       DimXpert tree.
// kadov_tag{{<spaces>}}4. Create the total runout geometric tolerance:
// kadov_tag{{<spaces>}}   a. Click Geometric Tolerance on the DimXpert toolbar.
// kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}In the Geometric Tolerance Properties dialog:
// kadov_tag{{<spaces>}}      i.   Select Total Runout from the Symbol dropdown
//            list in the first row.
// kadov_tag{{<spaces>}}      ii.  In the Primary field, type A.
// kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}iii. Click the boss of the part and click again
//            outside the part to place
// kadov_tag{{<spaces>}}           the annotation.
// kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}iv.  Click OK to close the Geometric Tolerance
//            Properties dialog.
// kadov_tag{{<spaces>}}   b. Observe TotalRunout1 under Boss1 in the DimXpert
//       tree.
// kadov_tag{{<spaces>}}5. Create the angularity geometric tolerance:
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}a. Click Geometric Tolerance on the DimXpert toolbar.
// kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}In the Geometric Tolerance Properties dialog:
// kadov_tag{{<spaces>}}      i.   Select Angularity from the Symbol dropdown
//            in the first row.
// kadov_tag{{<spaces>}}      ii.  In the Primary field, type A.
// kadov_tag{{<spaces>}}      iii. Click a face of the notch and click again
// kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}   outside the part to place the annotation.
// kadov_tag{{<spaces>}}      iv.  Click OK to close the Geometric Tolerance
//            Properties dialog.
// kadov_tag{{<spaces>}}   b. Observe Angularity1 under Notch1 in the DimXpert
//       tree.
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}6. Create the parallelism geometric tolerance:
// kadov_tag{{<spaces>}}   a. Click Geometric Tolerance on the DimXpert toolbar.
// kadov_tag{{<spaces>}}      In the Geometric Tolerance Properties dialog:
// kadov_tag{{<spaces>}}      i.   Select Parallel from the Symbol dropdown
//            in the first row.
// kadov_tag{{<spaces>}}      ii.  In the Primary field, type A.
// kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}iii. Click the boss of the part and click again
// kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}   outside the part to place the annotation.
// kadov_tag{{<spaces>}}      iv.  Click OK to close the Geometric Tolerance
//            Properties dialog.
// kadov_tag{{<spaces>}}   b. Observe Parallelism1 under Boss1 in the DimXpert tree.
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}7. Close the part, saving it to another name.
// kadov_tag{{<spaces>}}    NOTE: Because this part is used in a SOLIDWORKS online
//           tutorial, do not save any changes to the original
//           file name.
// kadov_tag{{<spaces>}}8. Read how to load and run Code_Example_CSharp with this part.
 //------------------------------------------------------------------------
```
