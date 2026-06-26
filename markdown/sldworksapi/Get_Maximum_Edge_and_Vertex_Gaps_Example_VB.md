---
title: "Get Maximum Edge and Vertex Gaps Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Maximum_Edge_and_Vertex_Gaps_Example_VB.htm"
---

# Get Maximum Edge and Vertex Gaps Example (VBA)

This example returns the same data returned by theTools > Checkdialog box when the check boxes,Maximum
edge gapandMaximum vertex gap,
are selected.

This example shows how to iterate over each edge and vertex in a part to
obtain:

kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Whether
an edge or vertex is:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}* tolerant (distance to neighbor is greater than 5.0E-9 mm).

kadov_tag{{<spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}* exact (distance to neighbor is less than or equal to 5.0E-9 mm).

kadov_tag{{<spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Gap size
(or tolerance) in mm of each edge or vertex.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Maximum
edge and vertex gaps (or tolerances) in mm for the part.

```vb
 '----------------------------------------------------------------------------
 ' kadov_tag{{<spaces>}}Preconditions:
 ' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1. kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Open public_documents\samples\tutorial\assemblymates\head.sldprt.
 ' kadov_tag{{<spaces>}}2. kadov_tag{{<spaces>}}Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window for tolerance data for all edges
 ' and vertexes.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swApp kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}As SldWorks.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModel kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}As SldWorks.ModelDoc2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swPart kadov_tag{{<spaces>}}                 kadov_tag{{</spaces>}}As SldWorks.PartDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vBodyArr kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}As Variant
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vBody kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}As Variant
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swBody kadov_tag{{<spaces>}}                 kadov_tag{{</spaces>}}As SldWorks.Body2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vEdgeArr kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}As Variant
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vEdge kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}As Variant
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swEdge kadov_tag{{<spaces>}}                 kadov_tag{{</spaces>}}As SldWorks.Edge
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vVertexArr              As Variant
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vVertex                 As Variant
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swVertex                As SldWorks.Vertex
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swFaultEnt kadov_tag{{<spaces>}}             kadov_tag{{</spaces>}}As SldWorks.FaultEntity
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim bRet kadov_tag{{<spaces>}}                   kadov_tag{{</spaces>}}As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim tol                     As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swTanEnt kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}As SldWorks.Entity

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swApp = Application.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swPart = swModel
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "File = " & swModel.GetPathName
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}vBodyArr = swPart.GetBodies2(swAllBodies, True)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}For Each vBody In vBodyArr
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set swBody = vBody
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Body[" & swBody.GetType & "] --> " & swBody.GetSelectionId
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}vEdgeArr = swBody.GetEdges
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}vVertexArr = swBody.GetVertices
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim maxEdgeGap As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}maxEdgeGap = 0#
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For Each vEdge In vEdgeArr
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Find maximum edge gap
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set swEdge = vEdge kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bRet = swEdge.IsTolerant(tol)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If maxEdgeGap < tol Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}maxEdgeGap = tol
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}If (Not (bRet = False)) Then
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print "Edge is tolerant: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}"
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}Tolerance = " & tol
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Set swTanEnt = swEdge
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}bRet = swTanEnt.Select4(True, Nothing)
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print "Edge is not tolerant: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance = " & tol
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set swFaultEnt = swEdge.Check
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next vEdge
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print ""
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "Maximum edge gap is " & maxEdgeGap
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print ""
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim maxVertexGap As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}maxVertexGap = 0#
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For Each vVertex In vVertexArr
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Find maximum vertex gap
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set swVertex = vVertex
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bRet = swVertex.IsTolerant(tol)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If maxVertexGap < tol Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}maxVertexGap = tol
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If (Not (bRet = False)) Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print "Vertex is tolerant: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}"
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}Tolerance = " & tol
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Set swTanEnt = swVertex
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}bRet = swTanEnt.Select4(True, Nothing)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print "Vertex is not tolerant: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Tolerance = " & tol
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next vVertex
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print ""
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "Maximum vertex gap is " & maxVertexGap
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print ""
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Next vBody
End Sub
```
