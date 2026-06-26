---
title: "Get DimXpert Compound Width and Best Fit Plane Features Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Width_and_Bestfit_Plane_Features_Example_CSharp.htm"
---

# Get DimXpert Compound Width and Best Fit Plane Features Example (C#)

This example builds a part to demonstrate usage of the
SOLIDWORKS Document Manager API for the following DimXpert features:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Width

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Best fit
plane

//----------------------------------------------------------------------

//kadov_tag{{<spaces>}}1.
Open`public_documents`**\samples\tutorial\api\block.sldprt.**

//kadov_tag{{<spaces>}}2.
Open the DimXpert toolbar from**View > Toolbars**

// (select the first instance
of Toolbars on the View menu).

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}3.
Create the DimXpert best fit plane feature:

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}a.
Click**Location Dimension**on the DimXpert toolbar.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}b.
Select the left-front face of the block.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}c.
Click**Compound Plane**on the DimXpert pop-up

// toolbar.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}d.
Select the right front face of the block.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}e.
Click the green check mark on the DimXpert pop-up toolbar.

//kadov_tag{{<spaces>}}f.
Select the back face of the block.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}g.
Click outside the part to place the location dimension

// annotation.

// h. Observe the best fit plane DimXpert
feature on the

// DimXpertManager tab.

//kadov_tag{{<spaces>}}4.
Create the DimXpert width feature:

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}a.
Click**Size Dimension**on the DimXpert toolbar.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}b.
Select a front face of the block.

//kadov_tag{{<spaces>}}c. Click**Width**on the DimXpert pop-up toolbar.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}d.
Select the back face of the block.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}e.
Click the green check mark on the DimXpert pop-up toolbar.

//kadov_tag{{<spaces>}}f.
Click outside the part to place the size dimension annotation.

//kadov_tag{{<spaces>}}5.
Observe the following DimXpert feature on the DimXpertManager

// tab:kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}**Width1**.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}6.
Close the part, saving it to another name.

//kadov_tag{{<spaces>}}NOTE:
Because this part is used in a SOLIDWORKS online

// tutorial, do not save
any changes to the original

// file name.

//kadov_tag{{<spaces>}}7.
Read how to load and run[Code_Example_CSharp](Code_Example_CSharp.htm)with this part.

//----------------------------------------------------------------------
