---
title: "Get DimXpert Tolerance4 Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Tolerance4_Example_CSharp.htm"
---

# Get DimXpert Tolerance4 Example (C#)

This example builds a part to demonstrate usage of the
SOLIDWORKS Document Manager API for the following DimXpert annotations:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Angle-between
dimension tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Chamfer
dimension tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Line Profile
geometric tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Straightness
geometric tolerance

```vb
 //--------------------------------------------------------------------------
// kadov_tag{{<spaces>}}1. Open public_documents\samples\tutorial\api\plate_tolstatus.sldprt.
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2. Open the DimXpert toolbar from View > Toolbars
//    (select the first instance of Toolbars on the View menu).
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}3. Create the chamfer dimension tolerance:
// kadov_tag{{<spaces>}}   a. Click Auto-Dimension Scheme on the DimXpert toolbar.
// kadov_tag{{<spaces>}}   b. Ensure that the Chamfer feature filter is selected.
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}c. Click the green arrow to accept the settings.
// kadov_tag{{<spaces>}}   d. Observe ChamferDepth1 and ChamferDepth2 in the DimXpert tree.
// kadov_tag{{<spaces>}}4. Create angle-between dimension tolerance:
// kadov_tag{{<spaces>}}   a. Click Location Dimension on the DimXpert toolbar.
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}b. Click a face of the part.
//    c. Click a face perpendicular to the face selected
//       in step 2 (not the chamfer).
// kadov_tag{{<spaces>}}   d. Click outside the part to place the annotation.
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}e. Find the following in the DimXpert tree: kadov_tag{{<spaces>}}kadov_tag{{</spaces>}} AngleBetween1.
// kadov_tag{{<spaces>}}5. Create line profile and straightness geometric tolerances:
// kadov_tag{{<spaces>}}   a. Click  Geometric Tolerance on the DimXpert toolbar.
// kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}In the Geometric Tolerance Properties dialog:
// kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}i.   Select Straightness from the Symbol dropdown list.
// kadov_tag{{<spaces>}}      ii.  In second row, select Line Profile from the Symbol
//            dropdown list.
// kadov_tag{{<spaces>}}      iii. Type 0.25 in Tolerance1.
// kadov_tag{{<spaces>}}      iv.  Click the top face of the part.
// kadov_tag{{<spaces>}}      v.   Click outside the part to place the annotation.
// kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}vi.  Click OK to close the Geometric Tolerance
//            Properties dialog.
// kadov_tag{{<spaces>}}   b. Observe the following DimXpert annotations: kadov_tag{{<spaces>}}
//       LineProfile1 and Straightness1.
// kadov_tag{{<spaces>}}6. Close the part, saving it to another name.
// kadov_tag{{<spaces>}}   NOTE: Because these parts are used in a
//          SOLIDWORKS online tutorial, do not
//          save any changes to the original file name.
// kadov_tag{{<spaces>}}7. Read how to load and run Code_Example_CSharp with this part.
 //---------------------------------------------------------------------------
```
