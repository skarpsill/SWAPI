---
title: "Get UV Parameters for XYZ Location Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_UV_Parameters_For_XYZ_Location_Example_CSharp.htm"
---

# Get UV Parameters for XYZ Location Example (C#)

This example shows how to use IFace2 and ICurve interfaces
to get the UV parameters from the XYZ location.

//---------------------------------------------------------------------------
// Preconditions:
//kadov_tag{{<spaces>}}1. Openpublic_documents\samples\tutorial\cosmosxpress\aw_hook.sldprt.
//kadov_tag{{<spaces>}}2.
Verify that**Tools > System Options > Options > FeatureManager > Solid Bodies**
// drop-down selection is**Show**.
//kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}3.
Expand the Solid Bodies folder and select**Split Line1**.
// 4. Open the Immediate window or modify the macro to write the output to a
file.
//kadov_tag{{<spaces>}}
// Postconditions: Observe
the output in the Immediate window.
//----------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System;

using System.Diagnostics;

namespace ReverseEvalTestMIK_CSharp.csproj

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}partial
class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc2
swModel;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelectionMgr
swSelMgr;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Face2
swFace;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
void Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel
= (ModelDoc2)swApp.**ActiveDoc**;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelMgr
= (SelectionMgr)swModel.**SelectionManager**;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double[]
pntData = new double[3];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Body2
swBody = default(Body2);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Body2
procBody = default(Body2);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swBody
= (Body2)swSelMgr.**GetSelectedObject6**(1, -1);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}procBody
= swBody.**GetProcessedBody2**(0.5, 0.5);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Bypass surface split

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFace
= (Face2)procBody.**GetFirstFace**();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Set
swFace = swBody.**GetFirstFace**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}while
((swFace != null))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double[]
uvBnds = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}uvBnds
= (double[])swFace.**GetUVBounds**();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
UminFace = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
UmaxFace = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
VminFace = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
VmaxFace = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UminFace
= uvBnds[0];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UmaxFace
= uvBnds[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VminFace
= uvBnds[2];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VmaxFace
= uvBnds[3];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Surface
swSurf = default(Surface);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSurf
= (Surface)swFace.**GetSurface**();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}uvBnds
= (double[])swSurf.**Parameterization**();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
UminSurf = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
UmaxSurf = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
VminSurf = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
VmaxSurf = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UminSurf
= uvBnds[0];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UmaxSurf
= uvBnds[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VminSurf
= uvBnds[2];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VmaxSurf
= uvBnds[3];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}object[]
vEdges = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vEdges
= (object[])swFace.**GetEdges**();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
i = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(i = 0; i <= vEdges.GetUpperBound(0); i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Edge
swEdge = default(Edge);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEdge
= (Edge)vEdges[i];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Curve
swCurve = default(Curve);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCurve
= (Curve)swEdge.**GetCurve**();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double[]
vCurveParams = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vCurveParams
= (double[])swEdge.**GetCurveParams2**();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
startParam = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
endParam = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
incParam = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
curParam = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}startParam
= vCurveParams[6];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}endParam
= vCurveParams[7];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}incParam
= (endParam - startParam) / 10.0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}curParam
= startParam;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}while
(curParam < endParam)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double[]
vEdgePnt = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vEdgePnt
= (double[])swEdge.**Evaluate**(curParam);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double[]
vUVSurfParams = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
UEdge = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
VEdge = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the UV parameters for the point using IFace2::ReverseEvaluate

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vUVSurfParams
= (double[])swFace.ReverseEvaluate(vEdgePnt[0],
vEdgePnt[1], vEdgePnt[2]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
((vUVSurfParams != null))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UEdge
= vUVSurfParams[0];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VEdge
= vUVSurfParams[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Edge
point: " + " x: " + vEdgePnt[0] + " y: " + vEdgePnt[1]
+ " z: " + vEdgePnt[2]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("U
parameter returned from IFace2::ReverseEvaluate is " + UEdge);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(UEdge > UmaxFace | UEdge < UminFace)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("U
param error face");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Stop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("V
parameter returned from IFace2::ReverseEvalute is " + VEdge);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(VEdge > VmaxFace | VEdge < VminFace)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("V
param error face");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Stop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Face
reverse evaluate fails - empty data");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the UV parameters for the point using ICurve::ReverseEvaluate

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vUVSurfParams
= (double[])swSurf.ReverseEvaluate(vEdgePnt[0],
vEdgePnt[1], vEdgePnt[2]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
((vUVSurfParams != null))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UEdge
= vUVSurfParams[0];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}VEdge
= vUVSurfParams[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("U
parameter returned from ICurve::ReverseEvaluate is " + UEdge);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(UEdge > UmaxFace | UEdge < UminFace)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("U
param error surface");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Stop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("V
parameter returned from ICurve::ReverseEvaluateis " + VEdge);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(VEdge > VmaxFace | VEdge < VminFace)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("V
param error surface");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Stop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}curParam
= curParam + incParam;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFace
= (Face2)swFace.**GetNextFace**();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Complete");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
SldWorks swApp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

}
