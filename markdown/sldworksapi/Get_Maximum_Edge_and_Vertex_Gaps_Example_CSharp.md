---
title: "Get Maximum Edge and Vertex Gaps Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Maximum_Edge_and_Vertex_Gaps_Example_CSharp.htm"
---

# Get Maximum Edge and Vertex Gaps Example (C#)

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
 //----------------------------------------------------------------------------
 // kadov_tag{{<spaces>}}Preconditions:
 // kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1. kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Open public_documents\samples\tutorial\assemblymates\head.sldprt.
 // kadov_tag{{<spaces>}}2. kadov_tag{{<spaces>}}Open an Immediate window.
 //
 // Postconditions: Inspect the Immediate window for tolerance data for all edges
 // and vertexes.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 //----------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace GetMaximumEdgeandVertexGaps_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}PartDoc swPart = default(PartDoc);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] vBodyArr = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Body2 swBody = default(Body2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] vEdgeArr = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Edge swEdge = default(Edge);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] vVertexArr = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Vertex swVertex = default(Vertex);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}FaultEntity swFaultEnt = default(FaultEntity);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool bRet = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double tol = 0.0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Entity swTanEnt = default(Entity);
kadov_tag{{<spaces>}}
             kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart = (PartDoc)swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("File = " + swModel.GetPathName());
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}vBodyArr = (Object[])swPart.GetBodies2((int)swBodyType_e.swAllBodies, true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}foreach ( Object vBody in vBodyArr)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swBody = (Body2)vBody;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Body[" + swBody.GetType() + "] --> " + swBody.GetSelectionId());
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}vEdgeArr = (Object[])swBody.GetEdges();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}vVertexArr = (Object[])swBody.GetVertices();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}double maxEdgeGap = 0;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}maxEdgeGap = 0.0;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}foreach (Object vEdge in vEdgeArr)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}// Find maximum edge gap
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}swEdge = (Edge)vEdge;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}bRet = swEdge.IsTolerant(out tol);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}if (maxEdgeGap < tol)
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}maxEdgeGap = tol;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}if ((!(bRet == false)))
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print("Edge is tolerant: ");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" Tolerance = " + tol);
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}swTanEnt = (Entity)swEdge;
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}bRet = swTanEnt.Select4(true, null);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print("Edge is exact: Tolerance = " + tol);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}swFaultEnt = swEdge.Check;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Maximum edge gap is " + maxEdgeGap);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}double maxVertexGap = 0;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}maxVertexGap = 0.0;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}foreach (Object vVertex in vVertexArr)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}// Find maximum vertex gap
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}swVertex = (Vertex)vVertex;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}bRet = swVertex.IsTolerant(out tol);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}if (maxVertexGap < tol)
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}maxVertexGap = tol;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}if ((!(bRet == false)))
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print("Vertex is tolerant: ");
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" Tolerance = " + tol);
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}swTanEnt = (Entity)swVertex;
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}bRet = swTanEnt.Select4(true, null);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print("Vertex is exact: Tolerance = " + tol);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Maximum vertex gap is " + maxVertexGap);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
