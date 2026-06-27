---
title: "Get DimXpert Intersect Features Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Intersect_Features_Example_CSharp.htm"
---

# Get DimXpert Intersect Features Example (C#)

This example builds a part to demonstrate usage of the
SOLIDWORKS Document Manager API for the following DimXpert features:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Intersect
Point

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Intersect
Line

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Intersect
Circle

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Intersect
Plane

//--------------------------------------------------------------------------

//kadov_tag{{<spaces>}}1.
Open`public_documents`**\samples\tutorial\api\face_plate_ads_geo.sldprt.**

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2.
Open the DimXpert toolbar from**View > Toolbars**

// (select the first instance
of Toolbars on the View menu).

//kadov_tag{{<spaces>}}3.
Create a DimXpert Intersect Point Feature:

//kadov_tag{{<spaces>}}a.
Click**Location Dimension**on the DimXpert toolbar.

//kadov_tag{{<spaces>}}b.
Select the front face of the part.

//kadov_tag{{<spaces>}}c. Click**Create Intersection Point**on the DimXpert pop-up menu.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}d.
Select a cylinder whose axis intersects the first face at a point.

//kadov_tag{{<spaces>}}e.
Click the green check mark in the pop-up menu to create the

// intersect
point.

//kadov_tag{{<spaces>}}f.
Select a feature on the part to dimension against the intersect point.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}g.
Click outside the part to position the dimension in the view.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}h.
Observe the new DimXpert feature on the DimXpertManager tab:kadov_tag{{<spaces>}}

//**Intersect
Point1**

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}4.
Create a DimXpert Intersect Line Feature:

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}a.
Click**Location Dimension**on the DimXpert toolbar.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}b.
Select the front face of the part.

//kadov_tag{{<spaces>}}c.
Click**Create Intersection Line**on the DimXpert pop-up menu.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}d.
Select a perpendicular plane that would intersect the first plane

// if extended
(e.g., a top or side face of the part)

//kadov_tag{{<spaces>}}e.
Click the green check mark in the pop-up menu to create the

// intersect
line.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}f.
Select a feature on the part to dimension against the intersect line.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}g.
Click outside the part to position the dimension in the view.

//kadov_tag{{<spaces>}}h.
Observe the new DimXpert feature on the DimXpertManager tab:kadov_tag{{<spaces>}}

//kadov_tag{{</spaces>}}**Intersect
Line1**

//kadov_tag{{<spaces>}}5.
Create a DimXpert Intersect Circle Feature:

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}a.
Click**Size Dimension**on the DimXpert toolbar.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}b.
Select the front face of the part.

//kadov_tag{{<spaces>}}c.
Click**Intersect Circle**on the DimXpert pop-up menu.

//kadov_tag{{<spaces>}}d.
Select the opening conical surface of a flat head machine screw

// (LPattern1
or LPattern3) in the part.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}e.
Click the green check mark in the pop-up menu to finish the dimension.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}f.
Click outside the part to position the size dimension in the view.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}g.
Observe the new DimXpert feature on the DimXpertManager tab:kadov_tag{{<spaces>}}

//**Intersect
Circle1**

//kadov_tag{{<spaces>}}6.
Create a DimXpert Intersect Plane Feature:

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}a.
Click**Location Dimension**on the DimXpert toolbar.

//kadov_tag{{<spaces>}}b.
Zoom in on a flat head machine screw (LPattern1 or LPattern3).

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}c.
Select the opening conical surface of a flat head machine screw

// in the
part.

//kadov_tag{{<spaces>}}d.
Click**Intersect Plane**on the DimXpert pop-up menu.

//kadov_tag{{<spaces>}}e.
Select the inner cylindrical bore face of the flat head machine screw.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}f.
Click the green check mark in the pop-up menu to create the

// intersect
plane.

//kadov_tag{{<spaces>}}g.
Select the top face of one of the extruded entities.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}h.
Click outside the part to position the location dimension in the view.

//kadov_tag{{<spaces>}}i.
Observe the new DimXpert feature on the DimXpertManager tab:kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

//**Intersect
Plane1**

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}7.
Close the part, saving it to another name.

//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}NOTE:
Because this part is used in a SOLIDWORKS online tutorial,

// do not save
any changes to the original file name.

//kadov_tag{{<spaces>}}8.
Read how to load and run[Code_Example_CSharp](Code_Example_CSharp.htm)with this part.

//---------------------------------------------------------------------------
