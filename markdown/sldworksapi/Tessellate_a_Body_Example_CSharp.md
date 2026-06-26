---
title: "Tessellate a Body Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Tessellate_a_Body_Example_CSharp.htm"
---

# Tessellate a Body Example (C#)

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Verify that the part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Tessellates the body.
// 2. Examine the graphics area and Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//-----------------------------------------------------------------
using System;
```

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System.Diagnostics;

namespace TessellateABody_CSharp.csproj

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
partial class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
SldWorks swApp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
void Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
errors = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
warnings = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the active document

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc2
swModel = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS
2018\\samples\\tutorial\\advdrawings\\drive
shaft plate.sldprt", (int)swDocumentTypes_e.swDocPART, 0, "",
ref errors, ref warnings);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the document title

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(swModel.GetTitle());

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Cast down to a part

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PartDoc
swPart = (PartDoc)swModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Variant is returned, which can be dealt with as an object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Variant represents an array of references

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}System.Object
vBodies;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}System.Array
aBodies;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get bodies

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vBodies
= swPart.GetBodies2((int)swBodyType_e.swAllBodies,
false);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Cast to an array of bodies

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aBodies
= (System.Array)vBodies;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
iNumBodies = aBodies.Length;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
iNumSolidBodies = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
iNumSheetBodies = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Loop through array

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Body2
swBody;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(int b = 0; b < iNumBodies; b++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get a body and apply cast

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swBody
= (Body2)aBodies.GetValue(b);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Now call a method on a body

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
nBodyType = swBody.GetType();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(nBodyType == (int)swBodyType_e.swSheetBody)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iNumSheetBodies++;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(nBodyType == (int)swBodyType_e.swSolidBody)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iNumSolidBodies++;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Face2
swFace = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Tessellation
swTessellation = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bool
bResult = false;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Pass in null so the whole body will be tessellated

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation
= (Tessellation)swBody.GetTessellation(null);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Set up the Tessellation object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation.NeedFaceFacetMap= true;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation.NeedVertexParams= true;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation.NeedVertexNormal= true;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation.ImprovedQuality= true;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Tessellation
is configured for higher-quality data output.");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
How to handle matches across common edges

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation.MatchType
= (int)swTesselationMatchType_e.swTesselationMatchFacetTopology;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Do it

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bResult
= swTessellation.Tessellate();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the number of vertices and facets

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Number
of vertices: " + swTessellation.GetVertexCount());

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Number
of facets: " + swTessellation.GetFacetCount());

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Now get the facet data per face

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int[]
aFacetIds;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
iNumFacetIds;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int[]
aFinIds;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int[]
aVertexIds;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double[]
aVertexCoords1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double[]
aVertexCoords2;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Add sketch for this body

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Speed things up

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.SetAddToDB(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.SetDisplayWhenAdded(false);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.Insert3DSketch2(false);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Loop over faces

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFace
= (Face2)swBody.GetFirstFace();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}while
(swFace != null)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aFacetIds
= (int[])swTessellation.GetFaceFacets(swFace);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iNumFacetIds
= aFacetIds.Length;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(int iFacetIdIdx = 0; iFacetIdIdx < iNumFacetIds; iFacetIdIdx++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aFinIds
= (int[])swTessellation.GetFacetFins(aFacetIds[iFacetIdIdx]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
There should always be three fins per facet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(int iFinIdx = 0; iFinIdx < 3; iFinIdx++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aVertexIds
= (int[])swTessellation.GetFinVertices(aFinIds[iFinIdx]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Should always be two vertices per fin

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aVertexCoords1
= (double[])swTessellation.GetVertexPoint(aVertexIds[0]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aVertexCoords2
= (double[])swTessellation.GetVertexPoint(aVertexIds[1]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Create a line

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.CreateLine2(aVertexCoords1[0], aVertexCoords1[1],
aVertexCoords1[2], aVertexCoords2[0], aVertexCoords2[1], aVertexCoords2[2]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFace
= (Face2)swFace.GetNextFace();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Close sketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.Insert3DSketch2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Clear selection for next pass

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Restore settings

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.SetAddToDB(false);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.SetDisplayWhenAdded(true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

}
