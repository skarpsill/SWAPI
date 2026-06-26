---
title: "Tessellate a Body Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Tessellate_a_Body_Example_VB.htm"
---

# Tessellate a Body Example (VBA)

This example shows how to tessellate a body.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Tessellates the body.
' 2. Examine the graphics area and Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-----------------------------------------------------------------
Option Explicit
```

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
errors As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
warnings As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swApp As SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModel As ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swPart As PartDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
b As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nBodyType As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFace As Face2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swTessellation As Tessellation

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bResult As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iNumVertices As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iNumFacets As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
aFacetIds As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
aFinIds As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
aVertexIds As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
aVertexCoords1 As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
aVertexCoords2 As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iFacetIdIdx As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iFinIdx As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vBodies As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the active document

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS
2018\samples\tutorial\advdrawings\drive shaft
plate.sldprt", swDocumentTypes_e.swDocPART, 0, "", errors,
warnings)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the document title

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
swModel.**GetTitle**()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Cast down to a part

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swPart = swModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get bodies

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vBodies
= swPart.GetBodies2(swBodyType_e.swAllBodies,
False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Loop through array

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swBody As Body2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
b = 0 To UBound(vBodies)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get a body

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swBody = vBodies(b)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Now call a method on a body

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nBodyType
= swBody.[**GetType**]()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
nBodyType = swBodyType_e.swSolidBody Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFace = Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swTessellation = Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bResult
= False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Pass in null so the whole body will be tessellated

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swTessellation = swBody.GetTessellation(Empty)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set up the Tessellation object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation.NeedFaceFacetMap= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation.NeedVertexParams= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation.NeedVertexNormal= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set option to improve quality of data returned

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation.ImprovedQuality= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
("Tessellation is configured for higher-quality data.")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
How to handle matches across common edges

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation.MatchType
= swTesselationMatchType_e.swTesselationMatchFacetTopology

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Do the tessellation

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bResult
= swTessellation.Tessellate()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the number of vertices and facets

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iNumVertices
= swTessellation.GetVertexCount()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
("Vertex count: " & iNumVertices)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iNumFacets
= swTessellation.GetFacetCount()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
("Facet count: " & iNumFacets)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Speed things up

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.SetAddToDB(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.SetDisplayWhenAdded(False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Insert sketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.Insert3DSketch2(False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Now get the facet data per face

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFace = swBody.GetFirstFace()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}While
Not swFace Is Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aFacetIds
= swTessellation.GetFaceFacets(swFace)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
iFacetIdIdx = 0 To UBound(aFacetIds)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aFinIds
= swTessellation.GetFacetFins(aFacetIds(iFacetIdIdx))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
There should always be three fins per facet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
iFinIdx = 0 To 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aVertexIds
= swTessellation.GetFinVertices(aFinIds(iFinIdx))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Should always be two vertices per fin

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aVertexCoords1
= swTessellation.GetVertexPoint(aVertexIds(0))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aVertexCoords2
= swTessellation.GetVertexPoint(aVertexIds(1))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Create a line

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.CreateLine2aVertexCoords1(0), aVertexCoords1(1),
aVertexCoords1(2), aVertexCoords2(0), aVertexCoords2(1), aVertexCoords2(2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFace = swFace.GetNextFace()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Wend

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Close sketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.Insert3DSketch2(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Clear selection for next pass

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Restore settings

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.SetAddToDB(False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.SetDisplayWhenAdded(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Exit
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub
