---
title: "Get DimXpert Surface Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Surface_Feature_Example_CSharp.htm"
---

# Get DimXpert Surface Feature Example (C#)

This example builds a part to demonstrate usage of the
SOLIDWORKS Document Manager API for a DimXpert surface feature.

```vb
 //---------------------------------------------------------------------------
 // kadov_tag{{<spaces>}}1. Open:
 // public_documents\samples\tutorial\moldedproductdesignadvanced\mousesplit.sldprt
 // kadov_tag{{<spaces>}}2. Open the DimXpert toolbar from View > Toolbars
 //    (select the first instance of Toolbars on the View menu).
 // kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}3. Create the DimXpert surface feature:
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}a. Click Geometric Tolerance on the DimXpert toolbar.
 // kadov_tag{{<spaces>}}      In the Geometric Tolerance Properties dialog:
 // kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}i.   Select Profile of Surface from the Symbol dropdown
 //            list in the first row.
 //kadov_tag{{<spaces>}}       ii.  Click the top-right surface of the mouse.
 //kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}iii. Click outside the part to place the annotation.
 //kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}iv.  Click OK to close the Geometric Tolerance
 //            Properties dialog.
 // kadov_tag{{<spaces>}}   b. Observe SurfaceProfile1 under Profile Feature1 in the DimXpert tree.
 // kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}4. Close the part, saving it to another name.
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}NOTE: Because these parts are used in a SOLIDWORKS
 //          online tutorial, do not save any changes to the
 //          original file name.
 // kadov_tag{{<spaces>}}5. Read how to load and run Code_Example_CSharp with this part.
 //---------------------------------------------------------------------------
```
