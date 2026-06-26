---
title: "Get DimXpert Tolerance2 Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Tolerance2_Example_VBNET.htm"
---

# Get DimXpert Tolerance2 Example (VB.NET)

This example builds a part to demonstrate usage of the
SOLIDWORKS Document Manager API for the following DimXpert annotations:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Distance-between
dimension tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Composite
distance-between dimension tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Symmetry
geometric tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Radius
dimension tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Diameter
dimension tolerance

```vb
 '--------------------------------------------------------------------------
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1. Open public_documents\samples\tutorial\api\block.sldprt.
' kadov_tag{{<spaces>}}2. Open the DimXpert toolbar from View > toolbars
' kadov_tag{{<spaces>}}   (select the first instance of toolbars on the View menu).
' kadov_tag{{<spaces>}}3. Create a distance-between dimension tolerance:
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}a. Click Location Dimension on the DimXpert toolbar.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}b. Click the left-front face of the block.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}c. Click Create Compound Plane on the DimXpert
'       pop-up toolbar.
' kadov_tag{{<spaces>}}   d. Click the right front face of the block.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}e. Click the green check mark to accept the faces.
' kadov_tag{{<spaces>}}   f. Click the back face of the block to complete the
'       location dimension.
' kadov_tag{{<spaces>}}   g. Click outside the part to position the location dimension.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}h. Click ESC to end dimensioning.
' kadov_tag{{<spaces>}}   i. Observe the following DimXpert annotation: kadov_tag{{<spaces>}}kadov_tag{{</spaces>}} DistanceBetween1.
' kadov_tag{{<spaces>}}4. Create composite distance-between and radius dimension tolerances:
' kadov_tag{{<spaces>}}   a. Click Auto Dimension Scheme on the DimXpert toolbar.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}b. Select Part type:kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Prismatic.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}c. Select Tolerance type:kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Plus and Minus
' kadov_tag{{<spaces>}}   d. Click in the Primary Datum field; select face in front of right hole.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}e. Click in the Secondary Datum field; select top face of block.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}f. Select all feature filters.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}g. Click the green check mark to accept the DimXpert settings.
' kadov_tag{{<spaces>}}   h. Observe the following DimXpert annotations: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
'       Diameter1, DistanceBetween5, and Radius1.
' kadov_tag{{<spaces>}}5. Create a symmetry geometric tolerance:
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}a. Click Datum on the DimXpert toolbar.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}b. Click the face in front of the left hole and click
'       outside the part to place Datum A.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}c. Click the green check mark to finish the Datum
'       definition.
' kadov_tag{{<spaces>}}   d. Click Geometric Tolerance on the DimXpert toolbar.
' kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}In the Geometric Tolerance Properties dialog:
' kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}i.   Select Symmetry from the Symbol dropdown list.
' kadov_tag{{<spaces>}}      ii.  Type A for the Primary Datum.
' kadov_tag{{<spaces>}}      iii. Click the face in front of the right hole.
' kadov_tag{{<spaces>}}      iv.  Click outside the part to place the annotation.
' kadov_tag{{<spaces>}}      v.   Click OK to close the Geometric Tolerance
'            Properties dialog.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}e. Observe the following DimXpert annotation: kadov_tag{{</spaces>}}Symmetry1.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}6. Close the part, saving it to another name.
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}NOTE: Because this part is used in a SOLIDWORKS online
'          tutorial, do not save any changes to the original file name.
' kadov_tag{{<spaces>}}7. Read how to load and run Code_Example_VBNET with this part.
 '------------------------------------------------------------------------------
```
