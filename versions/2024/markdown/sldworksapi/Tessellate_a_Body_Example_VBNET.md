---
title: "Tessellate a Body Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Tessellate_a_Body_Example_VBNET.htm"
---

# Tessellate a Body Example (VB.NET)

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
```

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swconst

Imports System

Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
Sub Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
errors As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
warnings As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the active document

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModel As ModelDoc2 = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS
2018\samples\tutorial\advdrawings\drive shaft
plate.sldprt", swDocumentTypes_e.swDocPART, 0, "", errors,
warnings)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the document title

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
title As [String] = swModel.**GetTitle**()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Cast down to a part

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swPart As PartDoc = DirectCast(swModel, PartDoc)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Variant is returned, which can be dealt with as an object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Variant represents an array of references

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vBodies As System.Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
aBodies As System.Array

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get bodies

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vBodies
= swPart.GetBodies2(CInt(swBodyType_e.swAllBodies),
False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Cast to an array of bodies

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aBodies
= DirectCast(vBodies, System.Array)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iNumBodies As Integer = aBodies.Length

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iNumSolidBodies As Integer = 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iNumSheetBodies As Integer = 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Loop through array

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swBody As Body2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
b As Integer = 0 To iNumBodies - 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get a body and apply cast

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swBody
= DirectCast(aBodies.GetValue(b), Body2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Now call a method on a body

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nBodyType As Integer = swBody.[**GetType**]()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
nBodyType = CInt(swBodyType_e.swSheetBody) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iNumSheetBodies
+= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
nBodyType = CInt(swBodyType_e.swSolidBody) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iNumSolidBodies
+= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFace As Face2 = Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swTessellation As Tessellation = Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bResult As Boolean = False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Pass in null so the whole body will be tessellated

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation
= DirectCast(swBody.GetTessellation(Nothing),
Tessellation)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set up the Tessellation object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Required data

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation.NeedFaceFacetMap= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation.NeedVertexParams= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation.NeedVertexNormal= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set option to improve quality of data returned

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation.ImprovedQuality= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Tessellation
is configured for higher data quality.")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
How to handle matches across common edges

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swTessellation.MatchType
= CInt(swTesselationMatchType_e.swTesselationMatchFacetTopology)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Do the tessellation

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bResult
= swTessellation.Tessellate()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the number of vertices and facets

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iNumVertices As Integer = swTessellation.GetVertexCount()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Vertex
count: " & iNumVertices)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iNumFacets As Integer = swTessellation.GetFacetCount()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Facet
count: " & iNumFacets)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Now get the facet data per face

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
aFacetIds As Integer()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iNumFacetIds As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
aFinIds As Integer()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
aVertexIds As Integer()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
aVertexCoords1 As Double()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
aVertexCoords2 As Double()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Speed things up

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.SetAddToDB(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.SetDisplayWhenAdded(False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Insert sketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.Insert3DSketch2(False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Loop over faces

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFace
= DirectCast(swBody.GetFirstFace(),
Face2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}While
swFace IsNot Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aFacetIds
= DirectCast(swTessellation.GetFaceFacets(swFace),
Integer())

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iNumFacetIds
= aFacetIds.Length

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
iFacetIdIdx As Integer = 0 To iNumFacetIds - 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aFinIds
= DirectCast(swTessellation.GetFacetFins(aFacetIds(iFacetIdIdx)),
Integer())

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
There should always be three fins per facet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
iFinIdx As Integer = 0 To 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aVertexIds
= DirectCast(swTessellation.GetFinVertices(aFinIds(iFinIdx)),
Integer())

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Should always be two vertices per fin

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aVertexCoords1
= DirectCast(swTessellation.GetVertexPoint(aVertexIds(0)),
Double())

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}aVertexCoords2
= DirectCast(swTessellation.GetVertexPoint(aVertexIds(1)),
Double())

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Create a line

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.CreateLine2(aVertexCoords1(0), aVertexCoords1(1),
aVertexCoords1(2), aVertexCoords2(0), aVertexCoords2(1), aVertexCoords2(2))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFace
= DirectCast(swFace.GetNextFace(),
Face2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
While

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

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
swApp As SldWorks

End Class
