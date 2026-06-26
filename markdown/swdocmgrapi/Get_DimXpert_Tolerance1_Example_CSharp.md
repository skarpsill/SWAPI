---
title: "Get DimXpert Tolerance1 Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Tolerance1_Example_CSharp.htm"
---

# Get DimXpert Tolerance1 Example (C#)

This example builds a part to demonstrate usage of the
SOLIDWORKS Document Manager API for the following DimXpert annotations:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Circularity
geometric tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Cylindricity
geometric tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Countersink
angle dimension tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Countersink
diameter dimension tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Flatness
geometric tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Surface
profile geometric tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Length
dimension tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Width dimension
tolerance

```vb
 //--------------------------------------------------------------------------
// 1. Open public_documents\samples\tutorial\api\cover_with_geometric_tolerances.sldprt.
// 2. Click Auto Dimension Scheme on the DimXpert toolbar and
//    ensure that all feature filters are selected. kadov_tag{{<spaces>}}
//    Click the green check mark to accept the settings.
// 3. Click Geometric Tolerance on the DimXpert toolbar.
// kadov_tag{{<spaces>}}   In the Geometric Tolerance Properties dialog:
// kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}} a. Select Cylindricity from the Symbol dropdown in the first row.
// kadov_tag{{<spaces>}}   b. In the second row, select Profile of Surface from the
// kadov_tag{{<spaces>}}      Symbol dropdown list and type a tolerance of 0.5 next to it.
// kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}} c. Click the outer-base cylinder and click again outside
//kadov_tag{{<spaces>}}       the part to place the annotation.
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}d. Click OK to close the Geometric Tolerance Properties dialog.
// 4. In the DimXpertManager tab of the Management Panel, expand all of
// kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}} the nodes in the tree.
// 5. Observe the following DimXpert annotations: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Flatness1, Circularity1,
// kadov_tag{{<spaces>}}   Diameter1, kadov_tag{{</spaces>}} CounterSinkAngle1, CounterSinkDiameter1, Cylindricity1,
//    Surface Profile1, Length1, Width1
// 6. Close the part, saving it to another name.
//kadov_tag{{<spaces>}}    NOTE: Because this part is used in a SOLIDWORKS online tutorial,
//          do not save any changes to the original file name.
// 7. Read how to load and run Code_Example_CSharp with this part.
 //-------------------------------------------------------------------------
```
