---
title: "Get Edge Data By Name Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Edge_Data_By_Name_Example_CPlusPlus_COM.htm"
---

# Get Edge Data By Name Example (C++ COM)

This example shows how to get an edge by its
name and then get the underlying curve parameters and curve length. Import swconst.tlb.

IEdge::IGetCurveParams2 returns an array, so
this code must be used in an in-process DLL. Otherwise, use IEdge::GetCurveParams2
that returns a VARIANT.

void GetEdgeData(ISldWorks* m_pSldWorks)

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}HRESULT
res = NOERROR;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPMODELDOC2
p_ModelDoc = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPPARTDOC
p_PartDoc = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPENTITY
p_Entity = NULL;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
doctype;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Retrieve the model document pointer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}res
= m_pSldWorks->get_IActiveDoc2(
&p_ModelDoc );kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if(
res != S_OK || p_ModelDoc == NULL ) return;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}res
= p_ModelDoc->GetType(&doctype);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(doctype != swDocPART )return;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}res
= p_ModelDoc->QueryInterface(IID_IPartDoc, (LPVOID *)&p_PartDoc);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}res
= p_ModelDoc->GetType(&doctype);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(doctype != swDocPART )return;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get an entity by its name "FredsEdge"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}res
= p_PartDoc->IGetEntityByName(_T("FredsEdge"),
swSelEDGES, &p_Entity);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(res == S_OK && p_Entity != NULL)// If entity was found successfully

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPEDGE
p_Edge = NULL;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
See if Entity is an Edge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}res
= p_Entity->QueryInterface( IID_IEdge, (LPVOID*)&p_Edge);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(res == S_OK && p_Edge != NULL) // If Entity is an Edge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LPCURVE
p_Curve;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the edge's underlying curve

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}res
= p_Edge->IGetCurve(&p_Curve);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Since we do not keep the curve parameters with every edge, this call is
required or else the underlying curve parameters will be unknown.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
edgeData[10]={NULL};

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get Edge data

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}res
= p_Edge->IGetCurveParams2(&edgeData[0]);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Setup for ints packed into doubles

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}union
PackedIntskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
value;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
intData[2];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}
packedIntData;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the integers from the double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}packedIntData.value
= edgeData[8];kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
Notused = packedIntData.intData[0];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
curveType = packedIntData.intData[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the integers from the double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}packedIntData.value
= edgeData[9];kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
Notused2 = packedIntData.intData[0];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
curveTag = packedIntData.intData[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CString
message = _T("Attribute is on Edge with:\n");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

message.Format(_T("\tStartPt = \t%lf \t%lf \t%lf
\n \tEndPtkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
\t%lf \t%lf \t%lf \n\tParams = \t%lf \t%lf \n\tCurveType = \t%i \n\tCurveTag
= \t%i"),

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}edgeData[0],
edgeData[1], edgeData[2],

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}edgeData[3],
edgeData[4], edgeData[5],

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}edgeData[6],
edgeData[7],

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}curveType,
curveTag);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AfxMessageBox(
message );

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the length of the underlying curve

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}double
curveLength;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}res
= p_Curve->GetLength(edgeData[6],
edgeData[7],

&curveLength);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}message
= _T("The Edge length is:\n");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}message.Format(_T("\t%lf"),
curveLength);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AfxMessageBox(
message );

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}p_Curve->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
End if we got the Edge object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}p_Edge->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}p_Entity->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
End if we got the Entity by its name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}p_PartDoc->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}p_ModelDoc->Release();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

// End of function

}
