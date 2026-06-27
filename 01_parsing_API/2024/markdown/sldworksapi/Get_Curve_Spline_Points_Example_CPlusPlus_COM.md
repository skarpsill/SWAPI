---
title: "Get Curve Spline Points Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Curve_Spline_Points_Example_CPlusPlus_COM.htm"
---

# Get Curve Spline Points Example (C++ COM)

This example shows how to get the point coordinates
from a selected sketch spline segment.

The methods ICurve::IGetSplinePts and ICurve::IGetBCurveParams
return arrays, so this code must be used in an in-process DLL. Otherwise,
use the methods ICurve::GetSplinePts and ICurve::GetBCurveParams that
return VARIANTs.

void GetCurveSplinePoints(ISldWorks* m_pSldWorks)

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULT
hres;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPMODELDOC2
pModelDoc = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hres
= m_pSldWorks->get_IActiveDoc2(&pModelDoc);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(
pModelDoc == NULL)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPUNKNOWN
pUnk = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPSELECTIONMGR
pSelectMgr = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModelDoc->get_ISelectionManager( &pSelectMgr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(
pSelectMgr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSelectMgr->IGetSelectedObject3( 1, &pUnk);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSelectMgr->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPSKETCHSEGMENT
pSketchSeg = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(
pUnk)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pUnk->QueryInterface(
IID_ISketchSegment, (void **)&pSketchSeg);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pUnk->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pUnk
= NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPCURVE
pCurve = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(
pSketchSeg)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSketchSeg->IGetCurve( &pCurve);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pSketchSeg->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(
pCurve)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
nParamSize;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCurve->IGetBCurveParamsSize2( FALSE, TRUE,
&nParamSize);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
*dSplineParams = new double [nParamSize];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCurve->IGetBCurveParams( dSplineParams);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
*propArray = (int*)&dSplineParams[0];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
*dKnotArray = &dSplineParams[2];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
*dCtrlArray = &dSplineParams[ 2+ propArray[1]+propArray[2] ];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
nSplinePts;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCurve->IGetSplinePtsSize( propArray, dKnotArray,
dCtrlArray, &nSplinePts);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
*dSplinePts = new double[nSplinePts];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCurve->IGetSplinePts( dSplinePts);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for(
int i = 0; i < nSplinePts; i += 3)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}TRACE(
auT("x = %f, y = %f, z = %f\n"),

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dSplinePts[i],
dSplinePts[i+1], dSplinePts[+2]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}delete
[] dSplineParams;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}delete
[] dSplinePts;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pCurve->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pModelDoc->Release();

}
